import sqlite3

# Create a connection to the database
conn = sqlite3.connect('registration.db')
cursor = conn.cursor()

# Create a table to store user information
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                    )''')

# Function to insert user data into the database
def register_user(username, email, password):
    cursor.execute('''INSERT INTO users (username, email, password) 
                      VALUES (?, ?, ?)''', (username, email, password))
    conn.commit()
    print("Registration successful!")

# Function to retrieve user data from the database
def get_user(username):
    cursor.execute('''SELECT * FROM users WHERE username = ?''', (username,))
    return cursor.fetchone()

# Main function to run the registration process
def main():
    print("Welcome to the registration form!")
    username = input("Enter your username: ")
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    # Check if the username already exists
    if get_user(username):
        print("Username already exists. Please choose another one.")
    else:
        register_user(username, email, password)

# Run the main function
if __name__ == "_main_": 
    main()