class RollingAvg:
    def __init__(self,size):
        self.size=size

    def __call__(self, data):
        result = []
        for i in range(1, len(data)-1):
            avg = (data[i-1] + data[i] + data[i+1]) / 3
            result.append(avg)
        return [data[0]] + result + [data[-1]]

if __name__ == '__main__':
    data = [0, 1, 3, 3, 4, 15, 6, 7, 81, 9]
    print(list(map(RollingAvg(3),[data])))