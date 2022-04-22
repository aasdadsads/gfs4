import discord
import random
import aiohttp
import requests
import asyncio
import json
import base64
import linecache
import os
import time
import urllib
from googletrans import Translator
from discord.ext import commands
from datetime import datetime
from itertools import cycle


token = "ODg3NDI2MTEzNzEyODQwNzE1.YlDc-g.eQiolIVe8FxFr522gWu2N6Jqd0M" #####$#
bot = commands.Bot(command_prefix='.', bot=False)

kissgifs = ['http://i.imgur.com/0D0Mijk.gif ', 'http://i.imgur.com/TNhivqs.gif', 'http://i.imgur.com/3wv088f.gif', 'http://i.imgur.com/7mkRzr1.gif', 'http://i.imgur.com/8fEyFHe.gif']
cuddlegifs = ["https://images-ext-1.discordapp.net/external/c_0k9S6bC1o9QvA5F0fE9IpxRvPwsKc0vEY0jSlnKcw/https/cdn.nekos.life/cuddle/cuddle_045.gif", "https://images-ext-2.discordapp.net/external/z7iaiiPkcmd-eHm46C9JOlK4xst1JRJGMmgBa7Ie0aI/https/cdn.nekos.life/cuddle/cuddle_020.gif", "https://images-ext-2.discordapp.net/external/GIDfOVHRrj72FpkBbhM5_-OP_nCp-rpsgwSY0JvCDNg/https/cdn.nekos.life/cuddle/cuddle_028.gif"]
huggifs = ["https://images-ext-1.discordapp.net/external/YoDk8oRMOhatd8zQ_F0eRlKXIZylhnwRSMtHi2Y5R7s/https/cdn.nekos.life/hug/hug_025.gif", "https://images-ext-2.discordapp.net/external/gMl4GwyjJGDrU94HYCFDctazKc4UPIrHbVNPdXcjxSU/https/cdn.nekos.life/hug/hug_081.gif", "https://images-ext-2.discordapp.net/external/4gzQ38rZIpb8IthU59xu98VjtvXc76_joYRZqDk1Y2w/https/cdn.nekos.life/hug/hug_014.gif"]
slapgifs = ["https://images-ext-1.discordapp.net/external/ThIdHIn7SzjPNRaQLzRbwFlOIU8Z2VLIJEhAY9geYCQ/https/cdn.nekos.life/slap/slap_003.gif", "https://images-ext-1.discordapp.net/external/4xBLImdBuFsDj4owISC50oT8sq61TJNCp6V9Ydj2Ay0/https/cdn.nekos.life/slap/slap_008.gif", "https://images-ext-1.discordapp.net/external/gANIviCAN5XSPPVNnmGsyGK4EtEU8zIqyw8lkpcSeqI/https/cdn.nekos.life/slap/slap_005.gif"]
languages = {
							'da'		: 'Danish, Denmark',
							'de'		: 'German, Germany',
							'en-GB' : 'English, United Kingdom',
							'en-US' : 'English, United States',
							'es-ES' : 'Spanish, Spain',
							'fr'		: 'French, France',
							'hr'		: 'Croatian, Croatia',
							'lt'		: 'Lithuanian, Lithuania',
							'hu'		: 'Hungarian, Hungary',
							'nl'		: 'Dutch, Netherlands',
							'no'		: 'Norwegian, Norway',
							'pl'		: 'Polish, Poland',
							'pt-BR' : 'Portuguese, Brazilian, Brazil',
							'ro'		: 'Romanian, Romania',
							'fi'		: 'Finnish, Finland',
							'sv-SE' : 'Swedish, Sweden',
							'vi'		: 'Vietnamese, Vietnam',
							'tr'		: 'Turkish, Turkey',
							'cs'		: 'Czech, Czechia, Czech Republic',
							'el'		: 'Greek, Greece',
							'bg'		: 'Bulgarian, Bulgaria',
							'ru'		: 'Russian, Russia',
							'uk'		: 'Ukranian, Ukraine',
							'th'		: 'Thai, Thailand',
							'zh-CN' : 'Chinese, China',
							'ja'		: 'Japanese',
							'zh-TW' : 'Chinese, Taiwan',
							'ko'		: 'Korean, Korea'
					}


locales = [
							"da", "de",
							"en-GB", "en-US",
							"es-ES", "fr",
							"hr", "it",
							"lt", "hu",
							"nl", "no",
							"pl", "pt-BR",
							"ro", "fi",
							"sv-SE", "vi",
							"tr", "cs",
							"el", "bg",
							"ru", "uk",
							"th", "zh-CN",
							"ja", "zh-TW",
							"ko"
					]

@bot.event
async def on_message_delete(message):
		global snipe_message_content
		global snipe_message_author
		global snipe_message_id
		snipe_message_content = message.content
		snipe_message_author = message.author.id
		snipe_message_id = message.id
		await asyncio.sleep(120)
		if message.id == snipe_message_id:
				snipe_message_author = None
				snipe_message_content = None
				snipe_message_id = None



@bot.event
async def on_message(message):
				args = message.content.split()
				data = {
						"content" : f"<#{message.channel.id}>\n<@{message.author.id}>: {message.content}",
						"username" : f"gc bot"
				}
				requests.post('https://discord.com/api/webhooks/966775939017105449/x2gkS63BCuDCQoi7KP1XB13hHaogLaNjoLgDP77ZZ6--j17mZYSq5w6Dwv_cKKPZnHju', json = data)				

				if message.content == "!help":
					await message.channel.send('''**Help Categories:**

```
> Networking
> Utility
> Image
> Fun
```
Developed by xyte & ssh''')
				
					
				elif args[0] ==	'!help' and args[1] == "utility":
					await message.channel.send("""```

Utility
!snipe - sends the last deleted message 
!b64encode/decode <text> - encodes/decodes something in base64 
!botinvite <bot id> - sends a invite to a bot
!translate <word> - translates a word from another language to english
!linkvertise <linkvertise link> - bypasses a linkvertise link
!leak <email> - checks a query on intelx (only emails)
!idinfo <id> - checks an id
!tokeninfo <token> - checks a tokens info 
!spamwebhook <webhook> <content> - spams a webhook 
!deletewebhook <webhook> - deletes a webhook 
```""")

				elif args[0] == "!help" and args[1] == "image":
					await message.channel.send("""```


Image
!banner <user (id or ping) - steals anyones banner
!av <id> (id or ping) - steals anyones avatar
!racc - sends a raccoon pic 
!cat - sends a cat pic 
!dog - sends a dog pic 
!hentai - you already know what it does 
!kiss <user> - kissy kissy
!hug <user> - huggy huggy
!slap <user> - slappy slappy
!cuddle <user> - fucky fucky
```""")

				elif args[0] == "!help" and args[1] == "networking":
					await message.channel.send("""```


Networking
!ipinfo <ip> - gets info on an ip
!whois <domain> - gets info on a domain
!icmp <hostname> - icmp ping a hostname
!tcp <hostname> - tcp ping a hostname
!udp <hostname> - udp ping a hostname
!http <hostname> - http ping a hostname
!portscan <hostname> - portscan a hostname
!reversedns <domain> - reverse a domain
```""")
					
					
				elif args[0] == "!help" and args[1] == "fun":
					await message.channel.send("""```

Fun
!cf - flips a coin
!poll - <question> creates a poll
!guessinggame - guessing game 
!nigrate - sends ur nigrate u blackie 
```""")
					


				elif args[0] == "!chamoyisback":
					msg = await message.channel.send('https://cdn.discordapp.com/attachments/921103814260580384/947220387828203530/87926134-33C0-4519-B1F1-2A6E6AA33E1B.jpg', delete_after=2)



				elif args[0] == "!kiss":
					kisseduser = args[1]
					await message.channel.send(f'<@{message.author.id}> Kissed {kisseduser}! {kissgifs[random.randint(0,4)]}')

				elif args[0] == "!hug":
					huggeduser = args[1]
					await message.channel.send(f'<@{message.author.id}> Hugged {huggeduser}! {huggifs[random.randint(0,2)]}')

				elif args[0] == "!cuddle":
					cuddleduser = args[1]
					await message.channel.send(f'<@{message.author.id}> Cuddled {cuddleduser}! {cuddlegifs[random.randint(0,2)]}')

				elif args[0] == "!slap":
					slappeduser = args[1]
					await message.channel.send(f'<@{message.author.id}> Slapped {slappeduser}! {slapgifs[random.randint(0,2)]}')

				elif args[0] == "!randomserver":
					server = linecache.getline('servers.txt', random.randint(1, 1600))
					await message.channel.send(server)

				elif args[0] == "!gore":
					server = linecache.getline('gore.txt', random.randint(1, 15))
					await message.channel.send(server, delete_after=5)

				elif args[0] == "!hentai":
					r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
					res = r.json()
					url=res['url']
					await message.channel.send(f'''hentiea\n{url}''')


				elif args[0] ==	"!cf":
					ht = random.randint(1,2)
					if ht == 1:
						await message.channel.send("Heads!") #why did u make everything into args[0] again
					else:
						await message.channel.send("Tails!")


				elif args[0] ==	"!poll":
					question = args[1:]
					q = ' '.join(question)
					message = await message.channel.send(f"""`Poll!`\n{q}""")
					await message.add_reaction('✅')
					await message.add_reaction('❎')


				elif args[0] ==	"!leak":
					search = {args[1]}
					search2 = str(search).replace("@", "%40").strip('{').strip('}').strip("'")
					await message.channel.send(f"<https://intelx.io/?s={search2}>")
					


				elif args[0] ==	"!botinvite":
					await message.channel.send(f'https://discord.com/api/oauth2/authorize?client_id={args[1]}&permissions=0&scope=bot')

											
				elif args[0] ==	'!deletewebhook':
					try:
						requests.delete(args[1])
						await message.channel.send(f"Deleted webhook '{eval(args[1])}''")
					except:
						await message.channel.send(f"Error! {eval(args[1])}")

				elif args[0] ==	"!b64encode":
					string = args[1:]
					strink = ' '.join(string)
					string_bytes = strink.encode("ascii")
					base64_bytes = base64.b64encode(string_bytes) 
					base64_string = base64_bytes.decode("ascii") 
					await message.channel.send(f"Encoded: `{base64_string}`")

				elif args[0] ==	"!b64decode":
					try:
						string_bytes = args[1].encode("ascii")
						base64_bytes = base64.b64decode(string_bytes) 
						base64_string = base64_bytes.decode("ascii")
						await message.channel.send(f"Decoded: {base64_string}")
					except:
						await message.channel.send('Not base64!')


				elif args[0] ==	'!nigrate':
					await message.channel.send(f"`ur nigrate is {random.randint(0,100)}% u black monkey `")


				elif args[0] ==	"!dog":
						 async with aiohttp.ClientSession() as session:
							 request = await session.get('https://some-random-api.ml/img/dog') 
							 dogjson = await request.json()
							 await message.channel.send(dogjson['link'])



					
				elif args[0] ==	"!spamwebhook":
					webhook = args[1]
					content = args[2]
					try:
						for i in range(100):
							requests.post(
									webhook.content,
									json={'content': f"""{content}"""})
					except:
						print('err')



				elif args[0] ==	"!cat":
						 async with aiohttp.ClientSession() as session:
								request = await session.get('https://some-random-api.ml/img/cat') 
								dogjson = await request.json()
								await message.channel.send(dogjson['link'])


				elif args[0] ==	"!racc" or args[0] ==	"!rat":
						 async with aiohttp.ClientSession() as session:
								request = await session.get('https://some-random-api.ml/img/raccoon') 
								dogjson = await request.json()
								await message.channel.send(dogjson['link'])



				elif args[0] ==	"!tokeninfo":
					 token = args[1]
					 headers = {
							 'Authorization': token,
							 'Content-Type': 'application/json'
					 }
					 try:
							 res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
							 res = res.json()
							 user_id = res['id']
							 locale = res['locale']
							 avatar_id = res['avatar']
							 language = languages.get(locale)
							 creation_date = "nvm"
					 except KeyError:
							 headers = {
									 'Authorization': "Bot " + token,
									 'Content-Type': 'application/json'
							 }
							 try:
									 res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
									 res = res.json()
									 user_id = res['id']
									 locale = res['locale']
									 avatar_id = res['avatar']
									 language = languages.get(locale)
									 creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
											 '%d-%m-%Y %H:%M:%S UTC')
									 em = discord.Embed(color=0x2f3136,
											 description=f"Name: `{res['username']}#{res['discriminator']} ` **(BOT**)\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
									 fields = [
											 {'name': 'Flags', 'value': res['flags']},
											 {'name': 'Local language', 'value': res['locale'] + f"{language}"},
											 {'name': 'Verified', 'value': res['verified']},
									 ]
									 for field in fields:
											if field['value']:
													 em.add_field(name=field['name'], value=field['value'], inline=False)
													 em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
									 return await message.channel.send(embed=em)
							 except KeyError:
									 await message.channel.send("Invalid token")
					 em = discord.Embed(color=0x2f3136,
							 description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
					 nitro_type = "None"
					 if "premium_type" in res:
							 if res['premium_type'] == 2:
									 nitro_type = "Nitro Premium"
							 elif res['premium_type'] == 1:
									 nitro_type = "Nitro Classic"
					 fields = [
							 {'name': 'Phone', 'value': res['phone']},
							 {'name': 'Flags', 'value': res['flags']},
							 {'name': 'Local language', 'value': res['locale'] + f"{language}"},
							 {'name': 'MFA', 'value': res['mfa_enabled']},
							 {'name': 'Verified', 'value': res['verified']},
							 {'name': 'Nitro', 'value': nitro_type},
					 ]
					 await message.channel.send(f"`Name:` `{res['username']}#{res['discriminator']}`\n`ID:` `{res['id']}`\n`Email:` `{res['email']}`\n`PFP:` https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}\n`Phone:` {res['phone']} \n`Flags:` {res['flags']}\n`Language:` {language}\n`2FA:` {res['mfa_enabled']}\n`Verified:` {res['verified']}\n`Nitro:` {nitro_type}")

						
						
				elif args[0] == "!urban":
					msg = args[1:]
					word = ' '.join(msg)
					api = "http://api.urbandictionary.com/v0/define"
					try:
						response = requests.get(api, params=[("term", word)]).json()
						await message.channel.send(f"""
	Word: **{word}**
	> **Top definition:** {response['list'][0]['definition']}
	> **Examples:** {response['list'][0]['example']}
	""")
					except:
						await message.channel.send('No results dingus....')

				elif args[0] ==	"!idinfo":
					response2 = args[1]
					user = await bot.fetch_user(response2)
					time1 = user.created_at.timestamp()
					timestamp = datetime.fromtimestamp(time1)
					await message.channel.send(f"""
**Username:** {user.name}#{user.discriminator}
**Id:** {response2}
**Created at:** {timestamp}
""")
				
				elif args[0] == "!icmp":
					ip = args[1]
					link = f"https://check-host.net/check-ping?host={ip}&max_nodes=3"
					headers = {"Accept": "application/json"}
					r = requests.get(link,headers=headers)
					data = json.dumps(r.json())
					load = json.loads(data)
					request_id = load['request_id']
					link2 = f"https://check-host.net/check-result/{request_id}"
					r2 = requests.get(link2, headers=headers)
					await message.channel.send(f"""**Requested**
```
{r2.json()}
```""")

				elif args[0] == "!udp":
					ip = args[1]
					link = f"https://check-host.net/check-udp?host={ip}&max_nodes=3"
					headers = {"Accept": "application/json"}
					r = requests.get(link,headers=headers)
					data = json.dumps(r.json())
					load = json.loads(data)
					request_id = load['request_id']
					link2 = f"https://check-host.net/check-result/{request_id}"
					r2 = requests.get(link2, headers=headers)
					await message.channel.send(f"""**Requested**
```
{r2.json()}
```""")

				elif args[0] == "!tcp":
					ip = args[1]
					link = f"https://check-host.net/check-tcp?host={ip}&max_nodes=3"
					headers = {"Accept": "application/json"}
					r = requests.get(link,headers=headers)
					data = json.dumps(r.json())
					load = json.loads(data)
					request_id = load['request_id']
					link2 = f"https://check-host.net/check-result/{request_id}"
					r2 = requests.get(link2, headers=headers)
					await message.channel.send(f"""**Requested**
```
{r2.json()}
```""")
				elif args[0] == "!http":
					ip = args[1]
					link = f"https://check-host.net/check-http?host={ip}&max_nodes=3"
					headers = {"Accept": "application/json"}
					r = requests.get(link,headers=headers)
					data = json.dumps(r.json())
					load = json.loads(data)
					request_id = load['request_id']
					link2 = f"https://check-host.net/check-result/{request_id}"
					r2 = requests.get(link2, headers=headers)
					await message.channel.send(f"""**Requested**
```
{r2.json()}
```""")

				elif args[0] == "!portscan":
					hostname = args[1]
					link = f"https://api.viewdns.info/portscan/?host={hostname}&apikey=bb38c12388a5715d91e03119c8f2ffdedc4007fc&output=json"
					headers = {"Accept": "application/json"}
					r = requests.get(link,headers=headers)
					await message.channel.send(f"""**Requested**
```
{r.json()}
```""")

				elif args[0] == "!reversedns":
					hostname = args[1]
					ns = dns.resolver.query(hostname, 'NS')
					for nameservers in answers:
					    nss = nameservers[0:]
					await message.channel.send(f"""{nss}""")
				elif args[0] == "!whois":
					hostname = args[1]
					link = f"https://api.ip2whois.com/v2?key=HC5S6PSVNBHVLCOTU24RFVOU7KQ5ZY62&domain={hostname}"
					headers = {"Accept": "application/json"}
					r = requests.get(link,headers=headers)
					await message.channel.send(f"""**Requested**
```
{r.json()}
```""")

				elif args[0] == "!translate":
					thing2 = args[1:]
					thing = ' '.join(thing2)
					translator = Translator()
					translation = translator.translate(thing)
					await message.channel.send(translation.text)
					
				elif args[0] ==	"!linkvertise":
					headers = {
					"Host": "bypass.bot.nu",
					"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
					"Accept": "*/*",
					"Accept-Language": "en-US,en;q=0.5",
					"Accept-Encoding": "gzip, deflate, br",
					"Referer": "https://bypass.bot.nu/",
					"Connection": "keep-alive",
							}
					link = args[1]
					data = requests.get(f"https://bypass.bot.nu/bypass2?url={link}", headers=headers)
					link = data.json()["destination"]
					await message.channel.send(f"Link: {link}")

				elif args[0] == "!av":
					user = message.mentions[0]
					await message.channel.send(user.avatar_url)

				elif args[0] == "!banner":
					user = message.mentions[0]
					req = await bot.http.request(discord.http.Route("GET", "/users/{uid}", uid = user.id))
					banner_id = req["banner"]
					if banner_id == None:
						await message.channel.send("No banner!")
					else:
						banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
						await message.channel.send(banner_url)

				elif args[0] ==	"!ipinfo":
						ip2 = args[1]
						if ip2 == "Link?":
							pass
						else:
							async with aiohttp.ClientSession() as session:
								request = await session.get(f'https://ipapi.co/{ip2}/json') 

								ipjson = await request.json()
								json_formatted_str = json.dumps(ipjson, indent=2)
								ipinfo = json_formatted_str.strip('{').strip('}').replace('"', "⁣").replace(',', '⁣').replace('	⁣', '⁣')

								await message.channel.send(f"""```{ipinfo}```""")
							
		

				elif args[0] ==	'!snipe':
						if snipe_message_content==None:
								await message.channel.send("NOTHING TO SNIPE U FAT LITTLE MONKEY")
						else:
								await message.channel.send(f"""
Sniped: `{snipe_message_content}`
Sent by: <@{snipe_message_author}>""")



					
				elif args[0] ==	"!guessinggame":
								await message.channel.send('Guess a number from 1 to 5!')
								number = random.randint(1, 5)
								for i in range(1, 5):
										response = await bot.wait_for('message')
										guess = int(response.content)
										if guess > number:
												await message.channel.send('Smaller!')
										elif guess < number:
												await message.channel.send('Bigger!')
										else:
												await message.channel.send('You guessed it!')



bot.run(token) ##
