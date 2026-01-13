import discord
import random
# Importar pass_gen do bot_logic.py  
from bot_logic import pass_gen

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    # da tarefa
    elif message.content.startswith('.senha'):
        await message.channel.send("Sua senha é: " + pass_gen(10))
    # ------------------
    # da tarefa 2
    elif message.content.startswith('.caraoucoroa'):
        random1 = random.randint(1,2)
        if random1 == 1:
            await message.channel.send("A moeda saiu cara!")
        elif random1 == 2:
            await message.channel.send("A moeda saiu coroa!")
    # --------------------
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

client.run('teste')

