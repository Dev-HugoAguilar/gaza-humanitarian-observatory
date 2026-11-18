# Datos: fuentes, unidades, cortes y exclusiones

## Fuentes

| Fuente | Contenido | Corte |
|---|---|---|
| Tech for Palestine | 1 131 reportes diarios de Gaza, 1 131 de Cisjordania, 730 registros de infraestructura y 263 de prensa | 10 de noviembre de 2026 |
| Lista identificada de fallecidos | 72 835 registros con nombre y edad declarada | 7 de mayo de 2026 |
| OMS (EMRO) | Estimación de necesidades de rehabilitación por politrauma, con rangos de escenario | mayo de 2026 |

## Exclusiones de este repositorio

- **Lista nominal de fallecidos**: no se publica. Son datos personales de
  personas fallecidas (nombre y edad). El repositorio incluye el código que la
  procesa y no el registro.
- No se publican archivos con una fila por persona de ningún tipo.
- No se publican exportaciones crudas de las fuentes; solo agregados.

Ambas reglas se verifican en `tests/test_datos.py`, que falla si aparece un
archivo con esas características.

## Unidades que la interfaz respeta

- **Reporte diario**: publicación de una fuente para un periodo declarado; no
  equivale a 24 horas ni a las muertes ocurridas ese día.
- **Celda territorial**: agregado de daño sobre una rejilla; no es un edificio.
- **Rango de escenario (OMS)**: escenario de necesidades, no intervalo de
  confianza.
- **Personas identificadas**: solo cuentan las que la lista nombra; las personas
  no identificadas no se estiman ni se imputan.

## Reglas de lectura

- La ausencia de reporte se marca como falta de reporte utilizable, **nunca como
  cero**.
- Las categorías de lesiones pueden solaparse y no se suman entre sí.
- Los cortes con distinto nivel de detalle no se enlazan como una serie continua.
- Las prótesis colocadas no son personas.

## Límites

- La lista es incompleta y su corte (7 de mayo de 2026) no coincide con el
  acumulado diario (10 de noviembre de 2026): la diferencia incluye personas no
  identificadas.
- Los agregados describen lo reportado por las fuentes, con sus huecos.
- El observatorio no atribuye responsabilidad ni establece causalidad.

## Atribución

Cada sección cita su fuente y su corte. Este repositorio no incluye un archivo
`LICENSE` propio: se respetan las condiciones de cada fuente citada.
