from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel, Field


app = FastAPI()


class HotelSearchArgs:
    def __iter__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            has_spa: Optional[bool] = None,
            stars: Optional[int] = Query(None, ge=1, le=5),

    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


class SHotel(BaseModel):
    address: str
    name: str
    stars: int = Field(None, le=5, ge=1)


@app.get("/hotels")
def get_hotels(
        search_args: HotelSearchArgs = Depends()
) -> list[SHotel]:

    hotels = [
        {
            "address": "ул.Пушкина, д.Колотушкина",
            "name": "Mega Hotel",
            "stars": 5,
        }
    ]

    return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def book_hotel(booking: SBooking):
    pass
