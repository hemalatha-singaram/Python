'''challenge 3: Write a function merge_and_sort that takes two lists, merges them together and returns them sorted.
merge_and_sort([3, 1, 4], [2, 5, 0])  # should return [0, 1, 2, 3, 4, 5]'''
def merge_and_sort(list1, list2):
    merged_list=list1+list2
    merged_list.sort()
    return merged_list
list1=[3, 1, 4] 
list2=[2, 5, 0]
print(merge_and_sort(list1, list2))

    
