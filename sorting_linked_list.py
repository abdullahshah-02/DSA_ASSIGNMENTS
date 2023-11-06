class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_sorted_lists(left, right):
    dummy = ListNode()
    current = dummy

    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    current.next = left or right

    return dummy.next


def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    # Split the linked list into two halves
    middle = find_middle(head)
    left, right = head, middle.next
    middle.next = None

    left = merge_sort_linked_list(left)
    right = merge_sort_linked_list(right)

    return merge_sorted_lists(left, right)

def find_middle(head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3, ListNode(5, None)))))

    sorted_head = merge_sort_linked_list(head)

    print_linked_list(sorted_head)
