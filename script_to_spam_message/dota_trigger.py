import asyncio
import os
import subprocess
from dotenv import load_dotenv
from telethon import TelegramClient, events

# Load environment variables from .env file
load_dotenv()

# --- CONFIGURATION ---
API_ID = int(os.getenv('TELEGRAM_API_ID', '28508558'))
API_HASH = os.getenv('TELEGRAM_API_HASH', '8638b6ac44d3c90ad8d9859d9d5e3c2e')

# Load config from config.txt
def load_config():
    config = {}
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.txt')
    try:
        with open(config_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' in line:
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip()
    except FileNotFoundError:
        print("⚠️ config.txt not found. Using defaults.")
    return config

config = load_config()
TARGET_USER = config.get('TARGET_USER', '@D0STONboy')
TRIGGER_WORD = config.get('TRIGGER_WORD', 'dota')

print(f"[Config] TARGET_USER: {TARGET_USER}")
print(f"[Config] TRIGGER_WORD: {TRIGGER_WORD}")
print(f"[Trigger] Listening for '{TRIGGER_WORD}' word...")
print("[Status] Bot is running 24/7...\n")

async def main():
    # Using the same session for consistency
    client = TelegramClient('dota_trigger_session', API_ID, API_HASH)
    
    # Start without phone number - reuse existing session
    await client.connect()
    
    # Check if we're authorized, if not attempt to start
    if not await client.is_user_authorized():
        await client.start(phone='+998906446151')
    
    # --- DEBUG INFO ---
    me = await client.get_me()
    print(f"Logged in as: {me.first_name} (Username: @{me.username})")
    print(f"Watching for your own messages containing '{TRIGGER_WORD}'...\n")
    
    # Listen to your own outgoing messages
    @client.on(events.NewMessage(outgoing=True))
    async def trigger_handler(event):
        message_text = event.raw_text.strip().lower()
        
        # Check if message equals 'dota' or contains it as a standalone word
        if message_text == TRIGGER_WORD or f' {TRIGGER_WORD} ' in f' {message_text} ':
            print(f"\n[!] '{TRIGGER_WORD}' detected in your message!")
            print(f"[!] Starting spam script for {TARGET_USER}...")
            
            # Run spam.py as a subprocess
            script_dir = os.path.dirname(os.path.abspath(__file__))
            spam_script = os.path.join(script_dir, 'spam.py')
            
            # Get the correct Python executable from the virtual environment
            venv_path = os.path.join(os.path.dirname(script_dir), '.venv')
            python_exe = os.path.join(venv_path, 'Scripts', 'python.exe')
            
            if not os.path.exists(python_exe):
                # Fallback to just 'python' if venv not found
                python_exe = 'python'
            
            # Create environment with venv path
            env = os.environ.copy()
            env['VIRTUAL_ENV'] = venv_path
            env['PATH'] = os.path.join(venv_path, 'Scripts') + os.pathsep + env.get('PATH', '')
            
            try:
                # Run spam.py in the background with output visible
                process = subprocess.Popen(
                    [python_exe, spam_script],
                    cwd=script_dir,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    universal_newlines=True,
                    env=env
                )
                print(f"[✓] Spam script started! (PID: {process.pid})\n")
                
                # Check if process is still running after a short delay
                import time
                time.sleep(1)
                if process.poll() is not None:
                    # Process already exited, read the output
                    output = process.stdout.read() if process.stdout else ""
                    print(f"[!] Warning: Spam script exited quickly!")
                    if output:
                        print(f"[Output] {output}\n")
                else:
                    print(f"[✓] Spam script is running in background\n")
            except Exception as e:
                print(f"[✗] Error starting spam script: {e}\n")
    
    # Keep the client running
    await client.run_until_disconnected()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\nTrigger bot stopped.")
