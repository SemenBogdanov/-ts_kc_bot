from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from create_bot import BotDB


def send_main_menu(msg, bot):
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(KeyboardButton('Создание новой задачи'))
    keyboard.add(KeyboardButton('Справка'))
    bot.send_message(msg.from_user.id, 'Выберите пункт меню на клавиатуре снизу', reply_markup=keyboard)


def any_user(message: Message, bot: BotDB):
    """
    Any_user - запускается по команде /start, проверяет наличие tg.id в таблице зарегистрированных пользователей,
    акцептованных администратором для использования чат-бота
    """
    bot.send_message(message.chat.id, "Добрый день! "
                                      "Вас приветствует бот поддержки команды Битрикс "
                                      "операционной группы Координационного Центра!")
    msg = bot.send_message(message.chat.id, "Выполняется проверка авторизации!")

    if not bot.is_user_auth(message):
        bot.delete_message(message.chat.id, msg.message_id)
        bot.send_message(message.chat.id, f"Нет авторизации!\n\nК сожалению Вы не можете использовать этот "
                                          f"чат-бот!\n\nНеобходимо запросить авторизацию направив письмо на эл. "
                                          f"почту s.bogdanov@ac.gov.ru, приложив следующие данные:\n"
                                          f"1) USER_ID = {str(message.chat.id)}\n"
                                          f"2) ФИО\n"
                                          f"3) Рабочий адрес эл. почты\n"
                                          f"4) Должность\n"
                                          f"\n\n Заранее спасибо и удачного дня!", parse_mode='html')
        # bot.send_message('Авторизованные пользователи:')
        # bot.send_message(bot.KC_USERS.to_dict())
    else:
        bot.delete_message(message.chat.id, msg.message_id)
        bot.send_message(message.chat.id, "Вы авторизованы и можете пользоваться сервисом!")
        send_main_menu(message, bot)


def all_users(message: Message, bot: TeleBot):
    print('function_all_users')
    pass


def get_act_by_ID(message: Message, bot):
    # bot.send_message(message.chat.id,'insert id of activity')
    ans = bot.get_activity_by_id(350)
    print('Функция отработала!' + str(ans))
    bot.reply_to(message, str(ans))
