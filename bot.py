import os
from telethon import TelegramClient, events

# Данные Telegram API
API_ID = 31298491
API_HASH = "6c27838f93668b66eb1215238c2aca8a"

# Твой канал
TARGET =  "@novostokmsw"

# Каналы-источники
SOURCES = [
    "@moscowmap",
]

client = TelegramClient(
    "novostok_session",
    API_ID,
    API_HASH
)


@client.on(events.NewMessage(chats=SOURCES))
async def new_post(event):
    try:
        await client.send_message(
            TARGET,
            event.message
        )

        print("Новая публикация отправлена")

    except Exception as error:
        print("Ошибка:", error)


async def main():
    print("Бот запущен")
    await client.run_until_disconnected()


with client:
    client.loop.run_until_complete(main())