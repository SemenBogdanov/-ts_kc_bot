import telebot
from telebot.callback_data import CallbackData


from create_bot import BotDB

from tgbot.keyboards.kb_create_new_project import kb_activity_type


types_factory = CallbackData('activity_types', prefix='activity')

def start(call: telebot.types.CallbackQuery, bot: BotDB):
    data = dict()
    m = bot.send_message(call.from_user.id,
                         'Введите название проекта:')
    bot.register_next_step_handler(m, type_of_activity, bot=bot, data=data)


def type_of_activity(msg: telebot.types.Message, bot: BotDB, data):
    data['project_name'] = (str(msg.text))
    print(data)

    kb = kb_activity_type(bot, types_factory)
    print(kb)
    m = bot.send_message(msg.from_user.id, 'Выберите тип активности', reply_markup=kb)
    # bot.register_next_step_handler(m, get_status, bot=bot, data=data)


def get_status(msg: telebot.types.Message, data):
    bot.register_callback_query_handler(callback=get_status, func=lambda call: True, config=types_factory.filter())
    data['project_name'] = (str(msg.text)) # И ВОТ СЮДА ХОЧУ ЗАПИСАТЬ ТИП ПРОЕКТА
