import asyncio
import os
import shutil
import tarfile
from datetime import datetime, timedelta
from pyrogram import Client, idle
from pyrogram.session import Session
from pyrogram.enums import ParseMode
from config import API_HASH, API_ID, BOT_TOKEN, WORKERS

BACKUP_DIR = f"{os.path.expanduser('~')}/backups"
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

CHAT_ID = 5508410205
BACKUP_INTERVAL = 90
BACKUP_ITEMS = [
    "plugins",
    "config.py",
    "main.db",
    "main.db-shm",
    "main.db-wal",
    "saved.txt",
    "ANTI_RETESTE.txt",
    "GG.txt",
]

def delete_session_files():
    for file_name in ["bot.session", "bot.session-shm", "bot.session-wal"]:
        if os.path.exists(file_name):
            os.remove(file_name)

async def main():
    delete_session_files()

    client = Client(
        "bot",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        workers=WORKERS,
        parse_mode=ParseMode.HTML,
        plugins={"root": "plugins"},
    )

    Session.notice_displayed = True

    await client.start()
    print("Bot rodando...")
    client.me = await client.get_me()

    while True:
        now = datetime.now()
        backup_file = f"{BACKUP_DIR}/backup-{now.strftime('%Y-%m-%d_%H-%M-%S')}.tar.gz"

        with tarfile.open(backup_file, "w:gz") as tar:
            for item in BACKUP_ITEMS:
                if os.path.isfile(item):
                    tar.add(item)
                elif os.path.isdir(item):
                    tar.add(item, arcname=os.path.basename(item))

        await client.send_document(chat_id=CHAT_ID, document=backup_file)

        os.remove(backup_file)

        await asyncio.sleep(BACKUP_INTERVAL * 60)

    await client.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
