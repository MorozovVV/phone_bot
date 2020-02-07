import os
import telebot
from telebot import types
TOKEN = os.environ["TOKEN"]

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(content_typs=['text'])
def get_text_messages(message):
    phonenomber = '';
    phonenomber = message.text;
    bot.send_message(message.from_user.id, 'htts://api.whatsapp.com/send?phone=' + phonenomber)
bot.polling(none_stop=True, interval=1)
