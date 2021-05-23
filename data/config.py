import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))
DBHOST = str(os.getenv("DBHOST"))
ADMINS = str(os.getenv("ADMINS"))

ip = os.getenv("ip")

admins = [
    str(os.getenv("ADMINS"))
]

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 5432),
    'encoding': 'utf8'
}

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"

USERNAME_ADMIN1 = os.getenv("USERNAME_ADMIN1")
USERNAME_ADMIN2 = os.getenv("USERNAME_ADMIN2")
