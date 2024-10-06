def read_csv(file_path):
    import csv

    with open(file_path, mode="r", encoding="utf-8") as file:
        csv_header = csv.reader(file)
        header = next(csv_header)
        print(f"Header: {header}")
        first_row = next(csv_header)
        print(f"first_row: {first_row}")
