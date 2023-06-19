# Credits: @doudesuid

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ ᴘᴇʀɪɴᴛᴀʜ ᴜɴᴛᴜᴋ ᴘᴇɴɢɢᴜɴᴀ ʙᴏᴛ
 ├ /start - ᴍᴜʟᴀɪ ʙᴏᴛ
 ├ /about - ᴛᴇɴᴛᴀɴɢ ʙᴏᴛ ɪɴɪ
 ├ /help - ʙᴀɴᴛᴜᴀɴ ᴘᴇʀɪɴᴛᴀʜ ʙᴏᴛ ɪɴɪ
 ├ /ping - ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴄᴇᴋ ʙᴏᴛ ʜɪᴅᴜᴘ
 └ /uptime - ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ sᴛᴀᴛᴜs ʙᴏᴛ
 
 ❏ ᴘᴇʀɪɴᴛᴀʜ ᴋʜᴜsᴜs ᴀᴅᴍɪɴ
 ├ /logs - ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ʟᴏɢs ʙᴏᴛ
 ├ /setvar - ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴛᴜʀ ᴠᴀʀ ᴅᴇɴɢᴀɴ ᴄᴏᴍᴍᴀɴᴅ ᴅɪ ʙᴏᴛ 
 ├ /delvar - ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ᴠᴀʀ ᴅᴇɴɢᴀɴ ᴄᴏᴍᴍᴀɴᴅ ᴅɪ ʙᴏᴛ 
 ├ /getvar - ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ sᴀʟᴀʜ sᴀᴛᴜ ᴠᴀʀ ᴅᴇɴɢᴀɴ ᴄᴏᴍᴍᴀɴᴅ ᴅɪ ʙᴏᴛ 
 ├ /users - ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ sᴛᴀᴛɪsᴛɪᴋ ᴘᴇɴɢɢᴜɴᴀ ʙᴏᴛ 
 ├ /batch - ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ʟɪɴᴋ ᴍᴇɴᴊᴀᴅɪ sᴀᴛᴜ ғɪʟᴇ 
 ├ /speedtest - ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴇsᴛ ᴋᴇᴄᴇᴘᴀᴛᴀɴ sᴇʀᴠᴇʀ ʙᴏᴛ
 └ /broadcast - ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ʙʀᴏᴀᴅᴄᴀsᴛ ᴋᴇ ᴘᴇɴɢɢᴜɴᴀ ʙᴏᴛ

🐾 ᴅᴇᴠᴇʟᴏᴀᴅ ʙʏ </b> <a href='https://t.me/doudesuid'>ᴅᴏᴜᴅᴇsᴜɪᴅ</a>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("• ᴄᴏᴍᴍᴀɴᴅs •", callback_data="help"),
            InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close")
        ],
    ]

    ABOUT = """
<b>ᴛᴇɴᴛᴀɴɢ ʙᴏᴛ ɪɴɪ:

@{} ᴀᴅᴀʟᴀʜ ʙᴏᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴜɴᴛᴜᴋ ᴍᴇɴʏɪᴍᴘᴀɴ ᴘᴏsᴛɪɴɢᴀɴ ᴀᴛᴀᴜ ғɪʟᴇ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴅɪ ᴀᴋsᴇs ᴍᴇʟᴀʟᴜɪ ʟɪɴᴋ ᴋʜᴜsᴜs.

 • ᴘᴇɴᴄɪᴘᴛᴀ: <a href='https://t.me/doudesuid'>ᴀʙᴏᴜᴛ ᴍᴇ</a>
 • ᴘᴇɴɢᴇʟᴏʟᴀ: <a href='https://t.me/doudesuid'>ᴀʙᴏᴜᴛ ᴍᴇ</a>

🐾 ᴅᴇᴠᴇʟᴏᴀᴅ ʙʏ </b> <a href='https://t.me/doudesuid'>ᴅᴏᴜᴅᴇsᴜɪᴅ</a>
"""
