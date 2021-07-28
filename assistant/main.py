# import click

from app import create_app, db
from app.models import User
# from assistant.find import find as bfind


def build():
    app = create_app()
    with app.app_context():
        try:
            db.create_all()
        except:  # noqa
            pass

        if User.query.filter_by(username='john').first() is None:
            User.register('john', 'cat')
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
