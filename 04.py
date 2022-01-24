import csv
csvdata = open("C0F9N0-2022-01-15.csv", "r", encoding="utf-8-sig")
data = csv.reader(csvdata, delimiter=',')
for i in data:
    print(i)
csvdata.close()
