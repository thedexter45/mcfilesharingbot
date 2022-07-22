#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://github.com/CodeXBotz/File-Sharing-Bot'>Click here</a>\n○ Channel : @CodeXBotz\n○ Support Group : @CodeXBotzSupport</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [[
            InlineKeyboardButton('😊𝙰𝙳𝙼𝙸𝙽', url='https://t.me/dexte_r_46')
        ], [
            InlineKeyboardButton('🎭 𝙲𝙷𝙰𝙽𝙽𝙴𝙻', url='https://t.me/MC_Moviescafe'),
            InlineKeyboardButton('🍿 𝙶𝚁𝙾𝚄𝙿', url='https://t.me/MOVIE_CAFE_no1')
        ], [
            InlineKeyboardButton("ℹ️ About Me", callback_data = "about"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close")
        ]]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
