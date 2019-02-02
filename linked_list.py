class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


def find_junction_of_2_lists(head1, head2):
    """
    this function detects and return the first common node of 2 linked lists
    :param head1: Node, the first node of list 1
    :param head2: Node, the first node of list 1
    :return: Node, the first common node
    """
    def length(head):
        node = head
        counter = 1
        while node.next:
            counter += 1
            node = node.next
        return counter

    def get_to_node_in_index(head, index):
        node = head
        for x in range(index):
            node = node.next
        return node

    list1_len = length(head1)
    list2_len = length(head2)
    diff = abs(list1_len - list2_len)
    node1 = get_to_node_in_index(head1, diff)
    node2 = head2
    
    for i in range(min(list1_len, list2_len)):
        if node1 == node2:
            return node1
        node1 = node1.next
        node2 = node2.next



