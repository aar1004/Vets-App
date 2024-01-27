class ScreenInterface:
    def __init__(self, title=""):
        self.title = title
        self.next = None
        self.previous = None

    def show(self):
        print(">> {}".format(self.title))


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, interface):
        self.size += 1

        if self.head is None:
            self.head = interface
            self.tail = interface
        else:
            self.tail.next = interface
            interface.previous = self.tail

            self.tail = interface

    def pop(self):
        if self.size != 0:
            self.size -= 1

            self.tail = self.tail.previous

        else:
            print("Stack is empty...")

    def iterate(self):
        temp = self.tail
        while temp is not None:
            temp.show()
            temp = temp.previous

            if temp == self.tail:
                break
