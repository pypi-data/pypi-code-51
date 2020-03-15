# -*- coding: utf-8 -*-

"""Converter for HGNC."""

import json
import logging
from typing import Iterable

from tqdm import tqdm

from ..path_utils import ensure_path
from ..struct import Obo, Reference, Synonym, SynonymTypeDef, Term, from_species

logger = logging.getLogger(__name__)

PREFIX = 'hgnc'
DEFINITIONS_URL = 'ftp://ftp.ebi.ac.uk/pub/databases/genenames/new/json/hgnc_complete_set.json'

previous_symbol_type = SynonymTypeDef(id='previous_symbol', name='previous symbol')
alias_symbol_type = SynonymTypeDef(id='alias_symbol', name='alias symbol')
previous_name_type = SynonymTypeDef(id='previous_name', name='previous name')
alias_name_type = SynonymTypeDef(id='alias_name', name='alias name')

gene_xrefs = [
    ('ensembl', 'ensembl_gene_id'),
    ('ncbigene', 'entrez_id'),
    ('cosmic', 'cosmic'),
    ('vega', 'vega_id'),
    ('ucsc', 'ucsc_id'),
    ('merops', 'merops'),
    ('lncipedia', 'lncipedia'),
    ('orphanet', 'orphanet'),
    ('pseudogene', 'pseudogene.org'),
    ('ena', 'ena'),
    ('refseq', 'refseq_accession'),
    ('mgi', 'mgd_id'),
    ('ccds', 'ccds_id'),
    ('rgd', 'rgd_id'),
    ('omim', 'omim_id'),
    ('uniprot', 'uniprot_ids'),
    ('ec-code', 'enzyme_id'),
    ('rnacentral', 'rna_central_id'),
    ('mirbase', 'mirbase'),
    ('snornabase', 'snornabase'),
]


def get_obo() -> Obo:
    """Get HGNC as OBO."""
    terms = list(get_terms())
    return Obo(
        ontology=PREFIX,
        name='HGNC',
        terms=terms,
        typedefs=[from_species],
        synonym_typedefs=[previous_name_type, previous_symbol_type, alias_name_type, alias_symbol_type],
        auto_generated_by='bio2obo:hgnc',
    )


def get_terms() -> Iterable[Term]:
    """Get HGNC terms."""
    unhandled = set()
    path = ensure_path(PREFIX, DEFINITIONS_URL)
    with open(path) as file:
        entries = json.load(file)['response']['docs']

    for entry in tqdm(entries, desc=f'Mapping {PREFIX}'):
        name, symbol, identifier = entry.pop('name'), entry.pop('symbol'), entry.pop('hgnc_id')[len('HGNC:'):]

        xrefs = []
        for xref_prefix, key in gene_xrefs:
            xref_identifiers = entry.pop(key, None)
            if xref_identifiers is None:
                continue
            if not isinstance(xref_identifiers, list):
                xref_identifiers = [xref_identifiers]
            for xref_identifier in xref_identifiers:
                xrefs.append(Reference(prefix=xref_prefix, identifier=str(xref_identifier)))

        provenance = [
            Reference(prefix='pubmed', identifier=str(pubmed_id))
            for pubmed_id in entry.pop('pubmed_id', [])
        ]

        gene_group_ids = entry.pop('gene_group_id', [])
        gene_groups = entry.pop('gene_group', [])
        parents = [
            Reference(
                prefix='hgnc.genefamily',
                identifier=str(hgncgenefamily_id),
                name=gene_group_label,
            )
            for hgncgenefamily_id, gene_group_label in zip(gene_group_ids, gene_groups)
        ]

        synonyms = []
        for alias_symbol in entry.pop('alias_symbol', []):
            synonyms.append(Synonym(name=alias_symbol, type=alias_symbol_type))
        for alias_name in entry.pop('alias_name', []):
            synonyms.append(Synonym(name=alias_name, type=alias_name_type))
        for previous_symbol in entry.pop('previous_symbol', []):
            synonyms.append(Synonym(name=previous_symbol, type=previous_symbol_type))
        for previous_name in entry.pop('prev_name', []):
            synonyms.append(Synonym(name=previous_name, type=previous_name_type))

        term = Term(
            name=symbol,
            definition=name,
            reference=Reference(prefix=PREFIX, identifier=identifier),
            xrefs=xrefs,
            provenance=provenance,
            parents=parents,
            synonyms=synonyms,
        )
        term.append_relationship(from_species, Reference(prefix='taxonomy', identifier='9606', name='Homo sapiens'))

        unhandled.update(set(entry))
        yield term

    # logger.warning('Unhandled:')
    # for u in sorted(unhandled):
    #     logger.warning(u)


if __name__ == '__main__':
    get_obo().write_default()
