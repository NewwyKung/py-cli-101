import click
from InquirerPy import inquirer

@click.group()
def cli():
    """Project Management CLI Tool"""
    pass

@cli.command()
def init():
    """Initializes a new project interactively."""
    click.echo("Starting new project setup...")
    
    # Click จัดการคำสั่ง 'init' แล้ว
    
    # InquirerPy เข้ามาจัดการการโต้ตอบกับผู้ใช้
    name = inquirer.text(message="What is the project name?").execute()
    
    language = inquirer.select(
        message="Select main language:",
        choices=["Python", "Go", "Node.js"]
    ).execute()
    
    click.echo(f"Initializing project '{name}' with {language}...")
    # โค้ดที่เหลือสำหรับสร้างไฟล์ ...
    
if __name__ == '__main__':
    cli()