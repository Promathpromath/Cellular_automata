class File():
    def __init__(self, filename):
        self.filename = filename

    def write_file(self, field):
        with open(self.filename, 'a') as file:
            for row in field:
                for item in row:
                    file.write(str(int(item.is_life)))
            file.write('\n')

    def read_file(self):
        with open(self.filename, 'r') as file:
            data = file.readlines()
            return data

    def clear_file(self):
        file = open(self.filename, 'w')
        file.close()
