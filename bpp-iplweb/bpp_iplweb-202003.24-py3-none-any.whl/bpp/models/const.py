from collections import OrderedDict
from enum import Enum

TO_AUTOR = 0
TO_REDAKTOR = 1
TO_INNY = 2
TO_TLUMACZ = 3
TO_KOMENTATOR = 4
TO_RECENZENT = 5
TO_OPRACOWAL = 6

GR_WPROWADZANIE_DANYCH = 'wprowadzanie danych'

CHARAKTER_SLOTY_KSIAZKA = 1
CHARAKTER_SLOTY_ROZDZIAL = 2

RODZAJ_PBN_ARTYKUL = 1
RODZAJ_PBN_ROZDZIAL = 2
RODZAJ_PBN_KSIAZKA = 3


class DZIEDZINA(Enum):
    NAUKI_HUMANISTYCZNE = 1
    NAUKI_INZ_TECH = 2
    NAUKI_MEDYCZNE = 3
    NAUKI_ROLNICZE = 4
    NAUKI_SPOLECZNE = 5
    NAUKI_SCISLE = 6
    NAUKI_TEOLOGICZNE = 7
    NAUKI_SZTUKA = 8


WYZSZA_PUNKTACJA = [DZIEDZINA.NAUKI_SPOLECZNE,
                    DZIEDZINA.NAUKI_HUMANISTYCZNE,
                    DZIEDZINA.NAUKI_TEOLOGICZNE]

DZIEDZINY = OrderedDict()
DZIEDZINY[DZIEDZINA.NAUKI_HUMANISTYCZNE] = "Nauki humanistyczne"
DZIEDZINY[DZIEDZINA.NAUKI_INZ_TECH] = "Nauki inżynieryjno-techniczne"
DZIEDZINY[DZIEDZINA.NAUKI_MEDYCZNE] = "Nauki medyczne i o zdrowiu"
DZIEDZINY[DZIEDZINA.NAUKI_ROLNICZE] = "Nauki rolnicze"
DZIEDZINY[DZIEDZINA.NAUKI_SPOLECZNE] = "Nauki społeczne"
DZIEDZINY[DZIEDZINA.NAUKI_SCISLE] = "Nauki ścisłe i przyrodnicze"
DZIEDZINY[DZIEDZINA.NAUKI_TEOLOGICZNE] = "Nauki teologiczne"
DZIEDZINY[DZIEDZINA.NAUKI_SZTUKA] = "Sztuka"


class TRYB_KALKULACJI(Enum):
    AUTORSTWO_MONOGRAFII = 1
    REDAKCJA_MONOGRAFI = 2
    ROZDZIAL_W_MONOGRAFI = 3
