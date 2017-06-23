def multiply(arr,number):
    for i in range(len(arr)):
        arr[i] *= number
    return arr

a = [2,4,10,22]
b = multiply (a,5)

print b
