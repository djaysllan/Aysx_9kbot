from typing import Union
import asyncio
import arrow
import io
from faker import Faker
import re
import os
import shutil
from pytz import timezone
import base64
import httpx
import requests
import pytz
import apscheduler
import sqlite3
import traceback
import os
import json
import random
import time
from config import PIX_MIN, PIX_MAX
from pagamento1 import Pagamento_cu
from config import keyAsaas
from pagamentogestor import PagamentoGestor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.errors import BadRequest
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from database import cur, save, db
from config import ADMINS
from config import GRUPO_PRIV, GRUPO_ABT
from utils import create_mention, get_info_wallet, dobrosaldo
from config import BOT_LINK
from config import BOT_LINK_SUPORTE
import traceback

@Client.on_message(filters.command(["start", "menu"]))
@Client.on_callback_query(filters.regex("^start$"))
async def start(c: Client, m: Union[Message, CallbackQuery]):
    try:
        user_id = m.from_user.id

        rt = cur.execute(
            "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
        ).fetchone()

        kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton("‌️️🟢 Menu_1", callback_data="comprar_log"),
                    InlineKeyboardButton("🔴 Menu_2", callback_data="menu_2"),
                ],
                [
                    InlineKeyboardButton("👾 Achou bugs?", callback_data="bug"),
                    InlineKeyboardButton("🪪 Dados", callback_data="user_info"),
                ],
            ],
        )

        bot_logo, support_user = cur.execute(
            "SELECT main_img, support_user FROM bot_config WHERE ROWID = 0"
        ).fetchone()

        start_message = f"""<a href='{bot_logo}'>&#8204</a><b>🪖 | Bem vindo ao tesla search um oferecimento stn 4devs!!</b>
        
<b>🟢 - Melhor checker/search grátis disponível atualmente no mercado disponível para privado e grupos!!</b>
<b>⚠️ - Entre no canal e grupo para saber o status de alguma gate.</b>

<b>💻 • Meu criador @teslaofc</b>

<b>📢 | <a href='https://t.me/teslad3v'>Canal</a></b>
<b>🫂 | <a href='https://t.me/magico_grupo'>Grupo</a></b>
<b>⚠️ | <a href='https://t.me/termos_ofc'>Termos de uso(não valido para este bot)</a></b>"""

        if isinstance(m, CallbackQuery):
            send = m.edit_message_text
        else:
            send = m.reply_text
        save()
        await send(start_message, reply_markup=kb)
    except Exception as e:
        traceback.print_exc()
        
emails = []

user_data = {}

@Client.on_message(filters.command(["email_valido"]))
async def gen_mail(c: Client, m: Union[Message, CallbackQuery]):
    response_gen_mail = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
    mailbox_info = response_gen_mail.json()
    email_address = mailbox_info[0]
    emails.append({"email": email_address, "history": []})
    
    buttons = [
        [
            InlineKeyboardButton("🔴 Verificar E-mails", callback_data=f"breb"),
            InlineKeyboardButton("🔴 Ver Histórico", callback_data=f"ooaoao"),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await m.reply(f"Endereço de e-mail gerado: {email_address}", reply_markup=reply_markup)

async def check_emails(c: Client, email_index: int):
    email = emails[email_index]
    response_check_mail = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={email['email'].split('@')[0]}&domain={email['email'].split('@')[1]}")
    mail_list = response_check_mail.json()
    for mail in mail_list:
        mail_id = mail['id']
        if mail_id not in email['history']:
            email['history'].append(mail_id)
            email_subject = mail['subject']
            email_from = mail['from']
            email_date = arrow.get(mail['date']).to('local').format('YYYY-MM-DD HH:mm:ss')
            email_body_html = mail['body']
            email_body_text = html2text.html2text(email_body_html)
            await c.send_message(chat_id=m.chat.id, text=f"Novo e-mail recebido em {email['email']}:\n\nAssunto: {email_subject}\nDe: {email_from}\nData: {email_date}\n\nCorpo do e-mail:\n{email_body_text}")

@Client.on_callback_query(filters.regex(r"^cpf_1$"))
async def consulta_menu(c: Client, m: CallbackQuery):

    dev_info_text = f"""<b>🔎 | Use /cpf (cpf)</b>"""
    back_button = InlineKeyboardButton("Voltar", callback_data="comprar_log")

    await m.message.edit_text(
        dev_info_text,
        reply_markup=InlineKeyboardMarkup([[back_button]]),
        disable_web_page_preview=True
    )
    
@Client.on_callback_query(filters.regex(r"^bug$"))
async def consulta_menu(c: Client, m: CallbackQuery):

    dev_info_text = f"""<b>💻 | Achou algum erro ou bug relate para o meu criador @teslaofc</b>"""
    back_button = InlineKeyboardButton("Voltar", callback_data="start")

    await m.message.edit_text(
        dev_info_text,
        reply_markup=InlineKeyboardMarkup([[back_button]]),
        disable_web_page_preview=True
    )
    
@Client.on_callback_query(filters.regex(r"^auth_1$"))
async def menu_chk(c: Client, m: CallbackQuery):

    dev_info_text = f"""<b>🔄 - Para testar sua info use o comando /chk (cc)</b>

<b>Use o comando no seguinte formato:</b>

<b>/chk 5291722832572636|05|2030|000</b>

<b>- Não teste cartões de débito!!</b>
<b>- O bot possui um limite de 50 dies por usuário se passar disso você levara ban!</b>
<b>- Limite de testes por dia e 200 ccs!</b>

<b>🟢 Gate: Auth</b>
"""

    back_button = InlineKeyboardButton("Voltar", callback_data="comprar_log")

    await m.message.edit_text(
        dev_info_text,
        reply_markup=InlineKeyboardMarkup([[back_button]]),
        disable_web_page_preview=True
    )
    
@Client.on_message(filters.command("premium", prefixes="/") & filters.user(ADMINS))
async def premium_command(c: Client, m: Message):
    command = m.text.split(maxsplit=2)

    if len(command) < 3:
        await m.reply("Formato incorreto. Use /premium id data")
        return

    user_id = command[1]
    premium_date = command[2]

    db.execute('SELECT premium FROM users WHERE id = ?', (user_id,))
    current_premium = db.fetchone()[0]

    if current_premium:
        await m.reply("Usuário já é Premium.")
        return

    db.execute('UPDATE users SET premium = ? WHERE id = ?', (premium_date, user_id))
    conn.commit()

    await m.reply("Usuário Premium adicionado com sucesso!")