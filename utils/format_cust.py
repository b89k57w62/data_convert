import csv


def format_cust(input_file, output_file):
    customer_id = 1

    with open(input_file, "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        input_headers = reader.fieldnames

        with open(output_file, "r", encoding="utf-8") as outfile:
            existing_headers = outfile.readline().strip().split(",")

        with open(output_file, "a", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=existing_headers)

            for row in reader:
                new_row = {key: "" for key in existing_headers}
                new_row["type"] = "customer"
                new_row["customer_internal_id"] = str(customer_id)

                field_mapping = {
                    "email": "customer_primary_email",
                    "firstname": "customer_full_name",
                    "middlename": "customer_full_name",
                    "lastname": "customer_full_name",
                    "_address_telephone": "customer_primary_phone_number",
                    "group_id": "customer_group_name",
                    "taxvat": "customer_tax_id",
                    "_address_street": "customer_shipping_address_street_1",
                    "_address_city": "customer_shipping_address_city_1",
                    "_address_country_id": "customer_shipping_address_country_code_1",
                    "_address_postcode": "customer_shipping_address_postal_code_1",
                    "_address_region": "customer_shipping_address_state_or_province_name_1",
                }

                firstname = row.get("firstname", "")
                middlename = row.get("middlename", "")
                lastname = row.get("lastname", "")
                full_name = " ".join(filter(None, [firstname, middlename, lastname]))
                new_row["customer_full_name"] = full_name

                addr_firstname = row.get("_address_firstname", "")
                addr_middlename = row.get("_address_middlename", "")
                addr_lastname = row.get("_address_lastname", "")
                addr_full_name = " ".join(
                    filter(None, [addr_firstname, addr_middlename, addr_lastname])
                )
                new_row["customer_shipping_address_recipient_full_name_1"] = (
                    addr_full_name
                )

                for old_field, new_field in field_mapping.items():
                    if old_field in input_headers and new_field != "customer_full_name":
                        new_row[new_field] = row.get(old_field, "")

                writer.writerow(new_row)
                customer_id += 1
