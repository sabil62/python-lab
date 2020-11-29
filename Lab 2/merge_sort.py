def mergeSort(A, p, r):         #merge sort 
    if p < r:
        q = int((p+r-1)/2)      # partition between p-r

        mergeSort(A, p, q)      # the part from p to q is here
        mergeSort(A, q + 1, r)  # the part from after q that is q+1 to r is here
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1      #as A starts from 0 so +1 is added
    n2 = r - q

    L = [0] * (n1)      # making L and R initialize
    R = [0] * (n2)

    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]

    i = 0
    j = 0
    k = p

    while (i < n1 and j < n2):
        if (L[i] <= R[j]):      #if left side one is smaller then right the final array
            A[k] = L[i]         #taken first
            i += 1
        else:
            A[k] = R[j]         # if right is smaller then it is taken first
            j += 1
        k += 1

    while (i < n1):
        A[k] = L[i]
        i += 1
        k += 1

    while (j < n2):
        A[k] = R[j]
        j += 1
        k += 1

