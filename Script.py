class script(object):
    START_TXT = """🙅‍♂ 𝐒𝐨𝐫𝐫𝐲! 𝐍𝐨 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐅𝐫𝐨𝐦 𝐀𝐝𝐦𝐢𝐧 """
    START2_TXT = """𝐇𝐞𝐥𝐥𝐨 {} ,
👌 **I'm Movie Finder Bot**
😁 **I Can Give You Movies**
😋 **Just Send Me Movie Name **
🔮 **And Wait For Me To Do Magic**
🧑🏻‍💻 **Maintained By** <a href=https://t.me/iPRIMEHUB>𝐏𝐫𝐢𝐦𝐞𝐇𝐮𝐛</a>
"""
    HELP_TXT = """**😢 Sorry! No Support From Admin**\n **Any Queries ->** <a href=https://t.me/PrimeFeedBackBot>FeedBack</a>
"""

    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    SEARCHES_TEXT = """ **To Search Here, Click On Search Here Button 🔘...\nAnd To Search Somewhere, Click On Go Inline Button 🔘...**
"""

    DISCLAIMER_TXT = """⚠️𝘿𝙄𝙎𝘾𝙇𝘼𝙄𝙈𝙀𝙍
𝙰𝚕𝚕 𝚝𝚑𝚎 𝚌𝚘𝚗𝚝𝚎𝚗𝚝𝚜 𝚑𝚎𝚛𝚎 𝚊𝚛𝚎 𝚎𝚒𝚝𝚑𝚎𝚛 𝚏𝚘𝚛𝚠𝚊𝚛𝚍𝚎𝚍 𝚏𝚛𝚘𝚖 𝚘𝚝𝚑𝚎𝚛 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚘𝚛 𝚌𝚘𝚙𝚒𝚎𝚍 𝚏𝚛𝚘𝚖 𝚝𝚑𝚎𝚖. 𝚆𝚎 𝚍𝚘𝚗'𝚝 𝚘𝚠𝚗 𝚊𝚗𝚢 𝚘𝚏 𝚝𝚑𝚎 𝙼𝚘𝚟𝚒𝚎𝚜 𝚘𝚛 𝚂𝚎𝚛𝚒𝚎𝚜.
𝙸𝚏 𝚈𝚘𝚞 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚛𝚒𝚐𝚑𝚝 𝚘𝚠𝚗𝚎𝚛 𝚊𝚗𝚍 𝚠𝚊𝚗𝚝 𝚝𝚘 𝚛𝚎𝚖𝚘𝚟𝚎 𝚊𝚗𝚢 𝚌𝚎𝚛𝚝𝚊𝚒𝚗 𝚏𝚒𝚕𝚎𝚜, 𝙿𝚕𝚎𝚊𝚜𝚎 𝚛𝚎𝚙𝚘𝚛𝚝 𝚞𝚜, 𝚠𝚎 𝚊𝚛𝚎 𝚛𝚎𝚊𝚍𝚢 𝚝𝚘 𝚛𝚎𝚖𝚘𝚟𝚎 𝚝𝚑𝚘𝚜𝚎 𝚌𝚘𝚗𝚝𝚎𝚗𝚝 𝚊𝚜 𝚜𝚘𝚘𝚗 𝚊𝚜 𝚠𝚎 𝚌𝚊𝚗!
𝙰𝚍𝚖𝚒𝚗 𝙸𝚜 𝙽𝚘𝚝 𝚁𝚎𝚜𝚙𝚘𝚗𝚜𝚒𝚋𝚕𝚎 𝙵𝚘𝚛 𝚊𝚗𝚢 𝙳𝚒𝚛𝚎𝚌𝚝 & 𝚒𝚗𝚍𝚒𝚛𝚎𝚌𝚝 𝙿𝚛𝚘𝚏𝚒𝚝 𝚕𝚘𝚜𝚜"""

    REQUEST_TXT = """𝐁𝐞𝐟𝐨𝐫𝐞 𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐢𝐧𝐠 𝐌𝐚𝐤𝐞 𝐒𝐮𝐫𝐞 𝐓𝐡𝐞 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐈𝐬𝐧'𝐭 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐎𝐧 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 🙅‍♂️"""

    DONATE_MESSAGE = """
🥺Please Consider Donate it's helps me to keep Service alive and Motivated.
☺️It doesn't matters if you donate ₹10 or ₹50
or ₹100, what matters is that **You Donate**

               <a href=https://PayPal.me/rahulrahaman>Paypal |</a> </a> <a href=https://bit.ly/3FPKXRp>Paytm | </a><a href=bit.ly/3AhV8gv>Gpay</a>

 **upi-** ```iamrahulrahaman@ybl``` (tap2copy)
"""
    
#the end
