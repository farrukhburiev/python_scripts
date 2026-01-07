# Telegram Channel User Remover Bot

A Python script to remove all users from your Telegram channel one by one.

## Prerequisites

1. **Python 3.8+** installed
2. **Telegram API credentials** from https://my.telegram.org

## Setup Instructions

### Step 1: Get Telegram API Credentials

1. Go to https://my.telegram.org
2. Login with your phone number
3. Go to "API development tools"
4. Create a new app:
   - App title: anything (e.g., "Channel Bot")
   - Short name: anything
5. Copy your **API ID** and **API Hash**

### Step 2: Install Required Package

```bash
pip install telethon
```

Or if you have Python 3.9+:
```bash
pip install telethon cryptg
```

### Step 3: Run the Bot

```bash
python telegram_kick_bot.py
```

You'll be prompted to enter:
- **API ID**: From my.telegram.org
- **API Hash**: From my.telegram.org  
- **Phone number**: Your Telegram account phone (with country code, e.g., +1234567890)
- **Channel username**: Your channel name without @ (e.g., if channel is @mychannel, enter: mychannel)

### Step 4: Choose Action

Menu options:
```
1. Remove all users - Kicks everyone except the owner
2. View channel members - Lists all users
3. Remove specific user - Remove by user ID
4. Exit
```

## Important Notes

⚠️ **Requirements:**
- You must be the **channel owner** to remove users
- Your account must have **admin permissions** in the channel
- The script removes users one by one with delays to avoid Telegram rate limiting

⚠️ **Safety:**
- This action is **irreversible** - removed users cannot rejoin unless you add them back
- Use with caution!
- The bot skips the channel owner automatically

## How It Works

1. Connects to Telegram using your credentials
2. Gets the channel and list of all members
3. Removes each user one by one by restricting their view_messages permission
4. Shows progress for each removal
5. Displays final statistics

## Troubleshooting

**"Not admin in this channel" error:**
- Make sure you're the channel owner
- Ensure you have admin privileges in the channel

**"Session already exists" error:**
- Delete `session_name.session` file and try again

**"Flood wait" error:**
- Telegram is rate limiting you
- The script already has delays - just wait and try again

**"Phone number invalid" error:**
- Use format with country code: +1234567890 (not 1234567890)

## Example Usage

```
Enter API ID: 123456789
Enter API Hash: abcd1234efgh5678ijkl
Phone number: +1234567890
Channel username: my_channel

Select option: 1
🚫 STARTING MASS USER REMOVAL
✅ [1/50] john_user
✅ [2/50] jane_user
...
```

## Advanced: Manual User Removal

Edit the script to add this function for removing specific users:

```python
# Remove by username
await bot.remove_user_by_username(channel_username, "username")

# Remove by user ID
await bot.remove_user_by_id(channel_username, 123456789)
```

## Notes

- Removals are one-by-one with 0.5 second delays
- The bot logs all actions
- Session file is saved locally for faster future logins
- You can interrupt with Ctrl+C

Enjoy! 🚀
