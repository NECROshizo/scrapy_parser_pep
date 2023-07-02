import csv
from collections import Counter
from datetime import datetime as dt
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.quantity_status = Counter()

    def process_item(self, item, spider):
        self.quantity_status.update((item['status'],))
        return item

    def close_spider(self, spider):
        date = dt.now().strftime('%Y-%m-%dT%H-%M-%S')
        with open(
            BASE_DIR / f'results/status_summary_{date}.csv', 'w',
            encoding='utf-8',
            newline=''
        ) as file:
            writer = csv.writer(file)
            writer.writerows(
                ('Статус', 'Количество'),
                *(self.quantity_status.items()),
                ('Total', sum(self.quantity_status.values()))
            )
