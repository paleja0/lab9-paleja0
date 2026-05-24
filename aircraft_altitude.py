from aircraft import Aircraft

def main():
    model = input("Enter aircraft model:\n")
    my_aircraft = Aircraft(model)

    while True:
        command_input = input("Enter command (A for ascent, D for descent, X to exit):\n").strip()
        
        if command_input.upper() == "X":
            break
            
        # Segmentar la instrucción (ej: ["A", "5000"])
        parts = command_input.split()
        if len(parts) == 2:
            action = parts[0].upper()
            feet = int(parts[1])
            
            if action == "A":
                my_aircraft.ascent(feet)
            elif action == "D":
                my_aircraft.descent(feet)
        
    print(f"Final altitude: {my_aircraft.altitude} feet")

if __name__ == "__main__":
    main()