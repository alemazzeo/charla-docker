import pathlib

import click

import example.text_operations as to


@click.group()
def cli():
    pass


@cli.command()
@click.argument(
    "file",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        path_type=pathlib.Path,
    ),
)
@click.option(
    "-n", type=int, default=10, show_default=True, help="Number of printed words"
)
def count_words(file: pathlib.Path, n: int):
    """Prints the n most frequent words in a text file"""

    with open(file, mode="r") as f:
        text = f.read()
    words = to.count_words(text)

    for word, count in sorted(words.items(), key=lambda x: x[1], reverse=True)[0:n]:
        print(f"{word:20s}: {count:02d}")


if __name__ == "__main__":
    cli()
