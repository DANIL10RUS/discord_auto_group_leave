import discord
import asyncio
import time
import os
import sys
import iniconfig

#
# Улучшенный код и перевод: Github: danil10rus,Discord: d10rus
#
# Любые вопросы не стесняйтесь сообщать в мой Discord Otter7070
#

# CONFIG START
dir = os.path.abspath(__file__).replace(os.path.basename(__file__), "")
cfg = iniconfig.IniConfig(f"{dir}settings.ini")

token = cfg["Settings"]["token"]
prefix = cfg["Settings"]["prefix"]
command = cfg["Settings"]["command"]
leaveMessage = cfg["Settings"]["leaveMessage"]
### CONFIG END

# Проверка токена
if token == "TOKEN" "":
    print("Ошибка! Вы не ввели токен! Прочитайте инструкцию в settings.ini!")
    time.sleep(3)
    exit()

# Клиент Discord
client = discord.Client()


@client.event
async def on_ready():
    print(
        "Проверка токена прошла успешно! Введите "
        + prefix
        + ""
        + command
        + " в любой чат, и скрипт будет выполнен!"
    )  # Сообщает пользователю, что скрипт запущен.


@client.event
async def on_message(message):
    if message.author == client.user:
        cmd = str(message.content).split(" ")
        if cmd[0] == prefix + command:
            await message.delete()
            count = 0
            for channel in client.private_channels:
                if isinstance(channel, discord.GroupChannel):
                    if (
                        channel.id != message.channel.id
                    ):  # Если сообщение было отправлено в групповом чате, то из него не будет произведён выход
                        count = count + 1

                        await channel.send(leaveMessage)
                        await channel.leave()
                        print(
                            "Вы вышли из группы по ID: " + str(channel.id)
                        )  # Выводит идентификатор группы в консоль
                        # Задержка
                        time.sleep(0.1)
            await message.channel.send(
                "``Вы вышли из групповых чатов в этом количестве: ["
                + str(count)
                + "]!``"
            )
            await client.close()  # Обновлено, потому что они изменили код по какой-то причине


# Если вы получаете ошибку неправильного токена или код 401, убедитесь, что у вас установлена версия discord.py не выше 1.7.3!

client.run(token, bot=False)
input(
    "Нажмите ENTER чтобы выйти"
)  # Позвольте пользователю ёпта, прочитать данные до того, как скрипт закроется.
