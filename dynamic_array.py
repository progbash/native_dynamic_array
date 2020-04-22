import ctypes

class DynamicArray(object):
    def __init__(self):
        # dinamik massivimin uzunluğu (length)
        self.len = 0
        # dinamik massivimin tutumu
        self.capacity = 1
        # massivim ozu
        self.A = self.make_array(self.capacity)

    # massivin uzunluğunu tapmaq üçün metodum
    def __len__(self):
        return self.len

    # hər hansı bir elementi almama yardım edəcək bu metod
    def __getitem__(self, index):
        if not 0 <= index < self.len:
            return IndexError("index is out of bounds")
        return self.A[index]

    # element əlavə etmək metodu
    def append(self, element):
        # tutum dolubsa, onu orijinal dinamik massivlərdəki kimi 2 dəfə artırmaq lazımdır
        self._resize(self.capacity*2)
        self.A[self.len] = element # massivimin sonuna elementi əlavə etdim
        self.len += 1  # massivimin uzunluğunu artırdım

    # tutumu genişləndirəcək
    def _resize(self, extended_capacity):
        B = self.make_array(extended_capacity)
        # elementləri köhnə massivdən yenisinə daşıyıram
        for element in range(self.len):
            B[element] = self.A[element]
        self.A = B
        self.capacity = extended_capacity

    # the magic happens :)
    def make_array(self, extended_capacity):
        return (extended_capacity*ctypes.py_object)()

array = DynamicArray()
array.append(1)
array.append(2)
print(array[0], array[1])