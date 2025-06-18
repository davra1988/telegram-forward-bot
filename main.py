
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = '7895909973:AAHcXdxErE8THjVakM0UBEjuysbj6_fO9sI'
SOURCE_CHANNEL_USERNAME = 'Radar_Alerts'
DESTINATION_CHAT_ID = '@israelnow26'

async def forward_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post and update.channel_post.chat.username == SOURCE_CHANNEL_USERNAME:
        await context.bot.forward_message(
            chat_id=DESTINATION_CHAT_ID,
            from_chat_id=update.channel_post.chat.id,
            message_id=update.channel_post.message_id
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward_post))

print("✅ Bot is running and forwarding from Radar_Alerts to israelnow26...")
app.run_polling()
