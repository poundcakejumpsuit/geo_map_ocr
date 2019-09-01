import click

from lib.parse_map import parse


@click.group()
def cli():
	pass

@cli.command()
@click.option('--file', help='absolute filepath of input pdf', required=True)
def process_map(file):
	parse(file)


if __name__ == '__main__':
	cli()
	
