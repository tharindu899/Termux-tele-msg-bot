
# Telegram Message Sender Bot

Automatically send formatted messages to Telegram channels/groups with image support. Perfect for notifications, announcements, or content distribution.

## ⚙️ Prerequisites
1. Python 3.7+
2. Telegram bot token from [@BotFather](https://t.me/BotFather)
3. Target Chat ID (use [@RawDataBot](https://t.me/RawDataBot) to find)
4. Termux (Android) or Linux environment

## 🚀 Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/telegram-message-sender.git
cd telegram-message-sender
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Create `.env` file with:
```env
TG_BOT_TOKEN="YOUR_BOT_TOKEN"
TG_CHAT_ID="TARGET_CHAT_ID"
OWNER_USERNAME="@your_username"
UPDATE_CHANNEL="@your_channel"
GROUP_CHAT_ID="your_group_chat_id"
WEBSITE_URL="https://your-website.com"
```

### 4. Create Message File (`message.txt`)
Use special directives and message content:
```text
#format=html
#photo=./banner.jpg

<b>Announcement</b> 📢
New update is live!
✅ Improved performance
✅ Bug fixes
✅ New features

<i>Join our channel for updates!</i>
```

### 5. File Structure
```bash
├── .env
├── message.txt     # Message content
├── banner.jpg      # Optional image
└── sender.py       # Main script
```

## 📝 Message Formatting Guide
### Directives (First 3 lines)
```text
#format=html          # html/markdown
#photo=./image.jpg    # Optional image path
```

### Format Options
**HTML Mode:**
```html
<b>Bold</b>, <i>Italic</i>, <u>Underline</u>
<a href="https://example.com">Link</a>
```

**Markdown Mode:**
```markdown
*Bold*, _Italic_, __Underline__
[Link](https://example.com)
```

## 🖼️ Button Configuration
Buttons are automatically generated from `.env`:
```env
OWNER_USERNAME="@admin"
UPDATE_CHANNEL="@news"
GROUP_CHAT_ID="-100123456"
WEBSITE_URL="https://my-site.com"
```

## ▶️ Running the Script
```bash
# Make executable
chmod +x sender.py

# Send message
./sender.py
```

## 🔧 Troubleshooting
- **File not found:** Ensure image paths in `message.txt` are correct
- **Invalid chat ID:** Use negative IDs for groups/channels (-100 prefix)
- **Parse errors:** Avoid unsupported tags in your message format
- **Permission issues:** Run `termux-setup-storage` in Termux

## 📦 Dependencies
- `python-telegram-bot` ~20.3
- `python-dotenv` ~1.0
- Python 3.7+

## ⚠️ Important Notes
1. Bot must be admin in target channel/group
2. Use absolute paths for images in cron jobs
3. Escape special characters in HTML/Markdown
4. Max image size: 10MB
5. Add bot to groups before sending

## 📄 License
MIT License - See [LICENSE](LICENSE) file
```
