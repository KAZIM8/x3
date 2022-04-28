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


@Client.on_message(filters.command(["ب"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("لحضه..")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>-›  بنك</b> `{delta_ping * 1000:.3f} ms` \n<b>-›  وقت</b> - `{uptime}`"
    )


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["تح"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("اني")
    await loli.edit("احبك")
    await loli.edit("@YTLTY")
    await loli.edit("انتضر")
    await loli.edit("هسه")
    await loli.edit("شويه")
    await loli.edit("او")
    await loli.edit("يحدث")
    await loli.edit("@hithon")
    await loli.edit("خلاص اشتغل[.](https://telegra.ph/file/733cc4e44a383f9e9f8ce.mp4) ")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.command(["اوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b> hi {m.from_user.mention}!

**Bot Music**

**التشغيل أغنيه** : دز امر '.ش' + اسم الاغنيه 
**التشغيل فيديو** : دز امر '.ش_فيد' + اسم الاغنيه او المقطع 
———————————————————
**اذا تريد توقف مؤقت** : دز امر 'استئناف'
**اذا تريد توكف الاستئناف** : دز امر 'ايقاف_استئناف'
**اذا تريد توكف الاغنيه** : دز امر '.اوكف او .اسكت'
———————————————————
**اذا تريد تحمل اغنيه** : دز امر '.ح'+ اسم الاغنيه
**اذا تريد فيد** : دز امر '.ح_فيد' او 'نزل فيد 
———————————————————
**اذا تريد تتخطى اغنيه** : امر ".سكب"
——————————————————

The Channel : @hithon
 The developer : @ytlty [.](https://telegra.ph/file/cb593816385ad8318d9c3.mp4) 
"""
    await m.reply(HELP)
@Client.on_message(filters.command(["مطور"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""

# await m.reply_to_message.delete()
                await m.reply_video(
                    video="https://telegra.ph/file/1e0632f3f03c75efc530e.mp4",

<b>  هلا {m.from_user.mention}

**تحديث V.2**

The Music Userbot
 The developer : @ytlty 
"""
    await m.reply(REPO, disable_web_page_preview=True)
