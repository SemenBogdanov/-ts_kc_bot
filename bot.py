# filters
import telebot.types
from telebot.callback_data import CallbackData

from tgbot.chains_dialog.ch_create_new_project import get_status
from tgbot.filters.custom_filters import ActitityCallbackFilter
from tgbot.filters.admin_filter import AdminFilter

# handlers
from tgbot.handlers.admin import admin_user
from tgbot.handlers.callback_handler_1 import callback_func
from tgbot.handlers.spam_command import anti_spam
from tgbot.handlers.user import any_user, all_users, get_act_by_ID
from tgbot.keyboards.main_menu import f_main_menu

# middlewares
from tgbot.middlewares.antiflood_middleware import antispam_func



# states
from tgbot.states.register_state import Register

# utils
from create_bot import BotDB

# config
from key import TOKEN

# db = BotDB()

# remove this if you won't use middlewares:
from telebot import apihelper

apihelper.ENABLE_MIDDLEWARE = True

# I recommend increasing num_threads
bot = BotDB(TOKEN)


def register_handlers():
    bot.register_message_handler(any_user, commands=['start'], pass_bot=True)
    bot.register_message_handler(f_main_menu, func=lambda message: True, content_types=['text'], pass_bot=True)

    bot.register_callback_query_handler(callback_func, func=lambda call: True, pass_bot=True)

    # bot.register_message_handler(get_updates, commands=['getUpdates'], admin=True, pass_bot=True)
    # bot.register_message_handler(admin_user, commands=['start'], admin=True, pass_bot=True)

    bot.register_message_handler(anti_spam, commands=['spam'], pass_bot=True)

    # bot.register_message_handler(all_users, commands=['allusers'], admin=True, pass_bot=True)
    # bot.register_message_handler(get_act_by_ID, commands=['getactbyid'], admin=True, pass_bot=True)


# def register_callback_query_handlers():
#     bot.register_callback_query_handler(callback=get_status, func=lambda call: True, config=types_factory.filter())


register_handlers()
# register_callback_query_handlers()

# Middlewares
bot.register_middleware_handler(antispam_func, update_types=['message'])

# custom filters
bot.add_custom_filter(AdminFilter())
bot.add_custom_filter(ActitityCallbackFilter())

while True:
    try:
        print("Бот запущен!")
        # logger.debug("Бот запущен!")
        # update_globals()
        bot.polling(none_stop=True, interval=0)
        break
    except Exception as ex:
        # glob.logger.warning("Перезагрузка бота")
        # glob.logger.warning(traceback.format_exc())
        bot.stop_polling()
