# TODO: Import modules
import car_utils
from car import *

def main():
    cars = {}  # Dictionary to store cars with car_id as key and car objects as values

    while True:
        print("\nMenu:")
        print("1. Add a new car")
        print("2. View all cars")
        print("3. Drive a car")
        print("4. Paint a car")
        print("5. Exit")

        choice = input("Choose an option:\n")

        if choice == '1':
            # Llamamos a car_utils para generar el carro
            new_car = car_utils.create_car_from_input()
            # Lo guardamos en el diccionario usando el car_id como clave
            cars[new_car.car_id] = new_car
            # Imprimimos el carro y el mensaje de éxito exigido por el README
            print(new_car)
            print("Car added.")

        elif choice == '2':
            # Mostramos todos los carros usando la función de car_utils
            car_utils.display_cars(cars)

        elif choice == '3':
            car_id = input("Enter the car ID to drive:\n")
            miles = float(input("How many miles to drive?\n"))
            # Buscamos el carro en el diccionario
            if car_id in cars:
                cars[car_id].drive(miles)
                print("Mileage updated.")
                print(cars[car_id])
            else:
                print("Car not found.")
          
        elif choice == '4':
            car_id = input("Enter the car ID to paint:\n")
            new_color = input("Enter the new color:\n")
            # Buscamos el carro en el diccionario
            if car_id in cars:
                cars[car_id].change_color(new_color)
                print("Color updated.")
                print(cars[car_id])
            else:
                print("Car not found.")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
