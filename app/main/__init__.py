from flask import Blueprint

main = Blueprint('main', __name__)

# TODO: Fix the relative imports
from . import routes  # noqa
