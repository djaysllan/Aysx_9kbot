from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from config import ADMINS
from database import cur, save

OPTIONS = {
    "Menu imagem": "main_img",
    "Suporte": "support_user",
}

@Client.on_callback_query(filters.regex(r"^bot_config$") & filters.user(ADMINS))
async def option_edit(c: Client, m: CallbackQuery):
    keyboard = []
    for k, v in OPTIONS.items():
        keyboard.append([InlineKeyboardButton(text=k, callback_data=f"edit {v}")])
    keyboard.append([InlineKeyboardButton(text="🔙 Voltar", callback_data="painel")])
    kb = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await m.message.edit_text(
        "<b>🔄 Config imagem/suporte:\n</b>"
        "<b>Selecione abaixo o que você deseja alterar:</b>",
        reply_markup=kb,
    )

@Client.on_callback_query(filters.regex(r"^edit (?P<item>\w+)") & filters.user(ADMINS))
async def edit_config(c: Client, m: CallbackQuery):
    msg_type = {
        "main_img": "<b>Imagem do menu (www.tesla.br)</b>",
        "support_user": "<b>Novo suporte do bot (@suporte)",
    }

    item = m.matches[0]["item"]

    if item not in msg_type:
        return
    await m.message.delete()
    new_arg = await m.message.ask(
        f"<b>para editar o </b> {msg_type[item]} <b> mande como o exemplo do ()!!</b>",
        reply_markup=ForceReply(),
    )
    if new_arg == "/cancel":
        return
    else:
        cur.execute(f"UPDATE bot_config SET {item}=?", [new_arg.text])
        kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton("🔙 Voltar", callback_data="painel")],
            ]
        )
        await m.message.reply_text("<b>✅ Item alterado com sucesso</b>", reply_markup=kb)
        save()
