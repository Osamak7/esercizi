class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.list = []  
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.list.append(new_node)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.list.append(new_node)

    def get_node(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            count += 1
            current = current.next
        return None

def has_cycle(head: Node) -> bool:
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

ll1 = LinkedList()
for i in range(5):
    ll1.append(i)
node1 = ll1.get_node(1)  # Node with value 1
node4 = ll1.get_node(4)  # Node with value 4
node4.next = node1  # Creating a cycle



class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.list = []  # This is not used in the logic, but included as per your request
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.list.append(new_node)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.list.append(new_node)

    def get_node(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            count += 1
            current = current.next
        return None
        
def is_palindrome(head:Node):
        listan=[]
        if head.next:
            listan.append(head.value)
            node=head.next
            while node:
                listan.append(node.value)
                node=node.next
                print(listan)
            if listan == listan[::]:
                return True
            else:
                return False
            
        
 	

ll1 = LinkedList()
for value in [1, 2, 3, 2, 1]:
    ll1.append(value)
print(is_palindrome(ll1.head))