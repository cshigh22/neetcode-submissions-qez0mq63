class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        
        length = len(self.arr) // 2

        if len(self.arr) % 2 == 0:
            return (self.arr[length] + self.arr[length - 1]) / 2
        else:
            return self.arr[length]
        