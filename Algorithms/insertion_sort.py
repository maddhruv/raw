##for i = 1, 2, 3.....n
##  insert A[i] into sorted array A[0:i-1]
##  by pair-wise swap down to the correct position

##THIS IS WORSE :(

## theta(n2) algo => theta(n) steps and theta(n) swaps

A = [5, 4, 3, 2, 1, -1, -3]

def insertion_sort(A):
    for i in range(1,len(A)):
        j = i
        while j > 0 and A[j] < A [j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
    return A

print(insertion_sort(A))
