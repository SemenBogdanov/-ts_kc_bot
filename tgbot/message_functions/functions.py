def update_message_cb(bot, call, text, keyboard, parse_mode: str = 'Markdown'):
    if call.message.content_type == 'text':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text,
                              reply_markup=keyboard, parse_mode=parse_mode)
    else:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.from_user.id, text=text, reply_markup=keyboard, parse_mode=parse_mode)


def delete_message_cb(bot, call):
    bot.delete_message(call.message.chat.id, call.message.message_id)


def delete_message_mg(bot, message):
    bot.delete_message(message.chat.id, message.message_id)
