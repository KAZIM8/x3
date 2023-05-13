import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
# hithon
if os.path.exists(".env"):
    load_dotenv(".env")
# 
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")
HNDLR = os.getenv("HNDLR", "")
GROUP_MODE = os.getenv("GROUP_MODE", "True")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))
contact_filter = filters.create(    lambda _, __, message: (message.from_user and message.from_user.is_contact)    or message.outgoing)


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Hi"))
call_py = PyTgCalls(bot)
