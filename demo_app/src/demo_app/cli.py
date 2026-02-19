"""CLI application using Click."""

import click
from demo_app import hello, process_data


@click.group()
def main():
    """Demo CLI application with multiple commands."""
    pass


@main.command()
def greet():
    """Display a simple greeting."""
    message = hello()
    click.echo(message)


@main.command()
@click.argument("text")
def process(text):
    """Process text through multiple transformation steps."""
    result = process_data(text)
    click.echo(result)


@main.command()
@click.option("--name", default="World", help="Name to greet.")
@click.option("--count", default=1, help="Number of greetings.")
def hello_complex(name, count):
    """Say hello with custom name and repetition count."""
    for i in range(count):
        message = generate_greeting(name, i + 1)
        click.echo(message)


def generate_greeting(name: str, iteration: int) -> str:
    """Generate a greeting message."""
    return format_greeting(name, iteration)


def format_greeting(name: str, iteration: int) -> str:
    """Format the greeting with iteration number."""
    greeting = build_greeting_text(name)
    return f"[{iteration}] {greeting}"


def build_greeting_text(name: str) -> str:
    """Build the greeting text."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    main()
