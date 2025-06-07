import mysql.connector

# 🔌 Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",         # change if needed
    password="niraj@2801",  # replace with your MySQL password
    database="contact_book"
)
cursor = conn.cursor()

# 📜 Menu Function
def menu():
    print("\n=== Contact Book ===")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

# ➕ Add Contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    cursor.execute("INSERT INTO contacts (name, phone_number, email) VALUES (%s, %s, %s)", (name, phone, email))
    conn.commit()
    print("✅ Contact added!")

# 📖 View Contacts
def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    print("\n--- All Contacts ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3]}")

# 🔍 Search Contact
def search_contact():
    name = input("Enter name to search: ")
    cursor.execute("SELECT * FROM contacts WHERE name LIKE %s", ('%' + name + '%',))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3]}")
    else:
        print("❌ No contact found.")

# ❌ Delete Contact
def delete_contact():
    contact_id = input("Enter contact ID to delete: ")
    cursor.execute("DELETE FROM contacts WHERE id = %s", (contact_id,))
    conn.commit()
    print("🗑️ Contact deleted!")

# 🔁 Run Menu
while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("👋 Exiting... Bye!")
        break
    else:
        print("⚠️ Invalid choice! Try again.")
