from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Hello! Bot is working perfectly ✅")

updater = Updater(token="8349228331:AAE55h1wtadp_-v_7uO2AJlQ4JdxvNt7TCw", use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
