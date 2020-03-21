import click
import spacy
from multimethod import multimethod


class Vocabulary:
    def __init__(self, filename):
        with open(filename) as f:
            self.dict = set(f.read().splitlines())

    @multimethod
    def __call__(self, span):
        return any(self(token) for token in span if token.lemma_ != "-PRON-")

    @__call__.register(object, spacy.tokens.Token)
    def _(self, token):
        return token.lemma_ not in self.dict


def valid(token):
    return token.is_alpha and not token.is_stop


def find(infile, dictionary):
    nlp = spacy.load("en_core_web_sm")
    with open(infile) as f:
        doc = nlp(f.read())

    is_oov = Vocabulary(dictionary)
    spacy.tokens.Span.set_extension("oov", getter=is_oov)
    spacy.tokens.Token.set_extension("oov", getter=is_oov)

    print("Noun phrases:")
    print(list(set([span.text for span in doc.noun_chunks if span._.oov])))

    print("Tokens:")
    print(list([t.lemma_ for t in doc if t._.oov and valid(t)]))


@click.command()
@click.option("--infile", type=str, default="text.txt")
@click.option("--dictionary", type=str, default="google-10000-english.txt")
def main(infile, dictionary):
    find(infile, dictionary)


if __name__ == '__main__':
    main()
#
