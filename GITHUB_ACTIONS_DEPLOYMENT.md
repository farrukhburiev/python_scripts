# GitHub Actions Deployment Guide

## Setup Instructions

### Step 1: Add Secrets to GitHub

1. Go to your GitHub repo
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add two secrets:
   - Name: `TELEGRAM_API_ID` | Value: your_api_id
   - Name: `TELEGRAM_API_HASH` | Value: your_api_hash

### Step 2: Workflow will run automatically

The workflow will:
- Run on every push to main branch
- Run on schedule every hour
- Can be triggered manually from GitHub UI

### Step 3: Monitor Execution

1. Go to **Actions** tab in your repo
2. Click on the workflow run to see logs

---

## ⚠️ Important Limitations

GitHub Actions has a **6-hour timeout per job**. This means:
- Bot will run for 6 hours maximum per session
- After 6 hours, it restarts automatically
- This may cause you to miss the trigger if it happens outside the 6-hour window

---

## ✅ Better Free Alternative: Railway.app (Recommended)

For a truly always-on 24/7 bot, **Railway.app** is better:

### Railway.app Advantages:
- Free tier: $5 credits/month (enough for this bot)
- No timeout limits
- Automatic restart on crash
- Easy GitHub integration
- 24/7 uptime

### Setup on Railway:

1. **Go to** https://railway.app
2. **Sign up** with GitHub
3. **Click "Create Project"**
4. **Select "Deploy from GitHub repo"**
5. **Select your telegram-bot repo**
6. **Add Environment Variables:**
   - `TELEGRAM_API_ID` = your_api_id
   - `TELEGRAM_API_HASH` = your_api_hash
7. **Set Start Command:** `python dota_trigger.py` (in script_to_spam_message folder)
8. **Deploy!**

Railway will show estimated monthly cost (usually $0-1 for this bot).

---

## If You Want to Stick with GitHub Actions

You can make it work by:
1. Using the workflow as-is (restarts every hour)
2. Or creating a more complex setup with persistent storage
3. But Railway.app is simpler and more reliable

---

## Comparison

| Platform | Cost | Always-On | Timeout | Setup |
|----------|------|-----------|---------|-------|
| GitHub Actions | Free (2000 min/month) | No (6 hr limit) | 6 hours | Easy |
| Railway.app | Free tier included | Yes | None | Easy |
| DigitalOcean | $5/month | Yes | None | Medium |
| Render | Free tier | No (spins down) | None | Easy |

**Recommendation:** Use Railway.app for best free experience with 24/7 uptime.

---

## Manual Trigger from GitHub UI

Even with the 6-hour limit, you can trigger manually:
1. Go to **Actions** tab
2. Click **Telegram DOTA Trigger Bot**
3. Click **Run workflow** → **Run workflow**

This instantly starts the bot for another 6 hours.
