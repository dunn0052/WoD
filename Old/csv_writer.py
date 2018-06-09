# modified from https://www.blog.pythonlibrary.org/2014/02/26/python-101-reading-and-writing-csv-files/
import csv

# Python 3.x version
# to use in Python 2.x, simply change 'w' -> 'wp' and remove newline='' from
# writers.
# make data list into csv for use in excel ex:
# data = [[data1,data2,data3],[data4,data5,data6],...] into
#
#          data1|data2|data3
#          data4|data5|data6
#
# when imported into excel

class CsvData:
    def __init__(self, path = None, header = ""):
        self._header = header.split(",")
        self._path = path
        self._data = []
        self._data.append(self._header)

    # add data to CSV
    def add_data(self, data):
        self._data.append(data)

    def change_path(self, path):
        self._path = path
        
    #write to csv file to path   
    def csv_writer(self):
        if(self._path == None):
            print("csv_writer Error: no path specified - use change_path()")
            return
        with open(self._path, "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            if(self.header_exists()):
                for line in self._data:
                    writer.writerow(line)
            else:
                for line in self._data[1:]:
                    writer.writerow(line)             

    # header = "header1,header2,header3,..." as one string
    def add_header(self, header):
        self._header = header.split(",")
        self._data[0] = self._header

    def header_exists(self):
        if(self._header == ['']):
            return False
        else:
            return True

        

    # stores data as a dictionary list and writes to csv
    def csv_dict_writer(self):
        if(self._path == None):
            print("csv_dict_writer Error: no path specified - use change_path()")
            return
        elif(self._header == ['']):
            print("csv_dict_writer Error: no header specified - use add_header()")
            return
        with open(self._path, "w") as out_file:
            writer = csv.DictWriter(out_file, delimiter=',', fieldnames=self._header)
            writer.writeheader()
            for row in self.to_dict():
                writer.writerow(row)
            
    # change data to dict for use in dict_writer. keys = headers
    def to_dict(self):
        my_list = []
        for values in self._data[1:]:
            inner_dict = dict(zip(self._header, values))
            my_list.append(inner_dict)
        return my_list

    def clear(self):
        self._data = []
        self._header = []
        self._path = ""

