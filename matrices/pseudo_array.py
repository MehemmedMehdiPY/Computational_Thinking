
class array_(list):
    def __init__(self, arr):
        super().__init__(arr)
        self.shape = self._is_consistent()

    def _is_consistent(self):
        new_self = self.copy()
        shape = [1]
        while len(new_self):
            length = len(new_self)
            
            dimension = length
            for dim in shape:
                dimension //= dim
            shape.append(dimension)

            new_self_update = new_self[0]
            for i in range(1, length):
                if type(new_self[i]) in (int, float):
                    new_self_update = []
                    continue
                elif len(new_self[i]) != len(new_self[i - 1]):
                    raise ValueError(
                        "setting an array element with a sequence. The requested array has an inhomogeneous shape after {} dimensions. The detected shape was {} + inhomogeneous part.".format(
                                len(shape), tuple(shape[1:])
                            ))
                new_self_update = new_self_update + new_self[i]
            new_self = new_self_update
        return tuple(shape[1:])

class array(array_):
    def __init__(self, arr):
        super().__init__(arr)
        self.T = self._transpose()            
    
    def _empty(self, shape = None):
        if shape is None:
            shape = self.shape
        
        if len(shape) == 0:
            return array_([])
        
        if len(shape) == 1:
            return array_([0] * shape[0])
        
        arr_empty = [0] * shape[-1]
        for dim in shape[-2::-1]:
            arr_empty = [arr_empty.copy() for _ in range(dim)]
        return array_(arr_empty)

    def _transpose(self):
        arr_transpose = self._empty(self.shape[::-1])
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                arr_transpose[j][i] = self[i][j]
        arr_transpose.T = self
        return arr_transpose

    def multiply(self, arr):
        new_shape = (self.shape[0], arr.shape[1])
        arr_res = self._empty(new_shape)
        for i in range(new_shape[0]):
            for j in range(new_shape[1]):
                row = self[i]
                col = arr.T[j]
                arr_res[i][j] = self._multiply(row=row, col=col)
        return array(arr_res)
    
    def _add_row(self, row1, row2, sign = 1):
        shape = (len(row1), )
        row = self._empty(shape)
        for i in range(len(row1)):
            row[i] = row1[i] + row2[i] * sign
        return row
    
    def _add(self, arr, sign = 1):
        arr_res = self._empty(arr.shape)
        for i in range(self.shape[0]):
            row1 = self[i]
            row2 = arr[i]
            arr_res[i] = self._add_row(row1=row1, row2=row2, sign=sign)
        return arr_res

    def add(self, arr):
        return self._add(arr, sign=+1)
    
    def substract(self, arr):
        return self._add(arr, sign=-1)
    
    def _multiply(self, row, col):
        return sum([col[i] * row[i] for i in range(len(col))])


print('salam')
if __name__ == "__main__":

    print(type(array))

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



    import numpy as np

    a = np.array(arr)
    b = np.array(arr_2)

    print(a.dot(b))
    print(arr.multiply(arr_2))

    print(a.dot(b).tolist() == arr.multiply(arr_2))


    print(arr.T)
    print(arr_2)
    print(arr_2.substract(arr.T))