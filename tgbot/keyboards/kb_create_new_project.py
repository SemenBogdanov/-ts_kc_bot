import telebot.types as types


def kb_activity_type(act_types, types_factory):
    kb = types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text=activity['activity_type'],
                    callback_data=types_factory.new(activity_types=activity['id'])
                )
            ]
            for activity in act_types
        ]
    )
    print('Успешно дошло до конца. Возвращаю клаву')
    return kb
