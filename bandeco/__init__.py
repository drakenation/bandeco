"""Entry point for the CLI."""
from .bandeco import run
from .bandeco import run_and_print


def main():
    """Entry point for the CLI."""
    exit(run_and_print())
