import csv


def limit_to_100_rows(input_file, output_file, limit=100):
    with open(input_file, mode="r", encoding="utf-8") as infile, open(
        output_file, mode="w", newline="", encoding="utf-8"
    ) as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        count = 0
        for row in reader:
            if count < limit:
                writer.writerow(row)
                count += 1
            else:
                break
