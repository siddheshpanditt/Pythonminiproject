rooms = ["Available"] * 10

def menu():
    print("\nWelcome to the Management System!")
    print("1: Check which rooms are available")
    print("2: Book a room")
    print("3: Cancel a room booking")
    print("4: Exit")

def show_me_status():
    print("\nCurrent Room Status:")
    for i, status in enumerate(rooms, start=1):
        print(f"Room {i}: {status}")
    print(f"Total Available Rooms: {rooms.count('Available')}")
    print(f"Total Booked Rooms: {rooms.count('Booked')}")

def management_system():
    while True:
        menu()
        option = input("\nWhat would you like to do? Enter 1, 2, 3, or 4: ")

        if option == "1":
            available = [i + 1 for i in range(len(rooms)) if rooms[i] == "Available"]
            if available:
                print(f"\nAvailable rooms: {', '.join(map(str, available))}")
            else:
                print("\nSorry, no rooms are available right now.")
        elif option == "2":
            number_of_room = int(input("\nEnter the number of room you want to book (1-10): "))
            if 1 <= number_of_room <= len(rooms):
                if rooms[number_of_room - 1] == "Available":
                    rooms[number_of_room - 1] = "Booked"
                    print(f"\nRoom {number_of_room} is now booked for you!")
                else:
                    print(f"\nRoom {number_of_room} is already booked.")
            else:
                print("\nInvalid room number. Please choose between 1 and 10.")
        elif option == "3":
            number_of_room = int(input("\nEnter the number of room to cancel booking (1-10): "))
            if 1 <= number_of_room <= len(rooms):
                if rooms[number_of_room - 1] == "Booked":
                    rooms[number_of_room - 1] = "Available"
                    print(f"\nBooking for Room {number_of_room} has been canceled.")
                else:
                    print(f"\nRoom {number_of_room} is not booked.")
            else:
                print("\nInvalid room number. Please choose between 1 and 10.")
        elif option == "4":
            print("\nThank you for using the Management System. Goodbye!")
            break
        else:
            print("\nThat's not a valid option. Please try again.")

        show_me_status()

management_system()