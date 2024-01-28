import psutil
import time
import requests

token = "your-discord-token-here"
delay = 5
status = "online"

while True:
    RAM = psutil.virtual_memory()[2]
    CPU = psutil.cpu_percent(2)

    RAM = "RAM: " + str(RAM) + "%"
    CPU = "CPU: " + str(CPU) + "%"

    final = CPU + " " + RAM

    response = requests.patch(
        'https://canary.discord.com/api/v9/users/@me/settings',
        json={'custom_status': {'text': final}, 'status': status},
        headers={'Content-Type': 'application/json', 'Authorization': token}
    )

    time.sleep(delay)

