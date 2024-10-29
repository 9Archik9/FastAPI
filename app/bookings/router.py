from fastapi import APIRouter

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookings():
    return await BookingDAO.find_by_id(1)
