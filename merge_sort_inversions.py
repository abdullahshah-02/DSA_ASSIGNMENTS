def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inversions = merge_sort(arr[:mid])
    right, right_inversions = merge_sort(arr[mid:])
    merged, split_inversions = merge(left, right)

    total_inversions = left_inversions + right_inversions + split_inversions
    return merged, total_inversions


def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0
    inversions = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
            inversions += len(left) - left_idx

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged, inversions


def count_inversions(arr):
    _, inversions = merge_sort(arr)
    return inversions


arr = [8, 4, 2, 1]
inversions = count_inversions(arr)
print(f"Number of inversions: {inversions}")
