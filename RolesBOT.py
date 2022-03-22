import discord
from discord.ext import commands #импорты, не трогаем


prefix = 'rol!' #тут ваш префикс

client = commands.Bot(command_prefix=prefix,intents = discord.Intents.all()) #включите на сайте интенты (раздел bot->переводим ползунок PRESENCE INTENT, SERVER MEMBERS INTENT, MESSAGE CONTENT INTENT)                 
client.remove_command('help')   
@client.event
async def on_ready():
	print('на старте') #сообщает, что бот запустился, в кавычках можете ставить любой текст


hform = f"""{prefix}add @пинг или ID - выдать роль всем участникам сервера
{prefix}rem @пинг или ID - забрать роль у всех участников сервера"""


@client.command()
async def help(ctx):
	embed = discord.Embed(title='Команды RolesBOT', description=hform, color=discord.Color.orange())
	await ctx.send(embed=embed)



@client.command()
async def add(ctx, role:discord.Role=None):
	if not ctx.author.guild_permissions.administrator:
		embed = discord.Embed(title='❎| Отсутствуют права', description=f'{ctx.author.mention}, у вас отсутствуют права администратора', color=discord.Color.red()) #Показывает, что отсутсвуют права администратора
		embed.set_thumbnail(url=ctx.author.avatar_url) #показывает аватарку автора справа, если не надо просто убираем эту строчку
		await ctx.send(embed=embed) #просто вывод ембеда, не трогаем
		return #действие остановлено
	if not role:
		embed = discord.Embed(title='❎| Отсутствует роль или ее ID', description=f'{ctx.author.mention} введите роль или ее ID', color=discord.Color.red()) #Показывает, что отсутсвует роль
		embed.set_thumbnail(url=ctx.author.avatar_url) #показывает аватарку автора справа, если не надо просто убираем эту строчку
		await ctx.send(embed=embed) #просто вывод ембеда, не трогаем
	else:
		number = 0 
		number1 = 0
		for mroles in role.members:
			number +=1
			number1 +=1
		nmroles = len(ctx.guild.members) - number
		lroles = len(ctx.guild.members) - number1 #с 37 по 43 строчку не трогать, это для подсчета
		embed = discord.Embed(title='🕐|Начинаю выдачу ролей', description=f'Всем участникам сервера выдаются роли {role.mention}', color=discord.Color.green()) #информация о выдаче роли
		msg = await ctx.send(embed=embed) #вывод эмбеда, не трогаем
		for member in ctx.guild.members: #получаем всех участников сервера
			await member.add_roles(role) #выдаем роль участникам
			lroles -= 1 #тоже не трогаем
			embed = discord.Embed(title='🕐|Начинаю выдачу роли', description=f'Выдана роль {role.mention} участнику {member.mention}\nОсталось участников **{int(lroles)}**', color=discord.Color.green()) #показывает информацию кому выдается и остаток
			await msg.edit(embed=embed) #изменение эмбеда, не трогаем
		embed = discord.Embed(title='✅|Выдача роли окончена', description=f'**{int(nmroles)}** участникам сервера выдалась роль {role.mention}', color=discord.Color.green()) #сообщение о успешном завершении
		await msg.edit(embed=embed) #изменение эмбеда

@client.command()
async def rem(ctx, role:discord.Role=None):
	if not ctx.author.guild_permissions.administrator:
		embed = discord.Embed(title='❎| Отсутствуют права', description=f'{ctx.author.mention}, у вас отсутствуют права администратора', color=discord.Color.red()) #Показывает, что отсутсвуют права администратора
		embed.set_thumbnail(url=ctx.author.avatar_url) #показывает аватарку автора справа, если не надо просто убираем эту строчку
		await ctx.send(embed=embed) #просто вывод ембеда, не трогаем
		return #действие остановлено
	if not role:
		embed = discord.Embed(title='❎| Отсутствует роль или ее ID', description=f'{ctx.author.mention} введите роль или ее ID', color=discord.Color.red()) #Показывает, что отсутсвует роль
		embed.set_thumbnail(url=ctx.author.avatar_url) #показывает аватарку автора справа, если не надо просто убираем эту строчку
		await ctx.send(embed=embed) #просто вывод ембеда, не трогаем
	else:
		number = 0 
		number1 = 0
		for mroles in role.members:
			number +=1
			number1 +=1
		lroles = len(ctx.guild.members) - number1 #с 66 по 71 строчку не трогать, это для подсчета
		embed = discord.Embed(title='🕐|Начинаю выдачу ролей', description=f'Всем участникам сервера выдаются роли {role.mention}', color=discord.Color.green()) #информация о забирании роли
		msg = await ctx.send(embed=embed) #вывод эмбеда, не трогаем
		for member in ctx.guild.members: #получаем всех участников сервера
			await member.remove_roles(role) #забираем роль у участников
			number1 -= 1 #тоже не трогаем
			embed = discord.Embed(title='🕐|Начинаю забирание роли', description=f'Забрана роль {role.mention} у участника {member.mention}\nОсталось участников **{int(number1)}**', color=discord.Color.green()) #показывает информацию кому забирается и остаток
			await msg.edit(embed=embed) #изменение эмбеда, не трогаем
		embed = discord.Embed(title='✅|Забирание роли окончено', description=f'у **{int(number)}** участников сервера была забрана роль {role.mention}', color=discord.Color.green()) #сообщение о успешном завершении
		await msg.edit(embed=embed) #изменение эмбеда



client.run('ТОКЕН', bot=True)#тут токен вашего бота