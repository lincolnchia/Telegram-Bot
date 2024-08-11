from typing import Final
import asyncio
import logging
from telegram import Update 
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7409833167:AAFWGjpHO6Xirhd4bstakrlW0y09SOD07gw'
BOT_USERNAME: Final = '@Linc_Attendence_Bot'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi please type on of the following commands to start using the bot \n /start \n /applyingLeave "
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I don't understand that command")
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    echo_handler = CommandHandler('echo', echo)
    unknown_handler = MessageHandler(filters.COMMAND,unknown)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(unknown_handler)
    
    application.run_polling()