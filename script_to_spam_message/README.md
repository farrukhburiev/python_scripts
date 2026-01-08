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

---

### DOTA Trigger Bot (Auto-trigger with "dota" keyword)
Watches your own messages and automatically triggers the spam script when you type "dota".

**Features:**
- Listens to your own outgoing messages 24/7
- Automatically triggers spam script when "dota" is detected
- Uses the same `config.txt` configuration
- No manual trigger needed - fully automated

**Setup & Run:**
```bash
cd script_to_spam_message
python dota_trigger.py
```

**How it works:**
1. Bot watches all your outgoing messages
2. When you type "dota" (as a standalone word or exact message), it automatically starts the spam script
3. The spam script uses the target user from `config.txt`
4. Both scripts run simultaneously (trigger watches, spam sends)

**Keep it running 24/7:**
- On Windows: Use Task Scheduler to run `dota_trigger.py` at startup
- On Linux/Mac: Use `nohup python dota_trigger.py &` or add to crontab
- Or use a process manager like PM2 or screen
- **Recommended:** Deploy to DigitalOcean for 24/7 uptime (see [DEPLOYMENT.md](DEPLOYMENT.md))

## Cloud Deployment

For 24/7 uptime without keeping your PC on:

### ✅ **Railway.app (Recommended - FREE)**
- **Always-on 24/7**: Yes
- **Cost**: Free ($5/month credits, bot uses ~$0.50)
- **Setup time**: 5 minutes
- **Easiest**: Yes

👉 [Railway.app Setup Guide](../RAILWAY_DEPLOYMENT.md)

### Alternative Options:
- **GitHub Actions**: Free but has 6-hour timeout per run
- **DigitalOcean**: Cheap ($5-6/month) but not free

See detailed guides:
- [Railway.app Deployment](../RAILWAY_DEPLOYMENT.md) ← **START HERE**
- [GitHub Actions Deployment](../GITHUB_ACTIONS_DEPLOYMENT.md)
- [DigitalOcean Deployment](DEPLOYMENT.md)

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
