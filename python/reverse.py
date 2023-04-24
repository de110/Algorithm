arr=[1,[2,3,[4,5]]];

def reverse(arr):
    if isinstance(arr,list):
        arr=arr[::-1]
        return [reverse(arr[0])+arr[1:]]
    else:
        return arr

reverse(arr)


# recall
