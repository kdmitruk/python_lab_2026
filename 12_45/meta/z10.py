class DictFile:

    def __init__(self, path):
        self.data = {}
        self.path = path

        try:
            file = open(path, 'r')
            for line in file.readlines():
                line_items = line.split(":")
                self.data[line_items[0]] = line_items[1].strip()
            file.close()
        except:
            print(f"No such file: {path}")

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value
        self.__update_file()

    def __update_file(self):
        file = open(self.path, 'w')
        for key, value in self.data.items():
            file.write(f'{key}: {value} \n')
        file.close()

    def __delitem__(self, key):
        del self.data[key]
        self.__update_file()


if __name__ == '__main__':
    config = DictFile("data.txt")
    #config["key2"] = config["key2"] + '*'
    del config["key1"]