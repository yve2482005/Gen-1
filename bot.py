from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
from generate_image import generate_image

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Send me a text prompt to generate an image.")

async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text
    await update.message.reply_text("Generating your image, please wait...")

    # Generate image
    output_path = generate_image(prompt)

    # Send image
    with open(output_path, "rb") as img:
        await update.message.reply_photo(img)

app = ApplicationBuilder().token("7681255229:AAF9xN3UUQAbjuKPAn0qQm2nUVjxooP9F2M").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters=None, callback=generate))

if __name__ == "__main__":
    app.run_polling()