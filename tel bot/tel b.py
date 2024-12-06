
import telebot
import webbrowser

from telebot.util import webhook_google_functions

bot = telebot.TeleBot('7941294693:AAGPvRbxGdiOZ6F8TGDv0-SfP3cM0khcljs')


@bot.message_handler(commands=['site','Website'])
def site(message):
    webbrowser.open('https://erp.student.najottalim.uz/login')

@bot.message_handler(commands=['support'])
def support(message):
    bot.send_message(message.chat.id,'Последнняя домашнняя работа это с 21 до - 29')

@bot.message_handler(commands=['homework'])
def homework(message):
    bot.send_message(message.chat.id,'Последнняя домашнняя работа это с 21 до - 29')


@bot.message_handler(commands=['start'])
def support(message):
    bot.send_message(message.chat.id,f'hi how are you,{message.from_user.first_name}')



#@bot.message_handler(commands=['start'])
#def main(message):
    #bot.send_message(message.chat.id, f'hi how are you, {message.from_user.first_name} {message.from_user.last_name}' )

#@bot.message_handler()
#def info(message):
#    if message.text.lower() == 'привет':
#        bot.send_message(message.chat.id,f'hi how are you, {message.from_user.first_name} {message.from_user.last_name}')
#    elif message.text.lower() == 'id':
#        bot.reply_to(message, f'ID: {message.from_user.id} ')


bot.polling(none_stop=True)