import discord
import os
import sys
import datetime
import random
import subprocess
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
@bot.command(name="member_info", help="Mira la informacion de un miembro", brief="[Mira la informacion de un miembro]")
async def some_function_random_ctx(ctx, member: discord.Member) :
    try :
        #member = discord.Member
        #options =  member or ctx.author
        activity = None or member.activity.name
        user_info_embed = discord.Embed(colour=0xff00ff).set_author(name=f"{member} ~ {member.id}", icon_url=member.avatar_url)
        user_info_embed.add_field(name=f"Entro a el servidor {ctx.guild}", value=member.joined_at)
        user_info_embed.add_field(name="Roles", value=str(member.roles))
        user_info_embed.add_field(name="Actividad", value=activity)
        user_info_embed.add_field(name="Estado", value=member.status)
        user_info_embed.add_field(name="Rol mas alto", value=member.top_role)
        user_info_embed.add_field(name=f"Permisos en el servidor {ctx.guild}", value=member.guild_permissions)
        user_info_embed.add_field(name="Estado Mobil", value=member.mobile_status)
        user_info_embed.add_field(name="Estado Web", value=member.web_status)
        user_info_embed.add_field(name="Estado de aplicacion de escritorio", value=member.desktop_status)
        user_info_embed.add_field(name="Banderas Publicas", value=member.public_flags)
        user_info_embed.add_field(name="Creo su cuenta de discord", value=member.created_at)
        user_info_embed.add_field(name="Es alguien del sistema como Discord", value=member.system)
        user_info_embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=user_info_embed)
        #await ctx.send(options.id)
    except :
        await ctx.send("Una excepcion ocurrio...")
    finally : 
        await ctx.send("Recuerda que si ocurrio una excepcion es porque algo fallo.")
@bot.command(name="role_info", help="Muestra informacion de un rol, requiere mencion", brief="[Muestra informacion de un rol]")
async def role_info_command_function(ctx, role: discord.Role):
    if role.mentionable == False:
        mentionable_latin = "No"
    elif role.mentionable == True:
        mentionable_latin = "Si"
        pass
    role_info_command_embed = discord.Embed(colour=0xff00ff).set_author(name=f"{role.name} ~ {role.id}")
    role_info_command_embed.add_field(name="Rol creado el", value=role.created_at)
    role_info_command_embed.add_field(name="Colores del rol", value=f"{role.colour} ~ {role.color}")
    role_info_command_embed.add_field(name=f"MIembros del servidor {ctx.guild} con el rol", value=len(role.members))
    role_info_command_embed.add_field(name="Posicion del rol", value=role.position)
    role_info_command_embed.add_field(name="Permisos del rol", value=role.permissions)
    role_info_command_embed.add_field(name="Mencionable por los usuario(general)", value=mentionable_latin)
    await ctx.send(embed=role_info_command_embed)
# Comando publicado en portalmybot.com
@bot.command(name="say", help="Mando un mensaje segun los argumentos que pongas despues del comando", brief="[Digo lo que tu dices]") # Utilizaremos discord.ext.commands para este comando, necesitaran poner un nombre, ayuda, breve ayuda
async def say_command_function(ctx): # Funcion asincrona con cualquier nombre, parametro ctx (context)
    mentions = ("@everyone", "@here") # En la variable mentions guaradara una tupla con cadenas (str tuple)
    var_1 = ctx.message.content # En la variable var_1 guardara lo que contiene el mensaje que se envio 
    if var_1.startswith(mentions) or var_1.endswith(mentions) or var_1 == f"d!say {mentions}" : # Si var_1 comienza o termina con mentions o var_1 es igual a <prefiz>say mentions, cuando de true la condicion se pasara al siguiente bloque de codigo
        await ctx.send("No puedes mencionar a everyone ni a here") # Enviamos un mensaje
    else : # Si no dio true la sentencia de arriba, pasaremos a este bloque de codigo llegando a el fin
        await ctx.send(ctx.message.content) # Enviamos finalmente lo que contiene el mensaje
@bot.command(name="unban", help="Remueve el baneo de un miembro baneado, es necesario su ID del usuario baneado", brief="[Remueve un baneo]")
async def some_random_function_unban(ctx, args1):
    ctx_member = await bot.fetch_user(args1)
    await ctx.guild.unban(ctx_member)
    await ctx.send(f"El miembro <@{ctx_member}> ~ {ctx_member.id} fue removido de la lista de baneados, ya puede ingresar de nuevo al servidor")
@bot.command(name="exec", help="Ejecuta comandos en terminales bash / shell con este comando", brief="[Ejecuta comandos en la consola]")
async def exec_command_function_random(ctx, args1):
    try:
        res = subprocess.call(args1, shell=False)
        await ctx.send(res)
    except:
        await ctx.send("Una excepcion ocurrio...")
    finally:
        await ctx.send("Output: ✅")
@bot.command(name="emoji_info", help="Muestra la informacion detallada de un emoji, requiere introducir el emoji en el 1er argumento", brief="[Muestra informacion detallada de un emoji]")
async def some_random_function_emoji_info(ctx, emoji: discord.Emoji):
    true_false = {
        True: "Si",
        False: "No",
    }
    print(emoji.url)
    emoji_info_embed = discord.Embed(colour=0xff00ff).set_author(name=f"{emoji.name} ~ {emoji.id}", icon_url=emoji.url).set_thumbnail(url=emoji.url)
    emoji_info_embed.add_field(name="Animado", value=true_false[emoji.animated])
    emoji_info_embed.add_field(name="Creado el", value=emoji.created_at)
    emoji_info_embed.add_field(name="Administrado por alguna integracion por Twitch", value=true_false[emoji.managed])
    emoji_info_embed.add_field(name="Requiere :: por el cliente", value= true_false[emoji.require_colons])
    emoji_info_embed.add_field(name="Usalo de la siguiente manera", value=f"`<:{emoji.name}:{emoji.id}>`") 
    emoji_info_embed.add_field(name="Disponible", value=true_false[emoji.available])
    await ctx.send(embed=emoji_info_embed)
@bot.command(name="ascii", help="Devuelve un string convertido a una representacion imprimible de un objeto", brief="[Devuelve una version imprimible del texto]")
async def some_random_ascii_function(ctx, args1):
    cifrado = ascii(args1)
    await ctx.send(f"Cifrado correcto={cifrado}")
@bot.event
async def on_ready():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"    Nombre de usuario: {bot.user}")
    print(f"    ID del usuario: {bot.user.id}")
    print(f"    Discord.py Version: {discord.__version__}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    await bot.change_presence(status= discord.Status.idle, activity=discord.Activity(type=5, name="prefix = d! && d!help"))
bot.run(os.getenv("DISCORD_BOT_TOKEN"))