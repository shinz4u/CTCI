class LinkedList:
    def __init__(self, data=None):
        self.head = Node(data)

    def add_node_tail(self, new_data=None):
        new_node = Node(new_data)
        node = self.head
        while node.next:
            node = node.next
        else:
            node.next = new_node

    def add_node_head(self, new_data=None):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, data):
        previous = self.head
        node = self.head
        while node.next:
            if node.data == data:
                if node == self.head:  # For head node
                    self.head = node.next
                    return True
                else:
                    previous.next = node.next # Everything in between
            previous = node
            node = node.next

        if node.data == data:  # To check if this is the last node (corner case)
            previous.next = None
            return True
        else:
            return False


    def insert_node_after(self, prior_node_data, node_data):
        node = self.head
        node_to_insert = Node(node_data)
        while node.next:
            if prior_node_data == node.data:
                node_to_insert.next = node.next
                node.next = node_to_insert
                return True
            node = node.next

        if prior_node_data == node.data:
            node_to_insert.next = node.next
            node.next = node_to_insert
            return True
        return False

    def insert_node_before(self, node_to_insert, following_node):
        pass


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node

if __name__ == '__main__':
    linked = LinkedList(1)
    linked.add_node_tail(2)
    linked.add_node_tail(3)
    linked.add_node_tail(4)
    linked.add_node_tail(5)
    linked.add_node_tail(6)

    linked.delete_node(1)
    linked.delete_node(3)
    linked.delete_node(6)

    linked.add_node_head(7)
    linked.add_node_head(8)

    linked.add_node_tail(9)
    linked.add_node_tail(10)

    linked.insert_node_after(2, 3)
    linked.insert_node_after(5, 6)
    linked.insert_node_after(10, 11)

    node = linked.head
    while node:
        print(node.data)
        node = node.next



