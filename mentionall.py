import os, logging, asyncio
import random
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

# ÆkmÉ OÄlum...!!!
emj = ['ð','ð¥°','ð','ð¤©','ð','ð¾','ð¤¡','ð¥³','ð»','ð¼','ð½','ð','ð¸','ð¤´','ðð»','ð¤¶','ð§ââï¸','ð§','ð§ââï¸','ð§ââï¸','ð§','ð§ââï¸','ð§','ð','ð','ð¶','ð¶','ð±','ð­','ð¹','ð°','ð¦','ð»','ð¼','ð¨','ð¯','ð¦','ð®','ð·','ð½','ð¸','ðµ','ð','ð','ð','ð','ð£','ð¥','ð¦','ð','ð¦','ð','ð','ð¹','ð¥','ðº','ð¸','ð¼','ð»','â­ï¸','ð','â¨','â¡ï¸','ð¥','ð','âï¸','ð«','ð','ðº','ð«','ð','â','ð§¸','ð¦','ð©âð¦°','ð®','âï¸','ð','ð¦','ð¨ð»ââï¸','ð¥¶','ð¿','ð','ð','ð','â¥ï¸','ð','ð','ð','ð','ð','ð¤','ð¤','â¡','ð','ð¤¡','ð','ð¥','ð¼','ð¤','â','ð©âð¨','ð§','ð¼','ð','ð¹','ð¥','ð·','ðº','ð¸','ðµï¸','ð»','ð','ð','ð¾','ð±','ð¿','ð','âï¸','ð','ðµ','ð´','ð³','ð²','ðï¸','ðªï¸','âï¸','â','âï¸','ðï¸','ð','ð','ð¤¶','ð©âð¼','ð§','ð§','ð','ðº','ð©âð¦°','ðª','ð¦','ð¢','ð','ð¤','ð£','ð¥','ð¦','ð','ðï¸','ð¦¢','ð¦©','ð¦','ð¬','ð','ð³','ð','ð ','ð¦','ð¡','ð¦','ð¦','ð¦','ð¦','ð','ð¦','ð·ï¸','ð¸ï¸','ð','ð¦','ð¦','ð','ð','ð¾','ð','ð','ð','ð','ð','ð¥­','ð','ð','ð','ð¥','ð','ð¥¥','ð¶ï¸','ð','ð','ð§','ð¥','ð¦','ð§','ð¨','ð¦','ð¥§','ð°','ð®','ð','ð§','ð­','ð¬','ð©','ðº','ð»','ð¥','ð¾','ð·']
# ÆkmÉ OÄlum...!!!

#  gÃ¼zel isimler...!!! 
cumle = ['ÃzÃ¼mlÃ¼ kekim â¨', 'Nar Ã§iÃ§eÄi â¨', 'Papatya ð¼', 'Karanfil â¨', 'GÃ¼l ð¹', 'AyÄ±cÄ±k ð»', 'Mutlu pandam ð¼', 'Ay parem â¨', 'BallÄ± lokmam â¨', 'BebiÅim ð¥°', 'Lale ð·', 'Zambak â', 'Nergis â¨', 'SÃ¼mbÃ¼l âï¸', 'NilÃ¼fer âï¸', 'MenekÅe âï¸', 'Lavanta â¨', 'GÃ¼l pare â¨', 'Reyhan ð·', 'KaktÃ¼s âï¸', 'BÃ¶ÄÃ¼rtlen âï¸', 'Orkide âï¸', 'Manolya â¨', 'AyÃ§iÃ§eÄi â¨', 'Tweety âï¸', 'Star â¨', 'Yonca ð', 'AteÅ bÃ¶ceÄi â¨',]
#  gÃ¼zel isimler...!!!

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**MÐÆ¦ÓÆÆÆ** TOXÄ°C TAGGER ÆÆ Æ¬ GÃNCELLENMÄ°Å HALÄ°YLE KARÅINIZDA...! ÆÐÆÆ ÆÆ¦Æ²ÆÆ Æ³Æ ÆÐÆ¬ÆÆÆ Æ Ô¼ÆÆ¦ÆÆ ÐÆÔ¼ÐÆ³ÆÆ ÆÐÆ¦ÆÆ§ÆÆÆ ÆÆÆÆ ÆÆÆ¦ÆÆÆÆ. \n\n ÆÆ MÆ²Æ¬Ô¼ÆÆ¦ÆMÆ GÃRMEK ÆÃÆÆ /help Æ³ÆÈ¤ÆÆ. ",
                    buttons=(
                      [
                         Button.url('â ÆÆ¦Æ²ÆÆ ÐÆÔ¼Ð â ', 'http://t.me/Majeste_TaggerBot?startgroup=a')
                      ],
                      [
                         Button.url('ð£ KANAL', 'https://t.me/pubgvipcheat01'),
                         Button.url('ð® DEVELOPER', 'https://t.me/onlinewof'),
                         Button.url('ð SUPPORT', 'https://t.me/pubglitefucker')
                      ]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Toxic Tagger Botun KomutlarÄ±**\n\n/utag - Ãyeleri 5 Ô¼Æ etiketler . \n /etag - Ã¼yeleri emoji ile etiketler \n /itag - Ã¼yeleri gÃ¼zel isimlerle etiketler . \n /hiztag - Ã¼yeleri aÅÄ±rÄ± hÄ±zlÄ± bir Åekile etiketler \n /tektag - herkesi Æ¬ÐÆ Æ¬ÐÆ ÐÆ¬ÆÆÐÆ¬Ô¼ÐÆ¦ \n\n **KomutlarÄ± Sadece YÃ¶neticiler Kullanabilir...!**"
  await event.reply(helptext,
                    buttons=(
                      [
                         Button.url('â ÆÆ¦Æ²ÆÆ ÐÆÔ¼Ð â', 'http://t.me/toxicrobbot?startgroup=a')
                      ],
                      [
                         Button.url('ð£ kanal', 'https://t.me/pubgvipcheat01'),
                         Button.url('ð®sahip', 'https://t.me/onlinewof'),
                         Button.url('ð grup', 'https://t.me/pubglitefucker')
                      ]
                    ),
                    link_preview=False
                   )


@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanÄ±labilir.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__YalnÄ±zca yÃ¶neticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajlar iÃ§in Ã¼yelerden bahsedemem! (gruba eklemeden Ã¶nce gÃ¶nderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Bana bir argÃ¼man ver!__")
  else:
    return await event.respond("__Bir mesajÄ± yanÄ±tlayÄ±n veya baÅkalarÄ±ndan bahsetmem iÃ§in bana bir metin verin!__")
    
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"ð¤ - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Ä°Ålem BaÅarÄ±lÄ± Bir Åekilde Durduruldu â")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"ð¤ - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Ä°Ålem BaÅarÄ±lÄ± Bir Åekilde Durduruldu â")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern="^/hiztag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanÄ±labilir.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__YalnÄ±zca yÃ¶neticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajlar iÃ§in Ã¼yelerden bahsedemem! (gruba eklemeden Ã¶nce gÃ¶nderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Bana bir argÃ¼man ver!__")
  else:
    return await event.respond("__Bir mesajÄ± yanÄ±tlayÄ±n veya baÅkalarÄ±ndan bahsetmem iÃ§in bana bir metin verin!__")
    
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"ð¤ - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Ä°Ålem BaÅarÄ±lÄ± Bir Åekilde Durduruldu â")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(0)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"ð¤ - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Ä°Ålem BaÅarÄ±lÄ± Bir Åekilde Durduruldu â")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(0)
        usrnum = 0
        usrtxt = ""

# Emoji Modulu (aykhan_s)
@client.on(events.NewMessage(pattern="^/itag ?(.*)"))
async def etag(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanÄ±labilir.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__YalnÄ±zca yÃ¶neticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajlar iÃ§in Ã¼yelerden bahsedemem! (gruba eklemeden Ã¶nce gÃ¶nderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Bana bir argÃ¼man ver!__")
  else:
    return await event.respond("__Bir mesajÄ± yanÄ±tlayÄ±n veya baÅkalarÄ±ndan bahsetmem iÃ§in bana bir metin verin!__")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Ä°Ålem BaÅarÄ±lÄ± Bir Åekilde Durduruldu â")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Ä°Ålem BaÅarÄ±lÄ± Bir Åekilde Durduruldu â")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

#  gÃ¼zel isimler...!!!
@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def nick(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanÄ±labilir.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__YalnÄ±zca yÃ¶neticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajlar iÃ§in Ã¼yelerden bahsedemem! (gruba eklemeden Ã¶nce gÃ¶nderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Bana bir argÃ¼man ver!__")
  else:
    return await event.respond("__Bir mesajÄ± yanÄ±tlayÄ±n veya baÅkalarÄ±ndan bahsetmem iÃ§in bana bir metin verin!__")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emj)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Ä°Ålem BaÅarÄ±lÄ± Bir Åekilde Durduruldu â")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emj)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Ä°Ålem BaÅarÄ±lÄ± Bir Åekilde Durduruldu â")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu komutu gruplar ve kanallar iÃ§in geÃ§erliâï¸**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadace yoneticiler kullana bilirã½**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Ã¶nceki mesajÄ± etiketleye bilmerim*")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("BaÅlamak iÃ§in Sebep YazÄ±nâï¸")
  else:
    return await event.respond("**iÅleme baÅlamam iÃ§in sebep yazÄ±n..**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id})**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**IÅlem BaÅarÄ±yla Durduruldu\n\n** created bu:- @onlinewof**â****")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in tekli_calisan:
        await event.respond("IÅlem BaÅarÄ±yla Durduruldu**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

print(">> Bot Deploy edildi merak etme ð @onlinewof bilgi alabilirsin <<")
client.run_until_disconnected()
