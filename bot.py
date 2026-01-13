import discord
from discord.ext import commands
import random
# Importar pass_gen do bot_logic.py  
from bot_logic import pass_gen
import os
import aiohttp

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def senha(ctx):
    await ctx.send("Sua senha é: " + pass_gen(10))

@bot.command()
async def caraoucoroa(ctx):
    random1 = random.randint(1,2)
    if random1 == 1:
        await ctx.send("A moeda saiu cara!")
    elif random1 == 2:
        await ctx.send("A moeda saiu coroa!")

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def emoji(ctx):
    await ctx.send(":sob:")

@bot.command()
async def gif(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1114663006438178889/1368031073384267796/STK-20250502-WA0000.webp?ex=69397078&is=69381ef8&hm=eb92b2a74e8146a8978048036b0436be2033626961dc785fb2e21e0c21169017&")

@bot.command()
async def users(ctx):
    quantidade = ctx.guild.member_count
    await ctx.send(f"Hão {quantidade} usuários no servidor")

@bot.command()
async def id(ctx):
    user_id = ctx.author.id
    await ctx.send(f"Seu id é {user_id}")

@bot.command()
async def meme(ctx):
    rand = random.randint(1,10)
    if rand == 1 or rand == 2 or rand == 3 or rand == 4:
        with open("imagens/meme1-prog.jpg" , "rb") as f:
            image = discord.File(f)
            await ctx.send("Meme Comum!")
            await ctx.send(file = image)
    elif rand == 5 or rand == 6 or rand == 7:
        with open("imagens/meme2-prog.jpg" , "rb") as f:
            image = discord.File(f)
            await ctx.send("Meme Raro!")
            await ctx.send(file = image)
    elif rand == 8 or 9:
        with open("imagens/meme3-prog.webp" , "rb") as f:
            image = discord.File(f)
            await ctx.send("Meme Épico!")
            await ctx.send(file = image)
    elif rand == 10:
        with open("imagens/meme4-prog.jpeg" , "rb") as f:
            image = discord.File(f)
            await ctx.send("Meme Lendário!")
            await ctx.send(file = image)
        
async def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            data = await res.json()
            return data['url']


@bot.command()
async def duck(ctx):
    image_url = await get_duck_image_url()
    await ctx.send(image_url)



bot.run('teste')
