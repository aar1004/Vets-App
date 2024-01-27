from session16a import customer_menu
from session16b import pets_menu
from session16c import consultation_menu
import datetime


def main_menu():
    message = """
    >>MAIN MENU<<
    0.quit
    1.manage customers
    2.manage pets
    3.manage consulatations
    
    """

    print(message)
    choice = int(input("Enter Your Choice:"))

    while True:
        if choice == 1:
            customer_menu()
        elif choice == 2:
            pets_menu()
        elif choice == 3:
            consultation_menu()
        elif choice == 0:
            break
        else:
            print("invalid choice")
        print(message)
        choice = int(input("Enter Your Choice:"))


def main():
    date1 = datetime.datetime.today()

    welcome = """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    welcome to vet's app
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    main_menu()

    bye = """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    thank you for using vets app !
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    date2 = datetime.datetime.today()
    print("App usage:", date2 - date1)
    print(bye)


if __name__ == "__main__":
    main()
