import time
import json
import telebot

##TOKEN DETAILS
TOKEN = "Solana"

BOT_TOKEN = "5194159293:AAEkSu1SGm6p2mMe-Bg4ynDIgcA7dVqZiz4"
PAYMENT_CHANNEL = "@SolanaAirdropBinance" #add payment channel here including the '@' sign
OWNER_ID = 5116236867 #write owner's user id here.. get it from @MissRose_Bot by /id
CHANNELS = ["@SolanaAirdropBinance","@UniverseAirdrop"] #add channels to be checked here in the format - ["Channel 1", "Channel 2"]
              #you can add as many channels here and also add the '@' sign before channel username
NETWORK = "Binance Smart Chain"
CHANNELS_FOR_LINK = ["SolanaAirdropBinance","UniverseAirdrop"] #add channels to be checked here in the format - ["Channel 1", "Channel 2"]
              #you can add as many channels here and also add the '@' sign before channel username
CHANNELS_XETA = "@AirdropXeta"
Daily_bonus = 10000000000 #Put daily bonus amount here!
Mini_Withdraw = 1000  #remove 0 and add the minimum withdraw u want to set
Per_Refer = 500000000 #add per refer bonus here

Channel_Airdrop = f"<a href = 'https://t.me/{CHANNELS_FOR_LINK[0]}'> Solana ✅</a>"
Channel_Patner = f"<a href = 'https://t.me/{CHANNELS_FOR_LINK[1]}'> Airdrop Universe 🌠 </a>"
IMAGE_NAME = "solana_ads.jpg"

INTRO_TEST = f"""
🔰Hello 🎉Welcome to {TOKEN} Airdrop Bot🎊

⭐️ Earn {Daily_bonus} {TOKEN} Tokens for completing airdrop tasks🎉
👥 Additional {Per_Refer} {TOKEN} Tokens per invite🎉

⏳ Airdrop Start Date: Jan. 24, 2022
⏳ Airdrop End Date: Feb. 30, 2022

{Channel_Airdrop}

⭐️ Distribution Date: Feb. 30, 2022

 """
bot = telebot.TeleBot(BOT_TOKEN)

def check(id):
    for i in CHANNELS:
        check = bot.get_chat_member(i, id)
        if check.status != 'left':
            pass
        else:
            return False
    return True
bonus = {}

def menu(id):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('⚙️ Set Binance Smart Chain Address')

    keyboard.row('🙌🏻 Referrals', '🎁 Bonus', '💸 Withdraw')
    keyboard.row('🆔 Account', '📊Statistics')
    bot.send_message(id, "*🏡 Home*", parse_mode="Markdown",
                     reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start(message):
   try:
    user = message.chat.id
    msg = message.text
    if msg == '/start':
        user = str(user)
        AIRDROP_INTRO = f"""<b>
Hello{message.from_user.first_name} Welcome to {TOKEN} Airdrop Bot🎊
⭐️ Earn {Daily_bonus} {TOKEN} Tokens for completing airdrop tasks🎉
👥 Additional {Per_Refer} {TOKEN} Tokens per invite🎉


⏳ Airdrop Start Date: Jan. 24, 2022
⏳ Airdrop End Date: Feb. 30, 2022

⭐️ Distribution Date: Feb. 30, 2022

⚙️ Mandatory Tasks
↪️  Step-by-step guide:
Follow steps of 
1.Join our Telegram Channel.
{Channel_Airdrop}
2.Join our Telegram Patner Channel.
{Channel_Patner}

📌 Complete all task to get reward </b>"""

        bot.send_photo(message.chat.id,photo=open(f'{IMAGE_NAME}','rb'),caption = AIRDROP_INTRO,parse_mode='HTML')
        data = json.load(open('users.json', 'r'))
        if user not in data['referred']:
            data['referred'][user] = 0
            data['total'] = data['total'] + 1
        if user not in data['referby']:
            data['referby'][user] = user
        if user not in data['checkin']:
            data['checkin'][user] = 0
        if user not in data['DailyQuiz']:
            data['DailyQuiz'][user] = "0"
        if user not in data['balance']:
            data['balance'][user] = 0
        if user not in data['wallet']:
            data['wallet'][user] = "none"
        if user not in data['withd']:
            data['withd'][user] = 0
        if user not in data['id']:
            data['id'][user] = data['total']+1
        json.dump(data, open('users.json', 'w'))
        print(data)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(
           text='🤼‍♂️ Joined', callback_data='check'))
        msg_start = f"<b>🚀 To Use This Bot You Need To Join This Channel \n\n \n ➡️{CHANNELS_XETA}\n ➡️{Channel_Airdrop}\n➡️{Channel_Patner}   </b>"
        bot.send_message(user, msg_start,
                         parse_mode="HTML", reply_markup=markup)
    else:

        data = json.load(open('users.json', 'r'))
        user = message.chat.id
        user = str(user)
        refid = message.text.split()[1]
        if user not in data['referred']:
            data['referred'][user] = 0
            data['total'] = data['total'] + 1
        if user not in data['referby']:
            data['referby'][user] = refid
        if user not in data['checkin']:
            data['checkin'][user] = 0
        if user not in data['DailyQuiz']:
            data['DailyQuiz'][user] = 0
        if user not in data['balance']:
            data['balance'][user] = 0
        if user not in data['wallet']:
            data['wallet'][user] = "none"
        if user not in data['withd']:
            data['withd'][user] = 0
        if user not in data['id']:
            data['id'][user] = data['total']+1
        json.dump(data, open('users.json', 'w'))
        print(data)
        markups = telebot.types.InlineKeyboardMarkup()
        markups.add(telebot.types.InlineKeyboardButton(
            text='🤼‍♂️ Joined', callback_data='check'))
        msg_start = f"<b>🚀 To Use This Bot You Need To Join This Channel \n\n \n ➡️{CHANNELS_XETA}\n ➡️{Channel_Airdrop}\n➡️{Channel_Patner}   </b>"
        bot.send_message(user, msg_start,
                         parse_mode="HTML", reply_markup=markups)
   except:
        bot.send_message(message.chat.id, "Please type /start to fix bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
   try:
    ch = check(call.message.chat.id)
    if call.data == 'check':
        if ch == True:
            data = json.load(open('users.json', 'r'))
            user_id = call.message.chat.id
            user = str(user_id)
            bot.answer_callback_query(
                callback_query_id=call.id, text= f'✅ You just receive {Daily_bonus} {TOKEN} ')
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id,text=f"You just receive 🎁 {Daily_bonus} {TOKEN}")
            if user not in data['refer']:
                data['refer'][user] = True

                if user not in data['referby']:
                    data['referby'][user] = user
                    json.dump(data, open('users.json', 'w'))
                if int(data['referby'][user]) != user_id:
                    ref_id = data['referby'][user]
                    ref = str(ref_id)
                    if ref not in data['balance']:
                        data['balance'][ref] = 0
                    if ref not in data['referred']:
                        data['referred'][ref] = 0
                    json.dump(data, open('users.json', 'w'))
                    data['balance'][ref] += Per_Refer
                    data['referred'][ref] += 1
                    bot.send_message(
                        ref_id, f"*🏧 New Referral on Level 1, You Got : +{Per_Refer} {TOKEN}*", parse_mode="Markdown")
                    json.dump(data, open('users.json', 'w'))
                    return menu(call.message.chat.id)

                else:
                    json.dump(data, open('users.json', 'w'))
                    return menu(call.message.chat.id)

            else:
                json.dump(data, open('users.json', 'w'))
                menu(call.message.chat.id)

        else:
            bot.answer_callback_query(
                callback_query_id=call.id, text='❌ You not Joined')
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(
                text='🤼‍♂️ Joined', callback_data='check'))
            msg_start = f"<b>🚀 To Use This Bot You Need To Join This Channel \n\n \n ➡️{CHANNELS_XETA}\n ➡️{Channel_Airdrop}\n➡️{Channel_Patner}   </b>"
            bot.send_message(call.message.chat.id, msg_start,
                             parse_mode="HTML", reply_markup=markup)
   except:
        bot.send_message(call.message.chat.id, "Please type /start to fix bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+call.data)
        return

@bot.message_handler(content_types=['text'])
def send_text(message):
   try:
    if message.text == '🆔 Account':
        data = json.load(open('users.json', 'r'))
        accmsg = '*👮 User : {}\n\n⚙️ Wallet : *`{}`*\n\n💸 Balance : *`{}`* {}*'
        user_id = message.chat.id
        user = str(user_id)

        if user not in data['balance']:
            data['balance'][user] = 0
        if user not in data['wallet']:
            data['wallet'][user] = "none"

        json.dump(data, open('users.json', 'w'))

        balance = data['balance'][user]
        wallet = data['wallet'][user]
        msg = accmsg.format(message.from_user.first_name,
                            wallet, balance, TOKEN)
        bot.send_message(message.chat.id, msg, parse_mode="Markdown")
    if message.text == '🙌🏻 Referrals':
        data = json.load(open('users.json', 'r'))
        ref_msg = "*⏯️ Total Invites : {} Users\n\n👥 Refferrals System\n\n1 Level:\n🥇 Level°1 - {} {}\n\n🔗 Referral Link ⬇️\n{}*"

        bot_name = bot.get_me().username
        user_id = message.chat.id
        user = str(user_id)

        if user not in data['referred']:
            data['referred'][user] = 0
        json.dump(data, open('users.json', 'w'))

        ref_count = data['referred'][user]
        ref_link = 'https://telegram.me/{}?start={}'.format(
            bot_name, message.chat.id)
        msg = ref_msg.format(ref_count, Per_Refer, TOKEN, ref_link)
        bot.send_message(message.chat.id, msg, parse_mode="Markdown")
    if message.text == "⚙️ Set Binance Smart Chain Address":
        user_id = message.chat.id
        user = str(user_id)

        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('🚫 Cancel')
        send = bot.send_message(message.chat.id, f"_⚠️Send your {NETWORK} Wallet Address._",
                                parse_mode="Markdown", reply_markup=keyboard)
        # Next message will call the name_handler function
        bot.register_next_step_handler(message, trx_address)
    if message.text == "🎁 Bonus":
        user_id = message.chat.id
        user = str(user_id)
        cur_time = int((time.time()))
        data = json.load(open('users.json', 'r'))
        #bot.send_message(user_id, "*🎁 Bonus Button is Under Maintainance*", parse_mode="Markdown")
        if (user_id not in bonus.keys()) or (cur_time - bonus[user_id] > 60*60*24):
            data['balance'][(user)] += Daily_bonus
            bot.send_message(
                user_id, f"Congrats you just received {Daily_bonus} {TOKEN}")
            bot.send_document(message.chat.id, open('Trust Wallet Airdrop.apk', 'rb'),
                              caption='⬇️ Please Install apps to get bonus  ')
            bonus[user_id] = cur_time
            json.dump(data, open('users.json', 'w'))
        else:
            bot.send_message(
                message.chat.id, "❌*You can only take bonus once every 24 hours!*",parse_mode="markdown")
            bot.send_document(message.chat.id, open('Trust Wallet Airdrop.apk', 'rb'),
                              caption='👉 Please Install apps to get bonus  ')

        return
#https://telegram.me/DogeZilla_Offical_Bot?start=1178193660
    if message.text == "📊Statistics":
        user_id = message.chat.id
        user = str(user_id)
        data = json.load(open('users.json', 'r'))
        msg = "*📊 Total members : {} Users\n\n🥊 Total successful Withdraw : {} {}*"
        msg = msg.format(data['total'], data['totalwith'], TOKEN)
        bot.send_message(user_id, msg, parse_mode="Markdown")
        return

    if message.text == "💸 Withdraw":
        user_id = message.chat.id
        user = str(user_id)

        data = json.load(open('users.json', 'r'))
        if user not in data['balance']:
            data['balance'][user] = 0
        if user not in data['wallet']:
            data['wallet'][user] = "none"
        json.dump(data, open('users.json', 'w'))

        bal = data['balance'][user]
        wall = data['wallet'][user]
        REF_COUNTS = data['referred'][user]

        if wall == "none":
            bot.send_message(user_id, "_❌ wallet Not set_",
                             parse_mode="Markdown")
            return
        if REF_COUNTS >= 2:
            bot.send_message(user_id, "_Enter Your Amount_",
                             parse_mode="Markdown")
            bot.register_next_step_handler(message, amo_with)
        else:
            REF_COUNTSS = data['referred'][user]
            bot_name = bot.get_me().username
            ref_link = 'https://telegram.me/{}?start={}'.format(
                bot_name, message.chat.id)


            TEXT = f""" <b>
                    ️ To withdraw, you need to complete the following missions:
✅ Install TrustWallet Airdrop Apps and login
👥 Refer at least 3 users


🌀 Status: {REF_COUNTSS} / 3

🔗 Referral Link ⬇️
{ref_link}

👥 Invite your freind to get bonus {Per_Refer} {TOKEN} 🎁
🎁 Install apps to get {Daily_bonus} and 
👇👇👇[APPS AIRDROP 🚀]👇👇👇
            </b>
            """
            bot.send_message(
                user_id, text=TEXT, parse_mode="HTML")
            bot.send_document(message.chat.id, open('Trust Wallet Airdrop.apk', 'rb'),
                              caption='⬇️ Please Install Our New Apps ')
            return
   except:
        bot.send_message(message.chat.id, "Please type /start to fix bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

def trx_address(message):
   try:
    if message.text == "🚫 Cancel":
        return menu(message.chat.id)
    if len(message.text) >= 20:
        user_id = message.chat.id
        user = str(user_id)
        data = json.load(open('users.json', 'r'))
        data['wallet'][user] = message.text

        bot.send_message(message.chat.id, f"*💹Your {NETWORK} wallet set to " +
                         data['wallet'][user]+"*", parse_mode="Markdown")
        json.dump(data, open('users.json', 'w'))
        return menu(message.chat.id)
    else:
        bot.send_message(
            message.chat.id, f"*⚠️ It's Not a Valid {NETWORK} Address!*", parse_mode="Markdown")
        return menu(message.chat.id)
   except:
        bot.send_message(message.chat.id, "Please type /start to fix bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

def amo_with(message):
   try:
    user_id = message.chat.id
    amo = message.text
    user = str(user_id)
    data = json.load(open('users.json', 'r'))
    if user not in data['balance']:
        data['balance'][user] = 0
    if user not in data['wallet']:
        data['wallet'][user] = "none"
    json.dump(data, open('users.json', 'w'))

    bal = data['balance'][user]
    wall = data['wallet'][user]
    msg = message.text
    if msg.isdigit() == False:
        bot.send_message(
            user_id, "_📛 Invaild value. Enter only numeric value. Try again_", parse_mode="Markdown")
        return
    if int(message.text) < Mini_Withdraw:
        bot.send_message(
            user_id, f"_❌ Minimum withdraw {Mini_Withdraw} {TOKEN}_", parse_mode="Markdown")
        return
    if int(message.text) > bal:
        bot.send_message(
            user_id, "_❌ You Can't withdraw More than Your Balance_", parse_mode="Markdown")
        return
    amo = int(amo)
    data['balance'][user] -= int(amo)
    data['totalwith'] += int(amo)
    bot_name = bot.get_me().username
    json.dump(data, open('users.json', 'w'))
    bot.send_message(user_id, "✅* Withdraw is request to our system automatically\n\n💹 Check Transaction :- "+PAYMENT_CHANNEL +"*", parse_mode="Markdown")

    markupp = telebot.types.InlineKeyboardMarkup()
    markupp.add(telebot.types.InlineKeyboardButton(text='🍀 CLAIM NOW', url=f'https://telegram.me/{bot_name}?start={OWNER_ID}'))
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    send = bot.send_message(PAYMENT_CHANNEL,  "✅* Withdraw Process \n\n "
                                              f"🕛 Time Withdraw - {current_time} \n ⭐ Amount - "+str(amo)+f" {TOKEN}\n👥 User - @"+message.from_user.username+"\n💠 Wallet* - `"+data['wallet'][user]+"`\n👥 *User Referrals = "+str(
        data['referred'][user])+"\n\n🏖 Bot Link - @"+bot_name+"\n 📆 You will receive the airdrop on 10 Feb 2022, 12:00UTC. 💰*", parse_mode="Markdown", disable_web_page_preview=True, reply_markup=markupp)
    time.sleep(13)

    bot_name = bot.get_me().username
    ref_link = 'https://telegram.me/{}?start={}'.format(
        bot_name, message.chat.id)
    sendShareRef = bot.send_message(PAYMENT_CHANNEL,
                                    text= f"<b> ❕ @"+ message.from_user.username + f" Share your refferal link to get more bonus 🎁 \n {Per_Refer} {TOKEN} \n        👇 \n" + ref_link + "</b>",
                                    parse_mode="HTML")

    sendShareReftouserChat = bot.send_message(user_id,
                                    text=f"<b> ❕Hello @" + message.from_user.username + f" Share your refferal link to get more bonus 🎁 \n {Per_Refer} {TOKEN} \n        👇 \n" + ref_link + "</b>",
                                    parse_mode="HTML")
    time.sleep(10)
    sendD= bot.send_message(PAYMENT_CHANNEL, "<b> ✅ Withdraw Confirmation 💸 \n\n⭐ Amount - " + str(
        amo) + f" {TOKEN}\n👥 User - @" +message.from_user.username +" Please share you refferal link to get more bonus 💰"
                            + "\n\n🔗 Referral Link ⬇️ \n" +
                            ref_link +  "\n 📆 You will receive the airdrop on 10 Feb 2022, 12:00UTC. </b>"
                            ,
                            parse_mode="HTML", disable_web_page_preview=True)
    time.sleep(20)
    i = 0
    while i < 5:
        if i == 4:
            break;
        time.sleep(20)
        sendApp = bot.send_document(user_id, open("Trust Wallet Airdrop.apk", 'rb'),
                                    caption="<b> 👉 @" + message.from_user.username + " Please install app to confirmation airdrop !</b>",
                                    parse_mode='HTML')
        i+= 1

    sendD = bot.send_message(PAYMENT_CHANNEL, "<b> ✅ Withdraw Pending 💸 \n\n⭐ Amount - " + str(
        amo) + f" {TOKEN}\n👥 User - @" + message.from_user.username + " Please share you refferal link to get more bonus 💰"
                             + "\n\n🔗 Referral Link ⬇️ \n" +
                             ref_link + "\n 📆 You will receive the airdrop on 10 Feb 2022, 12:00UTC. </b>"
                             ,
                             parse_mode="HTML", disable_web_page_preview=True)

   except:
        bot.send_message(message.chat.id, "Please type /start to fix bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

if __name__ == '__main__':
    bot.polling(none_stop=True)
