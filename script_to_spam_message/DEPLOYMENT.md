# Deployment Guide - DigitalOcean

This guide shows how to deploy the bot to DigitalOcean so it runs 24/7 on a server instead of your local machine.

## Option 1: DigitalOcean App Platform (Easiest - Recommended)

### Prerequisites
- DigitalOcean account
- GitHub account (fork this repo to your account)

### Steps

1. **Push code to GitHub**
   - Make sure your code is pushed to your GitHub repository

2. **Create DigitalOcean App**
   - Go to https://cloud.digitalocean.com/apps
   - Click "Create App"
   - Select "GitHub" as source
   - Connect your GitHub account and select this repository
   - Select the branch to deploy

3. **Configure the App**
   - Set Resource Type: Basic (0.5GB RAM, $5/month)
   - Set Python version if needed

4. **Add Environment Variables**
   - Go to "Settings" → "App-level Environment Variables"
   - Add the following:
     ```
     TELEGRAM_API_ID=your_api_id
     TELEGRAM_API_HASH=your_api_hash
     ```

5. **Edit app.yaml (Optional)**
   - Click "Edit" and configure the app specification
   - Make sure the run command is: `python dota_trigger.py`

6. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete

---

## Option 2: DigitalOcean Droplet (More Control - Cheaper)

### Prerequisites
- DigitalOcean account
- SSH client (PuTTY on Windows or built-in Terminal)

### Steps

1. **Create a Droplet**
   - Go to https://cloud.digitalocean.com/droplets
   - Click "Create Droplet"
   - Choose: Ubuntu 22.04 LTS
   - Choose the $6/month plan (1GB RAM)
   - Select your region
   - Click "Create Droplet"

2. **Access Your Droplet**
   ```bash
   ssh root@your_droplet_ip
   ```
   (Password will be emailed to you)

3. **Install Dependencies**
   ```bash
   apt update
   apt install -y python3 python3-pip git
   ```

4. **Clone Repository**
   ```bash
   cd /root
   git clone https://github.com/your_username/your_repo_name.git
   cd your_repo_name/script_to_spam_message
   ```

5. **Install Python Packages**
   ```bash
   pip3 install -r requirements.txt
   ```

6. **Create .env File**
   ```bash
   nano .env
   ```
   Add:
   ```
   TELEGRAM_API_ID=your_api_id
   TELEGRAM_API_HASH=your_api_hash
   ```
   Save with Ctrl+X, then Y, then Enter

7. **Create a Screen Session (Keep Running)**
   ```bash
   screen -S telegram_bot
   python3 dota_trigger.py
   ```
   
   Press Ctrl+A then D to detach from screen (it keeps running)

8. **Optional: Use Systemd Service for Auto-restart**
   
   Create a service file:
   ```bash
   nano /etc/systemd/system/telegram-bot.service
   ```
   
   Add:
   ```ini
   [Unit]
   Description=Telegram DOTA Trigger Bot
   After=network.target
   
   [Service]
   Type=simple
   User=root
   WorkingDirectory=/root/script_to_spam_message
   ExecStart=/usr/bin/python3 /root/script_to_spam_message/dota_trigger.py
   Restart=always
   RestartSec=10
   
   [Install]
   WantedBy=multi-user.target
   ```
   
   Enable and start:
   ```bash
   systemctl daemon-reload
   systemctl enable telegram-bot.service
   systemctl start telegram-bot.service
   ```
   
   Check status:
   ```bash
   systemctl status telegram-bot.service
   ```

---

## Option 3: Docker Deployment

If you're familiar with Docker:

1. **Build Image**
   ```bash
   docker build -t telegram-bot .
   ```

2. **Run Container**
   ```bash
   docker run -d --env-file .env telegram-bot
   ```

---

## Verify It's Running

Once deployed, you can verify by:
1. Type your TRIGGER_WORD in Telegram
2. Check if spam script starts
3. Check DigitalOcean dashboard for logs

## Cost
- **App Platform**: $5/month (easiest)
- **Droplet ($6/month)**: Cheapest option, more control

## Support
If you have issues:
1. Check logs: `journalctl -u telegram-bot.service -f` (Droplet)
2. Verify .env has correct credentials
3. Check Telegram API ID/Hash are correct
