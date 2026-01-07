# Telegram Scripts Collection

A collection of Telegram bot scripts for various automation tasks.

## Projects

### 1. Script to Spam Message
Telegram bot for progressive message spamming with remote control.

**Features:**
- Progressive message spamming (1 to N dots/characters)
- Remote control with "go" command
- Rate limit handling
- Session persistence
- Environment variable configuration

**Setup:**
```bash
cd script_to_spam_message
pip install -r requirements.txt
python spam.py
```

**Configuration:**
Create a `.env` file in the project root:
```
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
```

### 2. Script to Remove Users
Telegram bot for managing group members.

## Requirements
- Python 3.8+
- Telethon library
- Python-dotenv

## Security
⚠️ Never commit `.env` files or session files to version control. Use environment variables for sensitive data.

## License
See individual project folders for licenses.
