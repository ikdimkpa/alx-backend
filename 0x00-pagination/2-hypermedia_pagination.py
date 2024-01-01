#!/usr/bin/env python3
"""
   Implement a get_hyper method that takes the same arguments (and defaults)
   as get_page and returns a dictionary containing the following key-value
   pairs:

   page_size: the length of the returned dataset page
   page: the current page number
   data: the dataset page (equivalent to return from previous task)
   next_page: number of the next page, None if no next page
   prev_page: number of the previous page, None if no previous page
   total_pages: the total number of pages in the dataset as an integer
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """takes two integer arguments page and page_size."""
    return ((page - 1) * page_size, page_size * page)


class Server:
    """
       Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """A get method that returns a particular page"""

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        try:
            start_index, end_index = index_range(page, page_size)
            return self.dataset()[start_index:end_index]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
           returns a dictionary containing the following key-value pairs
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        start, end = index_range(page, page_size)

        # estimating the next page
        if (page < total_pages):
            next_page = page+1
        else:
            next_page = None

        # estimating the previous page
        if (page == 1):
            prev_page = None
        else:
            prev_page = page - 1

        return {'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page
                }
