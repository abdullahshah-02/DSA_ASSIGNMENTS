def merge_sorted_lists_descending(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort_descending(left)
    right = merge_sort_descending(right)

    return merge_sorted_lists_descending(left, right)


if __name__ == "__main__":
    arr = [4, 2, 1, 3, 5]

    sorted_arr = merge_sort_descending(arr)

    print(sorted_arr)