import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    
    hashed_password = hash_password(password)
    
    with open("users.txt", "a") as file:
        file.write(username + "," + hashed_password + "\n")
    
    print("Registration Successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    hashed_password = hash_password(password)
    attempts = 0
    
    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
            
        for user in users:
            stored_username, stored_password = user.strip().split(",")
            
            if username == stored_username:
                while attempts < 3:
                    if hashed_password == stored_password:
                        print("Login Successful!")
                        return
                    else:
                        attempts += 1
                        if attempts == 3:
                            print("Account Locked due to 3 failed attempts!")
                            return
                        print("Wrong password. Try again.")
                        password = input("Enter password again: ")
                        hashed_password = hash_password(password)
                
        print("Username not found!")
    
    except FileNotFoundError:
        print("No users registered yet!")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid Choice")