from queue import Queue

def main ():
    support_queue = Queue()
    ticket_number = 1

    print("\nWelcome to Thidodeaxu's Tech!")

    while True:
        print("n\\2 Type the number for the action you wish to perform and then hit Enter.")

        print("n\1. Open a new ticket")
        print("2. List all open tickets")
        print("3. Close ticket")
        print("4. Review all closed tickets")
        print("5. Review previously closed tickets")
        print("6. Quit")

        choice = input("\nWhat do you want to do? ")

        if choice == "1":
            issue = input("Enter the issue to be fixed: ")

            ticket_number = f"# {ticket_number:001}"

            print("\nTicket Number:")
            print("Ticker:")

            ticket_number +=1


        else:

            print("\nI'm sorry, that is not a appropriate action.")

