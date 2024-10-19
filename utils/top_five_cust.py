import csv
import re


def process_cust_orders(file_path):
    customer_dict = {}
    with open(file_path, mode="r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if not row or row[0] == "全部":
                continue

            period, customer_name, order_count, avg_order_value, total_order_value = row
            order_count = int(order_count)
            avg_order_value = int(re.sub(r"[^\d]", "", avg_order_value))
            total_order_value = int(re.sub(r"[^\d]", "", total_order_value))

            if customer_name in customer_dict:
                customer_dict[customer_name][
                    "customer_number_of_placed_orders"
                ] += order_count
                customer_dict[customer_name][
                    "customer_sales_value"
                ] += total_order_value
            else:
                customer_dict[customer_name] = {
                    "customer_full_name": customer_name,
                    "customer_number_of_placed_orders": order_count,
                    "customer_sales_value": total_order_value,
                    "customer_average_order_value": 0,
                }

    for customer in customer_dict.values():
        customer["customer_average_order_value"] = round(
            customer["customer_sales_value"]
            / customer["customer_number_of_placed_orders"]
        )

    return customer_dict
