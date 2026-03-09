import telebot
import os
from flask import Flask
from threading import Thread

# سيرفر صغير عشان الاستضافة ما تفصلش
app = Flask('')

@app.route('/')
def home():
    return "Bot is Alive!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# التوكن بتاعك
TOKEN = "8690470203:AAEhLBtLVLnkjWZj_fjDsywzX6rkApTEE9Y"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ البوت شغال دلوقتي على الاستضافة 24 ساعة!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "رسالتك وصلتني يا بطل!")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
