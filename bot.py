import bs4, requests, os
import telebot
from bs4 import BeautifulSoup

from keep_alive import keep_alive
keep_alive()

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

def getSakuga():
    try:
        url = "https://www.sakugabooru.com/post/random"
        bUrl = "https://www.sakugabooru.com/data/"

        response = requests.get(url)
        response.raise_for_status()
        global current_url
        current_url = response.url
        soup = BeautifulSoup(response.text, 'html.parser')
        divSak = soup.find(class_='original-file-unchanged')
        sakD = divSak.find(bUrl)
        fSak = str(divSak.get('href'))
        print(current_url)
        if bUrl in fSak:
            return fSak
    except Exception as e:
        print("Errore durante il recupero dei dati:", e)
        return None

@bot.message_handler(commands=['random'])
def send_random_video(message):
    video_url = getSakuga()
    if not video_url:
        bot.send_message(message.chat.id, "weird error, try again!")
        return

    try:
        response = requests.get(video_url)
        response.raise_for_status()
        with open('sakuga.mp4', 'wb') as f:
            f.write(response.content)
        video = open('sakuga.mp4', 'rb')

        markup = telebot.types.InlineKeyboardMarkup()
        artist_button = telebot.types.InlineKeyboardButton(text="Vai alla pagina", url=current_url)
        markup.add(artist_button)

        bot.send_video(message.chat.id, video, reply_markup=markup)
        video.close()
        os.remove('sakuga.mp4')
    except Exception as e:
        print("Errore durante l'invio del video:", e)
        bot.send_message(message.chat.id, "weird error, try again!")

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, "https://github.com/Mishikiari/KitaBot")

bot.polling()
