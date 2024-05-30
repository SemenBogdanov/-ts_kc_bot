import telebot.types as types
from telebot.callback_data import CallbackData


from create_bot import BotDB



from tgbot.message_functions.functions import delete_message_mg


# def kb_activity_type(bot):
#     keyboard = types.InlineKeyboardMarkup(row_width=2)
#     btn1 = types.InlineKeyboardButton(text='Проекты', callback_data=f'ch_create_new_project_activity_type_project')
#     btn2 = types.InlineKeyboardButton(text='Стратгруппа', callback_data=f'ch_create_new_project_activity_type_stratgroup')
#     btn3 = types.InlineKeyboardButton(text='Инциденты', callback_data=f'ch_create_new_project_activity_type_incidents')
#     btn4 = types.InlineKeyboardButton(text='Проекты ИТ', callback_data=f'ch_create_new_project_activity_type_itproject')
#     btn5 = types.InlineKeyboardButton(text='Стратегия КЦ', callback_data=f'ch_create_new_project_activity_type_strategykc')
#     btn6 = types.InlineKeyboardButton(text='Кайцен', callback_data=f'ch_create_new_project_activity_type_kaicen')
#     btn7 = types.InlineKeyboardButton(text='Иная деятельность', callback_data=f'ch_create_new_project_activity_type_other')
#     btn8 = types.InlineKeyboardButton(text='Скрыть сообщение', callback_data=f'hide_buttons')
#     keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
#     return keyboard


def kb_activity_type(bot: BotDB, types_factory):

    ACTIVITY_TYPES = bot.ACTIVITY_TYPES
    print(ACTIVITY_TYPES)
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text=activity['name'],
                    callback_data=types_factory.new(activity_types=activity['id'])
                )
            ]
            for activity in ACTIVITY_TYPES
        ]
    )
