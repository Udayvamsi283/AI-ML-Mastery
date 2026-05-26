FILE = "data/notes.txt"

def add_note():
    note = input("Enter your note: ")
    with open(FILE,"a") as f:
        f.write(note+"\n")
    print("Note added successfully!")

def view_notes():
    try:
        with open(FILE,"r") as f:
            notes = f.read()
            if notes:
                print("Your Notes:")
                print(notes)
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes found.")
    
def main():
    while True:
        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            
main()