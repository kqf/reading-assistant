import click

from app import create_app, db
from app.models import User
from assistant.find import find as bfind


@click.group()
def main():
    pass


@main.command()
@click.option("--infile", type=str, default="text.txt")
@click.option("--dictionary", type=str, default="google-10000-english.txt")
def find(infile, dictionary):
    bfind(infile, dictionary)


@main.command()
def serve():
    app = create_app()
    with app.app_context():
        db.create_all()
        if User.query.filter_by(username='john').first() is None:
            User.register('john', 'cat')
    app.run()


if __name__ == '__main__':
    main()
