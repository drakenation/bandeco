"""Entry point for the CLI."""
from .bandeco import run
from .bandeco import run_and_print
from .utils import write_error


def main():
    """Entry point for the CLI."""
    try:
        run_and_print()
        exit(0)
    except ValueError as exception:
        write_error(exception)
        exit(1)
