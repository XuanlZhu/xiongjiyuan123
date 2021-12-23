import csv

class CsvUtil:
    def __init__(self,csv_file):
        self.csv_file = csv_file

    def read_csv(self):
        with open(self.csv_file,'r') as f:
            f = list(csv.reader(f))
            f.pop(0)
            print(f)
            return f
