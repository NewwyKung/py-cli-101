import click
import os
from InquirerPy import inquirer

@click.group()
def cli():
    pass

directory = './Project/File Manager/files/'

@cli.command()
def file():
    """File Manager"""
    action = inquirer.select(
        message="Choose an action:",
        choices=["List Files", "Open", "Create File", "Delete File", "Rename File", "Exit"],
    ).execute()

    if action == "Exit":
        return
    
    if action == "List Files":
        files = os.listdir(directory)
        click.echo("Files in directory:")
        for f in files:
            click.echo(f"- {f}")
    elif action == "Create File":
        filename = inquirer.text("Enter the filename to create:").execute()
        with open(os.path.join(directory, filename), 'w') as f:
            f.write("")  # Create an empty file
        click.echo(f"File '{filename}' created.")
    elif action == "Delete File":
        filename = inquirer.select(
            message="Select a file to delete:",
            choices=os.listdir(directory)
        ).execute()
        try:
            os.remove(os.path.join(directory, filename))
            click.echo(f"File '{filename}' deleted.")
        except FileNotFoundError:
            click.echo(f"File '{filename}' not found.")
    elif action == "Rename File":
        old_name = inquirer.select(
            message="Select a file to delete:",
            choices=os.listdir(directory)
        ).execute()
        new_name = inquirer.text("Enter the new filename:").execute()
        try:
            os.rename(os.path.join(directory, old_name), os.path.join(directory, new_name))
            click.echo(f"File '{old_name}' renamed to '{new_name}'.")
        except FileNotFoundError:
            click.echo(f"File '{old_name}' not found.")
    elif action == "Open":
        filename = inquirer.select(
            message="Select a file to open:",
            choices=os.listdir(directory)
        ).execute()
        try:
            os.startfile(os.path.join(directory, filename))
        except FileNotFoundError:
            click.echo(f"File '{filename}' not found.")

if __name__ == '__main__':
    cli()