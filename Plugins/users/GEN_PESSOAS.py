from typing import Union
import random
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_message(filters.command(["gerar"]))
async def gen_ggs(c: Client, m: Union[Message, CallbackQuery]):
    chat_id = m.chat.id

    def generate_cpf():
        return "".join([str(random.randint(0, 9)) for _ in range(11)])

    def generate_birthdate():
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(1950, 2005)
        return f"{day:02d}/{month:02d}/{year}"

    def generate_name():
        first_names = ["Diego", "João", "Maria", "Pedro", "Terezinha", "Lucia"]
        last_names = ["Silva", "Santos", "Oliveira", "Souza", "Ferreira"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def generate_address():
        streets = ["RUA", "AVENIDA", "PRAÇA", "ALAMEDA", "RODOVIA"]
        cities = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Salvador"]
        states = ["SP", "RJ", "MG", "RS", "BA"]
        return {
            "logradouro": f"{random.choice(streets)} {generate_name()}",
            "numero": random.randint(1, 999),
            "complemento": f"{random.choice(['SEM INFORMAÇÃO', 'APTO', 'CASA'])} {random.randint(1, 100)}",
            "bairro": generate_name(),
            "cidade": random.choice(cities),
            "estado": random.choice(states),
            "pais": "BRASIL",
            "cep": random.randint(10000000, 99999999)
        }

    cor = random.choice(["Branco", "Negro", "Pardo", "Amarelo", "Indígena"])
    tipo_sanguineo = random.choice(["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
    mae = generate_name()
    pai = generate_name()
    nacionalidade = random.choice(["BRASILEIRA", "ESTRANGEIRA"])
    cidade_nascimento = random.choice(["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Salvador"])
    estado_nascimento = random.choice(["SP", "RJ", "MG", "RS", "BA"])
    address = generate_address()
    email = "SEM INFORMAÇÃO"
    telefone1 = random.randint(1100000000, 1199999999)
    telefone2 = random.randint(1100000000, 1199999999)
    telefone3 = random.randint(1100000000, 1199999999)

    message = f"""
🔍 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗗𝗘 𝗖𝗣𝗙 🔍

• CPF: {generate_cpf()}

• CNS: SEM INFORMAÇÃO

• RG: SEM INFORMAÇÃO
• DATA DE EXPEDIÇÃO: SEM INFORMAÇÃO
• ORGÃO EXPEDIDOR: SEM INFORMAÇÃO
• UF - RG: SEM INFORMAÇÃO

• NOME: {generate_name()}
• NASCIMENTO: {generate_birthdate()}
• IDADE: {2023 - int(generate_birthdate().split('/')[-1])}
• SIGNO: {random.choice(["Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem", "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes"])}

• COR: {cor}
• TIPO SANGUÍNEO: {tipo_sanguineo}

• MÃE: {mae}
• PAI: {pai}

• NACIONALIDADE: {nacionalidade}
• CIDADE DE NASCIMENTO: {cidade_nascimento}
• ESTADO DE NASCIMENTO: {estado_nascimento}

• LOGRADOURO: {address['logradouro']}
• NÚMERO: {address['numero']}
• COMPLEMENTO: {address['complemento']}
• BAIRRO: {address['bairro']}
• CIDADE: {address['cidade']}
• ESTADO: {address['estado']}
• PAÍS: {address['pais']}
• CEP: {address['cep']}

• EMAIL: {email}

• TELEFONE: {telefone1}
• OPERADORA: DESCONHECIDA

• TELEFONE: {telefone2}
• OPERADORA: DESCONHECIDA

• TELEFONE: {telefone3}
• OPERADORA: DESCONHECIDA

🔛 BY: @TESLACHK_BOT
"""

    await c.send_message(chat_id, message)
