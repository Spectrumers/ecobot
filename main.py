import telebot
import random
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

eco_tips = [
    "Используй многоразовую кружку вместо одноразовых стаканчиков.",
    "Выключай воду, пока чистишь зубы — это экономит до 10 литров!",
    "Сортируй пластик: бутылки с маркировкой 1 (PET) принимают почти везде.",
    "Замени обычные пакеты на тканевую сумку (шоппер)."
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Эко-Помощник. "
                          "Я здесь, чтобы делиться полезными советами. "
                          "Напиши /tips, чтобы получить совет!")

@bot.message_handler(commands=['tips'])
def send_tip(message):
    tip = random.choice(eco_tips)
    bot.reply_to(message, f"💡 Эко-совет: {tip}")

if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)