import unittest
from utils.string_utils import slugify, truncate_string
from utils.date_utils import format_iso_datetime, add_business_days
from utils.collection_utils import chunk_list, flatten_list
from datetime import datetime

class TestUtils(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(slugify("Hello World!"), "hello-world")
        self.assertEqual(slugify("Python & Java"), "python-java")

    def test_truncate_string(self):
        text = "The quick brown fox jumps over the lazy dog"
        self.assertEqual(truncate_string(text, 20), "The quick brown fox...")
        self.assertEqual(truncate_string("Hello", 10), "Hello")

    def test_format_iso_datetime(self):
        dt = datetime(2023, 1, 1, 12, 0, 0)
        self.assertEqual(format_iso_datetime(dt), "2023-01-01T12:00:00Z")

    def test_add_business_days(self):
        # Friday Jan 2nd, 2026 to Monday Jan 5th, 2026
        start = datetime(2026, 1, 2)
        result = add_business_days(start, 1)
        self.assertEqual(result.weekday(), 0)  # Monday
        self.assertEqual(result.day, 5)

    def test_chunk_list(self):
        lst = [1, 2, 3, 4, 5]
        chunks = list(chunk_list(lst, 2))
        self.assertEqual(chunks, [[1, 2], [3, 4], [5]])

    def test_flatten_list(self):
        nested = [[1, 2], [3], [4, 5]]
        self.assertEqual(flatten_list(nested), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()