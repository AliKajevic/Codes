





def menu():
    while True:
        print("1. Member Add")
        print("2. Exit")
        secim = input("Enter One Option: ")

        if secim == "1":
            member_add()
        
        elif secim == "2":
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

    print("Member Added Successfully .")


if __name__ == "__main__":
    menu()