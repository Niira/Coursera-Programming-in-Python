import os


class FileReader:
    def __init__(self, path):
        self._path = path

    def read(self):
        if not os.path.exists(self._path):
            return ""
        else:
            with open(self._path, 'r') as f:
                text = f.read()
                return text


#reader = FileReader("input.txt")
#print(reader.read())
