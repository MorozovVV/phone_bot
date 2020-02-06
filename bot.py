import telebot
from telebot import types
phonenomber = '';
bot = telebot.TeleBot('%%')
@bot.message_handler(content_typs=['text'])
def get_text_messages(message):
    global phonenomber;
    phonenomber = message.text;
    bot.send_message(message.from_user.id, 'htts://api.whatsapp.com/send?phone='+phonenomber)
bot.polling(none_stop=True, interval=0)