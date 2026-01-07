# Telegram Spam Bot

A Telegram bot for progressive message spamming with remote control.

## Setup

1. Clone the repository
2. Create a `.env` file with your Telegram credentials:
   ```
   TELEGRAM_API_ID=your_api_id
   TELEGRAM_API_HASH=your_api_hash
   ```
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python spam.py`

## Features
- Progressive message spamming (1 to N dots)
- Remote control with "go" command
- Rate limit handling
- Session persistence
