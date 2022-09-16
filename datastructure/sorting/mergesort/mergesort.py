def merge(list1, list2):
    i = 0
    j = 0
    merge_arr = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_arr.append(list1[i])
            i += 1
        else:
            merge_arr.append(list2[j])
            j+= 1
    return merge_arr + list1[i:] + list2[j:]
def mergesort(my_list):
    if len(my_list) == 1:
        return my_list

    pivot = len(my_list)//2
    left_partition = mergesort(my_list[:pivot])
    right_partition = mergesort(my_list[pivot:])

    return merge(left_partition, right_partition)

if __name__ == '__main__':
    print(mergesort([1, 3, 5, 7, 9, 11, 13, 11]))
    print(mergesort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
    print(mergesort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))