import os
import random
from asyncio import Future, sleep
import time
from Script import script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

#txt messages
MSG = """**😔 Sorry! No Service Available..**\n**Instead Of Me Use** ~> <a href=https://t.me/inetflixrobot>🅽︎🅴︎🆃︎🅵︎🅻︎🅸︎🆇︎</a>"""
PIK = 'https://telegra.ph/file/f4d232fde3824518ae623.jpg'
PIK2 = 'https://telegra.ph/file/67474faec309ca88f7a71.jpg'
DONATE_QR = 'https://telegra.ph/file/97424ec12aabfe9b4b58c.jpg'
PINGU = """```pong!!!!```"""


#buttons
DONATE_BUTTON = [[
InlineKeyboardButton('Paypal', url=f'https://PayPal.me/rahulrahaman'), 
InlineKeyboardButton('GPay', url=f'https://bit.ly/3FPKXRp'),
InlineKeyboardButton('Paytm ', url=f'https://bit.ly/3FPKXRp'),
]]

REQUEST_BUTTON = [[
InlineKeyboardButton('📢 Support Channel', url=f'https://t.me/iPrimeHub'), 
InlineKeyboardButton('👥 Request Content', url=f'https://t.me/PrimeHubReq'),
]]


DISCLAIMER_BUTTON = [[
            InlineKeyboardButton('🫂 Dev', url=f'https://t.me/h7n9_alpha'),
            InlineKeyboardButton('ℹ️ Report', url=f'https://t.me/PrimeFeedbackBot')
        ]]

MOREBOTS_BUTTON = [
            [
            InlineKeyboardButton('🔗 File To Link Bot', url=f'https://t.me/FileLinkRBot'),
            InlineKeyboardButton('🥷 Force Subscribe Bot', url=f'https://t.me/primesubs_bot'),
            ],[
            InlineKeyboardButton('🐾 Request Tracker Bot', url=f'https://t.me/primecaption_bot'),
            InlineKeyboardButton('🖊️ Files Renamer Bot', url=f'https://t.me/PrimeRenamersBot'),
            ],[
            InlineKeyboardButton('🖇️ Link Shortner Bot', url=f'https://t.me/primeshort_bot'),
            InlineKeyboardButton('📥 URL Uploader Bot', url=f'https://t.me/PrimeDownloderBot'),
            ],[
            InlineKeyboardButton('🍆 Torrent Search Bot', url=f'https://t.me/PRIMETOROBot'),
            InlineKeyboardButton('🔥 Torrent Leeching ', url=f'https://t.me/PrimeLeech'),
            ]
         ]


#donate message
@Client.on_message(filters.command('donate') & filters.incoming & ~filters.edited)      #DONATE COMMANDS AND MASSAGES
def donate(bot, message): 
    reply_markup = InlineKeyboardMarkup(DONATE_BUTTON)
    q = message.reply_photo(
        photo=DONATE_QR,
        caption=script.DONATE_MESSAGE,
        reply_markup=reply_markup,
    )
    time.sleep(300)
    q.delete()
    message.delete(message.message_id)
 
#request to
@Client.on_message(filters.command("request") & filters.incoming & ~filters.edited)
def request(client, message):
    reply_markup = InlineKeyboardMarkup(REQUEST_BUTTON)
    w = message.reply_photo(
        photo=PIK2,
        caption = script.REQUEST_TXT,
        reply_markup=reply_markup,
        parse_mode='html',
    )
    time.sleep(30)
    w.delete()
    message.delete(message.message_id)

#help message
@Client.on_message(filters.command("help") & filters.incoming & ~filters.edited)
def help(client, message):
    text = script.HELP_TXT
    t = message.reply(
        text=text,
        reply_to_message_id=message.message_id,
        disable_web_page_preview=True
    )
    time.sleep(120)
    t.delete()
    message.delete(message.message_id)

#alive msg
@Client.on_message(filters.command("ping") & filters.incoming & ~filters.edited)
def help(client, message):
    text = PINGU
    pg = message.reply(
        text=text,
    )
    time.sleep(7)
    pg.delete()
    message.delete(message.message_id
    )


#disclaimer message
@Client.on_message(filters.command('disclaimer') & filters.incoming & ~filters.edited)      
def disclaimer(bot, message):
    text = script.DISCLAIMER_TXT
    reply_markup = InlineKeyboardMarkup(DISCLAIMER_BUTTON)
    l = message.reply(
        text=text,
        reply_to_message_id=message.message_id,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
    time.sleep(60)
    l.delete()
    message.delete(message.message_id)

@Client.on_message(filters.text & filters.private & filters.incoming & ~filters.edited)      
def regex(bot, message):
    mr = message.reply(
        text=MSG,
        disable_web_page_preview=True
    )
    time.sleep(30)
    mr.delete()
    message.delete(message.message_id
    )

