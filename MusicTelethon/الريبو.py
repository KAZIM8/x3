import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (    ("Minggu", 60 * 60 * 24 * 7),    ("Hari", 60 * 60 * 24),    ("Jam", 60 * 60),    ("Menit", 60),    ("Detik", 1),)
async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["تحديث"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("هلا")
    await loli.edit("جاي")
    await loli.edit("يحدث")
    await loli.edit("اصبر")
    await loli.edit("شويه")
    await loli.edit("@YTLTY")
    await loli.edit("@hithon")
    await loli.edit("يالله")
    await loli.edit("احبكم")
    await loli.edit("خلاص اشتغل[.](https://telegra.ph/file/1964cfb699e4eb20b926e.mp4) ")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.command(["م"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b> Hi {m.from_user.mention}!

**Bot Music**

**التشغيل أغنيه** : دز امر 'شغل' + اسم الاغنيه 
**التشغيل فيديو** : دز امر 'شغل_فيد' + اسم الاغنيه او المقطع 
———————————————————
**اذا تريد توقف مؤقت** : دز امر 'استئناف'
**اذا تريد توكف الاستئناف** : دز امر 'ايقاف_استئناف'
**اذا تريد توكف الاغنيه** : دز امر 'اوكف او اسكت'
———————————————————
**اذا تريد تحمل اغنيه** : دز امر 'حمل '+ اسم الاغنيه
**اذا تريد فيد** : دز امر 'حمل_فيد' او 'نزل فيد 

The Channel : @hithon
 The developer : @ytlty [.](https://telegra.ph/file/a3d723cb19ec27399dd7f.mp4)
"""
    await m.reply(HELP)
@Client.on_message(filters.command(["مطور"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>  Hi {m.from_user.mention}!

The Beta Userbot 
 The developer : @ytlty [.](https://telegra.ph/file/cedfcd25edfcdf8acc466.mp4)
"""
    await m.reply(REPO, disable_web_page_preview=True)
