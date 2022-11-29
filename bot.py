import os
import telebot
import requests
import bs4

from grabber import getSakuga

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)
sadD = os.getenv('sakD')

@bot.message_handler(commands=['daily'])
def daily(message):
  fSak=getSakuga()
  
  bot.send_message(message.chat.id, fSak)


@bot.message_handler(commands=['info'])
def info(message):
  bot.send_message(message.chat.id, "https://github.com/Mishikiari/KitaBot")

bot.polling()