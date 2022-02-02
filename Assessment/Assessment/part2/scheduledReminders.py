# Assumptions:
# Reminders are set using the number system
# Reminders done are removed
# The first Reminder will be at the top
# There is no restriction on the number reminders

class Queue:1
    def __init__(self):
        self.items = []

    def search(self, alist, item):
        pos = 0
        found = 0
        ii = 0
        while pos < len(alist) and not found:
            if alist[pos] == item:
                found = 1

            else:
                pos = pos + 1

        if (found == 1):
            print("\n\n\n")
            print("The reminder is set already")
            self.nav()
        else:
            print("\n\n\n")
            print("Reminder was not set")
            self.nav()

    def isEmpty(self):
        q = "The Reminders list is empty"

        r = "They are no reminders in the queue"
        if (self.size() > 0):
            print(r)
            print(self.nav())
        else:
            print(q)
            print(self.nav())
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def contents(self):
        return self.items

    def input(self):

        a = input(
            "Enter 1 to add a Rminder \nEnter 2 To Remove Reminder \nEnter 3 to View All Reminders in the Queue\nEnter 4 to check if there are Reminders in the Queue\nEnter 5 to search a Reminders\nEnter 6 to view the number of Reminders : ")
        if (a == '1'):
            y = input("Enter Description of Reminder:")

            self.enqueue(y)
            print(self.contents())
            print("Reminder  added Successfully!!!")
            self.nav()

        if (a == '2'):

            t = Queue()
            if (self.size() > 0):
                print(self.dequeue())
                print("Reminder Removed Successfully")
                self.nav()
            else:
                print("There are Reminders in the List")
                self.nav()

        if (a == '3'):
            print(self.contents())
            self.nav()
        if (a == '4'):
            self.isEmpty()
        if (a == '5'):
            w = input("Enter the Reminder you want to  you want to search : ")
            l = self.contents()
            print(self.search(l, w))
        if (a == '6'):
            f = self.size()
            print("The number of Reminders in the List is : " + str(f))
            self.nav()
        else:
            print("\n")
            print("Invalid Input Please Try Again!!!!")

            self.input()

    def nav(self):
        o = input("Press 1 to back to the main menu:")
        if (o == '1'):
            print("\n")
            self.input()
        else:
            print("Invalid Input!!! Please try again!!!")
            print("\n")
            self.nav()


s = Queue()
s.input()
