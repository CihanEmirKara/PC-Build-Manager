import re
import csv
import json
import sys

def name():
    valid_name = r"^\w{10}$"
    print("The username have 10 characters and not include space")
    n = input("Username: ")
    if re.search(valid_name, n):
        return n
    else:
        return False

def password():
    valid_password = r"^\d{6}$"
    print("The password only have 6 digit number")
    p = input("Password: ")
    if re.search(valid_password, p):
        return p
    else:
        return False

def sign_in():
    user_name = input("Username: ")
    user_password = input("Password: ")
    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            u = row["user_name"]
            p = row["password"]
            if u==user_name and p==user_password:
                print("Access successfully")
                return True
        print("Access Denied")
        return False

def username_check(user_name):

    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row.get("user_name") == user_name:
                return True 
    return False
                    
def sign_up():
    while True:
        user_name = name()
        if not user_name:
            continue
        if username_check(user_name):
            print("This username is already taken! Please try another.")
            continue
        break

    while True:
        user_password = password()
        if user_password:
            break

    with open("users.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["user_name", "password"])
        writer.writerow({
            "user_name": user_name,
            "password" : user_password
        })
    print("Account created successfully!")

def purpose():
    print("Choose your build purpose:")
    print("1 - Work")
    print("2 - Gaming")
    print("3 - Hybrit")
    choice = input("Your Choice: ")
    return choice

def budget():
    print("Select your budget type")
    print("1 - Entry")
    print("2 - Mid")
    print("3 - High")
    choice = input("Your Choice: ")
    return choice


def menu():
    print("1 - New PC Build ")
    print("2 - My Saved Builds")
    print("3 - Log out")
    choice = input("Your Choice: ")
    match choice:
        case "1":
            p = purpose()
            b = budget()
        case "2":
            ...
        case "3":
            sys.exit()
        case _:
            ...






def main():
    print("Welcome the PC Build Manager")
    print("1 - Sign in")
    print("2 - Sign up")
    choice = input("Your Choice: ")
    match choice:
        case "1":
            if sign_in():
                print("Redirecting...",end="")
                print("\r...           ")
                menu()
        case "2":
            sign_up()
        case _:
            main()

if __name__ == "__main__":
    main()