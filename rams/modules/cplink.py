import asyncio
import os
import time
from pyrogram.types import *
from pyrogram import *
from pyrogram import Client, filters, enums
from geezlibs.ram.helpers.basic import *
from geezlibs.ram.helpers.PyroHelpers import *
from geezlibs.ram.utils.misc import *
from geezlibs.ram.utils.tools import *
from geezlibs.ram import pyram, ram

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

@pyram("cp", ram)
async def kangcopy(client: Client, message: Message):
    mmk = await message.reply_text("`Processing . . .`")
    link = get_arg(message)
    bot = "Nyolong_lagi_bot"
    if not link:
        return await mmk.edit("Link nya mana ngentot!!")
    if link:
        try:
            await asyncio.sleep(1.5)
            await client.join_chat("sharinguserbot")
            await client.join_chat("pornhpub")
            await client.join_chat("userbotch")
        except Exception as e:
            return await mmk.edit(message, f"**ERROR:** `{e}`")
        try:
            await asyncio.sleep(1.5)
            tai = await mmk.edit("`Berhasil Mencuri...`")
            a = await client.send_message(bot, link)
            await asyncio.sleep(2)
            await a.delete()
            await tai.delete()
            async for c in client.get_chat_history(bot, limit=1):
                await c.copy(message.chat.id)
            await client.delete_message(bot, link)
        except BaseException:
            pass
        try:
            async for f in client.search_messages(message.chat.id, query="Trying to Download."):
                await f.delete()
            async for o in client.search_messages(message.chat.id, query="DOWNLOADING:"):
                await o.delete()
            async for g in client.search_messages(message.chat.id, query="Preparing to Upload!"):
                await g.delete()
        except BaseException:
            pass

@pyram("tt", ram)
async def kangtiktok(client: Client, message: Message):
    mmk = await message.reply_text("`Processing . . .`")
    link = get_arg(message)
    bot = "downloader_tiktok_bot"
    if not link:
        return await mmk.edit("Link nya mana ngentot!!")
    if link:
        try:
            await asyncio.sleep(1.5)
            await client.join_chat("pornhpub")
            await client.join_chat("userbotch")
        except Exception as e:
            return await mmk.edit(message, f"**ERROR:** `{e}`")
        try:
            await asyncio.sleep(1.5)
            tai = await mmk.edit("`Berhasil Mendownload...`")
            a = await client.send_message(bot, link)
            await asyncio.sleep(2)
            await a.delete()
            await tai.delete()
            async for c in client.get_chat_history(bot, limit=1):
                await c.copy(message.chat.id, caption="Powered by ©️ Geez|Ram")
            await client.delete_message(bot, link)
        except BaseException:
            pass
        try:
            async for f in client.search_messages(message.chat.id, query="Trying to Download."):
                await f.delete()
            async for o in client.search_messages(message.chat.id, query="DOWNLOADING:"):
                await o.delete()
            async for g in client.search_messages(message.chat.id, query="Preparing to Upload!"):
                await g.delete()
        except BaseException:
            pass

@pyram("ig", ram)
async def kangsosmed(client: Client, message: Message):
    mmk = await message.reply_text("`Processing . . .`")
    link = get_arg(message)
    bot = "saveasbot"
    if not link:
        return await mmk.edit("Link nya mana ngentot!!")
    if link:
        try:
            await asyncio.sleep(1.5)
            await client.join_chat("pornhpub")
            await client.join_chat("userbotch")
        except Exception as e:
            return await mmk.edit(message, f"**ERROR:** `{e}`")
        try:
            await asyncio.sleep(1.5)
            tai = await mmk.edit("`Berhasil Mendownload...`")
            a = await client.send_message(bot, link)
            await asyncio.sleep(2)
            await a.delete()
            await tai.delete()
            async for c in client.get_chat_history(bot, limit=2):
                await c.copy(message.chat.id, caption="Powered by ©️ Geez|Ram")
            await client.delete_message(bot, link)
        except BaseException:
            pass
        try:
            async for f in client.search_messages(message.chat.id, query="Trying to Download."):
                await f.delete()
            async for o in client.search_messages(message.chat.id, query="DOWNLOADING:"):
                await o.delete()
            async for g in client.search_messages(message.chat.id, query="Preparing to Upload!"):
                await g.delete()
        except BaseException:
            pass

@pyram("pint", ram)
async def kangsos(client: Client, message: Message):
    mmk = await message.reply_text("`Processing . . .`")
    link = get_arg(message)
    bot = "PinterestDownloaderDevsBot"
    if not link:
        return await mmk.edit("Link nya mana ngentot!!")
    if link:
        try:
            await asyncio.sleep(1.5)
            await client.join_chat("userbotch")
            await client.join_chat("pornhpub")
        except Exception as e:
            return await mmk.edit(message, f"**ERROR:** `{e}`")
        try:
            await asyncio.sleep(1.5)
            tai = await mmk.edit("`Berhasil Mendownload...`")
            a = await client.send_message(bot, link)
            await asyncio.sleep(2)
            await a.delete()
            await tai.delete()
            async for c in client.get_chat_history(bot, limit=1):
                await c.copy(message.chat.id, caption="Powered by ©️ Geez|Ram")
            await client.delete_message(bot, link)
        except BaseException:
            pass
        try:
            async for f in client.search_messages(message.chat.id, query="Trying to Download."):
                await f.delete()
            async for o in client.search_messages(message.chat.id, query="DOWNLOADING:"):
                await o.delete()
            async for g in client.search_messages(message.chat.id, query="Preparing to Upload!"):
                await g.delete()
        except BaseException:
            pass
# ==================================
#          LO NGENTOT
# ==================================
from pyrogram.types import Message
from geezlibs import logging
from geezlibs.ram.helpers.basic import edit_or_reply

@pyram("toanime", ram)
async def convert_image(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("Please Reply to photo")
    if message.reply_to_message:
        await message.edit("processing ...")
        await logging(client)
    reply_message = message.reply_to_message
    photo = reply_message.photo.file_id
    bot = "qq_2d_ai_bot"
    await client.send_photo(bot, photo=photo)
    await asyncio.sleep(18)
    async for result in client.search_messages(bot, limit=1):
        if result.photo:
            await message.edit("uploading...")
            converted_image_file = await client.download_media(result)
            await client.send_photo(message.chat.id, converted_image_file, caption="Powered by ©️ Geez|Ram")
            await message.delete()
        else:
            await message.edit("error message ...")


@pyram("jurus", ram)
async def deepfry(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("Reply Foto Untuk Mengedit")
    if message.reply_to_message:
        await message.edit("Gua bikin Jelek Fotolu nih!!!...")
        await logging(client)
    reply_message = message.reply_to_message
    photo = reply_message.photo.file_id
    bot = "image_deepfrybot"
    if not photo:
        return await message.edit("ini bukan foto bgst!!!!")
    await client.send_photo(bot, photo=photo)
    await asyncio.sleep(3)
    async for result in client.search_messages(bot, limit=1):
        if result.photo:
            await message.edit("utiwiii maszehh...")
            converted_image_file = await client.download_media(result)
            await client.send_photo(message.chat.id, converted_image_file, caption="Powered by ©️ Geez|Ram")
            await message.delete()
        else:
            await message.edit("error message ...")
