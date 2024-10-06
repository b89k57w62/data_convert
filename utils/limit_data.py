import csv


class DataLimiter:
    def limit_to_100_rows(self, input_file, output_file, limit=100):
        with open(input_file, mode="r", encoding="utf-8") as infile, open(
            output_file, mode="w", newline="", encoding="utf-8"
        ) as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            header = next(reader)
            writer.writerow(header)

            for i, row in enumerate(reader):
                if i < limit:
                    writer.writerow(row)
                else:
                    break
