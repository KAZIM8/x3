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


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["ريست"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("اني")
    await loli.edit("احبك")
    await loli.edit("@YTLTY")
    await loli.edit("انتضر")
    await loli.edit("هسه")
    await loli.edit("شويه")
    await loli.edit("او")
    await loli.edit("يشتغل")
    await loli.edit("@hithin")
    await loli.edit("تم شتغل[.](https://telegra.ph/file/7156094e1d7b093d32f3a.mp4) ")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.command(["اوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b> hi {m.from_user.mention}!

الاوامر [.](https://telegra.ph/file/7156094e1d7b093d32f3a.mp4) Bot Music 

التشغيل أغنيه : دز امر 'شغل' + اسم الاغنيه 
التشغيل فيديو : دز امر 'شغل_فيد' + اسم الاغنيه او المقطع 
———————————————————

اذا تريد توقف مؤقت : دز امر 'استئناف'
اذا تريد توكف الاستئناف : دز امر 'ايقاف_استئناف'
اذا تريد توكف الاغنيه : دز امر 'اوكف او اسكت'

———————————————————

اذا تريد تحمل اغنيه : دز امر 'حمل '+ اسم الاغنيه
اذا تريد فيد : دز امر 'حمل_فيد' او 'نزل فيد 


قناة السورس : 

The Channel : @hithon
 The developer : @ytlty
"""
    await m.reply(HELP)
@Client.on_message(filters.command(["سورس"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>  hi {m.from_user.mention}!

 **hithon music boots**


The Channel : @hithon
 The developer : @ytlty
"""
    await m.reply(REPO, disable_web_page_preview=True)
