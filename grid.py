import cell
import random

class Grid():
    def __init__(self, amount, probability):
        self.width_sreen = 1000
        self.amount = amount
        self.probability = probability
        self.list_prob = []
        self.cells = []

    def fill_probability(self):
        count = 0
        for _ in range(100):
            if count < self.probability:
                self.list_prob.append(True)
            else:
                self.list_prob.append(False)
            count += 1

    def fill_cells(self):
        size = self.width_sreen / self.amount
        x = 0
        for i in range(self.amount):
            y = i * size
            self.cells.append(list())
            for _ in range(self.amount):
                is_life = self.list_prob[random.randint(0, len(self.list_prob) - 1)]
                c = cell.Cell(x, y, size, is_life)
                self.cells[i].append(c)
                x += size
            x = 0

    def check(self, birth, survival):
        next_list = []
        for i in range(self.amount):
            next_list.append([])
            for _ in range(self.amount):
                next_list[i].append(None)

        for i in range(len(self.cells)):
            for k in range(len(self.cells[i])):
                count = 0
                if k - 1 >= 0:
                    if self.cells[i][k - 1].is_life == True:
                        count += 1
                if k - 1 >= 0 and i - 1 >= 0:
                    if self.cells[i - 1][k - 1].is_life == True:
                        count += 1
                if i - 1 >= 0:
                    if self.cells[i - 1][k].is_life == True:
                        count += 1
                if k + 1 < len(self.cells[i]) and i - 1 >= 0:
                    if self.cells[i - 1][k + 1].is_life == True:
                        count += 1
                if k + 1 < len(self.cells[i]):
                    if self.cells[i][k + 1].is_life == True:
                        count += 1
                if k + 1 < len(self.cells[i]) and i + 1 < len(self.cells):
                    if self.cells[i + 1][k + 1].is_life == True:
                        count += 1
                if i + 1 < len(self.cells):
                    if self.cells[i + 1][k].is_life == True:
                        count += 1
                if i + 1 < len(self.cells) and k - 1 >= 0:
                    if self.cells[i + 1][k - 1].is_life == True:
                        count += 1

                if self.cells[i][k].is_life == True:
                    res = True
                    for num in survival:
                        res = res and num != count
                    if res:
                        next_list[i][k] = False

                if self.cells[i][k].is_life == False:
                    for num in birth:
                        if count == num:
                            next_list[i][k] = True

        for i in range(len(next_list)):
            for k in range(len(next_list[i])):
                if next_list[i][k] != None:
                    self.cells[i][k].is_life = next_list[i][k]
        


    def control_end(self, data):
        last = data[-1]
        for i in range(len(data) - 1):
            if data[i] == last:
                return (True, len(data) - 1 - i)
        return (False, -1)