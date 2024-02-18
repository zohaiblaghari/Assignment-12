conversion_factors = {
    "c_to_f":"Celsius to fahrenheit", "f_to_c": "Fahrenheit to Celsius"
}
while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")
    choice = input("Enter your choice:")

    if choice == "1":
        celsius = float(input("Enter temperature in celsius:"))
        if conversion_factors["c_to_f"] == "Celsius to Fahrenheit":
            fahrenheit = celsius * 9/5 + 32
            print(f"{celsius}C is equal to {fahrenheit:.2f}F")
        else:
            print("Invalid conversion factor.")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in fahrenheit:"))
        if conversion_factors["f_to_c"] == "Fahrenheit to Celsius":
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}F is equal to {celsius:.2f}C")
        else:
            print("Invalid conversion factor.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. please try again.")