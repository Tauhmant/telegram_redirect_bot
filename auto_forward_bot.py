from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import os

# Replace with your bot's token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Replace with your group/chat IDs
SOURCE_CHAT_IDS = [-1001683017303, -1001039041151, -1002176178671, -1001751504041 ]  # Add source group/channel IDs
TARGET_GROUP_ID = 2397940295  # Replace with the target group ID

# -1001683017303 - Японский художник Avogado6
# -1001039041151 - Daigaku - Японский язык
# -1002176178671 - Ну да, японский
# -1001751504041 - Nihongo - Японский язык

# Message forward handler
async def forward_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if the message is from the source chats
    if update.effective_chat.id in SOURCE_CHAT_IDS:
        try:
            # Forward the message to the target group
            await context.bot.forward_message(
                chat_id=TARGET_GROUP_ID,
                from_chat_id=update.effective_chat.id,
                message_id=update.message.message_id
            )
            print(f"Message forwarded from {update.effective_chat.id} to {TARGET_GROUP_ID}")
        except Exception as e:
            print(f"Error: {e}")

# Main function to run the bot
def main():
    # Initialize the bot application
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Add a handler to forward messages from specific source chats
    message_handler = MessageHandler(filters.Chat(SOURCE_CHAT_IDS), forward_messages)
    app.add_handler(message_handler)
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
