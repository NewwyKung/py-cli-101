import click
from InquirerPy import inquirer

@click.group()
def cli():
    pass

@cli.command()
def calculator():
    """Simple Calculator"""
    while True:
        operation = inquirer.select(
            message="Choose an operation:",
            choices=["Add", "Subtract", "Multiply", "Divide", "Exit"],
        ).execute()

        if operation == "Exit":
            break

        num1 = int(inquirer.number("Enter the first number:").execute())
        num2 = int(inquirer.number("Enter the second number:").execute())

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2

        click.echo(f"The result is: {result}")

if __name__ == '__main__':
    cli()