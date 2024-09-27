import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands = ['selam'])
def selam(message):
    bot.reply_to(message, 'selam, endet neh')
@bot.message_handler(commands = ['help'])
def help(message):
    bot.send_message(message.chat.id, 'mn lrdah??')

bot.polling()