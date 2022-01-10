"""Favour composition over inheritance"""
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Protocol


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()


class PaymentType(Protocol):
    def calculate_price(self) -> int:
        ...


@dataclass
class DailyPayment:
    days: int
    price_per_day: int

    def calculate_price(self) -> int:
        if self.price_per_day:
            return self.price_per_day * self.days

@dataclass
class KmPayment:
    mks: int
    price_per_km: int

    def calculate_price(self) -> int:
        if self.price_per_km:
            return self.price_per_km * self.kms

@dataclass
class MonthlyPayment:
    months: int
    price_per_month: int

    def calculate_price(self) -> int:
        return self.price_per_month * self.months


@dataclass
class Rentable:
    brand: str
    model: str
    reserved: bool
    license_plate: str
    payment_type: PaymentType = field(default_factory=list)

    def add_payment_type(self, payment_type: PaymentType) -> int:
        self.payment_type.append(payment_type)

    def calculate_price(self) -> int:
        return sum([price for price in self.payment_type.calculate_price()])

    def reserve(self):
        self.reserved = True


@dataclass
class Trailer(Rentable):
    capacity_m3: int = 1


@dataclass
class Vehicle(Rentable):
    number_of_seats: int = 2
    storage_capacity_litres: int = 100
    color: str = "black"
    fuel_type: FuelType = FuelType.DIESEL


@dataclass
class Truck(Vehicle):
    cab_style: TruckCabStyle = TruckCabStyle.REGULAR


def main():
    pass


if __name__ == "__main__":
    main()
