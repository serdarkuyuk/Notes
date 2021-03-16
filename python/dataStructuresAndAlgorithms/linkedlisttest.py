class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                self.tail.next = newNode
                self.tail = newNode
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                newNode.next = currentNode.next
                currentNode.next = newNode

    def traverseSLL(self):
        if self.head:
            node = self.head
            while node:
                print(node.value)
                node = node.next
        else:
            print("No linklist head")

    def searchSLL(self, number):
        if self.head:
            node = self.head
            while node:
                if node.value == number:
                    return node.value
                node = node.next
        return "no value"

    def deleteSLL(self, location):
        if not self.head:
            return "there is no linked list"
        else:
            if location == 0:
                node = self.head
                if not node.next:
                    self.head = None
                    self.tail = None
                else:
                    self.head = node.next
            elif location == 1:
                node = self.head
                if not node.next:
                    self.head = None
                    self.tail = None
                else:
                    currentNode = self.head
                    while currentNode:
                        if currentNode.next == self.tail:
                            break
                        currentNode = currentNode.next
                    currentNode.next = None
                    self.tail = currentNode
            elif location != 0 or location != 1:
                node = self.head
                index = 0
                while index < location - 1:
                    node = node.next
                    index += 1
                node.next = node.next.next

    def deleteEntireSLL(self):
        if self.head:
            self.head = None
            self.tail = None
        else:
            print("There is no linked list.")


singlyLinkList = SlinkedList()
singlyLinkList.insertSLL(1, 1)
singlyLinkList.insertSLL(2, 1)
singlyLinkList.insertSLL(3, 1)
singlyLinkList.insertSLL(4, 1)
singlyLinkList.insertSLL(0, 1)
# singlyLinkList.traverseSLL()
# print(singlyLinkList.searchSLL(9))
print([node.value for node in singlyLinkList])

singlyLinkList.deleteEntireSLL()

print([node.value for node in singlyLinkList])


# node1 = Node(1)
# node2 = Node(2)

# singlyLinkList.head = node1
# singlyLinkList.head.next = node2
# singlyLinkList.tail = node2