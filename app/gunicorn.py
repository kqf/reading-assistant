from app import db
from app.models import User


preload_app = True


def on_starting(server):
    app = server.app.callable
    with app.app_context():
        db.create_all()
        if User.query.filter_by(username='john').first() is None:
            User.register('john', 'cat')
