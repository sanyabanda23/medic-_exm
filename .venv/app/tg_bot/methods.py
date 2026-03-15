from datetime import datetime
from httpx import AsyncClient
from app.config import settings

async def bot_send_message(client: AsyncClient, chat_id: int, text: str, kb: list | None = None):
    send_data = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    if kb:
        send_data["reply_markup"] = {"inline_keyboard": kb}
    await client.post(f"{settings.get_tg_api_url()}/sendMessage", json=send_data)

async def call_answer(client: AsyncClient, callback_query_id: int, text: str):
    await client.post(f"{settings.get_tg_api_url()}/answerCallbackQuery", json={
        "callback_query_id": callback_query_id,
        "text": text
    })

def get_greeting_text(first_name: str):
    return f"""
🏥 <b>Добро пожаловать в бот клиники "ЗдоровьеПлюс"!</b>

Здравствуйте, <b>{first_name}</b>! 👋

Мы рады приветствовать вас в нашей цифровой системе записи к врачам. Здесь вы сможете:

✅ Записаться на прием к любому специалисту
🗓 Управлять своими записями
ℹ️ Получать информацию о наших услугах

<i>Ваше здоровье - наш главный приоритет!</i>

Чтобы начать, выберите нужный пункт меню ниже 👇
"""


def get_about_text():
    return """
🏥 <b>О клинике "ЗдоровьеПлюс"</b>

Мы - современная многопрофильная клиника, предоставляющая высококачественные медицинские услуги с 2005 года.

<b>Наши преимущества:</b>

✅ Команда опытных врачей высшей категории
🏆 Новейшее диагностическое оборудование
🕒 Удобный график работы: ежедневно с 8:00 до 20:00
🏠 Комфортное расположение в центре города
💉 Широкий спектр медицинских услуг

<b>Наши отделения:</b>
• Терапия
• Кардиология
• Неврология
• Гинекология
• Урология
• Педиатрия
• Стоматология

<i>Мы заботимся о вашем здоровье и комфорте на каждом этапе лечения!</i>

Чтобы записаться на прием или узнать больше о наших услугах, воспользуйтесь меню бота.
"""


def get_booking_text(appointment_count):
    if appointment_count > 0:
        message_text = f"""
📅 <b>Ваши записи к врачам</b>

У вас запланировано <b>{appointment_count}</b> {pluralize_appointments(appointment_count)}.

Чтобы просмотреть детали ваших записей, нажмите кнопку "Просмотреть записи" ниже.
"""
    else:
        message_text = """
📅 <b>Ваши записи к врачам</b>

В настоящее время у вас нет запланированных приемов.

Чтобы записаться к врачу, воспользуйтесь кнопкой "Записаться на прием" в главном меню.
"""
    return message_text


def pluralize_appointments(count: int) -> str:
    if count == 1:
        return "прием"
    elif 2 <= count <= 4:
        return "приема"
    else:
        return "приемов"


def format_appointment(appointment, start_text="🗓 <b>Запись на прием</b>"):
    appointment_date = datetime.strptime(appointment['day_booking'], '%Y-%m-%d').strftime('%d.%m.%Y')
    return f"""
{start_text}

📅 Дата: {appointment_date}
🕒 Время: {appointment['time_booking']}
👨‍⚕️ Врач: {appointment['doctor_full_name']}
🏥 Специализация: {appointment['special']}

ℹ️ Номер записи: {appointment['id']}

Пожалуйста, приходите за 10-15 минут до назначенного времени.
"""