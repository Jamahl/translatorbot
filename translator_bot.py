from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Send me a message in English or Spanish, and I will translate it.')

def translate_text(update, context):
    """Translate the user's message to the opposite language (English <-> Spanish) and send the translation."""
    user_message = update.message.text  # Get the text from the user
    
    # Detect the language of the user's message
    detected_language = translator.detect(user_message).lang

    # Determine the target language based on the detected language
    if detected_language == 'en':
        target_language = 'es'
    elif detected_language == 'es':
        target_language = 'en'
    else:
        update.message.reply_text('Please send me messages in English or Spanish.')
        return

    # Translate the message to the target language
    translated = translator.translate(user_message, dest=target_language)
    update.message.reply_text(translated.text)  # Send the translated text back to the user

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("6818149753:AAHADC6yYLe8h6tFrRvhb85x_Xyon7zapWQ", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # On the command /start, send the start message
    dp.add_handler(CommandHandler("start", start))

    # On receiving a text message, translate it
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_text))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM, or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
