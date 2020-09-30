class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):


        # saving previos 
        prev = None
        # saving current node
        cur_node = self.head
        # while the current node is not none
        while cur_node is not None:
            # get the next node
            next_node = cur_node.get_next()
            # update the curent.next to the prev
            cur_node.set_next(prev)
            # update the prev to the current node
            prev = cur_node
            # update the cur node to the next node
            cur_node = next_node

        # when it reaches the end update the prev node to head
        self.head = prev

        pass



NodeLIst = LinkedList()

NodeLIst.add_to_head(1)
NodeLIst.add_to_head(2)
NodeLIst.add_to_head(3)
NodeLIst.add_to_head(4)
NodeLIst.add_to_head(5)


NodeLIst.reverse_list(NodeLIst.head, None)