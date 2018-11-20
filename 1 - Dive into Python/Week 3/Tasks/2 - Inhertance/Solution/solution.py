import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.car_type = None

    def get_photo_file_ext(self):
        return '.' + self.photo_file_name.split('.')[-1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand=brand, photo_file_name=photo_file_name, carrying=carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand=brand, photo_file_name=photo_file_name, carrying=carrying)
        self.body_whl = body_whl
        if body_whl == '':
            self.body_width = 0.0
            self.body_height = 0.0
            self.body_length = 0.0
        else:
            self.body_width = float(self.body_whl.split('x')[0])
            self.body_height = float(self.body_whl.split('x')[1])
            self.body_length = float(self.body_whl.split('x')[2])
        self.car_type = 'truck'

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand=brand, photo_file_name=photo_file_name, carrying=carrying)
        self.extra = extra
        self.car_type = 'spec_machine'


def get_car_list(csv_filename):
    car_list = []

    if not os.path.exists(csv_filename):
        return car_list

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            print(row)
            if len(row) == 7:
                if row[0] == 'car':
                    tmp = Car(brand=row[1], passenger_seats_count=row[2], photo_file_name=row[3], carrying=row[5])
                    car_list.append(tmp)
                elif row[0] == 'truck':
                    tmp = Truck(brand=row[1], photo_file_name=row[3], body_whl=row[4], carrying=row[5])
                    car_list.append(tmp)
                elif row[0] == 'spec_machine':
                    tmp = SpecMachine(brand=row[1], photo_file_name=row[3], carrying=row[5], extra=row[6])
                    car_list.append(tmp)
                else:
                    pass
            else:
                pass

    return car_list


#print(get_car_list("coursera_week3_cars.csv"))
