LOG_FILE = "data/log.txt"

def log_message(level, msg):
    entry = f"[{level.upper()}] {msg}\n"
    with open(LOG_FILE, "a") as f:
        f.write(entry)
    print("Log entry added successfully.")

def main():
    while True:
        print("\n1. INFO Message")
        print("2. ERROR Message")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            msg = input("Enter your INFO message: ")
            log_message("INFO", msg)
        elif choice == "2":
            msg = input("Enter your ERROR message: ")
            log_message("ERROR", msg)
        elif choice == "3":
            print("Goodbye!")
            break
main()        