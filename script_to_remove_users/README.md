# Telegram Channel User Remover Bot 🚫

A Python bot that removes all users from your Telegram channel one by one. Perfect for channel cleanup, resetting, or mass user removal.

## Features

✅ **Mass User Removal** - Remove all users from your channel automatically  
✅ **Channel ID & Username Support** - Works with both channel IDs and usernames  
✅ **Two-Factor Authentication** - Supports 2FA protected accounts  
✅ **Individual User Removal** - Remove specific users by ID  
✅ **Member Listing** - View all channel members  
✅ **Progress Tracking** - Real-time removal status  
✅ **Rate Limit Handling** - Built-in delays to avoid Telegram restrictions  

## Prerequisites

- **Python 3.8+**
- **Telegram Account** (with admin rights in your channel)
- **Telegram API Credentials** from [my.telegram.org](https://my.telegram.org)

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/telegram-channel-remover.git
cd telegram-channel-remover
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install telethon cryptg
```

### Step 3: Get Telegram API Credentials

1. Visit [my.telegram.org](https://my.telegram.org)
2. Login with your Telegram phone number
3. Go to "API development tools"
4. Create a new app:
   - App title: `Channel Bot` (or anything)
   - Short name: `channel_bot`
5. Copy your **API ID** and **API Hash**

## Usage

### Run the Bot

```bash
python telegram_kick_bot.py
```

### Interactive Menu

```
📝 Enter your Telegram credentials:
API ID: [Enter your API ID]
API Hash: [Enter your API Hash]
Phone number: [+1234567890]

❓ How do you want to identify the channel?
1. By username (e.g., mychannel)
2. By channel ID (e.g., -1001234567890)

[Select option]

🤖 Menu:
1. Remove all users - Kicks everyone except owner
2. View channel members - Lists all members
3. Remove specific user - Remove by user ID
4. Exit
```

## Getting Your Channel ID

1. Open your channel in Telegram
2. View the channel info/settings
3. The ID format is: `-100123456789` (channel IDs always start with -100)

Or use the URL method:
- If URL is `https://t.me/c/123456789`, your ID is `-100123456789`

## Important Notes

⚠️ **Requirements:**
- You must be the **channel owner** to remove users
- Your account needs **admin permissions**
- The bot automatically skips the channel owner

⚠️ **Safety:**
- This action is **irreversible** - removed users cannot rejoin unless manually added
- Use with caution!
- Test with a small group first

⚠️ **Telegram Limits:**
- Telegram has rate limits to prevent abuse
- The bot includes 0.5-second delays between removals
- If you hit a "flood wait" error, wait and try again

## Troubleshooting

### "Not admin in this channel" Error
- Verify you're the channel owner
- Ensure your account has admin privileges
- Try signing in again

### "Session already exists" Error
- Delete `session_name.session` and `session_name.session-journal` files
- Run the script again

### "Flood wait" Error
- Telegram rate-limited your account
- Wait 30-60 minutes and try again
- The delays in the script should prevent this

### "Invalid code" Error
- The verification code from Telegram is time-sensitive (usually 5 minutes)
- Check your Telegram app for the code
- If it expires, the script will ask for a new one

### Cannot Type Password
- Make sure your terminal supports input
- Try running in PowerShell or CMD (not some restricted shells)
- Use `python telegram_kick_bot.py` directly

## Project Structure

```
telegram-channel-remover/
├── telegram_kick_bot.py      # Main bot script
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
├── README.md                # This file
└── LICENSE                  # MIT License
```

## How It Works

1. **Authentication** - Connects to Telegram using your credentials
2. **Channel Access** - Retrieves the channel and member list
3. **Removal Loop** - Iterates through members and removes each one
4. **Progress Tracking** - Shows real-time removal status
5. **Error Handling** - Skips failed removals and logs errors

## Code Example

```python
import asyncio
from telegram_kick_bot import TelegramChannelCleaner

async def main():
    bot = TelegramChannelCleaner(api_id=123456, api_hash="abc123", phone="+1234567890")
    await bot.start()
    
    # Remove all users from channel
    await bot.remove_all_users(-1001234567890)
    
    await bot.close()

asyncio.run(main())
```

## Advanced Usage

### Remove Specific User
```python
await bot.remove_user_by_id(channel_id, user_id)
```

### Get Channel Members
```python
members = await bot.get_channel_members(channel_id)
```

## License

MIT License - See LICENSE file for details

## Disclaimer

This tool is for **administrative purposes only**. Use it responsibly on channels you own or have explicit permission to manage. The authors are not responsible for misuse.

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push and create a Pull Request

## Support

If you encounter issues:
1. Check the **Troubleshooting** section
2. Review [Telethon Documentation](https://docs.telethon.dev)
3. Open an issue on GitHub

## Author

Created for efficient Telegram channel management.

---

**Star ⭐ this repo if it helped you!**
