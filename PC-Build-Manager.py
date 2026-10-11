import re
import csv
import json
import sys
import os

def clear():
    #print("\033[H\033[J", end="")
    os.system('cls' if os.name == 'nt' else 'clear')


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
    options = {
        "1":"work",
        "2":"gaming",
        "3":"hybrid"
    }
    while True:
        print("Choose your build purpose:")
        print("1 - Work")
        print("2 - Gaming")
        print("3 - Hybrid")
        choice = input("Your Choice: ").strip()
        if choice in options:
            return options[choice]
        print("!!Invalid choice!!")

def budget():
    options = {
        "1":"entry",
        "2":"mid",
        "3":"high"
    }
    while True:
        print("Select your budget type")
        print("1 - Entry")
        print("2 - Mid")
        print("3 - High")
        choice = input("Your Choice: ").strip()
        if choice in options:
            return options[choice]
        print("!!Invalid choice!!")

def get_components(purpose, budget):
    with open("components.json", "r") as file:
        data = json.load(file)
        components = data.get(purpose, {}).get(budget, {})
        return components

def cpu(components):
    cpu_name = components["cpu"][0]["name"]
    print(cpu_name)

def select_components(t1, t2, components):

    order = ["cpu", "gpu", "motherboard", "psu"]
    selected_build = {}

    for comp_name in order:
        if comp_name in components:
            selected_build[comp_name] = display(t1, t2, components, comp_name)

    clear()
    print(f"   {t2} ============= SELECTED BUILD ============ {t1}")
    for comp_name, item in selected_build.items():
        price = item.get("fallback_price", "N/A")
        print(f"{comp_name.upper():<12}: {item['name']} ({price} TL)")
    print("================================================")
    input("\nPress Enter to return to menu...")

    return selected_build



def display(t1, t2, components, name):
    items = components.get(name, [])
    if not items:
        return None

    while True:
        clear()
        print(f" {t2} --- {name.upper()} --- {t1} ")

        for idx, item in enumerate(items, 1):
            print(f"[{idx}] -------------------------")
            for key, value in item.items():
                if key in ["epey_url", "fallback_price"]:
                    continue
                print(f"{key}: {value}")

        choice = input("\nYour Choice (1, 2...): ").strip()
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(items):
                return items[index]

        input("Invalid choice! Press Enter to try again...")


def menu():
    print("1 - New PC Build ")
    print("2 - My Saved Builds")
    print("3 - Log out")
    choice = input("Your Choice: ")
    match choice:
        case "1":
            clear()
            p = purpose()
            b = budget()
            c = get_components(p,b)
            my_build = select_components(p, b, c)


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
                #menu() TEMPORARLY INACTIVE
        case "2":
            sign_up()
        #TEMPORARLY ACTIVE case 3
        case "3":
            menu()
        case _:
            main()

if __name__ == "__main__":
    main()