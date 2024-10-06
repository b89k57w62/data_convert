import re

class IDProcessor:
    def __init__(self):
        self.id_counter = 1
        self.sku_counter = 1

    def process_type_and_ids(self, data, output_file):
        processed_data = []
        for item in data:
            if len(processed_data) >= 100:
                break
            
            processed_item = item.copy()
            processed_item['type'] = 'product'
            processed_item['product_internal_id'] = f'{self.id_counter:05d}'
            processed_item['product_sku'] = str(self.sku_counter)
            
            # Process description
            if processed_item['product_description']:
                processed_item['product_description'] = self.process_description(processed_item['product_description'])
            
            processed_data.append(processed_item)
            self.id_counter += 1
            self.sku_counter += 1
        
        return processed_data

    def process_description(self, description):
        
        description = description.strip()
        formatted_description = f"<p><strong>描述</strong></p>\n<p>{description}</p>"
        return formatted_description
