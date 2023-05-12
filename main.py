import os , random , time

try:

	import requests , telebot 	from telebot import types 

except ModuleNotFoundError:

	os.system('pip install requests')

	os.system('pip install telebot')

	os.system('pip install pyTelegramBotAPI')

bot = telebot.TeleBot("5736354783:AAFGixehl-NchvL0UxEhnFxUVIfyZJKFpSY")

@bot.message_handler(commands=["start"])

def start(message):

   ur = ('https://t.me/CRISTIANUUU/20','https://t.me/CRISTIANUUU/24','https://t.me/CRISTIANUUU/32','https://t.me/CRISTIANUUU/31','https://t.me/CRISTIANUUU/21','https://t.me/CRISTIANUUU/22','https://t.me/CRISTIANUUU/25','https://t.me/CRISTIANUUU/33','https://t.me/CRISTIANUUU/29','https://t.me/CRISTIANUUU/36','https://t.me/CRISTIANUUU/20','https://t.me/CRISTIANUUU/38','https://t.me/CRISTIANUUU/35','https://t.me/CRISTIANUUU/98')

   url = str("".join(random.choice(ur)for i in range(1)))

   print(url)

   Name = message.chat.first_name

   A = types.InlineKeyboardMarkup(row_width=1)

   F = types.InlineKeyboardButton(text = "⌯ 𝚂𝚃𝙰𝚁𝚃 ReseT ⌯",callback_data="y")

   A.add(F)

   bot.send_photo(message.chat.id,url,f"""*صباح الفل يسطا ({Name}) 🥶

•━━━━━━━━━━━━•

بوت ريست انستا ل⚡️

برمجة علاء 🙂

*""",parse_mode = "markdown")

@bot.message_handler(func=lambda m: True)

def reset(message):

	email = message.text

	ch = bot.send_message(message.chat.id,text=f"• انتظر قليلاً  ...!\n • Plases WaiT ...!")

	url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"

	headers = {}

	headers['Content-Length']='319'

	headers['Content-Type']='application/x-www-form-urlencoded;charset=UTF-8'

	headers['Host']='i.instagram.com'

	headers['Connection']='Keep-Alive'

	headers['User-Agent']='Instagram6.12.1Android(26/8.0.0;560dpi;1440x2560;samsung/Verizon;SM-G930V;heroqltevzw;qcom;en_US)'

	headers['Cookie']='mid=YwEuiAABAAGBdZ2ajZXFL5EOuNSE;csrftoken=ayOokI9GUT5f9Up0aLulP8mSehjppSys'

	headers['Cookie2']='$Version=1'

	headers['Accept-Language']='en-US'

	headers['X-IG-Connection-Type']='WIFI'

	headers['X-IG-Capabilities']='AQ=='

	headers['Accept-Encoding']='gzip' 

	data = f"ig_sig_key_version=4&signed_body=e97dc9c43a2967793f2dd2b4f567fae41b45e8a2b545a3ec4acd5faca5879e7a.%7B%22user_email%22%3A%22{email}%22%2C%22device_id%22%3A%22android-074b337ee8f413e0%22%2C%22guid%22%3A%228013fb43-e663-4a10-a892-5ffea66a508b%22%2C%22_csrftoken%22%3A%22ayOokI9GUT5f9Up0aLulP8mSehjppSys%22%7D"

	res = requests.post(url,headers=headers,data=data).json()

	if res['status']=='ok':

		bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f"بعتلك ريست يسطا ✅ \n{res}")

	else:

		bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f"• Fail ReSeT ❌")

try:

	bot.infinity_polling()

except:

	bot.infinity_polling()
