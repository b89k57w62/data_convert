from utils.format_header import format_header
from utils.format_product import format_product
from utils.format_cust import format_cust


def main():
    input_file = "your_input_file.csv"
    header_file = None # chose one of formal_cust_formatted.csv or formal_product_formatted.csv
    output_file = "your_output_file.csv"
    format_header(header_file, output_file)
    if input_file.endswith("raw_product.csv"):
        format_product(input_file, output_file)

    if input_file.endswith("raw_cust.csv"):
        format_cust(input_file, output_file)


if __name__ == "__main__":
    main()
