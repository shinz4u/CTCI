class stack():
    def __init__(self):
        self.top = None
        self.min = []

    def pop(self):
        """ Pop the top of the stack"""
        if not self.is_empty():
            pop_node = self.top
            self.top = pop_node.next
            if pop_node == self.min[-1]:
                self.min.pop()
            return pop_node
        else:
            raise Exception("Empty Stack, No Element to pop")

    def push(self, data):
        if type(data) is stack_node:
            new_node = data
            new_node.next = None
        else:
            new_node = stack_node(data=data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.check_min(new_node)

    def get_min(self):
        if not self.is_empty():
            return self.min[-1].data
        else:
            raise Exception("Empty Stack, No Elements at all")

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise Exception("Empty Stack, No Elements at all")

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def check_min(self, node):
        if len(self.min) > 0:
            if self.min[-1].data > node.data:
                self.min.append(node)
                return "new min is {node_data}".format(node_data=node.data)
        else:
            self.min.append(node)

class stack_node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

if __name__ == '__main__':
    stack = stack()
    stack.push(10)
    stack.push(9)
    stack.push(8)
    stack.push(2)
    stack.push(6)
    stack.push(5)
    stack.push(2)
    stack.push(1)
    print(stack.peek())  # Get 1
    print(stack.get_min())  # Get 1
    stack.pop()  # Removing 1
    print(stack.get_min())  # Get 2
    stack.pop()
    print(stack.get_min())  # Get 2
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack.get_min())  # Get 8
    stack.pop()
    print(stack.get_min())
    stack.push(3)
    print(stack.get_min())
    stack.push(5)
    stack.push(1)
    print(stack.get_min())
    stack.pop()
    stack.pop()
    print(stack.get_min())
    stack.pop()
    stack.pop()
    stack.pop()









