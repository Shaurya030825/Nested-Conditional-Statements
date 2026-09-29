print("======================================")
print("Welcome to Holiday Activity Planner")
print("=======================================")
print()

print("Step 1- Pick your holiday type")
print(" 1- Beach Holiday")
print(" 2- Mountain Holiday")
print()

choice= int(input("Enter 1 or 2:"))
print()

if choice== 1:
    print("Step 2: Pik your beach activity.")
    print(" 1- Swimming")
    print(" 2-Sandcastle building")
    print()

    beach_activity= int(input("Enter 1 or 2:"))
    print()

    if beach_activity==1:
        print("You picked:  swimming")
        print("Best time:   morning")
        print("Remember:    carry sunscreen and water")

    else:
        print("You picked:  Building Sandcastle")
        print("Best time:   Evening")
        print("Remember:    Carry a bucket and spade")

elif choice== 2:
    print("Pick your muntain activity")
    print(" 1-  Hiking")
    print(" 2- Camping")
    print()

    mountain_activity= int(input("Enter 1 or 2:"))
    print()

    if mountain_activity== 1:
        print("You picked:  Hiiking")
        print("Best for:    Exploring trails")
        print("Remember:    Wear comfortable shoes")

    else:
        print("You picked:  Camping")
        print("Best for:    Staying close to nature")
        print("Remember:    Carry a tent and torch")

else:
    print("That is not a valid choice.")
    print("Please enter 1 for beach holiday or 2 for Mountain Holiday.")

print()
print("============================")
print("Your holiday plan is ready!")
print("Enjoy your trip")
print("===========================")