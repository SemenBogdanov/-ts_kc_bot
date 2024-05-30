import logging

import pandas
import psycopg2
import sqlalchemy

from key import db_user, db_pass, db_ip, db_port, db_name
from telebot import TeleBot
from telebot.types import Message
from tgbot.utils.database import db_connect


class BotDB(TeleBot):
    def __init__(self, token: str):
        """Инициализация подключения БД"""
        super().__init__(token, num_threads=5)
        self.cursor = None
        self.conn = None
        self.query = None
        self.KC_USERS = self.get_tg_id_kc_users()
        self.ACTIVITY_TYPES = self.get_activity_types()

    # DATABASE FUNCTIONS---------------------------------------------------------
    @staticmethod
    def db_connect():
        return db_connect('psy')

    def get_data_from_source(self, query, content=None):
        self.conn = self.db_connect()
        try:
            self.cursor = self.conn.cursor()
            if content:
                self.cursor.execute(query, content)
                res = self.cursor.fetchall()
                # self.cursor.close()
                return res
            else:
                self.cursor.execute(query)
                res = self.cursor.fetchall()
                # print(res)
                # self.cursor.close()
                return res
        except Exception as e:
            # glob.logger.debug('======> %s' % traceback.format_exc())
            print('Ошибка при работе с PostgreSQL', e)
        finally:
            if self.conn:
                self.cursor.close()
                self.conn.close()

    def get_activity_by_id(self, activity_id):
        self.query = f'''
                    SELECT * 
                    FROM nsi_data.p_ts_a_001_activity_dict
                    WHERE 
                    id = (%s)
                    '''
        self.content = (activity_id,)
        return self.get_data_from_source(self.query, self.content)

    def get_tg_id_kc_users(self):
        """"""
        kc_users = []
        self.query = f"SELECT tg_id from public.kc_employees where tg_id is not null"
        for row_users in self.get_data_from_source(self.query):
            kc_users.extend(row_users)
        print('''info: перечень акцептованных пользователей успешно загружен''')
        return kc_users

    def get_activity_types(self):
        """Get all activity types from database table"""
        self.query = f"SELECT id, activity_type FROM dal_data.p_ts_bot_001_activity_type"
        res = self.get_data_from_source(self.query)
        activity_types = [{'id': str(item[0]), 'activity_type': str(item[1])} for item in res]
        return activity_types

    # def get_all_records(self):
    #     """Получить все строки"""
    #     query = "select * from people;"
    #     self.cur.execute(query)
    #     res = self.cur.fetchall()
    #     return res

    # ---------------------------------------------------------DATABASE FUNCTIONS

    def is_user_auth(self, message: Message):
        is_accepted = True if message.from_user.id in self.KC_USERS else False
        print(f'''info: выполнена проверка пользователя {message.from_user.id}: {is_accepted}''')
        return is_accepted


    def get_friends(self):
        """Получаем список друзей для проверки дней рождений"""
        query = "select persone_name, birthday_date from people where type_persons = '1';"
        self.cur.execute(query)
        res = self.cur.fetchall()
        # print(res)
        return res

    def get_colleagues(self):
        """Получаем список коллег для проверки дней рождений"""
        query = "select persone_name, birthday_date from people p where p.type_persons = '2';"
        self.cur.execute(query)
        res = self.cur.fetchall()
        # print(res)
        return res

    def add_birthday(self, p_name, p_date, p_type):
        """Добавляем новую запись о дне рождения в таблицу"""
        try:
            query = """INSERT INTO people (persone_name, birthday_date, type_persons) values (%s,%s,%s)"""
            values = (str(p_name), str(p_date), str(p_type),)
            self.cur.execute(query, values)
            self.conn.commit()
            return True
        except Exception as e:
            print("Ошибка при вставке {}", e)
            return False

    def del_by_id(self, id):
        """Удаляем запись о дне рождении по ID"""
        try:
            self.cur.execute("delete from people p where p.id = %s", (id,))
            self.conn.commit()
            return True
        except:
            return False

    def find_by_surname(self, surname, tp):
        if tp == 2:
            self.cur.execute("select * from people p where p.persone_name like %s "
                             "and p.type_persons = %s::varchar ", (surname, tp,))
            res = self.cur.fetchall()
            if res:
                return res
            else:
                return False
        elif tp == 1:  # private
            self.cur.execute("select * from people p where p.persone_name like %s ", (surname,))
            res = self.cur.fetchall()
            if res:
                return res
            else:
                return False

    def getinfo(self):
        return self.conn.info

    def rolllback(self):
        return self.conn.rollback()

    def close_db(self):
        """Закрытие соединения с БД"""
        self.conn.close()

