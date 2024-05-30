import telebot
from telebot.callback_data import CallbackDataFilter
from telebot.custom_filters import AdvancedCustomFilter


class ActitityCallbackFilter(AdvancedCustomFilter):
    key = 'config'

    def check(self, call: telebot.types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)