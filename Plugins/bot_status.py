from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)

from config import ADMINS, BOT_LINK_SUPORTE
from utils import is_bot_online, get_news_user

@Client.on_message(
    ~filters.user(ADMINS) & filters.regex(r"^/") & filters.private, group=-1
)
async def bot_status_msg(_, message: Message):
    if not is_bot_online():
        await message.reply_text(
            f"<b>😀 | Estamos fazendo uma manutenção temporária no chk volte mais tarde!!</b>"
        )
        await message.stop_propagation()


@Client.on_callback_query(~filters.user(ADMINS), group=-1)
async def bot_status_cq(_, callback_query: CallbackQuery):
    if not is_bot_online():
        await callback_query.answer(
            f"<b>😀 | Estamos fazendo uma manutenção temporária no chk volte mais tarde!!</b>",
            show_alert=True,
            cache_time=5,
        )
        await callback_query.stop_propagation()


@Client.on_inline_query(~filters.user(ADMINS), group=-1)
async def bot_status_inline(_, inline_query: InlineQuery):
    if not is_bot_online():
        results = [
            InlineQueryResultArticle(
                title="⚠ Bot em manutenção.",
                description="Tente novamente mais tarde.",
                input_message_content=InputTextMessageContent(
                    f"<b>😀 | Estamos fazendo uma manutenção temporária no chk volte mais tarde!!</b>"
                ),
            )
        ]

        await inline_query.answer(results, cache_time=5)
        await inline_query.stop_propagation()

