from pkg import UNION_DATA, __version__, pep_0584_update


def test_version():
    assert __version__ == "0.1.0"


def test_pep_0584_update():
    INITIAL_DATA = {"data": 0}
    assert pep_0584_update(INITIAL_DATA) == {**INITIAL_DATA, **UNION_DATA}
