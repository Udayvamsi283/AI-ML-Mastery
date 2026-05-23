contacts = {
    "Uday" : "1234567890",
    "Alice" : "0987654321",
    "Bob" : "5555555555"
}
def add_contact(name, number):
    contacts[name] = number
    print(f"Contact {name} added with number {number}.")
def get_contact(name):
    return contacts.get(name, "Contact not found.")
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")
def display_contacts():
    if contacts:
        print("Contact List:")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("No contacts found.")

# Example usage
add_contact("Charlie", "1112223333")
print(get_contact("Alice"))
delete_contact("Bob")
display_contacts()