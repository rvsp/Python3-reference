def insert_sort(L):
    """
    Insertion Sort
    --------------
    Advantages:
        - simple implementation
        - efficient for small data sets
        - efficient at sorting partially sorted datasets
        - can sort list as it is recieved
        - in-place
        - stable
    Disadvantages:
        - quadratic time complexity
    Time Complexity:
        - worst:   O(n^2)
        - average: O(n^2)
        - best:    O(n)
    """
    for i in range(1, len(L)):
        for j in range(i, 0, -1):
            if L[j] < L[j-1]:  # reverse until element L[j] >= L[j-1]
                L[j-1], L[j] = L[j], L[j-1] # swapping
            else:
                break

if __name__ == '__main__':
    L = list(range(10, 0, -1))
    print('Unsorted list: ' + repr(L));
    insert_sort(L)
    print('Sorted list: ' + repr(L))
