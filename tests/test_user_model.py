import pytest
from app import create_app, db
from app.models import User


@pytest.fixture
def app():
    app = create_app()
    app_ctx = app.app_context()
    app_ctx.push()
    db.create_all()
    yield app
    db.drop_all()
    app_ctx.pop()


def test_password(app):
    u = User(username='john')
    u.set_password('cat')
    assert u.verify_password('cat')
    assert not u.verify_password('dog')


def test_registration(app):
    User.register('john', 'cat')
    u = User.query.filter_by(username='john').first()
    assert u is not None
    assert u.verify_password('cat')
    assert not u.verify_password('dog')
