import requests
import time
from pyrogram import Client, filters
from pyrogram.types import Message

API_CPF = "http://aaaaaa/dev-consult/sus.php?cpf="
last_command_time = {}

@Client.on_message(filters.command(["cpf"]))
async def cpf_aqui(c: Client, m: Message):
    if len(m.command) != 2:
        await m.reply("⚠️ Comando incorreto. Use o comando com o número de CPF!!")
        return

    user_id = m.from_user.id
    current_time = time.time()
    last_time = last_command_time.get(user_id, 0)
    elapsed_time = current_time - last_time

    if elapsed_time < 4:
        await m.reply("⏳ Por favor, aguarde 4 segundos antes de testar um novo CPF.")
        return

    last_command_time[user_id] = current_time

    cpf_number = m.command[1]
    api_url = f"{API_CPF}{cpf_number}"

    try:
        response = requests.get(api_url)
        data = response.json()

        if "result" in data and "hits" in data["result"]:
            hits = data["result"]["hits"]["hits"]
            if hits:

                response_text = f"""
<b>🔎 Dados do cpf {cpf_number}:</b>

<b>Nome:</b> <code>{nome}</code>
<b>Data de Nascimento:</b> <code>{data_nascimento}</code>
<b>Sexo:</b> <code>{sexo}</code>
<b>Endereço:</b> <code>{endereco}, {bairro}, {municipio}, {uf}</code>

<b>📍 - Patrocinador: @T00lsPubl1c</b>

<b>@TESLACHK_BOT</b>
"""
                await m.reply(response_text)
            else:
                await m.reply("🔴 CPF não encontrado na base de dados.")
        else:
            await m.reply("🔴 Não foi possível obter informações do CPF. Tente novamente mais tarde.")
    except Exception as e:
        await m.reply(f"❌ Erro: {str(e)}")
