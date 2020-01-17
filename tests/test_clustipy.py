from pathlib import Path

from unittest import TestCase
from netaddr import IPAddress

import ClustIPy


class TestClustIPy(TestCase):
    def setUp(self):
        self.ipaddr = [IPAddress(_) for _ in Path('tests/test_address').read_text().splitlines()]

    def test_agglomerative(self):
        result = ClustIPy.agglomerative(self.ipaddr, 20)
        self.assertLessEqual(len(result), 20)
        for a in self.ipaddr:
            self.assertGreater(len([_ for _ in result if a in _]), 0)

    def test_kmeans(self):
        result = ClustIPy.kmeans(self.ipaddr, 20)
        self.assertLessEqual(len(result), 20)
        for a in self.ipaddr:
            self.assertGreater(len([_ for _ in result if a in _]), 0)
