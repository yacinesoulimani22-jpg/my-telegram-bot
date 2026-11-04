from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 1. أمر الترحيب (/start)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك يا ياسين! أنا بوتك الذكي، كيف يمكنني مساعدتك اليوم؟")

# 2. أمر المساعدة الجديد (/help)
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("الأوامر المتاحة:\n/start - بدء البوت\n/help - عرض المساعدة")

# 3. الرد الذكي على الرسائل والكلمات
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower() # تحويل النص إلى حروف صغيرة لسهولة القراءة
    
    if "سلام" in text or "مرحبا" in text or "hi" in text:
        await update.message.reply_text("وعليكم السلام ورحمة الله! أهلاً بك.")
    elif "كيف حالك" in text:
        await update.message.reply_text("أنا بوت يعمل بكامل طاقتي وجاهز لمساعدتك! 🚀")
    else:
        await update.message.reply_text(f"لقد استلمت رسالتك: {text}")

if __name__ == '__main__':
    TOKEN = "9175532563:AAFx39wsy-tM3M2E4QT1piek5hW4JyJUAT1"
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    # ربط الأوامر والدوال بالبوت
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("البوت يعمل الآن...")
    app.run_polling()