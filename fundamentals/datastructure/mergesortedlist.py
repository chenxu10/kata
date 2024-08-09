from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # if both inputs are empty
        current = dummy
        
        def iterate_while_both_lists_have_nodes(list1, list2, current):
            while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            return list1,list2,current
            
        def append_if_list_not_emprty_after_iteration(list1, list2, current):
            if list1:
                current.next = list1
            if list2:
                current.next = list2
    
        list1, list2, current = iterate_while_both_lists_have_nodes(list1, list2, current)   
        append_if_list_not_emprty_after_iteration(list1, list2, current)
        return dummy.next



def test_merge_two_sorted_list():
    S = Solution()
    l1 = ListNode(1,ListNode(2))
    l2 = ListNode(2,ListNode(3))
    merge_sorted_list = S.mergeTwoLists(l1,l2)
    assert merge_sorted_list.next.val == 2
    assert merge_sorted_list.next.next.val == 2

def main():
    test_merge_two_sorted_list()
    
if __name__ == '__main__':
    main()