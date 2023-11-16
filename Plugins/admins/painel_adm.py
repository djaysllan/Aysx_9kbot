from typing import Union
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import ADMINS
from database import cur, save

@Client.on_message(filters.command("painel") & filters.user(ADMINS))
@Client.on_callback_query(filters.regex("^painel$") & filters.user(ADMINS))
async def panel(c: Client, m: Union[Message, CallbackQuery]):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("⚠️ Manutenção", callback_data="bot_status"),
                InlineKeyboardButton("🏦 Lara", callback_data="change_lara"),
            ],
            [
                InlineKeyboardButton("🛠 Configs 2", callback_data="bot_config"),
            ],
        ]
    )

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text

    await send(
        "<b>🏆 | Painel adm de gerenciamento do chk:</b>\n"
        "Selecione abaixo o que você deseja visualizar ou modificar.",
        reply_markup=kb,
    )
