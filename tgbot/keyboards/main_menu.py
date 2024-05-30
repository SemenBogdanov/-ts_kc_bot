import telebot.types as types
from tgbot.message_functions.functions import delete_message_mg


def f_main_menu(message, bot):
    """
    Функция выполняет проверку авторизации пользователя и отображает основное меню использования чат-бота
    """
    if not bot.is_user_auth(message):
        bot.send_message(message.chat.id, "Нет авторизации! Запросите тут: s.bogdanov@ac.gov.ru")
    else:
        if message.text == "Создание новой задачи":
            # engine.execute(log_action(message.from_user.id, 'Главное меню'))
            keyboard = types.InlineKeyboardMarkup(row_width=1)

            btn1 = types.InlineKeyboardButton(text='Создание нового проекта в системе БитриксПМ',
                                              callback_data=f'new_pm_project')
            btn2 = types.InlineKeyboardButton(text='Изменение статуса по существующему проекту',
                                              callback_data=f'сhange_status_pm_project')
            btn3 = types.InlineKeyboardButton(text='Добавление проекта в таймшиты сотрудникам',
                                              callback_data=f'add_ts_activity_to_employee')
            btn4 = types.InlineKeyboardButton(text='Изменение руководителя проекта', callback_data=f'change_rp')
            btn5 = types.InlineKeyboardButton(text='Изменение замещающего руководителя проекта',
                                              callback_data=f'change_z_rp')
            btn6 = types.InlineKeyboardButton(text='Закрытие проекта', callback_data=f'close_project')
            btn7 = types.InlineKeyboardButton(text='Информация по проекту', callback_data=f'close_project')
            btn8 = types.InlineKeyboardButton(text='ℹ️ Техническая поддержка', callback_data=f'support')
            btn9 = types.InlineKeyboardButton(text='Скрыть сообщение', callback_data=f'hide_buttons')
            keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
            delete_message_mg(bot, message)
            bot.send_message(message.from_user.id, 'Выберите кнопку для получения подробной информации:',
                             reply_markup=keyboard)
