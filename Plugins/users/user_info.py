import datetime as dt
import pytz
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
from datetime import datetime, timedelta

from database import cur, save
from config import ADMINS

@Client.on_callback_query(filters.regex(r"^user_info$"))
async def user_info(c: Client, m: CallbackQuery):
    user_id = m.from_user.id
    username = m.from_user.username

    cur.execute("SELECT balance FROM users WHERE id=?", [user_id])
    result = cur.fetchone()
    if result is not None:
        balance = result[0]
    else:
        balance = 0

    submenu_keyboard = [
        [
            InlineKeyboardButton("💻 Dev", callback_data="dev_menu"),
        ],
        [
            InlineKeyboardButton("🔴 Histórico testados", callback_data="desnev_1"),
        ],
        [
            InlineKeyboardButton("<< Voltar", callback_data="start"),
        ],
    ]
    submenu_markup = InlineKeyboardMarkup(submenu_keyboard)

    menu_text = f"""<b>ℹ️ Seus dados abaixo:</b>

<b>🆔 ID: {user_id}</b>
<b>👤 User: @{username}</b>

<b>🤖 | Este bot esta em sua versão v1 podem aver erros ou bugs que devem ser reportados aos devs!!</b>

<b>⚠️ | Atualizações vão sair aqui @teslad3v</b>
"""

    await m.message.edit_text(
        menu_text,
        reply_markup=submenu_markup,
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex(r"^dev_menu$"))
async def dev_menu(c: Client, m: CallbackQuery):
    dev_name1 = "@teslaofc"
    dev_name2 = "@m4tr1xsm"
    dev_email = "@teslad3v"

    dev_info_text = f"""<b>👨‍💻 Desenvolvedores:</b>
    
<b>👤 • User:</b> {dev_name1}
<b>🔎 • Canal:</b> {dev_email}

<b>⚠️ - Não chame se vc estiver com dúvidas de como usar o chk ja esta bem explicado qualquer comando do bot. não chame se vc queira comprar ccs pois não vendemos! Não chame por qualquer coisa besta pois sera bloqueado chame se realmente for algo importante!!</b>

<b>✍️ - Alugo bots de ccs ou logins crio bots/script em geral apaenas para telegram. Não mecho com KL ou coisas relacionadas a chk de banco FGTS ou algo nesse porte!</b>
"""

    back_button = InlineKeyboardButton("Voltar", callback_data="user_info")

    await m.message.edit_text(
        dev_info_text,
        reply_markup=InlineKeyboardMarkup([[back_button]]),
        disable_web_page_preview=True
    )
    
@Client.on_callback_query(filters.regex(r"^vtex_1$"))
async def menu_chk(c: Client, m: CallbackQuery):

    dev_info_text = f"""<b>🔄 - Para testar sua info use o comando /vtex (cc)</b>

<b>Use o comando no seguinte formato:</b>

<b>/vtex 5291722832572636|05|2030|000</b>

<b>- Não teste cartões de débito!!</b>
<b>- O bot possui um limite de 50 dies por usuário se passar disso você levara ban!</b>
<b>- Limite de testes por dia e 200 ccs!</b>

<b>🟢 Gate: VTEX_1</b>
<b>⚠️ - AVISOS AQUI: @TESLAD3V/b>
"""

    back_button = InlineKeyboardButton("Voltar", callback_data="comprar_log")

    await m.message.edit_text(
        dev_info_text,
        reply_markup=InlineKeyboardMarkup([[back_button]]),
        disable_web_page_preview=True
    )