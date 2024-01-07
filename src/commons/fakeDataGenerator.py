from faker import Faker
from datetime import timedelta


class FakeDataGenerator:
    def __init__(self):
        self.fake = Faker()


    def generator_time_series_data(self, n: int = 10) -> list:
        time_stamp = self.fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
        time_series_data = list()
        for i in range(n):
            time_series_data.append({
                'time': time_stamp.strftime('%Y-%m-%d %H:%M:%S'),
                'value': self.fake.random_int(min=1, max=1000)
            })
            time_stamp = time_stamp + timedelta(days=1)

        return time_series_data
    
    def generator_comment_text(self, n: int = 10) -> list:
        comment_text = list()
        for i in range(n):
            comment_item = dict()
            comment_item['id'] = i
            comment_item['create_time'] = self.fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None).strftime('%Y-%m-%d %H:%M:%S')
            comment_item['content'] = self.fake.text()
            comment_item['user'] = self.fake.name()
            comment_text.append(comment_item)
        return comment_text 


    def generator_bar_data(self, n: int = 10) -> list:
        bar_data = list()
        for i in range(n):
            bar_data.append({
                'name': self.fake.name(),
                'value': self.fake.random_int(min=1, max=1000)
            })
        return bar_data
    

    def generator_pie_data(self, n: int = 10) -> list:
        pie_data = list()
        for i in range(n):
            pie_data.append({
                'name': self.fake.name(),
                'value': self.fake.random_int(min=1, max=1000)
            })
        return pie_data
    

    def generator_scatter_data(self, n: int = 10) -> list:
        scatter_data = list()
        for i in range(n):
            scatter_data.append({
                'x': self.fake.random_int(min=1, max=100),
                'y': self.fake.random_int(min=1, max=1000)
            })
        return scatter_data
    
    
    def generator_sankey_data(self, n: int = 10) -> list:
        sankey_data = list()
        for i in range(n):
            sankey_data.append({
                'source': self.fake.name(),
                'target': self.fake.name(),
                'value': self.fake.random_int(min=1, max=1000)
            })
        return sankey_data
    

    def generator_word_cloud_data(self, n: int = 10) -> list:
        word_cloud_data = list()
        for i in range(n):
            word_cloud_data.append({
                'name': self.fake.name(),
                'value': self.fake.random_int(min=1, max=1000)
            })
        return word_cloud_data
    

    def generator_heatmap_data(self, n: int = 10) -> list:
        heatmap_data = list()
        for i in range(n):
            heatmap_data.append({
                'x': self.fake.random_int(min=1, max=100),
                'y': self.fake.random_int(min=1, max=100),
                'value': self.fake.random_int(min=1, max=1000)
            })
        return heatmap_data
    
        