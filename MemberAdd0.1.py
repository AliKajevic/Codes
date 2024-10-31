import json 
DB= "memberlist.json"
def write_member(members):
    with open(DB,'w') as file:
        json.dump(members, file, indent=4)

def read_members():
    try:
        with open(DB, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]


def menu():
    while True:
        print("1. Member Add")
        print("2. MemberList")
        print("3. Exit")
        select = input("Enter One Option: ")

        if select == "1":
            member_add()
        elif select == "2":
            member_list()
        elif select == "3":
            print("Exit")
            break
        else:
            print("TRY AGAİN!!")


def member_add():
    print("New Member Create")
    name = input("Name: ")
    LName = input("Lastname: ")
    email = input("E-Mail: ")
    PN = input("Number:  ")

    new_member = {
        "Name": name,
        "Lastname": LName,
        "email": email,
        "Number" : PN
    }
    members = read_members()
    members.append(new_member)
    write_member(members)
    print("Member Added Successfully .")

def member_list():
    members = read_members()
    if not members:
        print("Not Founad This Member")
    else:
        for member in members:
            print(f"Name: {member['Name']}, Last Name: {member['Lastname']}, E-mail: {member['email']}, Number: {member['Number']} ")


if __name__ == "__main__":
    menu()