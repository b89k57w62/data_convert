import csv
from datetime import datetime
from format_header import format_header
def format_chinese_cust(input_file, output_file):
    country_name_to_code = {
        '台灣': 'TW',
        '香港': 'HK',
    }

    data_rows = []

    with open(input_file, "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        input_headers = reader.fieldnames

        for row in reader:
            date_str = row.get('客戶自', '')
            if date_str:
                date_obj = parse_chinese_datetime(date_str)
            else:
                date_obj = None

            row['parsed_date'] = date_obj
            data_rows.append(row)

    data_rows.sort(key=lambda x: x['parsed_date'] if x['parsed_date'] else datetime.min)

    with open(output_file, "r", encoding="utf-8") as outfile:
        existing_headers = outfile.readline().strip().split(",")

    with open(output_file, "a", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=existing_headers)

        customer_id = 1

        for row in data_rows:
            new_row = {key: "" for key in existing_headers}
            new_row["type"] = "customer"
            new_row["customer_internal_id"] = str(customer_id)

            field_mapping = {
                '姓名': 'customer_full_name',
                '電子郵件': 'customer_primary_email',
                '群組': 'customer_group_name',
                '電話': 'customer_primary_phone_number',
                '郵遞區號': 'customer_shipping_address_postal_code_1',
                '國家': 'customer_shipping_address_country_name_1',
                '州/地區/郡縣': 'customer_shipping_address_state_or_province_name_1',
            }

            full_name = row.get("姓名", "")
            new_row["customer_full_name"] = full_name

            new_row["customer_shipping_address_recipient_full_name_1"] = full_name

            for old_field, new_field in field_mapping.items():
                if old_field in input_headers and new_field != "customer_full_name":
                    value = row.get(old_field, "")
                    if old_field == '國家':
                        country_name = value
                        country_code = country_name_to_code.get(country_name, '')
                        new_row['customer_shipping_address_country_code_1'] = country_code
                    new_row[new_field] = value

            writer.writerow(new_row)
            customer_id += 1

def parse_chinese_datetime(date_str):
    date_str = date_str.replace('上午', 'AM').replace('下午', 'PM')
    date_format = '%Y/%m/%d %p%I:%M:%S'
    try:
        date_obj = datetime.strptime(date_str, date_format)
    except ValueError:
        date_obj = None
    return date_obj


if __name__ == "__main__":
    input_file = "/Users/wuhaosheng/dev/data_convert/data/raw_cust.csv"
    header_file = "/Users/wuhaosheng/dev/data_convert/data/formal_cust_formatted.csv"
    output_file = "/Users/wuhaosheng/dev/data_convert/data/output.csv"
    format_header(header_file, output_file)
    format_chinese_cust(input_file, output_file)