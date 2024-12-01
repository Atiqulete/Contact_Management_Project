import os

contacts_file = "contacts.txt"

def load_from_file():
    contacts = []
    if os.path.exists(contacts_file):
        with open(contacts_file, "r") as file:
            for line in file:
                name, email, phone, address = line.strip().split(",")
                contacts.append({'name': name, 'email': email, 'phone': phone, 'address': address})
    return contacts

def save_to_file(contact):
    with open(contacts_file, "a") as file:
        file.write(f"{contact['name']},{contact['email']},{contact['phone']},{contact['address']}\n")

def is_duplicate_number(phone, contacts):
    return any(contact['phone'] == phone for contact in contacts)

def add_contact():
    name = input("Enter Name: ")
    
    # Validate email input
    while True:
        email = input("Enter Email: ")
        if "@" in email:
            break
        else:
            print("Invalid email address. Please include '@' in your email.")
    
    phone = input("Enter Phone: ")
    address = input("Enter Address: ")

    contacts = load_from_file()

    if is_duplicate_number(phone, contacts):
        print("Error: This phone number already exists.")
        return

    contact = {'name': name, 'email': email, 'phone': phone, 'address': address}
    save_to_file(contact)
    print("Contact added successfully.")

def view_contacts():
    contacts = load_from_file()
    for contact in contacts:
        print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")

def remove_contact():
    phone = input("Enter the phone number of the contact to remove: ")
    contacts = load_from_file()
    contacts = [contact for contact in contacts if contact['phone'] != phone]

    with open(contacts_file, "w") as file:
        for updated_contact in contacts:
            file.write(f"{updated_contact['name']},{updated_contact['email']},{updated_contact['phone']},{updated_contact['address']}\n")
    print("Contact removed successfully.")

def update_contact():
    phone_to_update = input("Enter the phone number of the contact you want to update: ")
    contacts = load_from_file()

    contact_found = False
    for contact in contacts:
        if contact['phone'] == phone_to_update:
            contact_found = True
            print(f"Found contact: {contact['name']} - {contact['email']} - {contact['phone']} - {contact['address']}")
            
            contact['name'] = input(f"Enter new name (or press Enter to keep '{contact['name']}'): ") or contact['name']
            
            while True:
                new_email = input(f"Enter new email (or press Enter to keep '{contact['email']}'): ")
                if not new_email or "@" in new_email:
                    contact['email'] = new_email or contact['email']
                    break
                else:
                    print("Invalid email address. Please include '@' in your email.")
            
            contact['address'] = input(f"Enter new address (or press Enter to keep '{contact['address']}'): ") or contact['address']
            
            new_phone = input(f"Enter new phone number (or press Enter to keep '{contact['phone']}'): ")
            if new_phone:
                contact['phone'] = new_phone

            with open(contacts_file, "w") as file:
                for updated_contact in contacts:
                    file.write(f"{updated_contact['name']},{updated_contact['email']},{updated_contact['phone']},{updated_contact['address']}\n")
            print("Contact updated successfully.")
            break

    if not contact_found:
        print("Contact with this phone number not found.")

def search_contact():
    search_term = input("Enter name, email or phone number to search: ").lower()
    contacts = load_from_file()
    
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['email'].lower() or search_term in contact['phone']]
    
    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
    else:
        print("No contacts found.")
