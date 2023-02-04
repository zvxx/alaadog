import requests 
import os
import telebot
import os
from uuid import uuid4 as uid
from secrets import token_hex
import OneClick
import stdiomask
import requests
from uuid import uuid4 as uid
from secrets import token_hex
from OneClick import *
import requests
import telebot
from telebot import types
import instaloader
csr = token_hex(8)*2
bot = telebot.TeleBot('5782532236:AAHIqU5iutno82bQ52KlPFAp1c-AKttod8o')
@bot.message_handler(commands=["start"])
def st(message):
    ID = message.from_user.id
    bot.send_message(message.chat.id,"⋘──────━𓆩𝐋 𝐄 𝐕 𝐈𓆪‏━──────⋙\n❖ - 𝚂𝚎𝚗𝚍 𝚝𝚑𝚎 𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 𝚝𝚘 𝙴𝚡𝚝𝚛𝚊𝚌𝚝 𝚝𝚑𝚎 𝙸𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚗𝚍 𝙳𝚎𝚕𝚒𝚟𝚎𝚛 𝚊 𝚁𝚎𝚜𝚝 \n\n❖ - اࢪســل الــيـوزر لـكي يــتم اسـتـخراج مـعـلومات الـحساب وتـوصـيل ريـست لـلـجـيمـل \n⋘──────━𓆩𝐋 𝐄 𝐕 𝐈𓆪‏━──────⋙",reply_to_message_id=message.message_id)
@bot.message_handler(func=lambda i:True)
def start(message):
   try:
    msg = message.text
    ggg = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(ggg.context, msg)
    urlr='https://www.instagram.com/accounts/account_recovery_ajax/'
    headr= {
					        'accept': '*/*',
					        'accept-encoding': 'gzip, deflate, br',
					        'accept-language': 'en-US,en;q=0.9',
					        'content-length': '336',
					        'content-type': 'application/x-www-form-urlencoded',
					        'cookie': 'mid=YuPxZAABAAEUVYcD2B0cFEzLEyuU; ig_did=50092572-86B8-4779-8D7D-ED783D6BE001; dpr=3; datr=lPHjYm79ZCBQZ-8kyLncySC7; shbid="572\05454072972258\0541691059333:01f70b5caa78629654a33ffe9055bdc7663b824064ba3854ecfade7109c72ee455eb5eb8"; shbts="1659523333\05454072972258\0541691059333:01f7ce1fd97040b48210c72b760bfbbf68254544b85860f356f3dc04622ee5bfd6edb2d9"; rur="RVA\05454072972258\0541691069797:01f7513337be7c4309672fc0a95436c4f0b60d9f1ff74355b61efadb1b1079fb38505eea"; csrftoken=tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
					        'origin': 'https://www.instagram.com',
					        'referer': 'https://www.instagram.com/',
					        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
					        'sec-ch-ua-mobile': '?0',
					        'sec-fetch-dest': 'empty',
					        'sec-fetch-mode': 'cors',
					        'sec-fetch-site': 'same-origin',
					        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
					        'viewport-width': '30',
					        'x-asbd-id': '437806',
					        'x-csrftoken': 'tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
					        'x-ig-app-id': '936619743392459',
					        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
					        'x-instagram-ajax': 'caee87137ae9',
					        'x-requested-with': 'XMLHttpRequest'
						}
    datar={
							'query': f'{msg}'
						}
    rq = requests.post(urlr,headers=headr,data=datar).json()
    fa =str(rq['options']['can_use_facebook'])
    if fa =='True':
        L3 = 'مــربـوط فـيس بــوك'
    else:
        L3='غــير مــربـوط فـيس بــوك'
    ph = str(rq['options']['can_send_phone'])
    if ph =='True':
        L5 = ('مــربـوط رقــم')
    else:
    	L5='غــير مــربـوط رقــم'
    head = {
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      "Host": "i.instagram.com",
      "Connection": "Keep-Alive",
      "User-Agent": Hunter.Services(),
      "Cookie": "mid=YwvCRAABAAEsZcmT0OGJdPu3iLUs; csrftoken="+csr,
      "Cookie2": "$Version=1",
      "Accept-Language": "en-US",
      "X-IG-Capabilities": "AQ==",
      "Accept-Encoding": "gzip",}
    data= {"q":msg,
   "device_id":f"android{uid}",
   "guid":uid,
   "_csrftoken":csr}
    kid=requests.post('https://i.instagram.com/api/v1/users/lookup/',headers=head,data=data).json()
    api = f'https://www.instagram.com/{msg}/?__a=1&__d=dis'
    rr=requests.get(api).json()
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',

        'Accept-Language': 'en-US',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': 'AQ==',
							}
    data = {
        'ig_sig_key_version': '4',
        "user_id":iddd
							}
    res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers, data=data).json()
    data=data= {"user_email":message.text,
   "device_id":f"android{iddd}",
   "guid":iddd,
   "_csrftoken":csr}
    restt=requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',data=data,headers=head)
    res=restt.json()
    ress=restt.text
    if 'obfuscated_email' in ress:
    	fa =str(rq['options']['can_use_facebook'])
    	if fa =='True':
    		L3 = 'مــربـوط فـيس بــوك'
    	else:
    		L3='غــير مــربـوط فـيس بــوك'
    	ph = str(rq['options']['can_send_phone'])
    	if ph =='True':
    		L5 = ('مــربـوط رقــم')
    	else:
    		L5='غــير مــربـوط رقــم'
    	iddd = (profile.userid)
    	nam = (profile.full_name)
    	fol = (profile.followees)
    	fols =(profile.followers)
    	bio = (profile.mediacount)
    	bayo = (profile.biography,profile.external_url)
    	pc = (profile.profile_pic_url)
    	re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
    	ree = re.json()
    	dat = ree['date']
    	email=res['obfuscated_email']
    	bot.send_photo(message.chat.id,pc,caption=f"""𓊆𝑁𝐸𝑊 𝐼𝑁𝐹𝑂𝑅𝑀𝐴𝑇𝐼𝑂𝑁 𝐴𝐶𝐶𝑂𝑈𝑁𝑇 𝐼𝑁𝑆𝑇𝐴𝐺𝑅𝐴𝑀 𝐵𝑌 𝐿𝐸𝑉𝐼𓊇
⋘────━𓆩𝐋 𝐄 𝐕 𝐈𓆪‏━────⋙  
❖ - 𝖓𝖆𝖒𝖊 : {nam}
❖ - 𝖚𝖘𝖊𝖗𝖓𝖆𝖒𝖊 : @{msg}
❖️ - 𝕴𝕯 : {iddd}
❖ - 𝖋𝖔𝖑𝖑𝖔𝖜𝖊𝖗 : {fols}
❖️ - 𝖋𝖔𝖑𝖑𝖔𝖎𝖓𝖌 : {fol} 
❖ - 𝖉𝖆𝖙𝖆 𝖆𝖈𝖈𝖔𝖚𝖓𝖙 : {dat}
❖ - 𝖕𝖔𝖘𝖙𝖘 : {bio}
❖ - 𝕹𝖚𝖒𝖇𝖊𝖗 : {L5}
❖ - 𝖋𝖆𝖈𝖊𝖇𝖔𝖔𝖐 : {L3}
❖ - 𝖗𝖊𝖘𝖊𝖙 : {email}
❖ - 𝕷𝖎𝖓𝖐 : https://www.instagram.com/{msg}
⋘────━𓆩𝐋 𝐄 𝐕 𝐈𓆪‏━────⋙ 
𓊆𝑅𝐸𝑆𝑇 𝐼𝑆 𝐷𝑂𝑁𝐸 ✅𓊇
❖ - ᗷY : @u_r_r""",parse_mode="html")
   except:
    Leviiio=f"""UserName Error"""
    bot.send_message(message.chat.id, f"{Leviiio}"))
bot.polling(True)
