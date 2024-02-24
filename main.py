from enum import Enum


class Nationality(Enum):
    UAE = "UAE"
    US = "US"
    KSA = "KSA"


class Passenger:
    def __init__(self, name, eid, passport_number, age, gender, nationality):
        self._name = name
        self._eid = eid
        self._passport_number = passport_number
        self._age = age
        self._gender = gender
        self._nationality = nationality

    # Setters
    def set_name(self, name):
        self._name = name

    def set_eid(self, eid):
        self._eid = eid

    def set_passport_number(self, passport_number):
        self._passport_number = passport_number

    def set_age(self, age):
        self._age = age

    def set_gender(self, gender):
        self._gender = gender

    def set_nationality(self, nationality):
        self._nationality = nationality

    # Getters
    def get_name(self):
        return self._name

    def get_eid(self):
        return self._eid

    def get_passport_number(self):
        return self._passport_number

    def get_age(self):
        return self._age

    def get_gender(self):
        return self._gender

    def get_nationality(self):
        return self._nationality.value

    def display_details(self):
        print("Name:", self._name)
        print("EID:", self._eid)
        print("Passport Number:", self._passport_number)
        print("Age:", self._age)
        print("Gender:", self._gender)
        print("Nationality:", self._nationality.value)


class Student(Passenger):
    def __init__(self, name, eid, passport_number, age, gender, nationality, university, student_id):
        super().__init__(name, eid, passport_number, age, gender, nationality)
        self._university = university
        self._student_id = student_id

    # Setters
    def set_university(self, university):
        self._university = university

    def set_student_id(self, student_id):
        self._student_id = student_id

    # Getters
    def get_university(self):
        return self._university

    def get_student_id(self):
        return self._student_id

    def display_info(self):
        super().display_details()
        print("University:", self._university)
        print("Student ID:", self._student_id)


# Example usage:
student = Student("Majed Altamimi", 2893788, 98989, 45, "Male", Nationality.UAE, "Zayed University", 2022003040)
student.display_info()

from datetime import datetime


class Ticket:
    def __init__(self, passenger_name, flight_from, flight_to, flight_number, seat_number, departure_date,
                 departure_time, gate):
        self._passenger_name = passenger_name
        self._flight_from = flight_from
        self._flight_to = flight_to
        self._flight_number = flight_number
        self._seat_number = seat_number
        self._departure_date = departure_date
        self._departure_time = departure_time
        self._gate = gate

    # Setters
    def set_passenger_name(self, passenger_name):
        self._passenger_name = passenger_name

    def set_flight_from(self, flight_from):
        self._flight_from = flight_from

    def set_flight_to(self, flight_to):
        self._flight_to = flight_to

    def set_flight_number(self, flight_number):
        self._flight_number = flight_number

    def set_seat_number(self, seat_number):
        self._seat_number = seat_number

    def set_departure_date(self, departure_date):
        self._departure_date = departure_date

    def set_departure_time(self, departure_time):
        self._departure_time = departure_time

    def set_gate(self, gate):
        self._gate = gate

    # Getters
    def get_passenger_name(self):
        return self._passenger_name

    def get_flight_from(self):
        return self._flight_from

    def get_flight_to(self):
        return self._flight_to

    def get_flight_number(self):
        return self._flight_number

    def get_seat_number(self):
        return self._seat_number

    def get_departure_date(self):
        return self._departure_date

    def get_departure_time(self):
        return self._departure_time

    def get_gate(self):
        return self._gate

    # Other required function headers
    def display_info(self):
        print("Passenger Name:", self._passenger_name)
        print("Flight From:", self._flight_from)
        print("Flight To:", self._flight_to)
        print("Flight Number:", self._flight_number)
        print("Seat Number:", self._seat_number)
        print("Departure Date:", self._departure_date.strftime("%Y-%m-%d"))
        print("Departure Time:", self._departure_time.strftime("%H:%M"))
        print("Gate:", self._gate)

    def book_ticket(self):
        pass  # Should handle the process of booking a ticket

    def cancel_ticket(self):
        pass  # Should handle the process of canceling a ticket

    def upgrade_seat(self):
        pass  # Should handle the process of upgrading a seat

    def modify_booking(self):
        pass  # Should handle the process of modifying a booking


# Example usage:
ticket = Ticket("James Smith", "Chicago ORD", "New York Jfk", "NA4321", "09A", datetime(2020, 12, 6),
                datetime(2020, 12, 6, 11, 20), "3")
ticket.display_info()


class Luggage:
    def __init__(self, weight, height, content, size, color):
        self._weight = weight
        self._height = height
        self._content = content
        self._size = size
        self._color = color

    # Setters
    def set_weight(self, weight):
        self._weight = weight

    def set_height(self, height):
        self._height = height

    def set_content(self, content):
        self._content = content

    def set_size(self, size):
        self._size = size

    def set_color(self, color):
        self._color = color

    # Getters
    def get_weight(self):
        return self._weight

    def get_height(self):
        return self._height

    def get_content(self):
        return self._content

    def get_size(self):
        return self._size

    def get_color(self):
        return self._color

    # Display function
    def display_info(self):
        print("Weight:", self._weight)
        print("Height:", self._height)
        print("Content:", self._content)
        print("Size:", self._size)
        print("Color:", self._color)


# Example usage:
luggage = Luggage(20.5, 30.0, "Clothes", "Medium", "Black")
luggage.display_info()