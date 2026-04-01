# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # Push the head of each non-empty linked list into the heap
        # Use a tuple (node.val, id, node) to handle cases where two nodes have the same value
        # The 'id' helps break ties and ensures a stable sort, as heapq can't compare ListNode objects directly
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        # Create a dummy node and a pointer to build the new list
        dummy = ListNode()
        current = dummy

        # Process the heap until it's empty
        while min_heap:
            # Pop the smallest element (based on its value) from the heap
            val, i, smallest_node = heapq.heappop(min_heap)

            # Attach the smallest node to the merged list
            current.next = smallest_node

            # Move the current pointer forward
            current = current.next

            # If the popped node has a next node, push it into the heap
            if smallest_node.next:
                heapq.heappush(min_heap, (smallest_node.next.val, i, smallest_node.next))

        # The merged list starts from the dummy node's next pointer
        return dummy.next

            