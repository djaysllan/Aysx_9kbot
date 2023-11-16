from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import ADMINS
from database import cur, db
from utils import is_bot_online

def set_bot_status(status: bool):
    """Define o status do bot para o status definido."""

    cur.execute("UPDATE bot_config SET is_on = ? WHERE ROWID = 0", (status,))
    db.commit()

@Client.on_callback_query(filters.regex("^bot_status$") & filters.user(ADMINS))
async def bot_status(c: Client, m: CallbackQuery):
    is_on = is_bot_online()

    status = "✅ on" if is_on else "❌ off"
    reverse = "❌ off" if is_on else "✅ on"

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    reverse, callback_data="change_status " + reverse.split()[-1]
                ),
            ],
            [InlineKeyboardButton("🔙 Voltar", callback_data="painel")],
        ]
    )

    await m.edit_message_text(
        f"<b>🛠️ Modo manutenção:</b>\n"
        "Opção para deixar o bot em manutenção so ira funcionar para admins!!\n\n"
        f"<b>O bot está:</b> {status}",
        reply_markup=kb,
    )


@Client.on_callback_query(
    filters.regex(r"^change_status (?P<status>.+)") & filters.user(ADMINS)
)
async def change_status(c: Client, m: CallbackQuery):
    status = m.matches[0]["status"] == "on"

    set_bot_status(status)

    await m.answer(f"✅ O status foi definido para {status}")

    await bot_status(c, m)
