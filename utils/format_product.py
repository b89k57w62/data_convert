import csv
from datetime import datetime


def format_product(input_file, output_file):
    header_mapping = {
        "sku": "sku",
        "name": "title",
        "description": "description",
        "price": "price",
        "msrp": "compare-at-price",
        "url_key": "url-handle",
        "meta_title": "seo-title",
        "meta_description": "seo-description",
    }

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

    with open(output_file, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        new_header = next(reader)

    with open(output_file, "a", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)

        for row in latest_data:
            new_row = [""] * len(new_header)

            for old_key, new_key in header_mapping.items():
                if old_key in row:
                    new_row[new_header.index(new_key)] = row[old_key]

            new_row[new_header.index("field-type")] = "product"
            new_row[new_header.index("type")] = "PHYSICAL"

            description = row.get("description", "").replace("\n", "<br>")
            description = f"<p><strong>描述</strong></p>\n<p>{description}</p>"
            new_row[new_header.index("description")] = description

            new_row[new_header.index("product-image-url")] = ""
            new_row[new_header.index("product-image-alt-text")] = ""

            status_mapping = {"1": "ACTIVE", "2": "INACTIVE"}
            status_code = row.get("status", "")
            new_row[new_header.index("status")] = status_mapping.get(
                status_code, "INACTIVE"
            )

            try:
                qty = float(row.get("qty", "0"))
            except ValueError:
                qty = 0

            if qty > 0:
                new_row[new_header.index("inventory")] = "IN STOCK"
            else:
                new_row[new_header.index("inventory")] = "OUT OF STOCK"

            if "_category" in row:
                new_row[new_header.index("category")] = row["_category"]

            if row.get("_custom_option_title"):
                new_row[new_header.index("product-option-name-1")] = row[
                    "_custom_option_title"
                ]
                option_values = []
                if row.get("_custom_option_row_title"):
                    option_values.append(row["_custom_option_row_title"])
                new_row[new_header.index("product-option-value-1")] = ";".join(
                    option_values
                )

            writer.writerow(new_row)
