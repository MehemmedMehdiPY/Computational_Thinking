from pseudo_array import array

arr = array(
    [
        [1, 2, 5, 9],
        [3, 6, 1, 8]
    ]
)

arr_2 = array(
    [
        [7, 26, 35, 3],
        [5, 16, 10, 8]
    ]
)

print("First array in the shape of {}:".format(arr.shape))
print(arr)

print("\nSecond array in the shape of {}:".format(arr_2.shape))
print(arr_2)

newarr = arr.add(arr_2)
print("\nAddition results in the shape of {}:".format(newarr.shape))
print(newarr)
print(newarr.shape)

newarr = arr.substract(arr_2)
print("\nSubstraction results in the shape of {}:".format(newarr.shape))
print(newarr)
print(newarr.shape)