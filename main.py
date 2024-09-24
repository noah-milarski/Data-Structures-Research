from LinkedList.linked_list import LinkedList
from DoublyLinkedList.doubly_linked_list import DoublyLinkedList

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(10)
    ll.insert_at_end(15)
    ll.insert_at_end(20)

    ll.print()