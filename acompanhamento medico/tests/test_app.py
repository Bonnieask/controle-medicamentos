import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import adicionar_medicamento, listar_medicamentos


def test_adicionar_medicamento():
    adicionar_medicamento("Dipirona", "08:00")
    meds = listar_medicamentos()
    assert any(m["nome"] == "Dipirona" for m in meds)


def test_erro_dados_vazios():
    import pytest
    with pytest.raises(ValueError):
        adicionar_medicamento("", "")


def test_listagem():
    meds = listar_medicamentos()
    assert isinstance(meds, list)
