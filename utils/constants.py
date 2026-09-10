from enum import Enum

class Cachekey(Enum):
    POSTING_LIST = 'posting_list'

    def format(self, **kwargs):
        return self.value.format(**kwargs)