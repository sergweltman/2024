# API_TOKEN = '7844798792:AAFWlRTqRuEovFXF1uvq4aMnUlmqMt2tipc'
import telebot

# Замените 'YOUR_TELEGRAM_API_TOKEN' на ваш реальный токен, полученный от BotFather
TELEGRAM_API_TOKEN = '7844798792:AAFWlRTqRuEovFXF1uvq4aMnUlmqMt2tipc'

# Создание экземпляра бота
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я ваш новый Telegram-бот.")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Вот список доступных команд:\n"
        "/start - Начать взаимодействие с ботом\n"
        "/help - Получить список команд"
    )
    bot.reply_to(message, help_text)

# Запуск бота
bot.polling()