def insertion_sort(my_list):
    for x in range(1, len(my_list)):
        while (x > 0) and (my_list[x] < my_list[x-1]):
            my_list[x], my_list[x-1] = my_list[x-1], my_list[x]
            x -= 1
    return my_list

print insertion_sort([1, 5, 5, 23, 2, 5, 3])
print insertion_sort([5, 2, 4, 6, 1, 3])
