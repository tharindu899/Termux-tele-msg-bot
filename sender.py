#!/data/data/com.termux/files/usr/bin/python
import os
import asyncio
from dotenv import load_dotenv
from telegram import Bot, InputFile, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode

# Load Environment Variables
load_dotenv()
BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID")
OWNER = os.getenv("OWNER_USERNAME")
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL")  # Add to .env: UPDATE_CHANNEL="@YourChannel"
GROUP_CHAT = os.getenv("GROUP_CHAT_ID")
WEBSITE = os.getenv("WEBSITE_URL")

def parse_message_file(file_path="message.txt"):
    photo_path = None
    parse_mode = ParseMode.HTML
    message_lines = []
    
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                stripped = line.strip()
                if "photo=" in stripped:
                    photo_path = stripped.split("photo=", 1)[1].strip()
                elif "format=" in stripped:
                    fmt = stripped.split("format=", 1)[1].strip().lower()
                    parse_mode = ParseMode.HTML if fmt == "html" else ParseMode.MARKDOWN
            else:
                message_lines.append(line.rstrip('\n'))
    return photo_path, parse_mode, "\n".join(message_lines)

def create_keyboard():
    owner_username = OWNER.lstrip('@')
    channel_username = UPDATE_CHANNEL.lstrip('@')
    group_username = GROUP_CHAT.lstrip('@')
    
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("👑 Owner", url=f"https://t.me/{owner_username}"),
            InlineKeyboardButton("📢 Updates", url=f"https://t.me/{channel_username}")
        ],
        [
            InlineKeyboardButton("💬 Chat", url=f"https://t.me/{group_username}"),
            InlineKeyboardButton("🌐 Website", url=WEBSITE)
        ]
    ])

async def send_message():
    bot = Bot(token=BOT_TOKEN)
    photo_path, parse_mode, message = parse_message_file()
    keyboard = create_keyboard()
    
    try:
        if photo_path and os.path.exists(photo_path):
            with open(photo_path, "rb") as photo_file:
                await bot.send_photo(
                    chat_id=CHAT_ID,
                    photo=InputFile(photo_file),
                    caption=message,
                    parse_mode=parse_mode,
                    reply_markup=keyboard
                )
        else:
            await bot.send_message(
                chat_id=CHAT_ID,
                text=message,
                parse_mode=parse_mode,
                reply_markup=keyboard
            )
        print("✅ Message sent successfully!")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(send_message())
