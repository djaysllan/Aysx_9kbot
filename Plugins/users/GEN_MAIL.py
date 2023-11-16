from typing import Union
import asyncio
import arrow
import io
from faker import Faker
import re
from pyrogram import Client, filters
from pyrogram.errors import BadRequest
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

fake = Faker()

async def email_genn(client: Client, chat_id: int):
    username = fake.user_name()

    email_providers = [
        "gmail.com", "yahoo.com", "outlook.com", "hotmail.com",
        "example.com", "protonmail.com", "aol.com", "icloud.com",
        "mail.com", "zoho.com", "yandex.com", "mailinator.com",
    ]

    email_provider = fake.random_element(email_providers)

    email = f"{username}@{email_provider}"

    try:
        await client.send_message(chat_id, f"<b>📪 | GMAIL GERADO COM SUCESSO: <code>{email}</code></b>\n\n- <b>USE EM SITES OU APPS!!</b>")
    except BadRequest as e:
        print(f"Erro ao enviar o email: {e}")

@Client.on_message(filters.command(["email"]))
async def gen_mail(c: Client, m: Union[Message, CallbackQuery]):
    chat_id = m.chat.id
    await email_genn(c, chat_id)