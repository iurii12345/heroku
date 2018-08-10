# как написать бота

'''
fdgdf
fhdhdg
hjghj
'''

import telebot
from telebot import TeleBot

import constants
import descriptions
import prices

bot: TeleBot = telebot.TeleBot(constants.token)

# bot.send_message(5527665, "Тест")


print(bot.get_me())


def log(message, answer):
    print('\n ------')
    from datetime import datetime
    print(datetime.now())
    print('Сообщение от {0} {1}  (id = {2}) \n {3}'.format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print('Ответ бота \n', answer)


@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Дженерики Виагры', 'Дженерики Левитры', 'Дженерики Сиалиса')
    bot.send_message(message.from_user.id, 'Добро пожаловать!', reply_markup=user_markup)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Мои возможности весьма специфичны!')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = 'Я не понимаю 😕'
    if message.text == 'Дженерики Виагры':
        answer = descriptions.sildenafil
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Силденафил 100 мг')
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
        log(message, answer)
    elif message.text == 'Силденафил 100 мг':
        answer = 'Цены: \n 1 шт. - {0} \n 5 шт. - {1} \n 10 шт. - {2} \n 20 шт. - {3}'.format(prices.sildenafil100_1,
                                                                                              prices.sildenafil100_5,
                                                                                              prices.sildenafil100_10,
                                                                                              prices.sildenafil100_20)
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('999')
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
        log(message, answer)
    else:
        bot.send_message(message.from_user.id, answer)
        log(message, answer)


bot.polling(none_stop=True, interval=0)
