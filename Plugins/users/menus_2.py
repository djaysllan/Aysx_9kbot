import asyncio
import random
import re
from datetime import datetime
from pytz import timezone
from aiogram import Bot, Dispatcher, types
from pyrogram import Client, filters
from pyrogram.errors import BadRequest
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

@Client.on_callback_query(filters.regex(r"^menu_2$"))
async def compakc_list(c: Client, m: CallbackQuery):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("📌 PATROCÍNIO", callback_data="patro"),
                InlineKeyboardButton("🟢 EMAIL_VALIDO", callback_data="email_valido"),
            ],
            [
                InlineKeyboardButton("🔙 Voltar", callback_data="start"),
            ],
        ]
    )

    await m.message.edit_text("<b>🔄 | Lista de comandos/grupos disponíveis abaixo:</b>", reply_markup=kb)

@Client.on_callback_query(filters.regex(r"^full_co$"))
async def consulta_men3u(c: Client, m: CallbackQuery):

    dev_info_text = f"""
🔎 | GRUPOS DE CONSULTA GRÁTIS DISPONÍVEL TODAS AS CONSULTAS!!

1️⃣ @HAKAICARDERS
2️⃣ @GGNATZ
3️⃣ @MAGICO_GRUPO

📌 | NÃO PRECISAR ADC!
📌 | NÃO TEM TEMPO DE ESPERA!
📌 | CONSULTAS 24/07 LIBERADAS!!
"""
    back_button = InlineKeyboardButton("Voltar", callback_data="comprar_log")

    await m.message.edit_text(
        dev_info_text,
        reply_markup=InlineKeyboardMarkup([[back_button]]),
        disable_web_page_preview=True
    )
    
@Client.on_callback_query(filters.regex(r"^lotter$"))
async def consulta_menu2(c: Client, m: CallbackQuery):

    dev_info_text = f"""
🪖 | GRUPO DE DENUNCIAR LOTTERS!!

@ANTI_LOTTERS

⚠️ - AS DENUNCIAS SAEM NO WHATSAPP FAÇA SUA DENUNCIA PARA ALGUM ADM LA AQUI NO TELEGRAM E NO @TESLAOFC!!
"""
    back_button = InlineKeyboardButton("Voltar", callback_data="comprar_log")

    await m.message.edit_text(
        dev_info_text,
        reply_markup=InlineKeyboardMarkup([[back_button]]),
        disable_web_page_preview=True
    )
    
@Client.on_callback_query(filters.regex(r"^metodos$"))
async def consulta_men1u1(c: Client, m: CallbackQuery):

    dev_info_text = f"""
✍️ CANAL DE MÉTODOS/ESQUEMAS FREE!!

@PAPUDO_TRAMPOS

📌 - TRAMPOS - ESQUEMAS - SOURCHS DISPONÍVEIS GRÁTIS NO CANAL ACIMA!!
"""
    back_button = InlineKeyboardButton("Voltar", callback_data="comprar_log")

    await m.message.edit_text(
        dev_info_text,
        reply_markup=InlineKeyboardMarkup([[back_button]]),
        disable_web_page_preview=True
    )
    
@Client.on_callback_query(filters.regex(r"^gen_email$"))
async def a_menu1(c: Client, m: CallbackQuery):

    dev_info_text = f"""
📩 | NANSO-MAIL GERADOR!!

•> PARA GERAR UM EMAIL USE O COMANDO /email
"""
    back_button = InlineKeyboardButton("Voltar", callback_data="comprar_log")

    await m.message.edit_text(
        dev_info_text,
        reply_markup=InlineKeyboardMarkup([[back_button]]),
        disable_web_page_preview=True
    )
    
@Client.on_callback_query(filters.regex(r"^patro$"))
async def con9sulta_menu1(c: Client, m: CallbackQuery):

    dev_info_text = f"""
📌 | ABAIXO PATROCINADORES DO BOT:

•> STORE DE CCS:
@HECSTECH_BOT

•> TOOLS CANAL DE MÉTODOS:
@T00lsPubl1c

✅ | NÃO TAXADOS!!
✅ | NÃO ENVOLVIDOS EM NOTAS!!
✅ | TEM REFERÊNCIAS!!

⚠️ | PARA SE TORNAR UM PATROCINADOR SEJA COM ALUGUEL OU APIS CHAME @TESLAOFC
"""
    back_button = InlineKeyboardButton("Voltar", callback_data="menu_2")

    await m.message.edit_text(
        dev_info_text,
        reply_markup=InlineKeyboardMarkup([[back_button]]),
        disable_web_page_preview=True
    )
    
@Client.on_callback_query(filters.regex(r"^gen_ggs$"))
async def pombasks_luiz(c: Client, m: CallbackQuery):

    dev_info_text = f"""<b>💳 | GERADOR DE GGS LUHN:</b>

<b>🔶 - GERADOR DE GGS VÁLIDAS!</b>

<b>✅ GERADOR DE GGS EM LUHN!</b>
<b>✅ COLOQUE A DATA E CVV!</b>
<b>✅ ELE SO IRA GERAR OS NÚMERO DA GG!</b>

<b>ℹ️ SE VC E BURRINHO E NÃO LEU ALI EM CIMA PEGA O EXEMPLO: /gen_gg (BIN) APENAS A BIN SEM LETRA SEM DATA E NEM CVV!</b>

<b>↪️ COMANDO /gen_gg</b>
"""
    back_button = InlineKeyboardButton("Voltar", callback_data="comprar_log")

    await m.message.edit_text(
        dev_info_text,
        reply_markup=InlineKeyboardMarkup([[back_button]]),
        disable_web_page_preview=True
    )
    
@Client.on_callback_query(filters.regex(r"^email_valido$"))
async def loiusmenu1(c: Client, m: CallbackQuery):

    dev_info_text = f"""
<b>📤 | GERADOR DE EMAIL VÁLIDO:</b>

<b>🟢 E-mails com os @ validos!</b>
<b>🔴 E-mails gerados via api!</b>
<b>🟣 Ainda não e possível receber o código mais em breve ser a possível!!</b>

<b>↪️ COMANDO /email_valido</b>
"""
    back_button = InlineKeyboardButton("Voltar", callback_data="menu_2")

    await m.message.edit_text(
        dev_info_text,
        reply_markup=InlineKeyboardMarkup([[back_button]]),
        disable_web_page_preview=True
    )
    
@Client.on_callback_query(filters.regex(r"^gen_pess$"))
async def gennn_pess(c: Client, m: CallbackQuery):

    dev_info_text = f"""<b>👥 GERADOR DE DADOS PESSOAIS COMPLETO!!</b>

<b>✅ | GERA TUDO COMO SE FOSSE UMA CONSULTA DE CPF NORMAL!!</b>

<b>↪️ COMANDO /gerar</b>
"""
    back_button = InlineKeyboardButton("Voltar", callback_data="comprar_log")

    await m.message.edit_text(
        dev_info_text,
        reply_markup=InlineKeyboardMarkup([[back_button]]),
        disable_web_page_preview=True
    )
