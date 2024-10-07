import csv
from datetime import datetime


def format_data(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    for row in data:
        try:
            row["created_at"] = datetime.strptime(
                row["created_at"], "%Y-%m-%d %H:%M:%S"
            )
        except (ValueError, TypeError):
            row["created_at"] = datetime.min

    data.sort(key=lambda x: x["created_at"], reverse=True)

    latest_data = data[:100]

    internal_id_counter = 1
    sku_counter = 1

    with open(output_file, "a", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)

        for row in latest_data:
            new_row = []

            new_row.append("product")
            new_row.append(str(internal_id_counter).zfill(5))
            new_row.append(str(sku_counter))

            new_row.append(row.get("name", ""))
            new_row.append(row.get("price", ""))
            new_row.append("")
            new_row.append("false")
            new_row.append("0")
            new_row.append("")
            new_row.append("1")
            new_row.append("")
            new_row.append("")
            new_row.append("true")
            new_row.append(row.get("image", ""))
            new_row.append("")

            description = row.get("description", "").replace("\n", "<br>")
            description = f"<p><strong>描述</strong></p>\n<p>{description}</p>"
            new_row.append(description)

            new_row.append("true")
            new_row.append("")
            new_row.append(row.get("manufacturer", ""))
            new_row.append("")
            new_row.append(row.get("weight", ""))
            new_row.append("true")
            new_row.append("0.0")
            new_row.append("0.0")
            new_row.append("0.0")
            new_row.append("")
            new_row.append("")
            new_row.append("")
            new_row.append("")
            new_row.append("false")
            new_row.append(row.get("tax_class_id", ""))
            new_row.append(row.get("meta_title", ""))
            new_row.append(row.get("meta_description", ""))
            new_row.append("")
            new_row.append("")
            new_row.append("false")
            new_row.append("")
            new_row.append("5")
            new_row.append("false")
            new_row.append("")
            new_row.append("")
            new_row.append("")
            new_row.append("")
            new_row.append("")
            new_row.append("")
            new_row.append("")
            new_row.append("")
            new_row.append(row.get("url_key", ""))

            writer.writerow(new_row)

            internal_id_counter += 1
            sku_counter += 1


