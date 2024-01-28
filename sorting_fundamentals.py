'''

Sorting Algorithms

'''

A = [7,4,2,1,5,6,3]



# Insertion Sort
def insertionSort(A):
    for i in range(len(A)):
        j = i
        temp = A[i]

        while j > 0 and A[j-1] > temp:
            A[j] = A[j-1]     
            j -= 1
            
        A[j] = temp

    return A


# Merge Sort
def Merge(L, R):
    m = len(L) + len(R)
    S = []
    i = 1
    j = 1

    for k in range(m):
        if L[i] <= R[j]:
            S[k] = L[i]
            i += 1
        else:
            S[k] = R[j]
            j += 1

    return S


def MergeSort(A):
    n = len(A)
    h = n // 2 # double slash is like math.floor()

    if n <= 1:
        return A
    
    L = MergeSort(A[:h])
    R = MergeSort(A[h:])

    return Merge(L,R)


# Quick Sort
def Partition(A, low, high):
    pivot = A[high]
    i = low - 1

    for j in range(low, high):
            if A[j] <= pivot:
    
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1
    
                # Swapping element at i with element at j
                (A[i], A[j]) = (A[j], A[i])
    
        # Swap the pivot element with the greater element specified by i
    (A[i + 1], A[high]) = (A[high], A[i + 1])
    
        # Return the position from where partition is done
    return i + 1


def QuickSort(array, low, high):
    if low < high:
        k = Partition(array, low, high)
        h = len(A) // 2

        QuickSort(A, low, k - 1)
        QuickSort(A, k + 1, high)


QuickSort(A, 0, len(A)-1)

print(A)