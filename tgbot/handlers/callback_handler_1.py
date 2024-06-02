import telebot.types as types

from tgbot.chains_dialog import ch_create_new_project
from tgbot.message_functions.functions import update_message_cb, delete_message_cb


def callback_func(call: types.CallbackQuery, bot):
    # engine = connect_db('BOT_DB', 'alh')
    # if call.data.split(',')[0] in ('admin_verify_yes', 'admin_verify_no'):
    #     engine.execute(log_action(call.from_user.id, 'Администрирование бота', action='Решение о доступе к боту'))
    #     esia_auth = Esia(bot, group_id)
    #     esia_auth.esia_auth_admin_verify(call)
    #     if esia_auth.admin_verify_status is True:
    #         start_message(esia_auth.tg_id_after_admin_verify)

    # if call.data == 'main_menu':
    #     # engine.execute(log_action(call.from_user.id, 'Главное меню'))
    #     # keyboard = types.InlineKeyboardMarkup(row_width=1)
    #     # btn1 = types.InlineKeyboardButton(text='Высокоуровневый отчет: одностраничник', callback_data=f'main_status')
    #     # btn2 = types.InlineKeyboardButton(text='Управление играми', callback_data=f'manage_plays')
    #     # btn3 = types.InlineKeyboardButton(text='ИТ, Кибербезопасность', callback_data=f'cyber_security_it')
    #     # btn4 = types.InlineKeyboardButton(text='Спорт', callback_data=f'sport')
    #     # btn5 = types.InlineKeyboardButton(text='Просмотры', callback_data=f'views')
    #     # btn6 = types.InlineKeyboardButton(text='Социальные медиа и СМИ', callback_data=f'social_media_smi')
    #     # btn7 = types.InlineKeyboardButton(text='Билеты и зрители', callback_data=f'tickets_and_viewers')
    #     # btn8 = types.InlineKeyboardButton(text='Расписание ключевых событий', callback_data=f'schedule_key_events')
    #     # btn9 = types.InlineKeyboardButton(text='ℹ️ Техническая поддержка', callback_data=f'support')
    #     # btn10 = types.InlineKeyboardButton(text='Скрыть сообщение', callback_data=f'hide_buttons')
    #     # keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
    #     # update_message_cb(bot, call, 'Выберите кнопку для получения подробной информации:', keyboard)

    if call.data == 'hide_buttons':
        delete_message_cb(bot, call)
        return 1

    if call.data == 'new_pm_project':
        delete_message_cb(bot, call)
        # print(call)
        bot.send_message(call.message.chat.id, 'Создание нового проекта в системе БитриксПМ')
        ch_create_new_project.start(call, bot)
        return 1



    #
    #
    # if call.data == 'main_status':
    #     # engine.execute(log_action(call.from_user.id, 'Высокоуровневый отчёт ИБ'))
    #     call_btn.main_status(call)
    #     return 1
    #
    # if call.data == 'manage_plays':
    #     # engine.execute(log_action(call.from_user.id, 'Управление играми'))
    #     call_btn.manage_plays_message(call)
    #     return 1
    #
    # if call.data == 'mp_all_incidents':
    #     # engine.execute(log_action(call.from_user.id, 'УИ Инциденты в работе'))
    #     call_btn.manage_plays_inc_all(call)
    #     return 1
    #
    # if call.data == 'mp_fed':
    #     # engine.execute(log_action(call.from_user.id, 'УИ Федеральные инциденты'))
    #     call_btn.manage_plays_fed(call)
    #     return 1