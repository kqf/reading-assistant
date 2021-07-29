# import click

from app import create_app
# from assistant.find import find as bfind


def build():
    app = create_app()
    return app


# @click.group()
# def cli():
#     pass


# @cli.command()
# @click.option("--infile", type=str, default="text.txt")
# @click.option("--dictionary", type=str, default="google-10000-english.txt")
# def find(infile, dictionary):
#     bfind(infile, dictionary)


def main():
    app = build()
    app.run()


if __name__ == '__main__':
    main()
