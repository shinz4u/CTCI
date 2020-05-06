from stacks.min_stack import stack

# Stack , is a FILO system
# Queue is a FIFO system

class StackQueue():
    """
    Implements a queue using two stacks
    """
    def __init__(self):
        self.stack1 = stack()
        self.stack2 = stack()
        # self.stack1.push(data)

    def pop(self):
        if self.stack2.is_empty():
            if not self.move():
                print("Nothing to pop")
                return None
        return self.stack2.pop().data

    def push(self, data):
        self.stack1.push(data)

    def peek(self):
        if self.stack2.is_empty():
            if not self.move():
                print("Nothing to peek")
                return None
        return self.stack2.peek()

    def move(self):
        """
        Moves the content one by one to the stack2 prior to peeking or popping.
        :return:
        """
        if self.stack1.is_empty():
            return False
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        return True

if __name__ == "__main__":

    # stack1 = stack()
    # stack2 = stack()
    #
    # stack1.push("Sumini")
    # stack1.push("Lumini")
    # stack1.push("something")
    # stack1.push("nothing")
    #
    #
    # stack2.push(1)
    # stack2.push(2)
    # stack2.push(3)
    # stack2.push(4)
    # stack2.push(5)
    #
    #
    # print(stack1.top.data)
    # print(stack2.top.data)

    queue = StackQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    queue.push(6)
    queue.push(7)

    print("First pop is", queue.pop())

    print("Second pop is", queue.pop())

    queue.push(8)
    queue.push(9)
    queue.push(10)
    queue.push(11)
    queue.push(12)

    print("pop is", queue.pop())
    print("pop is", queue.pop())
    print("pop is", queue.pop())
    print("pop is", queue.pop())
    print("pop is", queue.pop())
    print("pop is", queue.pop())
    print("pop is", queue.pop())
    print("pop is", queue.pop())
    print("pop is", queue.pop())
    print("pop is", queue.pop())
    print("pop is", queue.pop())
    print("pop is", queue.pop())

    queue.push(13)
    print("peek is", queue.peek())
    queue.push(14)
    queue.push(15)
    print("pop is", queue.pop())
    print("pop is", queue.pop())




