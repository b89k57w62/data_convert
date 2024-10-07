import csv


class CSVReader:
    def read_csv(self, file_path):
        with open(file_path, mode="r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            # print(f"Header: {header}")
            first_row = next(csv_reader)
            print(f"first_row: {first_row}")


if __name__ == "__main__":
    csv_reader = CSVReader()
    csv_reader.read_csv("/Users/wuhaosheng/dev/data_convert/data/formal_data.csv")
