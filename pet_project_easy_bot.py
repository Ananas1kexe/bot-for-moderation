#MADE BY ANANAS1K  | ananas1k47 #

import disnake

from datetime import datetime, timedelta
from disnake import ButtonStyle
from disnake.ui import Button, View
from disnake.ext import commands

intents = disnake.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

@bot.event
async def on_ready():
    print(f"Бот {bot.user} запустился")
    activity = disnake.Game(name="made by ananas1k")
    await bot.change_presence(status=disnake.Status.online, activity=activity)
    

@bot.slash_command(description="Замьютить пользователя")
@commands.has_permissions(moderate_members=True)
async def mute(ctx, user: disnake.User, reason: str = None, duration: int = None):
    if ctx.guild.me.top_role <= user.top_role:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="Роль бота слишком низкая для выполнение этой команды",
            color=disnake.Color.red()
        )
        return embed
    if ctx.author.top_role <= user.top_role:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="У вас нет прав чтоб замьютить человека с более высокой ролью!",
            color=disnake.Color.red()
        )
        return embed
    
    if user.current_timeout:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description=f"У {user.name} уже есть активный мьют",
            color=disnake.Color.red()
        )
        await ctx.send(embed=embed, ephemeral=True)
        return

        
    if reason is None:
        reason = "Нет причины"
    if duration is None:
        duration = 10
    
    try:
        time = datetime.now() + timedelta(minutes=duration)    
        await user.timeout(until=time, reason=reason)
        embed = disnake.Embed(
            title="Пользователю был выдан мьют",
            description=f"** Краткая информация: **\nВыдал мьют: **@{ctx.author.name}**\nМут был выдан: **@{user.name}**\n Причина: **{reason}**\n Время: {duration}",
            color=disnake.Color.green()
        )
        await ctx.send(embed=embed, ephemeral = True)
        guild = user.guild
        if guild.system_channel:
            embed = disnake.Embed(
            title="Пользователю был выдан мьют",
            description=f"** Краткая информация: **\nВыдал мьют: **@{ctx.author.name}**\nМут был выдан: **@{user.name}**\n Причина: **{reason}**\n Время: {duration}",
            color=disnake.Color.green()
            )
            await guild.system_channel.send(embed=embed)
    except Exception as e:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description=f"Произошла ошибка  {e}\n"
            "Вы можете написать на сервер поддержки бота. Чтоб зайти на сервер нажмите на кнопку Cервер поддержки",
            color=disnake.Color.red()
        )
        button_support = Button(label="Cервер поддержки", url="https://discord.gg/KmskWpN5nb", style=disnake.ButtonStyle.link)
        
        view = View
        view.add_item(button_support)
        await ctx.send(embed = embed, view=view, ephemeral = True)
    
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, disnake.ext.commands.MissingPermissions):
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="У вас нет нужных прав чтобы использовать эту команду",
            color=disnake.Color.red()
        )
        await ctx.send(embed=embed, ephemeral=True)
        
        
@bot.slash_command(description="Размьютить пользователя")
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, user: disnake.User, reason: str = None):
    if ctx.guild.me.top_role <= user.top_role:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="Роль бота слишком низкая для выполнение этой команды",
            color=disnake.Color.red()
        )
        return embed
    if ctx.author.top_role <= user.top_role:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="У вас нет прав чтоб разамьютить человека с более высокой ролью!",
            color=disnake.Color.red()
        )
        return embed
    
    if not user.current_timeout:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description=f"У {user.name} уже снят мьют",
            color=disnake.Color.red()
        )
        await ctx.send(embed=embed, ephemeral=True)
        return
    if reason is None:
        reason = "Нет причины"
    
    try:
        await user.timeout(until=None, reason=reason)
        embed = disnake.Embed(
            title="Пользователю был снят мьют",
            description=f"** Краткая информация: **\nВыдал мьют: **@{ctx.author.name}**\nМут был выдан: **@{user.name}**\n Причина: **{reason}**\n",
            color=disnake.Color.green()
        )
        await ctx.send(embed=embed, ephemeral = True)
        
        guild = user.guild
        if guild.system_channel:
            embed = disnake.Embed(
            title="Пользователю был выдан мьют",
            description=f"** Краткая информация: **\nВыдал мьют: **@{ctx.author.name}**\nМут был выдан: **@{user.name}**\n Причина: **{reason}**\n",
            color=disnake.Color.green()
            )
            await guild.system_channel.send(embed=embed)
    except Exception as e:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description=f"Произошла ошибка  {e}\n"
            "Вы можете написать на сервер поддержки бота. Чтоб зайти на сервер нажмите на кнопку Cервер поддержки",
            color=disnake.Color.red()
        )
        button_support = Button(label="Cервер поддержки", url="https://discord.gg/KmskWpN5nb", style=disnake.ButtonStyle.link)
        
        view = View
        view.add_item(button_support)
        await ctx.send(embed = embed, view=view, ephemeral = True)

@unmute.error
async def mute_error(ctx, error):
    if isinstance(error, disnake.ext.commands.MissingPermissions):
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="У вас нет нужных прав чтобы использовать эту команду",
            color=disnake.Color.red()
        )
        await ctx.send(embed=embed, ephemeral=True)
        

@bot.slash_command(description="Выгнать пользователя с сервера")
@commands.has_permissions(administrator=True) #так же можно поставить moderate_members если вы хотите чтоб пользователь с правами модера мог тоже кикать ПРИМИЧАНИЕ!!! ПРАВА АДМИНА И МОДЕРА ОТЛИЧАЮТЬСЯ
async def kick(ctx, user: disnake.User, reason: str = None): 
    if ctx.guild.me.top_role <= user.top_role:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="Роль бота слишком низкая для выполнение этой команды",
            color=disnake.Color.red()
        )
        return embed
    if ctx.author.top_role <= user.top_role:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="У вас нет прав чтоб разамьютить человека с более высокой ролью!",
            color=disnake.Color.red()
        )
        return embed
    
    if reason is None:
        reason = "Нет причины"
    
    try:
        await user.kick(until=None, reason=reason)
        embed = disnake.Embed(
            title="Пользователь был кикнут",
            description=f"** Краткая информация: **\nКикнул мьют: **@{ctx.author.name}**\nКикнули: **@{user.name}**\n Причина: **{reason}**\n",
            color=disnake.Color.green()
        )
        await ctx.send(embed=embed, ephemeral = True)
        
        guild = user.guild
        if guild.system_channel:
            embed = disnake.Embed(
            title="Пользователь был кикнут",
            description=f"** Краткая информация: **\nКикнул мьют: **@{ctx.author.name}**\nКикнули: **@{user.name}**\n Причина: **{reason}**\n",
            color=disnake.Color.green()
            )
            await guild.system_channel.send(embed=embed)
    except Exception as e:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description=f"Произошла ошибка  {e}\n"
            "Вы можете написать на сервер поддержки бота. Чтоб зайти на сервер нажмите на кнопку Cервер поддержки",
            color=disnake.Color.red()
        )
        button_support = Button(label="Cервер поддержки", url="https://discord.gg/KmskWpN5nb", style=disnake.ButtonStyle.link)
        
        view = View
        view.add_item(button_support)
        await ctx.send(embed = embed, view=view, ephemeral = True)

@kick.error
async def mute_error(ctx, error):
    if isinstance(error, disnake.ext.commands.MissingPermissions):
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="У вас нет нужных прав чтобы использовать эту команду",
            color=disnake.Color.red()
        )
        await ctx.send(embed=embed, ephemeral=True)
        
        
        



@bot.slash_command(description="Замьютить пользователя")
@commands.has_permissions(moderate_members=True)
async def ban(ctx, user: disnake.User, reason: str = None):
    if ctx.guild.me.top_role <= user.top_role:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="Роль бота слишком низкая для выполнение этой команды",
            color=disnake.Color.red()
        )
        return embed
    if ctx.author.top_role <= user.top_role:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="У вас нет прав чтоб замьютить человека с более высокой ролью!",
            color=disnake.Color.red()
        )
        return embed
    

        
    if reason is None:
        reason = "Нет причины"

    
    try:
            
        await user.ban(until=None, reason=reason)
        embed = disnake.Embed(
            title="Пользователя забанили",
            description=f"** Краткая информация: **\nЗабанил: **@{ctx.author.name}**\nЗабанили: **@{user.name}**\n Причина: **{reason}**\n",
            color=disnake.Color.green()
        )
        await ctx.send(embed=embed, ephemeral = True)
        guild = user.guild
        if guild.system_channel:
            embed = disnake.Embed(
                title="Пользователя забанили",
                description=f"** Краткая информация: **\nЗабанил: **@{ctx.author.name}**\nЗабанили: **@{user.name}**\n Причина: **{reason}**\n",
                color=disnake.Color.green()
                )
            await guild.system_channel.send(embed=embed)
    except Exception as e:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description=f"Произошла ошибка  {e}\n"
            "Вы можете написать на сервер поддержки бота. Чтоб зайти на сервер нажмите на кнопку Cервер поддержки",
            color=disnake.Color.red()
        )
        button_support = Button(label="Cервер поддержки", url="https://discord.gg/KmskWpN5nb", style=disnake.ButtonStyle.link)
        
        view = View
        view.add_item(button_support)
        await ctx.send(embed = embed, view=view, ephemeral = True)
    
@ban.error
async def mute_error(ctx, error):
    if isinstance(error, disnake.ext.commands.MissingPermissions):
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="У вас нет нужных прав чтобы использовать эту команду",
            color=disnake.Color.red()
        )
        await ctx.send(embed=embed, ephemeral=True)
        
        
@bot.slash_command(description="Размьютить пользователя")
@commands.has_permissions(moderate_members=True)
async def unban(ctx, user: disnake.User, reason: str = None):
    if ctx.guild.me.top_role <= user.top_role:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="Роль бота слишком низкая для выполнение этой команды",
            color=disnake.Color.red()
        )
        return embed
    if ctx.author.top_role <= user.top_role:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="У вас нет прав чтоб разамьютить человека с более высокой ролью!",
            color=disnake.Color.red()
        )
        return embed
    
    if reason is None:
        reason = "Нет причины"
    
    try:
        await user.unban(until=None, reason=reason)
        embed = disnake.Embed(
            title="Пользователь был разбанен",
            description=f"** Краткая информация: **\nРазбанили: **@{ctx.author.name}**\nРазбанили был выдан: **@{user.name}**\n Причина: **{reason}**\n",
            color=disnake.Color.green()
        )
        await ctx.send(embed=embed, ephemeral = True)
        
        guild = user.guild
        if guild.system_channel:
            embed = disnake.Embed(
                title="Пользователь был разбанен",
                description=f"** Краткая информация: **\nРазбанили: **@{ctx.author.name}**\nРазбанили был выдан: **@{user.name}**\n Причина: **{reason}**\n",
                color=disnake.Color.green()
                )
            await guild.system_channel.send(embed=embed)
    except Exception as e:
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description=f"Произошла ошибка  {e}\n"
            "Вы можете написать на сервер поддержки бота. Чтоб зайти на сервер нажмите на кнопку Cервер поддержки",
            color=disnake.Color.red()
        )
        button_support = Button(label="Cервер поддержки", url="https://discord.gg/KmskWpN5nb", style=disnake.ButtonStyle.link)
        
        view = View
        view.add_item(button_support)
        await ctx.send(embed = embed, view=view, ephemeral = True)

@unban.error
async def mute_error(ctx, error):
    if isinstance(error, disnake.ext.commands.MissingPermissions):
        embed = disnake.Embed(
            title="Ой кажеться произошла ошибка:(",
            description="У вас нет нужных прав чтобы использовать эту команду",
            color=disnake.Color.red()
        )
        await ctx.send(embed=embed, ephemeral=True)


bot.run('Your token here')    
