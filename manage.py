import logging

import click

from lib.parse_map import parse


@click.group()
def cli():
	pass

@cli.command()
@click.option('--file', help='absolute filepath of input pdf', required=True)
def process_map(file):
	try:
		parse(file)
	except OSError:
		logging.error(f'{file} did not parse, may contain invalid data')


if __name__ == '__main__':
	cli()
	
