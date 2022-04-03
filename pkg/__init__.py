import typing

__version__ = "0.1.0"

UNION_DATA = {"newaddition": 1}


def pep_0584_update(data: typing.Dict):
    return data | UNION_DATA
