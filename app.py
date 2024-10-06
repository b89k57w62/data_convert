import csv
from utils.create_id import IDProcessor

class Pipeline:
    def __init__(self):
        self.id_processor = IDProcessor()

    def run(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        
        processed_data = self.id_processor.process_type_and_ids(data, output_file)
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(processed_data)

def main():
    input_file = 'data/input.csv'
    output_file = 'data/output.csv'
    pipeline = Pipeline()
    pipeline.run(input_file, output_file)

if __name__ == "__main__":
    main()
