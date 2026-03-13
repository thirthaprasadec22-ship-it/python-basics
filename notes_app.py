while True:

    print("\n1. Write a note")
    print("2. Read notes")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        note = input("Write your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note saved!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                print("\nYour Notes:")
                print(file.read())
        except FileNotFoundError:
            print("No notes found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")