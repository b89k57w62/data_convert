from utils.format_header import format_header
from utils.format_data import format_data

def main():
    input_file = 'your_input_file.csv'
    header_file = 'your_header_file.csv' 
    output_file = 'your_output_file.csv'
    format_header(header_file, output_file)

    format_data(input_file, output_file)

if __name__ == "__main__":
    main()