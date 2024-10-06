import csv


def process_type_and_ids(input_file, output_file):
    with open(input_file, mode="r", encoding="utf-8") as infile, open(
        output_file, mode="w", newline="", encoding="utf-8"
    ) as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        product_internal_id = 1
        product_sku = 1

        for row in reader:
            row[header.index("type")] = "product"

            row[header.index("product_internal_id")] = f"{product_internal_id:05d}"
            product_internal_id += 1
            row[header.index("product_sku")] = str(product_sku)
            product_sku += 1
            writer.writerow(row)
