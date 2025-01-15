import telebot
from openai import OpenAI
from gtts import gTTS
import os

# Инициализация клиента API OpenAI с вашим API ключом
client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Инициализация Telegram бота с вашим токеном
bot = telebot.TeleBot("7844798792:AAFWlRTqRuEovFXF1uvq4aMnUlmqMt2tipc")

# Словарь для хранения истории разговора для каждого пользователя
user_conversation_history = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который может отвечать на ваши вопросы. Задавайте их!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    user_input = message.text

    # Инициализация истории разговора для нового пользователя
    if user_id not in user_conversation_history:
        user_conversation_history[user_id] = []

    # Добавление ввода пользователя в историю разговора
    user_conversation_history[user_id].append({"role": "user", "content": user_input})

    # Отправка запроса в нейронную сеть
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=user_conversation_history[user_id]
        )

        # Извлечение и отправка ответа нейронной сети
        ai_response_content = chat_completion.choices[0].message.content
        bot.reply_to(message, ai_response_content)

        # Добавление ответа нейронной сети в историю разговора
        user_conversation_history[user_id].append({"role": "system", "content": ai_response_content})

        # Озвучивание текста
        tts = gTTS(text=ai_response_content, lang='ru')
        audio_file = f"response_{user_id}.mp3"
        tts.save(audio_file)

        # Отправка аудиофайла пользователю
        with open(audio_file, 'rb') as audio:
            bot.send_voice(message.chat.id, audio)

        # Удаление временного аудиофайла
        os.remove(audio_file)

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")

# Запуск бота
bot.polling()