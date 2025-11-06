import click

@click.group()
def cli():
    """Greeting CLI Tool"""
    pass

@click.group()
def say():
    pass

@say.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(name):
    """Says hello to the user."""
    click.echo(f"Hello, {name}!")

@say.command()
@click.option('--name', prompt='Your name', help='The person to bid farewell.')
def goodbye(name):
    """Says goodbye to the user."""
    click.echo(f"Goodbye, {name}!")

cli.add_command(say)

if __name__ == '__main__':
    cli()