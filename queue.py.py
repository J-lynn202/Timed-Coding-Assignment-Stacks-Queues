from node import Node

class Queue () :
    def __init__(self):
        self.front = None
        self.rear = None
        self.closed_tickets = {}

        def __len__(self):
            count = 0
            current = self.front

            while current is not None:
                count +=1
                current = current.next

                return count
            
            def enqueue(self,ticket_number, issue):
                new_ticket = Node(ticket_number, issue)

                if self.front is None:
                    self.front = new_ticket
                    self.rear = new_ticket
                else:
                    self.rear.next = new_ticket
                    self.rear = new_ticket

                    print("Ticket opened!")

            def display(self):
                        if len(self) == 0:
                             print("The queue is empty.")
                             return
                        current = self.front

                        print("\n===== ALL OPEN TICKETS =====")
                        print("Ticket Number:")
                        print("Ticket:")
                        print("")

            
                        print("\n===== CLOSING Ticket =====")
                        print("Ticket Number:")
                        print("Ticket:")
                        print("Ticket closed!")

                            