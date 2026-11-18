"""Contrato de datos del observatorio y guarda de no redistribución.

El repositorio publica agregados. Estas pruebas fijan las invariantes que la
documentación declara y **fallan si se versiona la lista nominal** o cualquier
archivo con registros por persona.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parents[1]
APP = RAIZ / "app" / "index.html"
SOURCE = RAIZ / "source"

#: Claves que indicarían un registro por persona.
CLAVES_PERSONALES = {"nombre", "nombres", "apellido", "apellidos", "nombre_completo"}


def json_de(rel: str) -> dict:
    return json.loads((RAIZ / rel).read_text(encoding="utf-8"))


def test_el_tablero_publicado_existe() -> None:
    assert APP.exists(), "falta app/index.html"
    assert APP.stat().st_size > 1_000_000, "el tablero publicable está incompleto"


def test_no_se_publica_la_lista_nominal() -> None:
    for archivo in RAIZ.rglob("*"):
        if ".git" in archivo.parts or not archivo.is_file():
            continue
        assert archivo.name != "personas.json", f"lista nominal versionada: {archivo}"
        assert archivo.suffix not in {".csv", ".xls", ".xlsx"}, f"registro crudo: {archivo}"


def test_ningun_json_tiene_registros_por_persona() -> None:
    for archivo in SOURCE.rglob("*.json"):
        datos = json.loads(archivo.read_text(encoding="utf-8"))
        candidatos = []
        if isinstance(datos, list):
            candidatos = datos[:5]
        elif isinstance(datos, dict):
            for valor in datos.values():
                if isinstance(valor, list) and valor and isinstance(valor[0], dict):
                    candidatos = valor[:5]
                    break
        for fila in candidatos:
            if not isinstance(fila, dict):
                continue
            intrusas = CLAVES_PERSONALES & {str(k).lower() for k in fila}
            assert not intrusas, f"{archivo.name} expone claves personales: {intrusas}"


@pytest.mark.parametrize(
    "ruta,clave",
    [
        ("source/expansion/observatorio.json", "daily"),
        ("source/pronostico/datos.json", "deaths"),
        ("source/redesign/datos.json", "grid"),
        ("source/visual.json", "report"),
    ],
)
def test_agregados_conservan_su_bloque(ruta: str, clave: str) -> None:
    datos = json_de(ruta)
    assert clave in datos, f"{ruta} perdió el bloque «{clave}»"


def test_los_agregados_son_serializables() -> None:
    for archivo in SOURCE.rglob("*.json"):
        datos = json.loads(archivo.read_text(encoding="utf-8"))
        assert json.dumps(datos, ensure_ascii=False)
