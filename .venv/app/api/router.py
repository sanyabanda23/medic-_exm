from datetime import date, datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dao import SpecializationDAO, DoctorDAO, BookingDAO, UserDAO
from app.api.schemas import SpecIDModel, BookingRequest
from app.dao.session_maker_fast_api import db
from app.tg_bot.scheduler_task import schedule_appointment_notification
import pytz