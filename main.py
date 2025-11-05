import click

@click.command()
def interactive_tool():
    """An interactive tool for project setup."""
    
    # ถามคำถามและบังคับให้เลือกจากรายการ
    project_type = click.prompt(
        'Select Project Type',
        type=click.Choice(['Web', 'Mobile', 'Data']),
        default='Web'
    )
    
    click.echo(f"Setting up a {project_type} project.")

if __name__ == '__main__':
    interactive_tool()