import telebot
from telebot.callback_data import CallbackData
from create_bot import BotDB
from tgbot.keyboards.kb_create_new_project import kb_activity_type


def start(call: telebot.types.CallbackQuery, bot: BotDB):
    m = bot.send_message(call.from_user.id, 'Введите название проекта:')
    bot.register_next_step_handler(m, type_of_activity, bot=bot, datas={})


def type_of_activity(msg: telebot.types.Message, bot: BotDB, datas):
    datas['project_name'] = msg.text
    print(datas)

    kb = kb_activity_type(bot.ACTIVITY_TYPES, bot.types_factory)
    bot.send_message(msg.from_user.id, 'Выберите тип активности', reply_markup=kb)
    bot.register_callback_query_handler(lambda call: get_status(call, bot, datas),
                                        # lambda call: call.data.startswith('activity'),
                                        # func=bot.types_factory.filter(),
                                        func=lambda call: True,
                                        config=bot.types_factory.filter()
                                        )
    print("Успешно зарегистрировано!")


def get_status(call: telebot.types.CallbackQuery, bot: BotDB, datas):

    print("Регистратция коллбэка внутри type_of_activity")
    print('внутри гетстатуса')
    print(datas)
    bot.answer_callback_query(call.id)
    print('отработал ответ коллбэка')
    # activity_type_id = call.data.split(':')[1]
    # data['activity_type'] = activity_type_id
    # print(f"Данные проекта:{data}")
    # bot.send_message(call.from_user.id, f"Вы выбрали тип активности с ID: {activity_type_id}")
