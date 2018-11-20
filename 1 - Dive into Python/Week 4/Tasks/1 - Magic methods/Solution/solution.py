import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path
        self.lines = ''
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                self.file_data = f.read()
            self.lines = self.file_data.split('\n')

    def write(self, new_line):
        with open(self.path, 'a') as f:
            f.write(new_line)

    def __add__(self, other):
        temp_path = os.path.join(tempfile.gettempdir(), 'tmp.txt')
        temp = File(temp_path)

        with open(self.path, 'r') as f:
            file1_data = f.read()

        with open(other.path, 'r') as f:
            file2_data = f.read()

        temp.write(file1_data + file2_data)

        return temp

    def __str__(self):
        return self.path

    def __iter__(self):
        self.current_iter = 0
        return self

    def __next__(self):
        if self.current_iter >= len(self.lines):
            raise StopIteration

        ans = self.lines[self.current_iter]
        self.current_iter += 1

        return ans


#f1 = File('input.txt')
#f2 = File('input.txt')
#
#print(f1)
#
#f3 = f1 + f2
#
#print(f3)
#
#for line in f3:
#    print(line)

