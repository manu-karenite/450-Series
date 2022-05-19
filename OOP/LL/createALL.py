class Node:
    def __init__(self, val):
        self.val = int(val)
        self.next = None


class LL:

    def __init__(self):
        self.head = None
        self.tail = None

    def createNode(self, val):
        n = Node(val)
        if self.head is None:
            self.head = n
            self.tail = n

        else:
            self.tail.next = n
            self.tail = self.tail.next

    def print(self):
        print("The Nodes in LL are : ")
        temp = self.head
        while temp is not None:
            print(temp.val, " ")
            temp = temp.next

    def insertNode(self, data, pos):
        # create a node first and then
        node = Node(data)
        if pos == 0:
            # wants to insert head into
            node.next = self.head
            self.head = node
            return
        # look for the position:

        target = 0
        temp = self.head
        while temp is not None:

            if target == pos:

                if temp.next is None:
                    temp.next = node
                    return

                else:
                    node.next = temp.next
                    temp.next = node
                    return

            else:
                temp = temp.next
                target = target+1
        # otherwise... nothing
        print("Could not Delete (index out of bounds)")

    def deleteNode(self, val):
        temp = self.head
        prev = None
        deleted = False
        while temp is not None:
            #print(type(val), type(temp.val))
            if val == temp.val:  # FOUND
                if temp.next is None:
                    if prev is None:  # deleted head
                        self.head = None
                        return
                    else:
                        prev.next = temp.next
                        temp.next = None
                        return
                elif temp.next is not None:
                    #print("not last")
                    if prev is None:
                        self.head = self.head.next
                        return

                    else:
                        # print("Hello")
                        prev.next = temp.next
                        temp.next = None
                        return
            else:
                # print("next")
                prev = temp
                temp = temp.next


def main():
    #print("Enter the elements : ")
    s = input()
    s = s.split(" ")
    obj = LL()
    for x in s:
        obj.createNode(x)
    obj.print()
    b = bool(input("Do you want to delete a node : "))
    if b == True:
        val = int(input("Enter the value of node you want to delete ? "))
        obj.deleteNode(val)
        obj.print()

    y = bool(input("Do you want to insert a node : "))
    if y == True:
        opt = input(
            "PLease enter the value and position after which you want to insert (indexed 0): ")
        [data, pos] = opt.split()
        data = int(data)
        pos = int(pos)
        obj.insertNode(data, pos)
        obj.print()


if __name__ == "__main__":
    main()
