
import os
import telebot
from telebot import types

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set")

bot = telebot.TeleBot(TOKEN)

OWNER_ID = 1946938561

users = {}
def main_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📚 الملخصات")
    btn2 = types.KeyboardButton("🧠 الكويزات")
    btn3 = types.KeyboardButton("البوتات الخاصة بنا 🤖")
    btn4 = types.KeyboardButton("نصائح قبل الامتحان📆")
    btn5 = types.KeyboardButton("📝 أسئلة امتحانات سابقة")
    btn6 = types.KeyboardButton("ℹ️ حول البوت")
    markup.add(btn1, btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    markup.add(btn6)
    return markup


@bot.message_handler(commands=["start"])
def start(message):

    user_id = message.from_user.id
    first_name = message.from_user.first_name

    users[user_id] = first_name

    bot.send_message(
        message.chat.id,
        "🎓 أهلاً بك في بوت رياضة 1",
        reply_markup=main_markup(),
    )


# ===== الملخصات =====
@bot.message_handler(commands=["users"])
def users_list(message):

    if message.from_user.id != OWNER_ID:
        bot.send_message(message.chat.id, "❌ غير مسموح")
        return

    text = "👥 المستخدمين:\n\n"

    for user_id, name in users.items():
        text += f"• {name} | {user_id}\n"

    text += f"\n📊 العدد الكلي: {len(users)}"

    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text == "📚 الملخصات")
def summaries(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📘 الاشتقاق بالتعريف")
    btn2 = types.KeyboardButton("📗 قوانين الاشتقاق")
    btn3 = types.KeyboardButton("📙 المثلثية")
    btn4 = types.KeyboardButton("📕 المثلثية العكسية")
    btn5 = types.KeyboardButton("📐 الميل")
    btn6 = types.KeyboardButton("📏 المماس")
    btn7 = types.KeyboardButton("📈 التزايد والتناقص")
    btn8 = types.KeyboardButton("🔄 نقاط الانقلاب")
    btn9 = types.KeyboardButton("🧮 المصفوفات")
    btn10 = types.KeyboardButton("📊 المحددات")
    btn11 = types.KeyboardButton("🟢 كرامر والمعادلات الخطية")
    btn12 = types.KeyboardButton("➡️ المتجهات")
    btn13 = types.KeyboardButton("📝 التفاضل الضمني")
    btn14 = types.KeyboardButton("🔙 رجوع")
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


@bot.message_handler(func=lambda message: message.text == "📘 الاشتقاق بالتعريف")
def d1(message):
    img_path = os.path.join(os.path.dirname(__file__), "اشتقاق_بالتعريف.png")
    with open(img_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="📘 ملخص الاشتقاق بالتعريف")


@bot.message_handler(func=lambda message: message.text == "📗 قوانين الاشتقاق")
def d2(message):
    img_path = os.path.join(os.path.dirname(__file__), "اشتقاق_البسيط.png")
    with open(img_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="📗 ملخص الاشتقاق البسيط")


@bot.message_handler(func=lambda message: message.text == "📙 المثلثية")
def d3(message):
    img_path = os.path.join(os.path.dirname(__file__), "مثلثية.png")
    with open(img_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="📙 ملخص اشتقاق الدوال المثلثية")


@bot.message_handler(func=lambda message: message.text == "📕 المثلثية العكسية")
def d4(message):
    img_path = os.path.join(os.path.dirname(__file__), "مثلثية_عكسية.png")
    with open(img_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="📕 ملخص اشتقاق الدوال المثلثية العكسية")


@bot.message_handler(func=lambda message: message.text == "📐 الميل")
def d5(message):
    img_path = os.path.join(os.path.dirname(__file__), "ميل.png")
    with open(img_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="📐 ملخص قوانين الميل")


@bot.message_handler(func=lambda message: message.text == "📏 المماس")
def d6(message):
    img_path = os.path.join(os.path.dirname(__file__), "مماس.png")
    with open(img_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="📏 ملخص قوانين المماس")


@bot.message_handler(func=lambda message: message.text == "📈 التزايد والتناقص")
def d7(message):
    img_path = os.path.join(os.path.dirname(__file__), "تزايد_تناقص.png")
    with open(img_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="📈 ملخص الدوال التزايدية والتناقصية")


@bot.message_handler(func=lambda message: message.text == "🔄 نقاط الانقلاب")
def d8(message):
    img_path = os.path.join(os.path.dirname(__file__), "نقاط_الانقلاب.png")
    with open(img_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="🔄 ملخص نقاط الانقلاب")


@bot.message_handler(func=lambda message: message.text == "🧮 المصفوفات")
def d9(message):
    img_path = os.path.join(os.path.dirname(__file__), "مصفوفات.png")
    with open(img_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="🧮 ملخص المصفوفات")


@bot.message_handler(func=lambda message: message.text == "📊 المحددات")
def d10(message):
    img_path = os.path.join(os.path.dirname(__file__), "محددات.png")
    with open(img_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="📊 ملخص المحددات")


@bot.message_handler(func=lambda message: message.text == "🟢 كرامر والمعادلات الخطية")
def d11(message):
    img_path = os.path.join(os.path.dirname(__file__), "كرامر.png")
    with open(img_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="🟢 ملخص كرامر والمعادلات الخطية")


@bot.message_handler(func=lambda message: message.text == "➡️ المتجهات")
def d12(message):
    img_path = os.path.join(os.path.dirname(__file__), "متجهات.png")
    with open(img_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="➡️ ملخص المتجهات")


@bot.message_handler(func=lambda message: message.text == "📝 التفاضل الضمني")
def d13(message):
    img_path = os.path.join(os.path.dirname(__file__), "تفاضل_ضمني.png")
    with open(img_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="📝 ملخص التفاضل الضمني")


@bot.message_handler(func=lambda message: message.text == "🔙 رجوع")
def go_back(message):
    bot.send_message(
        message.chat.id,
        "🏠 القائمة الرئيسية:",
        reply_markup=main_markup(),
    )


# ===== الأقسام الأخرى =====

@bot.message_handler(func=lambda m: m.text == "🧠 الكويزات")
def quizzes(message):
    bot.send_message(
        message.chat.id,
        "🧠 الكويزات\n\nهذا القسم فارغ حالياً.",
        reply_markup=main_markup(),
    )


@bot.message_handler(func=lambda m: m.text == "البوتات الخاصة بنا 🤖")
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


@bot.message_handler(func=lambda m: m.text == "نصائح قبل الامتحان📆")
def exam_review(message):
    base = os.path.dirname(__file__)
    with open(os.path.join(base, "نصائح1.png"), "rb") as p1:
        bot.send_photo(message.chat.id, p1, caption="📆 نصائح قبل امتحان الرياضة 1")
    with open(os.path.join(base, "نصائح2.png"), "rb") as p2:
        bot.send_photo(message.chat.id, p2, caption="✨ نصائح ذهبية قبل الامتحان", reply_markup=main_markup())


@bot.message_handler(func=lambda m: m.text == "📝 أسئلة امتحانات سابقة")
def past_exams(message):
    base = os.path.dirname(__file__)
    bot.send_message(message.chat.id, "📝 أسئلة امتحانات سابقة — رياضة 1\n\nجاري إرسال الأسئلة...")
    for i in range(1, 16):
        filename = f"امتحان_{i:02d}.jpg"
        with open(os.path.join(base, filename), "rb") as photo:
            bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, "✅ تم إرسال جميع الأسئلة.", reply_markup=main_markup())


@bot.message_handler(func=lambda m: m.text == "ℹ️ حول البوت")
def about(message):
    bot.send_message(
        message.chat.id,
        "ℹ️ حول البوت\n\n"
        "تم تصميم هذا البوت من قبل الطالب @mo_fat7ali\n\n"
        "وإن شاء الله نكون افدتكم 🤍",
        reply_markup=main_markup(),
    )


@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.send_message(
        message.chat.id,
        "اختر من القائمة 👇",
        reply_markup=main_markup(),
    )


if __name__ == "__main__":
    print("البوت يعمل الآن...")
    bot.infinity_polling()
