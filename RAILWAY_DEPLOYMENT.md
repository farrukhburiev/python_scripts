# Railway.app Deployment (Recommended Free Option)

Railway.app is the **best free solution** for 24/7 Telegram bots. You get $5/month free credits (enough for this bot).

## Setup (5 minutes)

### Step 1: Create Railway Account
1. Go to https://railway.app
2. Click **"Start Project"**
3. Sign in with **GitHub**
4. Click **"Authorize railway"**

### Step 2: Deploy from GitHub
1. Click **"Create Project"**
2. Click **"Deploy from GitHub repo"**
3. Select your telegram-bot repository
4. Select **main** branch
5. Click **"Deploy"**

### Step 3: Add Environment Variables
1. In Railway dashboard, click your project
2. Click **"Variables"** tab
3. Click **"Add Variable"** and add:
   ```
   TELEGRAM_API_ID = your_api_id_here
   TELEGRAM_API_HASH = your_api_hash_here
   ```
4. Click **"Save"**

### Step 4: Configure Start Command
1. Click **"Settings"**
2. Find **"Start Command"**
3. Enter: `cd script_to_spam_message && python dota_trigger.py`
4. Click **"Save"**

### Step 5: Deploy
1. Go to **"Deployments"** tab
2. Click **"Deploy"**
3. Wait for green checkmark (takes ~2 minutes)
4. Bot is now running 24/7! 🎉

---

## Monitor Your Bot

- **View Logs:** Click your project → **Logs** tab
- **Check Status:** Green = running, Red = error
- **Restart:** Click **"Restart"** button
- **Stop:** Click **"Pause"** button

---

## Cost

- **Free tier:** $5/month credits
- **This bot uses:** ~$0.50/month (CPU + memory)
- **Your cost:** FREE! ✅

---

## Troubleshooting

**Bot keeps crashing?**
1. Check the Logs tab for errors
2. Verify TELEGRAM_API_ID and TELEGRAM_API_HASH are correct
3. Make sure .env variables are set in Railway

**Can't see logs?**
1. Go to Logs tab → scroll to bottom
2. Look for errors like "ModuleNotFoundError"
3. Check if requirements.txt is being installed

**Bot not responding to "dota"?**
1. Make sure trigger word is set in config.txt
2. Check that you're using the correct account
3. Verify bot is actually running in Logs

---

## Update Your Bot

After making changes locally:
1. Push to GitHub: `git push origin main`
2. Railway **automatically redeploys**
3. New version live in ~2 minutes! 🚀

---

## Stop/Delete

To stop the bot:
- **Temporarily:** Click "Pause" in Railway
- **Permanently:** Click "Delete" in Settings

You won't be charged if it's paused or deleted.

---

## Next Steps

1. Sign up: https://railway.app
2. Deploy from your GitHub repo
3. Add secrets
4. Set start command
5. Click deploy
6. Done! ✅

Questions? Check Railway.app docs: https://docs.railway.app
