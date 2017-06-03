# CONSTANT
INF = 50000

class Sorter():
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def getInstance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance

    def __init__(self):
        self.nbreak = INF

    @property
    def nbreak_setted(self):
        if self.nbreak is INF:
            return False
        else:
            return True


    def set_nbreak(self, nbreak):
        self.nbreak = nbreak
        # print("set_nbreak={}".format(self.nbreak))

    def sort(self, arr, method):
        if method is "quick":
            return self.quick_sort(arr)
        elif method is "insertion":
            return self.insertion_sort(arr)
        elif method is "combine":
            return self.quick_insertion(arr)

    def quick_insertion(self,arr):
        if arr.size > self.nbreak:
            return self.quick_sort(arr)
        else:
            return self.insertion_sort(arr)

    def insertion_sort(self,arr):
        for i in range(1, len(arr)):
            j = i - 1
            temp = arr[i]
            while True:
                if not (arr[j] > temp and j >= 0):
                    break
                arr[j+1]  = arr[j]
                j = j - 1
            arr[j+1] = temp
        return arr

    def quick_sort(self,arr):
        if len(arr) <= 1:
            return arr

        pv = arr[int(len(arr) / 2)]
        left = []
        right = []
        middle = []
        for i in arr:
            if i < pv:
                left.append(i)
            elif i > pv:
                right.append(i)
            else:
                middle.append(i)

        return self.quick_sort(left) + middle + self.quick_sort(right)