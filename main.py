# Mongodb database
import pymongo
from pymongo import MongoClient

# Libretranslate API
from libretranslatepy import LibreTranslateAPI
lt = LibreTranslateAPI("https://translate.argosopentech.com/")
translation = True
fromLang = "en" # default
toLang = "de" # default

# For HTTP requests
import requests
import json

# API variables
from config import environ #config stores all the environment variables
Telegram_API = environ['telegram']
MongoDB_API = environ['database']

# Initialise mongodb
cluster = MongoClient(MongoDB_API)
db = cluster["users"]
collection = db["users"]

# Enable logging
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Python-telegram-bot Functions
from telegram.ext import (
  Updater, 
  CommandHandler, 
  MessageHandler, 
  Filters, 
  ConversationHandler,
)
from telegram import (
  ReplyKeyboardMarkup,
)

# Telegram API Token
TOKEN = Telegram_API

# Ice Breaker Questions
from icebreakerquestions import questions
import random # to randomise ice breaker question

# State variables
NAME, AGE, GENDER, INTEREST, VALUE, CONTINENT, SETLANGFROM, SETLANGTO = range(8)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("hello")    

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Help_msg")

def find(update, context):
  # check private/group status
  r = requests.get(f"https://api.telegram.org/bot{TOKEN}/getChat?chat_id={update.message.chat_id}")
  status = r.json()['result']['type']

  # prevent using this function in group chat
  if (status == "group" or status == "supergroup"):
    update.message.reply_text("You can only find friends in private chat!")
    print(status)
    return
  
  update.message.reply_text("By using this telegram bot, you consent to us collecting some personal information from you. Thank you!")
  update.message.reply_text("Please input your name")
  return NAME

def name(update, context):
  update.message.reply_text("Please input your age")
  name = update.message.text
  dict["name"] = name
  return AGE

def age(update, context):
  keyboard = [["Male", "Female"]]
  update.message.reply_text("Please input your gender", reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, input_field_placeholder="Male/Female?"))
  age = update.message.text
  dict["age"] = age
  return GENDER

def gender(update, context):    
  keyboard = [
    ["Watching netflix", "Sports", "Eating",],
    ["Sleeping","Listening to music", "Gaming",],
    ["Hanging out with friends", "Baking/Cooking",],
    ["Shopping", "Working out",],
  ]
  update.message.reply_text("Please choose your interests", reply_markup=ReplyKeyboardMarkup(keyboard, resize = True, one_time_keyboard=True, input_field_placeholder="Top 3 Interests?"))

  gender = update.message.text
  dict["gender"] = gender
  return INTEREST

def interest(update, context):
  keyboard = [
    ["Loyalty", "Spirituality", "Humility",],
    ["Compassion","Honesty", "Kindness",],
    ["Attentiveness", "Empathy", "Generosity", "Religious"],
]
  update.message.reply_text("Please Choose 3 most important values to you", reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, input_field_placeholder="Top 3 Values?"))
  interest = update.message.text
  dict["interests"] = interest
  
  return VALUE

def value(update, conext):
  update.message.reply_text("Choose your continent")

  keyboard = [
    ["Asia", "Africa", "Europe",], 
    ["North America", "South America", "Australasia"],
  ]
  
  update.message.reply_text("Please input your continent",
  reply_markup=ReplyKeyboardMarkup(keyboard,
  one_time_keyboard=True, input_field_placeholder="Continent?"))
  
  value = update.message.text
  dict["values"] = value
  return CONTINENT

def continent(update, conext):  
  continent = update.message.text
  dict["continent"] = continent

  # add user's name into db
  username = update.message.from_user.username
  dict["username"] = username

  # delete user in db if previously inside
  if (collection.find({"username": username})):
    print("found")
    collection.delete_many({"username": username})

  # add user input into mongodb
  collection.insert_one(dict)
  print(dict)
    
  # find all users in database and prints its username (TO UPDATE)
  for x in collection.find():
    print(x["username"])
  
  return ConversationHandler.END

def setlang(update, context):
  # check private/group status
  r = requests.get(f"https://api.telegram.org/bot{TOKEN}/getChat?chat_id={update.message.chat_id}")
  status = r.json()['result']['type']

  # prevent using this function in private chat
  if (status == "private"):
    update.message.reply_text("This command is only available in group chat!")
    print(status)
    return
  
  update.message.reply_text("Setting language...")
  
  keyboard = [["en", "de", "es",]]
  update.message.reply_text("Please choose the language to translate from", reply_markup=ReplyKeyboardMarkup(keyboard, resize = True, one_time_keyboard=True, selective = True))
  update.message.reply_text("Available languages include: 'en', 'de', 'es'")

  return SETLANGFROM

def setlangfrom(update, context):
  global fromLang
  fromLang = update.message.text
  
  keyboard = [["en", "de", "es",]]
  update.message.reply_text("Please choose the language to translate to", reply_markup=ReplyKeyboardMarkup(keyboard, resize = True, one_time_keyboard=True, selective=True))
  update.message.reply_text("Available languages include: 'en', 'de', 'es'")

  return SETLANGTO

def setlangto(update, context):
  global toLang
  toLang = update.message.text
  return ConversationHandler.END

def toggle_translation(update, context):
  global translation
  translation = not translation
  if (translation):
    update.message.reply_text("Translation enabled!")
  else:
    update.message.reply_text("Translation disabled!")

def translate(update, context):
    """Translate the user message."""
    # check private/group status
    r = requests.get(f"https://api.telegram.org/bot{TOKEN}/getChat?chat_id={update.message.chat_id}")
    status = r.json()['result']['type']

    # prevent using this function in private chat
    if (status == "private"):
      print(status)
      return
    
    msg = update.message.text
    lang = lt.detect(msg)
    if (translation): # translation enabled
      if (lang[0]["language"] == fromLang): # forward translate
        update.message.reply_text(lt.translate(msg, fromLang, toLang))
      else: # back translate
        update.message.reply_text(lt.translate(msg, toLang, fromLang))

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def cancel(update, context):
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)

    update.message.reply_text("Your input is cancelled. Please try again.")

    return ConversationHandler.END

# Ice breaker stuff
def breakice(update, context):
    update.message.reply_text("Let's break some ice!")

    # check private/group status
    r = requests.get(f"https://api.telegram.org/bot{TOKEN}/getChat?chat_id={update.message.chat_id}")
    status = r.json()['result']['type']

    # prevent using this function in private chat
    if (status == "private"):
      print(status)
      update.message.reply_text("Please add me to a group first!")
      return

    # bot is in a group -> proceed to break some ICEEE
    update.message.reply_text(questions[random.randint(0, len(questions))])
    print(status)
  

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # conversation handler for finding friends
    find_friends = ConversationHandler(
        entry_points=[CommandHandler("find", find)],
        states={
            NAME: [MessageHandler(Filters.text & (~ Filters.command), name)],
            AGE: [MessageHandler(Filters.text & (~ Filters.command), age)],
            GENDER: [MessageHandler(Filters.text & (~ Filters.command), gender)],
            INTEREST: [MessageHandler(Filters.text & (~ Filters.command), interest)],
            VALUE: [MessageHandler(Filters.text & (~ Filters.command), value)], 
            CONTINENT: [MessageHandler(Filters.text & (~ Filters.command), continent)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # conversation handler for setting language
    set_lang = ConversationHandler(
        entry_points=[CommandHandler("setlang", setlang)],
        states={
            SETLANGFROM: [MessageHandler(Filters.text & (~ Filters.command), setlangfrom)],
            SETLANGTO: [MessageHandler(Filters.text & (~ Filters.command), setlangto)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("breakice", breakice))
    dp.add_handler(CommandHandler("toggle_translation", toggle_translation))
    dp.add_handler(find_friends)
    dp.add_handler(set_lang)

    # translate handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()