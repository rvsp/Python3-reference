from random import randint, shuffle
def quicksort(array):
    """
    Quicksort
    ----------
    Advantages:
        - Fast for large data sets
    Disadvantages:
        - Not stable
    Time complexity:
        - worst:   O(n^2)
        - average: O(n*log(n))
        - best:    O(n*log(n))
    """
    if len(array) <= 1:
        return array
    pivot_index = randint(0, len(array)-1)
    print('pivot_index->',pivot_index)
    pivot = array.pop(pivot_index)
    less, greater = [], []
    for element in array:
        if element <= pivot:
            less.append(element)
        else:
            greater.append(element)
    return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    array = list(range(10, 0, -1))
    shuffle(array)
    print('Unsorted list: ' + str(array));
    array = quicksort(array)
    print('Sorted list: ' + str(array))
