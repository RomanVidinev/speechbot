from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from  voice import text_to_file
TOKEN = " Здесь нужно вставить свой номер токена для Телеграма "

def hello(update, context):
    update.message.reply_text(f'Hello {update.effective_user.first_name}') # при вводе команды /hello, выдается имя, зарегестрированное пользователем

def help_handler(update, context):
    help_text = """Для того, чтобы преобразовать текст в аудио, используйте наш бот. Напишите или скопируйте и вставьте любой текст, и он превратится в аудио сообщение."""
    update.message.reply_text(help_text) # при вводе команды /help, выдается строка выше

def reply(update, context):
    file_name = text_to_file(update.message.text)
    update.message.reply_voice(voice = open(file_name, 'rb')) # функция для вывода звукового файла, обращается к файлу voice.py


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

updater.start_polling()
updater.idle()
