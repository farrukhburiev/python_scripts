# Telegram Scripts Collection

A collection of Telegram bot scripts for various automation tasks.

## Projects

### 1. Script to Spam Message
Telegram bot for progressive message spamming with remote control.

**Features:**
- Progressive message spamming (1 to N characters)
- Remote control with "go" command to stop
- Rate limit handling
- Session persistence (keep session even after script stops)
- Easy configuration via `config.txt` (no code changes needed)
- Support for usernames, user IDs, group IDs, and channel IDs
- Customizable message symbol
- Customizable sleep interval between messages

**Setup:**
```bash
cd script_to_spam_message
pip install -r requirements.txt
python spam.py
```

**Configuration (config.txt):**
Edit the `config.txt` file to customize behavior:

```ini
# Target user/group/channel - can be:
#   - Username: @username
#   - User ID: 123456789
#   - Group ID: -123456789
#   - Channel ID: -100123456789
TARGET_USER=@D0STONboy

# Maximum number of message repetitions (1-99)
MAX_DOTS=70

# Symbol/character to repeat in messages (?, /, ., etc.)
MESSAGE_SYMBOL=?

# Sleep time (seconds) between messages
SLEEP_TIME=5
```

**Environment Setup:**
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
