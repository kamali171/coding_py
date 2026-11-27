class Stack:
    def __init__(self):
        self.stack = []

    # Insert element
    def push(self, data):
        self.stack.append(data)

    # Remove element
    def pop(self):
        if not self.stack:
            print("Stack is Empty")
        else:
            return self.stack.pop()

    # Display top element
    def peek(self):
        if not self.stack:
            print("Stack is Empty")
        else:
            return self.stack[-1]

    # Display stack
    def display(self):
        print(self.stack)


# Main program
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Top Element:", s.peek())

print("Deleted Element:", s.pop())

s.display()
