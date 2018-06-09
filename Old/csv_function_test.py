from csv_writer import CsvData

csv = CsvData("csvtest.csv")
csv2 = CsvData("csvtest2.csv")


COUNT = 5

for i in range(COUNT):
    csv.add_data([1,2,3])
    csv2.add_data([4,5,6])
csv.add_header("one,two,three")
csv.csv_writer()
csv2.csv_writer()
csv.change_path("dict_output.csv")
csv.csv_dict_writer()
