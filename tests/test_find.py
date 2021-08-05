import os
import pytest
import tempfile
from assistant.find import find


@pytest.fixture
def dictionary():
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write("day\nplay\nboy\nno\nwork")
    yield f.name
    os.unlink(f.name)


@pytest.fixture
def text():
    return "All work and no play makes Jack a dull boy"


# @pytest.mark.skip("TODO: fix the spacy version mismatch later")
@pytest.mark.parametrize("only_nouns, expected", [
    (True, ['Jack']),
    (False, ['Jack', 'make', 'Jack', 'dull']),
])
def test_assistant(text, dictionary, only_nouns, expected):
    res = find(text, dictionary, only_nouns=only_nouns)
    assert set(res) == set(expected)
