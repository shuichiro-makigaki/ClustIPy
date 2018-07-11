from pathlib import Path
import csv

import netaddr
import click

from clustipy import clustipy


@click.command()
@click.option('--incsv', help='Input CSV', required=True, type=click.Path())
@click.option('--nclusters', help='Number of clusters', required=True, type=int)
@click.option('--nocsvheader', help='Do not ignore the first line of CSV', is_flag=True, default=False)
@click.option('--nfield', help='Column number', type=int, default=0)
def main(incsv, nclusters, nocsvheader, nfield):
    networks = []
    with Path(incsv).open() as f:
        reader = csv.reader(f)
        if not nocsvheader:
            next(reader)
        for row in reader:
            networks.append(netaddr.IPNetwork(row[nfield]))
    result = clustipy.clustering(networks, nclusters)
    for r in result:
        print(r)


if __name__ == '__main__':
    main()
