import telebot
from telebot.callback_data import CallbackDataFilter
from telebot.custom_filters import AdvancedCustomFilter


class ActitityCallbackFilter(AdvancedCustomFilter):
    key = 'config'

    def check(self, call: telebot.types.CallbackQuery, config: CallbackDataFilter):
        print('Выполняется провека внутри класса ActitityCallbackFilter')
        r = config.check(query=call)
        print('Результат проверки: ', r)
        return r
