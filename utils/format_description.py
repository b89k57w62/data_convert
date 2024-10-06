import csv


class DescriptionFormatter:
    def format_description(self, content):
        return f"<p><strong>描述</strong></p>\n<p>{content}</p>"

    def process_csv(self, input_file, output_file):
        with open(input_file, mode="r", encoding="utf-8") as infile, open(
            output_file, mode="w", newline="", encoding="utf-8"
        ) as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            header = next(reader)
            writer.writerow(header)

            for row in reader:
                description_index = header.index("product_description")
                original_description = row[description_index]
                formatted_description = self.format_description(original_description)
                row[description_index] = formatted_description
                writer.writerow(row)
