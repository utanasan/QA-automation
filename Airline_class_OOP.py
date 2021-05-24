"""
Создать класс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели.
Функции- члены реализуют запись и считывание полей (проверка корректности).
Создать список объектов. Вывести:
a) список рейсов для заданного пункта назначения;
b) список рейсов для заданного дня недели;
"""


class Airline:
    def __init__(self, destination,flight_number,airplane_type,departure_time,week_days):
        self.destination=destination
        self.flight_number=flight_number
        self.airplane_type=airplane_type
        self.departure_time=departure_time
        self.week_days=week_days

    def get_destination(self):
        return self.destination

    def set_destination(self, destination):
        self.destination = destination

    def get_flight_number(self):
        return self.flight_number
    def set_flight_number(self,flight_number):
        self.flight_number = flight_number

    def get_airplane_type(self):
        return self.airplane_type
    def set_airplane_type(self,airplane_type):
        self.airplane_type=airplane_type

    def get_airplane_type(self):
        return self.airplane_type
    def set_airplane_type(self,airplane_type):
        self.airplane_type=airplane_type

    def get_departure_time(self):
        return self.departure_time
    def set_departure_time(self,departure_time):
        self.departure_time=departure_time

    def get_week_days(self):
        return self.week_days
    def set_week_days(self,week_days):
        self.week_days=week_days

    def __str__(self):
        return f"{self.destination} {self.flight_number} {self.airplane_type} {self.departure_time} {self.week_days}"



list_airlines=[
    Airline('London', '1111', 'XXX 000', '11:11', 'Mon'),
    Airline('Minsk', '1112', 'XXX 111', '12:12', 'Tue'),
    Airline('Vilnius', '1113', 'XXX 222', '13:13', 'Wed'),
    Airline('Riga', '1114', 'XXX 333', '14:14', 'Fr')
    ]

dest=input("Enter full city of destination: ")
for Airline in list_airlines:
        if Airline.get_destination() == dest:
            print(Airline)

day = input("Enter day of departure as three first letters: ")
for Airline in list_airlines:
        if Airline.get_week_days() == day:
            print(Airline)










