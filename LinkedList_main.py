from linked_list import *

if __name__ == "__main__":
    print("Building a Linked List...")
    my_list = LinkedList()
    
    print("\n--- Insert at HEAD (3, 2, 1) ---")
    my_list.insert_at_head(3)
    my_list.insert_at_head(2)
    my_list.insert_at_head(1)
    my_list.traverse()
    
    print("\n--- Insert at END (4, 5) ---")
    my_list.insert_at_end(4)
    my_list.insert_at_end(5)
    my_list.traverse()
    
    print("\n--- Delete 3 ---")
    my_list.delete(3)
    my_list.traverse()
    
    print("\n--- Search ---")
    my_list.search(4)
    my_list.search(99)
    
    print("\nDone!")