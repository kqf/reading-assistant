import os
import pytest
import tempfile
from assistant.main import find


@pytest.fixture
def dictionary():
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write("day\nplay\nboy\nno\nwork")
    yield f.name
    os.unlink(f.name)


@pytest.fixture
def text():
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write("All work and no play makes Jack a dull boy")
    yield f.name
    os.unlink(f.name)


def test_assistant(text, dictionary):
    find(text, dictionary)
