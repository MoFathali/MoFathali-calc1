import os
import telebot
from telebot import types

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set")

OWNER_CHAT_ID = 1946938561

bot = telebot.TeleBot(TOKEN)

# [FIX 4] حماية get_me() عند بدء التشغيل
try:
    BOT_USERNAME = bot.get_me().username
except Exception:
    BOT_USERNAME = "unknownbot"

# [FIX 1] مسار ثابت وصحيح بغض النظر عن مكان تشغيل البوت
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def img(filename):
    return os.path.join(BASE_DIR, filename)


def main_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("• 📚 الملخصات")
    btn2 = types.KeyboardButton("• 🧠 الكويزات")
    btn3 = types.KeyboardButton("• البوتات الخاصة بنا 🤖")
    btn4 = types.KeyboardButton("• نصائح قبل الامتحان📆")
    btn5 = types.KeyboardButton("• 📝 أسئلة امتحانات سابقة")
    btn6 = types.KeyboardButton("• ℹ️ حول البوت")
    btn7 = types.KeyboardButton("• تحديث")
    markup.add(btn1, btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    markup.add(btn6)
    markup.add(btn7)
    return markup


# ===== /start =====

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🎓 أهلاً بك في بوت رياضة 1",
        reply_markup=main_markup(),
    )
    if OWNER_CHAT_ID:
        user = message.from_user
        first = user.first_name or ""
        last = user.last_name or ""
        full_name = (first + " " + last).strip()
        username = f"@{user.username}" if user.username else "لا يوجد يوزر"
        notify = (
            f"👤 مستخدم جديد ضغط /start\n\n"
            f"الاسم: {full_name}\n"
            f"اليوزر: {username}\n"
            f"الآيدي: {user.id}"
        )
        try:
            bot.send_message(OWNER_CHAT_ID, notify)
        except Exception:
            pass


@bot.message_handler(func=lambda message: message.text == "• تحديث")
def refresh(message):
    bot.send_message(
        message.chat.id,
        "🔄 تم تحديث البوت بنجاح!\n🎓 أهلاً بك في بوت رياضة 1",
        reply_markup=main_markup(),
    )


# ===== الملخصات =====

@bot.message_handler(func=lambda message: message.text == "• 📚 الملخصات")
def summaries(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("• 📘 الاشتقاق بالتعريف")
    btn2 = types.KeyboardButton("• 📗 قوانين الاشتقاق")
    btn3 = types.KeyboardButton("• 📙 المثلثية")
    btn4 = types.KeyboardButton("• 📕 المثلثية العكسية")
    btn5 = types.KeyboardButton("• 📐 الميل")
    btn6 = types.KeyboardButton("• 📏 المماس")
    btn7 = types.KeyboardButton("• 📈 التزايد والتناقص")
    btn8 = types.KeyboardButton("• 🔄 نقاط الانقلاب")
    btn9 = types.KeyboardButton("• 🧮 المصفوفات")
    btn10 = types.KeyboardButton("• 📊 المحددات")
    btn11 = types.KeyboardButton("• 🟢 كرامر والمعادلات الخطية")
    btn12 = types.KeyboardButton("• ➡️ المتجهات")
    btn13 = types.KeyboardButton("• 📝 التفاضل الضمني")
    btn14 = types.KeyboardButton("• 🔙 رجوع")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5, btn6)
    markup.add(btn7, btn8)
    markup.add(btn9, btn10)
    markup.add(btn11, btn12)
    markup.add(btn13)
    markup.add(btn14)
    bot.send_message(
        message.chat.id,
        "📚 اختر الملخص:",
        reply_markup=markup,
    )


# [FIX 2] دالة مساعدة لإرسال الصور بأمان
def send_photo_safe(chat_id, filename, caption, reply_markup=None):
    try:
        with open(img(filename), "rb") as photo:
            bot.send_photo(chat_id, photo, caption=caption, reply_markup=reply_markup)
    except FileNotFoundError:
        bot.send_message(chat_id, f"⚠️ الملف غير موجود: {filename}")
    except Exception as e:
        bot.send_message(chat_id, "⚠️ حدث خطأ أثناء إرسال الصورة، حاول مرة أخرى.")


@bot.message_handler(func=lambda message: message.text == "• 📘 الاشتقاق بالتعريف")
def d1(message):
    send_photo_safe(message.chat.id, "اشتقاق_بالتعريف.png", "📘 ملخص الاشتقاق بالتعريف")


@bot.message_handler(func=lambda message: message.text == "• 📗 قوانين الاشتقاق")
def d2(message):
    send_photo_safe(message.chat.id, "اشتقاق_البسيط.png", "📗 ملخص الاشتقاق البسيط")


@bot.message_handler(func=lambda message: message.text == "• 📙 المثلثية")
def d3(message):
    send_photo_safe(message.chat.id, "مثلثية.png", "📙 ملخص اشتقاق الدوال المثلثية")


@bot.message_handler(func=lambda message: message.text == "• 📕 المثلثية العكسية")
def d4(message):
    send_photo_safe(message.chat.id, "مثلثية_عكسية.png", "📕 ملخص اشتقاق الدوال المثلثية العكسية")


@bot.message_handler(func=lambda message: message.text == "• 📐 الميل")
def d5(message):
    send_photo_safe(message.chat.id, "ميل.png", "📐 ملخص قوانين الميل")


@bot.message_handler(func=lambda message: message.text == "• 📏 المماس")
def d6(message):
    send_photo_safe(message.chat.id, "مماس.png", "📏 ملخص قوانين المماس")


@bot.message_handler(func=lambda message: message.text == "• 📈 التزايد والتناقص")
def d7(message):
    send_photo_safe(message.chat.id, "تزايد_تناقص.png", "📈 ملخص الدوال التزايدية والتناقصية")


@bot.message_handler(func=lambda message: message.text == "• 🔄 نقاط الانقلاب")
def d8(message):
    send_photo_safe(message.chat.id, "نقاط_الانقلاب.png", "🔄 ملخص نقاط الانقلاب")


@bot.message_handler(func=lambda message: message.text == "• 🧮 المصفوفات")
def d9(message):
    send_photo_safe(message.chat.id, "مصفوفات.png", "🧮 ملخص المصفوفات")


@bot.message_handler(func=lambda message: message.text == "• 📊 المحددات")
def d10(message):
    send_photo_safe(message.chat.id, "محددات.png", "📊 ملخص المحددات")


@bot.message_handler(func=lambda message: message.text == "• 🟢 كرامر والمعادلات الخطية")
def d11(message):
    send_photo_safe(message.chat.id, "كرامر.png", "🟢 ملخص كرامر والمعادلات الخطية")


@bot.message_handler(func=lambda message: message.text == "• ➡️ المتجهات")
def d12(message):
    send_photo_safe(message.chat.id, "متجهات.png", "➡️ ملخص المتجهات")


@bot.message_handler(func=lambda message: message.text == "• 📝 التفاضل الضمني")
def d13(message):
    send_photo_safe(message.chat.id, "تفاضل_ضمني.png", "📝 ملخص التفاضل الضمني")


@bot.message_handler(func=lambda message: message.text == "• 🔙 رجوع")
def go_back(message):
    bot.send_message(
        message.chat.id,
        "🏠 القائمة الرئيسية:",
        reply_markup=main_markup(),
    )


# ===== الأقسام الأخرى =====

@bot.message_handler(func=lambda m: m.text == "• 🧠 الكويزات")
def quizzes(message):
    bot.send_message(
        message.chat.id,
        "🧠 الكويزات\n\nهذا القسم فارغ حالياً.",
        reply_markup=main_markup(),
    )


@bot.message_handler(func=lambda m: m.text == "• البوتات الخاصة بنا 🤖")
def our_bots(message):
    bot.send_message(
        message.chat.id,
        "🤖 البوتات الخاصة بنا:\n\n"
        "🖥️ بوت مادة تنظيم الحاسبات\n@coccttbot\n\n"
        "💡 بوت مادة الأنظمة الرقمية\n@digitalccttbot\n\n"
        "📐 بوت مادة الرياضة 1\n@Calc1CCTTbot\n\n"
        "⏳ انتظروا بقية المواد ...\n\n"
        "——————————————\n"
        "🏢 حسيبات تيك | Hisabat Tech",
        reply_markup=main_markup(),
    )


@bot.message_handler(func=lambda m: m.text == "• نصائح قبل الامتحان📆")
def exam_review(message):
    send_photo_safe(message.chat.id, "نصائح1.png", "📆 نصائح قبل امتحان الرياضة 1")
    send_photo_safe(message.chat.id, "نصائح2.png", "✨ نصائح ذهبية قبل الامتحان", reply_markup=main_markup())


@bot.message_handler(func=lambda m: m.text == "• 📝 أسئلة امتحانات سابقة")
def past_exams(message):
    bot.send_message(message.chat.id, "📝 أسئلة امتحانات سابقة — رياضة 1\n\nجاري إرسال الأسئلة...")
    sent = 0
    # [FIX 3] إرسال الصور بأمان مع عداد للنجاح والفشل
    for i in range(1, 16):
        filename = f"امتحان_{i:02d}.jpg"
        try:
            with open(img(filename), "rb") as photo:
                bot.send_photo(message.chat.id, photo)
                sent += 1
        except FileNotFoundError:
            pass
        except Exception:
            pass
    if sent > 0:
        bot.send_message(message.chat.id, f"✅ تم إرسال {sent} سؤال.", reply_markup=main_markup())
    else:
        bot.send_message(message.chat.id, "⚠️ لا تتوفر أسئلة حالياً.", reply_markup=main_markup())


@bot.message_handler(func=lambda m: m.text == "• ℹ️ حول البوت")
def about(message):
    bot.send_message(
        message.chat.id,
        "ℹ️ حول البوت\n\n"
        "تم تصميم هذا البوت من قبل الطالب @mo_fat7ali\n\n"
        "وإن شاء الله نكون افدتكم 🤍",
        reply_markup=main_markup(),
    )


# [FIX 5] الـ fallback فقط للرسائل النصية، يتجاهل الصور والستيكرات وغيرها
@bot.message_handler(content_types=["text"], func=lambda m: True)
def fallback(message):
    inline_markup = types.InlineKeyboardMarkup()
    inline_markup.add(
        types.InlineKeyboardButton(
            "🔄 اضغط هنا لتحديث البوت",
            url=f"https://t.me/{BOT_USERNAME}?start=refresh",
        )
    )
    bot.send_message(
        message.chat.id,
        "⚠️ إدخال خاطئ!\n\nاضغط الزر أدناه لتحديث البوت والحصول على القائمة الجديدة 👇",
        reply_markup=inline_markup,
    )


if __name__ == "__main__":
    print("البوت يعمل الآن...")
    bot.infinity_polling()
