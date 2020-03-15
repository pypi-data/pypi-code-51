# -*- coding: utf-8 -*-

"""Converter for CGNC."""

from typing import Iterable

import pandas as pd

from ..path_utils import ensure_path
from ..struct import Obo, Reference, Synonym, Term, from_species

PREFIX = 'cgnc'
URL = "http://birdgenenames.org/cgnc/downloads.jsp?file=standard"


def get_obo() -> Obo:
    """Get CGNC as OBO."""
    terms = list(get_terms())
    return Obo(
        terms=terms,
        name='CGNC',
        ontology=PREFIX,
    )


def get_terms() -> Iterable[Term]:
    """Get CGNC terms."""
    path = ensure_path(PREFIX, URL, path=f'{PREFIX}.tsv')
    df = pd.read_csv(path, sep='\t', dtype={'Entrez Gene id': str, 'CGNC id': str})

    for cgnc_id, entrez_id, ensembl_id, symbol, name, synonyms, status, _ in df.values:
        xrefs = []
        if entrez_id and pd.notna(entrez_id):
            xrefs.append(Reference(prefix='ncbigene', identifier=entrez_id))
        if ensembl_id and pd.notna(ensembl_id):
            xrefs.append(Reference(prefix='ensembl', identifier=ensembl_id))

        if synonyms and pd.notna(synonyms):
            synonyms = [
                Synonym(name=synonym)
                for synonym in synonyms.split('|')
            ]
        else:
            synonyms = []

        term = Term(
            name=symbol,
            reference=Reference(prefix=PREFIX, identifier=cgnc_id),
            xrefs=xrefs,
            synonyms=synonyms,
            definition=name,
        )
        term.append_relationship(from_species, Reference(
            prefix='taxonomy', identifier='9031', name='Gallus gallus',
        ))
        yield term


if __name__ == '__main__':
    get_obo().write_default()
