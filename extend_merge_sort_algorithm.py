def merge_sorted_lists_descending(arrs):
    merged = []
    while any(arrs):
        max_values = [float('-inf')] * len(arrs)
        max_indices = []

        for i in range(len(arrs)):
            if arrs[i] and arrs[i][-1] >= max_values[i]:
                max_values[i] = arrs[i][-1]

        for i in range(len(arrs)):
            if arrs[i] and arrs[i][-1] == max_values[i]:
                max_indices.append(i)

        for idx in max_indices:
            merged.append(arrs[idx].pop())

    return merged


def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr

    sublists = [arr[i:i+1] for i in range(0, len(arr), 1)]
    while len(sublists) > 1:
        merged_sublists = []

        for i in range(0, len(sublists), 3):
            if i + 2 < len(sublists):
                merged_sublists.append(merge_sorted_lists_descending(sublists[i:i+3]))
            else:
                merged_sublists.append(merge_sorted_lists_descending(sublists[i:]))

        sublists = merged_sublists

    return sublists[0]


if __name__ == "__main__":
    arr = [4, 2, 1, 3, 5, 9, 7, 6]

    sorted_arr = merge_sort_descending(arr)

    print(sorted_arr)