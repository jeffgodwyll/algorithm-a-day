def quick_sort(my_list):
    if len(my_list) < 1:
        return my_list
    else:
        pivot = my_list[0]
        left = quick_sort([i for i in my_list[1:] if i < pivot])
        right = quick_sort([j for j in my_list[1:] if j > pivot])
        return left + [pivot] + right


print quick_sort([5, 1, 8, 2, 7])
