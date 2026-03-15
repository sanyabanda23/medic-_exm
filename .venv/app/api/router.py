from datetime import date, datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dao import SpecializationDAO, DoctorDAO, BookingDAO, UserDAO
from app.api.schemas import SpecIDModel, BookingRequest
from app.dao.session_maker_fast_api import db
from app.tg_bot.scheduler_task import schedule_appointment_notification
import pytz

MOSCOW_TZ = pytz.timezone("Europe/Moscow")


router = APIRouter() # инструмент FastAPI для модульной организации маршрутов (эндпоинтов) API. По сути, это «мини‑приложение»

@router.get("/specialists")
async def get_specialists(session: AsyncSession = Depends(db.get_db)):
    return await SpecializationDAO.find_all(session=session)

@router.get("/doctors/{spec_id}")
async def get_doctors_spec(spec_id: int, session: AsyncSession = Depends(db.get_db)):
    return await DoctorDAO.find_all(session=session,
                                    filters=SpecIDModel(specialization_id=spec_id))

@router.get("/doctor/{doctor_id}")
async def get_doctor_by_id(doctor_id: int, session: AsyncSession = Depends(db.get_db)):
    return await DoctorDAO.find_one_or_none_by_id(session=session, data_id=doctor_id)

@router.get("/booking/available-slots/{doctor_id}")
async def get_available_slots(
        doctor_id: int,
        start_date: date,
        session: AsyncSession = Depends(db.get_db)
):
    return await BookingDAO.get_available_slots(session=session, doctor_id=doctor_id, start_date=start_date)