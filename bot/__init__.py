# Fuck yea 👍
import logging
from logging.handlers import RotatingFileHandler
import os
import time
from pyrogram import Client


# TODO: is there a better way?




from bot.config import Config




AUTH_USERS = [1938207469,5154542366,-1001729288604]

SESSION_NAME = "WtfMan"
TG_BOT_TOKEN = "5342477919:AAGTcxHd1QY8K1wZ6zQTUPFurGrKh6b5R3c"
APP_ID = 2630541
API_HASH = "b3829c7abc1b23a555a6b2b2b236e016"

LOG_CHANNEL = "llapajsx"  # make sure to us this 
DOWNLOAD_LOCATION = "/app/downloads"
FREE_USER_MAX_FILE_SIZE = 2097152000
MAX_MESSAGE_LENGTH = 4096
FINISHED_PROGRESS_STR = "▓"
UN_FINISHED_PROGRESS_STR = "░"
BOT_START_TIME = time.time()
CHAT_ID = -1001729288604
LOG_FILE_ZZGEVC = "Log.txt"
BOT_USERNAME = "namansirBot"
UPDATES_CHANNEL = "Animedubed"
data = []
crf = []
watermark = []
resolution = []
codec = []
preset = []
audio_b = []

pid_list = []
app = Client(
        SESSION_NAME,
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        workers=2
    )
if os.path.exists(LOG_FILE_ZZGEVC):
    with open(LOG_FILE_ZZGEVC, "r+") as f_d:
        f_d.truncate(0)

# the logging things
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=FREE_USER_MAX_FILE_SIZE,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)
