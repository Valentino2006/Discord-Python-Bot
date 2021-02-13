import discord
import os
import sys
import datetime
import random
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

bot = commands.Bot(command_prefix="d!", description="Un proyecto de Valentino Aldayr")

async def on_command_error(ctx, error) :

    if isinstance(error, commands.CommandNotFound) :
        await ctx.send('a')

@bot.command(name="ping", help="Muestra mi latencia utilizando la API de Discord", brief="[Pong!]")
async def command(ctx) :
    embed_ping = discord.Embed(title="Pong! :ping_pong: ", colour=0xff00ff)
    embed_ping.add_field(name='Tiempo de repuesta', value=f"{bot.latency} segundos", inline=True)
    await ctx.send(embed=embed_ping)
# Comando publicado en portalmybot.com 
@bot.command(name="eval", help="-Un comando que solo podran utilizar mis desarrolladores-", brief="[Un comando para evaluar codigo en python]")
async def command(ctx, args1) : # Parametros, cualquier nombre a la funcion.
    try: # Try, except, finally usaremos 
        eval_args = eval(args1) # La variable eval_args guardara un metodo nativo de python "eval(...)", dentro del metodo evaluaremos los primeros argumentos en este caso "args1" [Lo pueden llamar como sea]
        embed_eval = discord.Embed(title="Success eval!", description=f"{eval_args}", colour=0xff00ff) # La variable embed_eval guardara un DiscordEmbed con titulo, descripcion, fields, lo que quieran segun los metodos de un discord.Embed
        embed_eval.add_field(name="Type", value=type(eval_args)) # El tipo de lo que evaluamos ...eval_args
        if ctx.author.id != 410211404969410592 : # Si la id del author del mensaje no es igual a int(...) [Ahi pones tu ID, en este caso yo puse el mio]
            await ctx.send("No eres desarrollador para utilizar este comando")  # Enviamos un mensaje
        else : # Si no es asi enviamos el embed_eval
            await ctx.send(embed=embed_eval)
    except NameError as error: # El nombre del error se guardara en la variable error [Pueden llamarla como quieran]
        await ctx.send("{0}".format(error)) # Enviamos
    finally: # Finalmente enviamos esto por algunas cosas cuando se ignoran en el except
        await ctx.send("Output: ✅") 
@bot.command(name="stats", help="Muestra mis estadisticas como bot de discord", brief="[Mis estadisticas]")
async def command(ctx) :
    embed_stats = discord.Embed(title="Mis Estadisticas", colour=0xff00ff).set_author(name=ctx.me, icon_url=ctx.me.avatar_url)
    embed_stats.add_field(name="Plataforma", value=sys.platform)
    embed_stats.add_field(name="Version", value=f"Python: {sys.version}, \n API Version: {sys.api_version} \n Discord Python Version: {discord.__version__}")
    embed_stats.add_field(name="Estadisticas como Discord Bot", value=f"Servidores: {len(bot.guilds)} \n Emojis: {len(bot.emojis)} \n Usuarios: {len(bot.users)} \n Canales Privados en los que estoy participando: {len(bot.private_channels)}")
    await ctx.send(embed=embed_stats)
@bot.command(name="avatar", help="Muestra el avatar de un usuario por id, mencion...", brief="[Muestra el avatar de un usuario]")
async def a(ctx, member: discord.Member) :
    try:
        if member :
            user_discord = member 
            embed_avatar = discord.Embed(title=f'{user_discord} Avatar', colour=0xff00ff, timestamp=datetime.datetime.now())
            embed_avatar.set_image(url=f"{user_discord.avatar_url}")
            await ctx.send(embed=embed_avatar)
        elif ctx.author :
            user_discord = ctx.author
            await ctx.send(embed=embed_avatar)
    except NameError as error :
        await ctx.send(f"Algun error ocurrio... {error}")
@bot.command(name="guild_info", help="Muestra informacion detallada de la guild en la que enviaste el mensaje", brief="[Informacion del servidor actual]")
async def algun_nombre(ctx) :
    embed_guild_info = discord.Embed(title=f"Informacion de {ctx.guild.name}", colour=0xff00ff).set_author(name=f"{ctx.guild.name} - {ctx.guild.id}", icon_url=ctx.guild.icon_url)
    embed_guild_info.add_field(name="Contador", value=f"Usuarios: {ctx.guild.member_count} \n Emojis: {len(ctx.guild.emojis)} \n Canales de Voz: {len(ctx.guild.voice_channels)} \n Canales de Texto: {len(ctx.guild.text_channels)} \n Total de canales: {len(ctx.guild.channels)} \n Roles: {len(ctx.guild.roles)} \n Categorias: {len(ctx.guild.categories)}")
    embed_guild_info.add_field(name="Server Boost", value=f"Nivel del servidor: {ctx.guild.premium_tier} \n Total de mejoras: {ctx.guild.premium_subscription_count} \n Usuarios mejorando el servidor: {len(ctx.guild.premium_subscribers)} \n Rol: {ctx.guild.premium_subscriber_role} \n Mejoras especiales: {ctx.guild.features}")
    embed_guild_info.add_field(name="Links", value=f"Banner URL: {ctx.guild.banner_url} \n Imagen del Servidor URL: {ctx.guild.icon_url}")
    embed_guild_info.add_field(name="Otros", value=f"Canal de Reglas: {ctx.guild.rules_channel} \n Nivel MFA: {ctx.guild.mfa_level} \n Nivel de Verificacion: {ctx.guild.verification_level} \n Fecha de creacion del servidor: {ctx.guild.created_at} \n Region: {ctx.guild.region}")
    await ctx.send(embed=embed_guild_info)
@bot.command(name="kick", help="Expulsa a un miembro del servidor", brief="[Expulsa a un miembro del servidor]")
async def some_function(ctx, member: discord.Member) :
    try :
        # print(args1)
        await member.kick(reason=None)
        await ctx.send(f"Miembro expulsado del servidor, \n datos= ID: {member.id} \n Nombre de Usuario: {member}")
    except NameError as error :
        await ctx.send(f"Algun error ocurrio ...{error}")
    finally :
        print(f"{ctx.author}")
@bot.command(name="ban", help="Banea a un miembro del servidor", brief="[Banea a un miembro del servidor]")
async def some_random_function(ctx, member: discord.Member) :
    try :
        await member.ban(reason=None)
        await ctx.send(f"Miembro baneado del servidor, \n datos= ID: {member.id} \n Nombre de Usuario: {member}")
    except NameError as error :
        ctx.send(f"Algun error ocurrio ...{error}")
    finally :
        print(f"{ctx.author}")
@bot.command(name="how_gay", help="Muestra un porcentaje aleatorio mas un string de lo tan gay que eres", brief="[Que tan gay eres?]")
async def some_random_crazy_function(ctx) :
    try :
        random_porcentaje = random.choice([10, 20, 30, 40, 50, 60, 70 , 80, 90, 100])
        await ctx.send(f'🏳️‍🌈{ctx.author} es {random_porcentaje}% gay')
    except NameError as error : 
        await ctx.send(f"Algun error ocurrio ...{error}")
    finally :
        print(f"{ctx.author}")
@bot.event
async def on_ready() :
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"    Nombre de usuario: {bot.user}")
    print(f"    ID del usuario: {bot.user.id}")
    print(f"    Discord.py Version: {discord.__version__}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    await bot.change_presence(status= discord.Status.idle, activity=discord.Activity(type=5, name="prefix = d! && d!help"))
bot.run(os.getenv("DISCORD_BOT_TOKEN"))