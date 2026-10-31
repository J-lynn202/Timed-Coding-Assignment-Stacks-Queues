class Node:
  def __init__(self,ticket_number, issue) :
    self.ticket_number = ticket_number
    self.issue = issue
    self.next = None