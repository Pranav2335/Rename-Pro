import os

class Config(object):
     # get a token from @BotFather
     TOKEN = os.environ.get("TOKEN", "")
     # The Telegram API things
     APP_ID = int(os.environ.get("APP_ID", ""))
     API_HASH = os.environ.get("API_HASH", "")
     #Array to store users who are authorized to use the bot
     ADMIN = os.environ.get("ADMIN", "1484847208")
     #Your Mongo DB Database Name
     DB_NAME = os.environ.get("DB_NAME", "Prv")
     #Your Mongo DB URL Obtained From mongodb.com
     DB_URL = os.environ.get("DB_URL", "")
