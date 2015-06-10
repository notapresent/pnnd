from news.models import NewsItem
from articles.models import Article

class MainPage(object):
    @classmethod
    def get_context(cls):
        rv = {}
        rv['news'] = NewsItem.get_latest(25)
        rv['main'] = None
        rv['context'] = None
        rv['left_column_data'] = {
            'comments': Article.last_in_section('comments', 4),
            'interview': Article.last_in_section('interview', 2)
        }
        return rv
