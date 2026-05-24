# Write your class definition here!
class Car:
    def __init__(self, car_id, brand, year, color, mileage=0.0):
        self.car_id = str(car_id)
        self.brand = str(brand)
        self.year = int(year)
        self.color = str(color)
        self.mileage = float(mileage)

    def change_color(self, new_color):
        self.color = str(new_color)

    def drive(self, miles):
        self.mileage += float(miles)

    def __str__(self):
        # Formato requerido: CAR001 - 2020 Red Toyota with 15000.0 miles
        return f"{self.car_id} - {self.year} {self.color} {self.brand} with {self.mileage:.1f} miles"
