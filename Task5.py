class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    def reverseLinkedList(head, k):
        prev = None
        current = head
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def getLength(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    # Check if there are at least k nodes to reverse
    length = getLength(head)
    if length < k:
        return head

    # Initialize dummy nodes for the new head and tail
    dummy_head = ListNode(0)
    dummy_head.next = head
    tail = dummy_head

    while length >= k:
        group_start = tail.next
        group_end = tail.next
        for _ in range(k):
            group_end = group_end.next

        # Reverse the group
        new_head = reverseLinkedList(group_start, k)

        # Connect the reversed group with the previous group
        tail.next = new_head
        group_start.next = group_end

        # Update tail and length
        tail = group_start
        length -= k

    return dummy_head.next

# Create the linked list based on the provided example
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Reverse the linked list in groups of size 2
k = 2
result = reverseKGroup(head, k)

# Print the result
while result:
    print(result.val)
    result = result.next
