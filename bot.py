import os
from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "I am alive!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

# تشغيل خادم الويب في خلفية مستقلة لكي لا يعطل عمل البوت
threading.Thread(target=run_web).start()
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from google import genai

# تحميل المتغيرات السرية من ملف .env
load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

client = genai.Client(api_key=GEMINI_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك يا ياسين! أنا بوتك الذكي، جاهز للإجابة على كل أسئلتك 🤖✨")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("فقط اكتب أي سؤال وسأقوم بالرد عليك مباشرة!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    try:
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=user_message,
        )
        await update.message.reply_text(response.text)
        
    except Exception as e:
        print(f"Error details: {e}")
        await update.message.reply_text("خوادم جوجل تشهد ضغطاً مؤقتاً، أعد إرسال رسالتك بعد لحظات.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("البوت الذكي يعمل الآن...")
    app.run_polling()