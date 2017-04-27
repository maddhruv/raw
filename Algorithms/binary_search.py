## sorted list

l = [1,3,5,7,9,11,13,15,17]

def search(k, L):
    half = len(L)//2
    if not len(L):
        raise ValueError
    if L[half] > k:
        return search(k,L[:half])
    elif L[half] < k:
        return half + search(k,L[half+1:])
    elif L[half] == k:
        return half
    else:
        raise "Not Found"

print(search(2,l))
