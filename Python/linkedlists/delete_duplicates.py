from linkedlists.linkedlist import LinkedList
# from linkedlists.linkedlist import LinkedList
# from linkedlist import LinkedList

def print_list(linked_list):
    node = linked_list.head
    while node:
        print(node.data)
        node = node.next
    print("All data has been printed")

def delete_dups(l):
    """
    delete_dups_node_next is a better function.
    :param l:
    :return:
    """
    node = l.head
    previous = l.head

    node_data_counts = {}
    while node:
        if node.data in node_data_counts:
            if node.next:
                previous.next = node.next
                node = node.next
            else:
                previous.next = None
                break # Do you need this to break out if last node is duplicate?
        else:
            if node.next:
                if node.data is None:
                    previous = node
                    node = node.next
                else:
                    node_data_counts[node.data] = 1
                    previous = node
                    node = node.next

def delete_dups_node_next(l):
    """
    Deleted None values too
    :param l:
    :return:
    """
    node = l.head
    previous = l.head

    node_data_counts = {}
    while node.next:
        if node.data in node_data_counts:
            previous.next = node.next
        else:
            # if node.data is None:
            #     previous = node
            # else:
            node_data_counts[node.data] = 1
            previous = node
        node = node.next
    else:
        if node.data in node_data_counts:
            previous.next = None

def is_null(l):
    node = l.head
    if node:
        return False
    else:
        return True

def is_empty():
    pass

if __name__ == '__main__':
    l = LinkedList(1)
    l.add_node_tail()
    l.add_node_tail(2)
    l.add_node_tail(3)
    l.add_node_tail(4)
    l.add_node_tail(5)
    l.add_node_tail(5)
    l.add_node_tail(5)
    l.add_node_tail(3)
    l.add_node_tail()
    l.add_node_tail()
    l.add_node_tail()
    l.add_node_tail(12)
    l.add_node_tail(1)
    l.add_node_tail(2)
    l.add_node_tail()
    l.add_node_tail(1)

    print_list(l)

    delete_dups_node_next(l)

    print_list(l)

    a = LinkedList(1)
    delete_dups_node_next(a)
    print_list(a)

    b = LinkedList(1)
    b.add_node_tail(0)
    delete_dups_node_next(b)
    print_list(b)

    c = LinkedList(0)
    c.add_node_tail(0)
    c.add_node_tail(0)
    c.add_node_tail(0)
    delete_dups_node_next(c)
    print_list(c)

    d = LinkedList()
    delete_dups_node_next(d)
    print_list(d)

