import os
import json
import csv

class WebScraper:
    def __init__(self, directory):
        self.directory = directory
        self.project_data = []

    def extract_info(self):
        for filename in os.listdir(self.directory):
            if filename.endswith('.md'):
                with open(os.path.join(self.directory, filename), 'r', encoding='utf-8') as file:
                    content = file.read()
                    title = self.get_title(content)
                    description = self.get_description(content)
                    self.project_data.append({'title': title, 'description': description, 'filename': filename})

    @staticmethod
    def get_title(content):
        lines = content.split('\n')
        return lines[0].replace('# ', '') if lines else ''

    @staticmethod
    def get_description(content):
        lines = content.split('\n')
        return lines[1] if len(lines) > 1 else ''

    def export_to_json(self, output_file):
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(self.project_data, json_file, ensure_ascii=False, indents=4)

    def export_to_csv(self, output_file):
        with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['title', 'description', 'filename'])
            writer.writeheader()
            writer.writerows(self.project_data)

if __name__ == '__main__':
    scraper = WebScraper(directory='path/to/your/markdown/files')
    scraper.extract_info()
    scraper.export_to_json('output.json')
    scraper.export_to_csv('output.csv')
