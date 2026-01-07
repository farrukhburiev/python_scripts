import asyncio
from telethon import TelegramClient, events, errors

# --- CONFIGURATION ---
API_ID = 28508558
API_HASH = '8638b6ac44d3c90ad8d9859d9d5e3c2e'

# The account receiving the dots and sending "go"
TARGET_USER = '@D0STONboy' 

MAX_DOTS = 20
SLEEP_TIME = 5 
# ---------------------

keep_running = True

async def main():
    global keep_running
    
    # Using a fresh session name to avoid cache issues
    client = TelegramClient('final_bot_session', API_ID, API_HASH)
    
    await client.start(phone='+998906446151')
    
    # --- DEBUG INFO ---
    me = await client.get_me()
    print(f"Logged in as: {me.first_name} (Username: @{me.username})")
    
    try:
        target_entity = await client.get_input_entity(TARGET_USER)
        print(f"Targeting: {TARGET_USER}")
    except Exception as e:
        print(f"Error finding {TARGET_USER}: {e}")
        return

    if me.username == TARGET_USER.replace('@', ''):
        print("⚠️ WARNING: You are messaging YOURSELF. This will go to Saved Messages.")
    # ------------------

    # 1. THE LISTENER
    @client.on(events.NewMessage(chats=target_entity, incoming=True, pattern='(?i)go'))
    async def stop_handler(event):
        global keep_running
        keep_running = False
        print("\n[!] 'go' received from target account!")
        
        # The custom message you wanted
        await event.respond('got u mf')
        
        print("Stopping script...")
        await client.disconnect()

    # 2. THE LOOP
    async def sending_loop():
        count = 1
        while keep_running:
            try:
                message_text = "?" * count
                
                # Send to the specific target
                await client.send_message(target_entity, message_text)
                print(f"Sent to {TARGET_USER}: {message_text}")
                
                count += 1
                if count > MAX_DOTS:
                    count = 1
                
                await asyncio.sleep(SLEEP_TIME)

            except errors.FloodWaitError as e:
                print(f"FloodWait: Waiting {e.seconds}s")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print(f"Loop Error: {e}")
                break

    # Run tasks
    await asyncio.gather(
        sending_loop(),
        client.run_until_disconnected()
    )

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\nScript stopped manually.")