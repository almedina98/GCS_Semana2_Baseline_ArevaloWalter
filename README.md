# Sistema Básico de Inventario

## Objetivo
Implementar un repositorio estructurado como depósito de elementos de configuración y establecer una línea base denominada Baseline v1.0, utilizando Git para mantener trazabilidad, reproducibilidad y control de cambios.

## Estructura
- `docs/SRS/`: especificación de requisitos.
- `docs/SDD/`: diseño del software.
- `src/`: código fuente.
- `tests/`: pruebas.
- `config/`: configuración de ejemplo.
- `scripts/`: scripts auxiliares.
- `CHANGELOG.md`: historial de cambios.

## Ejecución
Requiere Python 3.

```bash
python src/inventario.py
```

Prueba básica:

```bash
python tests/test_inventario.py
```

## Creación de la baseline
Cuando SRS_v1, SDD_v1, código, configuración y prueba estén revisados:

```bash
git tag -a v1.0 -m "Baseline v1.0: SRS+SDD approved + minimal build"
git push origin v1.0
```

## Control de cambios
Los cambios posteriores a la línea base deben realizarse en una rama independiente, por ejemplo `change/REQ-007`, para conservar el estado histórico identificado por `v1.0`.
