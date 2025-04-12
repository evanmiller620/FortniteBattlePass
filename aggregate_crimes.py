import csv
import json

aggregate_crimes = {

}

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if row[3] in aggregate_crimes:
                aggregate_crimes[row[3]] += 1
            else:
                aggregate_crimes[row[3]] = 1
            # print(row)
            # break

read_csv_file("crime_data_all_neighborhoods.csv")

with open("aggregate_crimes.json", "w") as file:
    json.dump(aggregate_crimes, file, indent=4)