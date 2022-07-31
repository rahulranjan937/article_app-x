import os
from dotenv import load_dotenv

load_dotenv()

dbHost = os.environ.get("host")
dbuser = os.environ.get("user")
dbpasswd = os.environ.get("password")
dbport = os.environ.get("port")
db = os.environ.get("database")

dbHost = "bv2rebwf6zzsv341.cbetxkdyhwsb.us-east-1.rds.amazonaws.com"
dbuser = "qq39ysw6ticedsg9"
dbpasswd = "wv6ve6ntpzp2eta9"
dbport = "3306"
db = "u7non66wzzet8ss7"
