from utils.format_header import format_header
from utils.format_product import format_product
from utils.format_cust import format_cust


def main():
    input_file = "/Users/wuhaosheng/dev/data_convert/data/raw_product.csv"
    header_file = "/Users/wuhaosheng/dev/data_convert/data/formal_product.csv"
    output_file = "/Users/wuhaosheng/dev/data_convert/data/output_product.csv"
    format_header(header_file, output_file)
    if input_file.endswith("raw_product.csv"):
        format_product(input_file, output_file)

    if input_file.endswith("raw_cust.csv"):
        format_cust(input_file, output_file)


if __name__ == "__main__":
    main()
