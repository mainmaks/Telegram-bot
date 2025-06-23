import os
import telebot
import random

TOKEN = '8056225723:AAGs2kI9ZMVFKhRz6ExLqcfMJoNi7sDqoOQ'

bot = telebot.TeleBot(TOKEN)
VIDEO_DIR = 'videos'
sent_videos = set()

@bot.message_handler(commands=['start'])
def start(message):
    with open('start.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption="Привет! Я Манго бот!\n\n Я отправляю эдиты/долгие ролики про манго! команда /video чтобы получить эдит ~20сек, видео пока нет 40+сек. \n\n 		b.y 1123")

@bot.message_handler(commands=['video'])
def send_video(message):
    all_videos = set(f for f in os.listdir(VIDEO_DIR) if f.endswith('.mp4'))
    remaining = list(all_videos - sent_videos)

    if not remaining:
        bot.send_message(message.chat.id, "😕 Все видео уже были отправлены. Напиши /reset чтобы начать заново.")
        return

    selected = random.choice(remaining)
    sent_videos.add(selected)

    path = os.path.join(VIDEO_DIR, selected)
    with open(path, 'rb') as vid:
        bot.send_video(message.chat.id, vid)

@bot.message_handler(commands=['reset'])
def reset(message):
    sent_videos.clear()
    bot.send_message(message.chat.id, "🔄 Список сброшен. Можно снова отправлять /video.")

bot.polling()


