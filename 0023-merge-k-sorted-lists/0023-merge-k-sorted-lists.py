class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, L1, L2):
        dummy = ListNode(0)
        curr = dummy 

        while L1 and L2:
            if L1.val < L2.val:
                curr.next = L1 # Fixed typo from '-' to '='
                L1 = L1.next
            else:
                curr.next = L2
                L2 = L2.next     
            curr = curr.next
            
        # Attach the remaining nodes
        curr.next = L1 or L2

        return dummy.next