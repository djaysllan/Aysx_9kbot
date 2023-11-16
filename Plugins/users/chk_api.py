import asyncio
import random
import re
from datetime import datetime
from pytz import timezone
from pyrogram import Client, filters
from aiogram import Bot, Dispatcher, types
from pyrogram.errors import BadRequest
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

bot_token = "6158517732"
bot = Bot(bot_token)
ADMIN_CHANNEL_IDS = [-1001764836994, -1001895292818]

CARD_REGEX = re.compile(r'^(?!0{6,})(?!.*\|00\|)\d{16}\|(?!0{2})\d{2}\|(?!00)\d{4}\|\d{3}')

@Client.on_callback_query(filters.regex(r"^comprar_log$"))
async def comprar_doc_list(c: Client, m: CallbackQuery):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("🔴 Auth_2", callback_data="outrooos"),
                InlineKeyboardButton("🟢 Auth", callback_data="auth_1"),
            ],
            [
                InlineKeyboardButton("🟢 VTEX", callback_data="vtex_1"),
                InlineKeyboardButton("🟢 CPF", callback_data="cpf_1"),
            ],
            [
                InlineKeyboardButton("🔴 NOME", callback_data="nome_1"),
                InlineKeyboardButton("🔴 TEL", callback_data="tel_1"),
            ],
            [
                InlineKeyboardButton("🟢 GEN_MAIL", callback_data="gen_email"),
                InlineKeyboardButton("🟢 GEN_PESSOA", callback_data="gen_pess"),
            ],
            [
                InlineKeyboardButton("🟢 GEN_GG", callback_data="gen_ggs"),
                InlineKeyboardButton("🟢 GG_CHK", callback_data="gg_1"),
            ],
            [
                InlineKeyboardButton("🔴 INDEX", callback_data="index_1"),
                InlineKeyboardButton("🟢 ANTI_LOTTER", callback_data="lotter"),
            ],
            [
                InlineKeyboardButton("🟢 MÉTODOS️", callback_data="metodos"),
                InlineKeyboardButton("🟢 CONSULTAS", callback_data="full_co"),
            ],
            [
                InlineKeyboardButton("🔙 Voltar", callback_data="start"),
            ],
        ]
    )

    await m.message.edit_text("<b>🔄 | Lista de comandos/grupos disponíveis abaixo:</b>", reply_markup=kb)

async def enviar_esp(chat_id: int):
    message = await bot.send_message(chat_id, "⏳ - Testando, aguarde...")
    await asyncio.sleep(3)
    return message

def netfree(card_data):
    with open("ANTI_RETESTE.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if card_data in line.strip():
                return True
    return False

async def porrado_aiogram(card_data):
    if netfree(card_data):
        return "<b>⚠️ | Esse cartão já foi testado anteriormente. Não é possível realizar o teste novamente.</b>"

    card_info = card_data.split("|")
    expiration_year, expiration_month = int(card_info[2]), int(card_info[1])

    current_date = datetime.now(timezone('America/Sao_Paulo')).date()
    if (expiration_year < current_date.year) or (expiration_year == current_date.year and expiration_month < current_date.month):
        return "<b>❌ | Cartão expirado! Por favor, forneça um cartão válido.</b>"

    result = generate_result()
    response = f"""<b>💳 | TESTE FINALIZADO!!</b>

<code>{card_data}</code>

<b>🔄 - Resultado: </b>
<b>🟢 - Gate: AUTH</b>
<b>⏳ - Tempo:  segundos</b>
<b>🪖 - Resposta: </b>
    """
    return response

user_test_status = {}

@Client.on_message(filters.command("chk"))
async def check_card(c: Client, m: types.Message):
    user_id = m.from_user.id

    if not await is_user_in_bot_channels(user_id):
        await m.reply("""🟢 | ATENÇÃO USUÁRIO PARA UTILIZAR O CHK ENTRE NOS CANAIS/GRUPOS ABAIXO EM TDS:

1️⃣ @TESLAD3V
2️⃣ @ANTI_LOTTERS
3️⃣ @MAGICO_GRUPO

🔎 - GRUPO DE CONSULTAS FREE @HAKAICARDERS | @GGNATZ

⚠️ - TOMOU LOTTER? FAÇA SUA DENUNCIA PARA UM ADM AQUI:
https://linktr.ee/anti_lotters

😃 LEMBRANDO QUE PARA USAR O CHK SO PRECISA ENTRAR NOS 3 PRIMEIROS GRUPOS!!
""")
        return