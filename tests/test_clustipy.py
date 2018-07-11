from pathlib import Path
import csv

from unittest import TestCase
import netaddr

from clustipy import clustipy


class TestClustipy(TestCase):
    def setUp(self):
        self.networks = []
        with Path('tests/test_address.csv').open() as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                self.networks.append(netaddr.IPNetwork(row[0].split('/')[0]))

    def test_main(self):
        result = clustipy.clustering(self.networks, 25)
        self.assertEqual(len(result), 25)
        for n in self.networks:
            self.assertIn(True, [n in c for c in result])
