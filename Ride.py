print("=================")
print("            Welcome to Ride Builder!              ")
print("======================")
print()

print(" 1- Bike")
print(" 2- Car")
print()
choice= int(input("Please select your vehicle"))
if choice== 1:
    print("Pick your bike type")
    print(" 1- Scooty")
    print(" 2- Mountain Bike")
    print()
    bike_type= int(input("Choose between 1 or 2:"))
    print()
    if bike_type== 1:
        print("Bike chosen:   Scooty")
        print("Speed:         80km/hr")
        print("Suitable for:  Cities road")
    else:
        print("Bike chosen:   Mountain bike")
        print("Speed:         40km/hr")
        print("Suitable for:  Rocky trails")    
elif choice== 2:
    print("Step 2- Choose you car")
    print(" 1- sedan")
    print(" 2- SUV")
    print()
    car_type= int(input("Enter 1 or 2:"))

    if car_type==1:
        print("You picked:  Sedan")
        print("Seats:       5 passenegrs")
        print("Best for:    Family trips")
    else:
        print("You picked:  SUV")
        print("Seats:       7 passengers")
        print("Best for:    Off road adventure")
else:
    print("That was not a valid choice")
    print("Please enter 1 for bike or 2 for car")
print()
print("=======================")
print("Your custom ride is ready!")
print("Enjoy the ride!")
print("===========================")