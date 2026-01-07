"""
Telegram Channel User Removal Bot
Removes all users from a Telegram channel one by one
"""

import asyncio
from telethon import TelegramClient
from telethon.errors import ChatAdminRequiredError, UserAlreadyParticipantError
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TelegramChannelCleaner:
    def __init__(self, api_id: int, api_hash: str, phone: str):
        """
        Initialize the Telegram bot
        
        Args:
            api_id: Your Telegram API ID (get from my.telegram.org)
            api_hash: Your Telegram API Hash (get from my.telegram.org)
            phone: Your phone number with country code (e.g., +1234567890)
        """
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone = phone
        self.client = TelegramClient('session_name', api_id, api_hash)
    
    async def start(self):
        """Start the bot and authenticate"""
        await self.client.connect()
        if not await self.client.is_user_authorized():
            await self.client.send_code_request(self.phone)
            print("\n📱 A code has been sent to your Telegram account or phone!")
            print("   Check your Telegram app for the code.\n")
            
            while True:
                try:
                    code = input("➡️  Enter the 5-digit code: ").strip()
                    if len(code) != 5 or not code.isdigit():
                        print("❌ Code must be 5 digits. Try again.")
                        continue
                    
                    try:
                        await self.client.sign_in(self.phone, code)
                        break
                    except Exception as e:
                        # Check if it's asking for 2FA password
                        if "password" in str(e).lower():
                            print("\n🔐 Two-step verification is enabled!")
                            print("   You need to enter your 2FA password.\n")
                            password = input("🔑 Enter your 2FA password: ").strip()
                            await self.client.sign_in(password=password)
                            break
                        else:
                            print(f"❌ Invalid code. Error: {str(e)}")
                            print("   Try again or check your Telegram app for the correct code.")
                except Exception as e:
                    print(f"❌ Authentication error: {str(e)}")
                    print("   Please check your password and try again.")
        
        logger.info("✅ Bot connected to Telegram")
    
    async def remove_all_users(self, channel_identifier):
        """
        Remove all users from a channel
        
        Args:
            channel_identifier: Channel username without @ (str) or channel ID (int)
        """
        try:
            # Get the channel
            channel = await self.client.get_entity(channel_identifier)
            if isinstance(channel, list):
                channel = channel[0]
            channel_name = getattr(channel, 'title', getattr(channel, 'first_name', str(channel_identifier)))
            logger.info(f"🎯 Found channel: {channel_name}")
            
            # Get all participants
            participants = await self.client.get_participants(channel)
            total_users = len(participants)
            logger.info(f"👥 Total users to remove: {total_users}")
            
            removed_count = 0
            failed_count = 0
            
            print("\n" + "="*50)
            print("🚫 STARTING MASS USER REMOVAL")
            print("="*50 + "\n")
            
            # Remove each user
            for i, participant in enumerate(participants, 1):
                try:
                    # Skip the owner
                    if hasattr(participant, 'is_self') and participant.is_self:
                        logger.info(f"⏭️  Skipping owner: {participant.first_name}")
                        continue
                    
                    # Remove the user
                    await self.client.edit_permissions(channel, participant, view_messages=False)
                    removed_count += 1
                    
                    username = participant.username or participant.first_name or "Unknown"
                    logger.info(f"✅ [{i}/{total_users}] Removed: {username}")
                    print(f"✅ [{i}/{total_users}] {username}")
                    
                    # Small delay to avoid rate limiting
                    await asyncio.sleep(0.5)
                
                except ChatAdminRequiredError:
                    logger.error(f"❌ Not admin in this channel - cannot remove users")
                    break
                except Exception as e:
                    failed_count += 1
                    username = participant.username or participant.first_name or "Unknown"
                    logger.warning(f"⚠️  Failed to remove {username}: {str(e)}")
            
            print("\n" + "="*50)
            print(f"✅ Removed: {removed_count}")
            print(f"❌ Failed: {failed_count}")
            print(f"⏭️  Skipped: {total_users - removed_count - failed_count}")
            print("="*50)
            
            return removed_count
        
        except Exception as e:
            logger.error(f"❌ Error: {e}")
            return 0
    
    async def remove_user_by_id(self, channel_identifier, user_id: int):
        """Remove a specific user by ID"""
        try:
            channel = await self.client.get_entity(channel_identifier)
            if isinstance(channel, list):
                channel = channel[0]
            await self.client.edit_permissions(channel, user_id, view_messages=False)
            logger.info(f"✅ User {user_id} removed from channel")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to remove user: {e}")
    async def get_channel_members(self, channel_identifier):
        """Get list of all channel members"""
        try:
            channel = await self.client.get_entity(channel_identifier)
            if isinstance(channel, list):
                channel = channel[0]
            participants = await self.client.get_participants(channel)
            
            channel_title = getattr(channel, 'title', str(channel_identifier))
            logger.info(f"\n👥 Members in {channel_title}:")
            print("-" * 60)
            for user in participants:
                username = user.username or user.first_name or "Unknown"
                print(f"  ID: {user.id:15} | Username: {username}")
            print("-" * 60)
            print(f"Total members: {len(participants)}")
            
            return participants
        except Exception as e:
            logger.error(f"❌ Error fetching members: {e}")
            return []
        
    async def close(self):
        """Close the bot connection"""
        if self.client.is_connected():
            self.client.disconnect()
        logger.info("👋 Bot disconnected")


async def main():
    """Main function"""
    print("\n" + "="*50)
    print("🤖 TELEGRAM CHANNEL USER REMOVER")
    print("="*50 + "\n")
    
    # Get credentials
    print("📝 Enter your Telegram credentials:")
    api_id = int(input("API ID (from my.telegram.org): "))
    api_hash = input("API Hash (from my.telegram.org): ")
    phone = input("Phone number (+1234567890): ")
    
    print("\n❓ How do you want to identify the channel?")
    print("1. By username (e.g., mychannel)")
    print("2. By channel ID (e.g., -1001234567890)")
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        channel_identifier = input("Channel username (without @): ")
    else:
        channel_identifier = int(input("Channel ID (negative number): "))
    
    # Create bot
    bot = TelegramChannelCleaner(api_id, api_hash, phone)
    
    try:
        # Connect
        await bot.start()
        
        # Show menu
        while True:
            print("\n" + "-"*50)
            print("1. Remove all users")
            print("2. View channel members")
            print("3. Remove specific user")
            print("4. Exit")
            print("-"*50)
            
            choice = input("Select option (1-4): ").strip()
            
            if choice == "1":
                await bot.remove_all_users(channel_identifier)
            elif choice == "2":
                await bot.get_channel_members(channel_identifier)
            elif choice == "3":
                user_id = int(input("Enter user ID: "))
                await bot.remove_user_by_id(channel_identifier, user_id)
            elif choice == "4":
                break
            else:
                print("❌ Invalid option")
    
    finally:
        await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
