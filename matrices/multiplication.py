from pseudo_array import array

arr = array(
    [
        [1, 2, 5, 9],
        [3, 6, 1, 8]
    ]
)

arr_2 = array(
    [
        [2, 6],
        [4, 7],
        [20, 4],
        [7, 51]
    ]
)

print("First array in the shape of {}:".format(arr.shape))
print(arr)

print("\nSecond array in the shape of {}:".format(arr_2.shape))
print(arr_2)

newarr = arr.multiply(arr_2)
print("\nMultiplication results in the shape of {}:".format(newarr.shape))
print(newarr)
print(newarr.shape)