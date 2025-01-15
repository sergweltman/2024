import telebot

   # Установите ваш токен бота, который вы получили от BotFather
API_TOKEN = '7844798792:AAFWlRTqRuEovFXF1uvq4aMnUlmqMt2tipc'

   # Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

   # Функция для вычисления выражения
def calculate(expression):
    try:
           # Используем eval для вычисления выражения
        result = eval(expression)
        return result
    except Exception as e:
        return f"Ошибка: {e}"

   # Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    expression = message.text
    result = calculate(expression)
    bot.reply_to(message, f"Результат: {result}")

   # Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)