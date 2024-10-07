import csv


def format_header(header_file, output_file):
    with open(header_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)

    with open(output_file, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)


