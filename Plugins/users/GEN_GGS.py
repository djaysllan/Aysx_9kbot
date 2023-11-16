from typing import Union
import random

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_message(filters.command(["gen_gg"]))
async def gen_ggs(c: Client, m: Union[Message, CallbackQuery]):
    chat_id = m.chat.id
    command_text = m.text.split(" ")
    if len(command_text) == 2:
        bin_value = command_text[1]
        cc_list = generate_cc(bin_value, 20)

        if len(cc_list) == 20:
            formatted_cc = "\n".join([f"{cc}" for cc in cc_list])
            message = (
                f"<b>💳 | GGS GERADAS COM SUCESSO:</b>\n\n<code>{formatted_cc}</code>\n\n"
                f"<b>🟣 Quantidade:</b> <code>20</code>\n"
                f"<b>🟢 Bin:</b> <code>{bin_value}</code>\n"
                f"<b>🔴 Geradas via algoritmo de luhn</b>\n"
                f"<b>⚠️ Aviso: Foi gerado apenas o número do cartão coloque a data e o cvv</b>\n"
            )
        else:
            message = "<b>⚠️ Não foi possível gerar as 20 GGS. Tente novamente com um BIN válido!!</b>"

        await c.send_message(chat_id, message)
    else:
        await c.send_message(chat_id, "<b>⚠️ Comando inválido. Use /gg (bin)</b>")

def generate_cc(bin_value, num_ggs):
    results = []

    while len(results) < num_ggs:
        count = bin_value[:12]
        digits = 16 - len(count)
        cc_resto = ''.join(random.choice("0123456789") for _ in range(digits))
        number = bin_value + cc_resto

        sum_table = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]]
        sum_value = 0
        flip = 0
        for i in range(len(number) - 1, -1, -1):
            sum_value += sum_table[flip & 0x1][int(number[i])]
            flip += 1

        if sum_value % 10 == 0:
            results.append(number)

    return results
