from utils.format_header import format_header
from utils.format_data import format_data

def main():
    input_file = '/Users/wuhaosheng/dev/data_convert/data/raw_data.csv'
    header_file = '/Users/wuhaosheng/dev/data_convert/data/formal_data.csv' 
    output_file = '/Users/wuhaosheng/dev/data_convert/data/output.csv'
    format_header(header_file, output_file)

    format_data(input_file, output_file)

if __name__ == "__main__":
    main()