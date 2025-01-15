import telebot
  # Замените 'YOUR_BOT_TOKEN' на токен вашего бота, полученный от BotFather
TOKEN = '7844798792:AAFWlRTqRuEovFXF1uvq4aMnUlmqMt2tipc'
bot = telebot.TeleBot(TOKEN)
# Обработчик для сообщений с текстом "привет"
@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def greet(message):
    bot.reply_to(message, "Привет! Как я могу помочь вам?")
# Обработчик для сообщений с текстом "как дела?"
@bot.message_handler(func=lambda message: message.text.lower() == "как дела?")
def how_are_you(message):
    bot.reply_to(message, "У меня всё отлично! Спасибо, что спросили. А у вас?")
# Запуск бота
bot.polling()