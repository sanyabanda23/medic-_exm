from httpx import AsyncClient
from app.api.dao import UserDAO, BookingDAO
from app.api.schemas import TelegramIDModel, UserModel
from app.tg_bot.kbs import back_kb, main_kb, generate_kb_profile
from app.tg_bot.methods import call_answer, bot_send_message, get_greeting_text, get_about_text, get_booking_text, format_appointment