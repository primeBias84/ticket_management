import os
import glob

class Ticket:
    def __init__(self, urgency, status, date):
        self.urgency = urgency
        self.status = status
        self.date = date

def get_tickets():
    ret = []
    for file in glob.glob("ticket*"):
        print(file)
        ret.append(file)

def open_ticket(name):
   file = open(name, "r")
   ret = []
   for x in file:
        ret.append(x)
   print(ret)

def main():
    get_tickets()
    open_ticket("ticket_001")

if __name__ == "__main__":
    main()
