import csv
from datetime import datetime
from collections import defaultdict
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.count_statuses = defaultdict(int)

    def process_item(self, item, spider):
        status = item['status']
        self.count_statuses[status] = self.count_statuses.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        FILE_DIR = BASE_DIR / 'results'
        FILE_DIR.mkdir(exist_ok=True)
        time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filepath = FILE_DIR / f'status_summary_{time}.csv'
        with open(filepath, 'w', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows((
                ('Status', 'Quantity'),
                *self.count_statuses.items(),
                ('Total', sum(self.count_statuses.values()))
            ))
