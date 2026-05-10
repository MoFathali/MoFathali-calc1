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

quiz_questions = [

    {
        "question": "📘 إذا كانت f(x)=3x²+2x-5 فما قيمة f'(2) ؟",
        "options": ["10", "12", "14", "16"],
        "answer": "14"
    },

    {
        "question": "📗 أوجد مشتقة:\nf(x)=sin(x)+x²",
        "options": ["cos(x)+2x", "sin(x)+2x", "cos(x)+x²", "2sin(x)"],
        "answer": "cos(x)+2x"
    },

    {
        "question": "📙 احسب:\nsin²(30°)+cos²(30°)",
        "options": ["0", "1", "2", "1/2"],
        "answer": "1"
    }
    ,
{
    "question": "📕 مشتقة tan(x) تساوي؟",
    "options": ["sec²(x)", "cos(x)", "csc²(x)", "tan²(x)"],
    "answer": "sec²(x)"
},

{
    "question": "📐 أوجد ميل المستقيم المار بالنقطتين:\n(2,3) و (6,11)",
    "options": ["1", "2", "3", "4"],
    "answer": "2"
},

{
    "question": "➡️ إذا كان المتجه A=(6,8)\nفما مقداره؟",
    "options": ["8", "10", "12", "14"],
    "answer": "10"
}
]

user_score = {}
user_question = {}


@bot.message_handler(func=lambda m: m.text == "🧠 الكويزات")
def quizzes(message):

    user_id = message.from_user.id

    user_score[user_id] = 0
    user_question[user_id] = 0

    bot.send_message(
        message.chat.id,
        "🧠 قبل ما تبدأ الكويز:\n\n"
        "📄 هات ورقة وقلم\n"
        "🧠 ركّز كويس\n"
        "⏳ وحاول تجاوب بدون غش 😄"
    )

    send_question(message.chat.id, user_id)


def send_question(chat_id, user_id):

    q_index = user_question[user_id]

    if q_index >= len(quiz_questions):

        score = user_score[user_id]

        if score == len(quiz_questions):
            rating = "🔥 وحش رياضيات"

        elif score >= 2:
            rating = "👏 ممتاز جدًا"

        elif score >= 1:
            rating = "👍 جيد لكن راجع أكثر"

        else:
            rating = "📚 يحتاج مراجعة قبل الامتحان"

        bot.send_message(
            chat_id,
            f"🏁 انتهى الكويز!\n\n📊 نتيجتك: {score}/{len(quiz_questions)}\n\n{rating}",
            reply_markup=main_markup()
        )

        return

    q = quiz_questions[q_index]

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for option in q["options"]:
        markup.add(types.KeyboardButton(option))

    markup.add(types.KeyboardButton("🔙 رجوع"))

    bot.send_message(
        chat_id,
        q["question"],
        reply_markup=markup
    )


@bot.message_handler(func=lambda m: True)
def check_answer(message):

    user_id = message.from_user.id

    if user_id not in user_question:
        return

    q_index = user_question[user_id]
    q = quiz_questions[q_index]

    if message.text == q["answer"]:

        user_score[user_id] += 1

        bot.send_message(
            message.chat.id,
            "✅ إجابة صحيحة"
        )

    else:

        bot.send_message(
            message.chat.id,
            f"❌ إجابة خاطئة\n\n✅ الإجابة الصحيحة: {q['answer']}"
        )

    user_question[user_id] += 1

    send_question(message.chat.id, user_id)


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
@bot.message_handler(commands=["users"])
def users_list(message):

    if message.from_user.id != OWNER_ID:
        bot.send_message(message.chat.id, "❌ غير مسموح")
        return
    print(users)
    text = "👥 المستخدمين:\n\n"

    for user_id, name in users.items():
        text += f"• {name} | {user_id}\n"

    text += f"\n📊 العدد الكلي: {len(users)}"

    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["broadcast"])
def broadcast(message):

    if message.from_user.id != OWNER_ID:
        bot.send_message(message.chat.id, "❌ غير مسموح")
        return

    msg = message.text.replace("/broadcast ","")

    sent = 0

    for user_id in users:

        try:
            bot.send_message(user_id, f"📢 رسالة من الإدارة:\n\n{msg}")
            sent += 1

        except:
            pass

    bot.send_message(
        message.chat.id,
        f"✅ تم إرسال الرسالة إلى {sent} مستخدم"
    )

@bot.message_handler(func=lambda m: m.text and not m.text.startswith("/"))
def fallback(message):
    bot.send_message(
        message.chat.id,
        "اختر من القائمة 👇",
        reply_markup=main_markup(),
    )


if __name__ == "__main__":
    print("البوت يعمل الآن...")
    bot.infinity_polling()
