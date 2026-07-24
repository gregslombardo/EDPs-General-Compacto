# Preparación para el Examen General de EDP

Ruta compacta, alineada con el temario oficial y con los exámenes generales
de 2023-1, 2023-2, 2025-1, 2025-2 y 2026-1.

## Empieza aquí

Para preparar el General estudia únicamente [`GENERAL/`](GENERAL/README.md).
Esa carpeta contiene la colección canónica:

- **26 notebooks**: uno por subsección del temario;
- **52 ejercicios normales**: exactamente dos por notebook;
- **8 problemas tipo General**: sólo en núcleos de alta recurrencia;
- teoría esencial, ejemplo guiado e interpretación geométrica o física.

Las carpetas [`LINEALES/`](LINEALES/), [`ONDA/`](ONDA/),
[`lAPLACE/`](lAPLACE/) y [`calor/`](calor/) se conservan como biblioteca
extendida y fuente de animaciones. No forman parte de la cuenta de práctica
obligatoria.

## Orden recomendado

1. Sigue el [índice de la ruta canónica](GENERAL/README.md).
2. Memoriza y reconstruye el
   [formulario de fórmulas principales](FORMULARIO_MEMORIZACION.md).
3. Lee el [plan de estudio](PLAN_ESTUDIO_GENERAL.md).
4. Usa la [matriz de cobertura](MATRIZ_COBERTURA_TEMARIO.md) para comprobar
   la correspondencia con el temario.
5. Resuelve los 52 ejercicios normales.
6. En una segunda vuelta, resuelve los 8 problemas tipo General.

## Validación reproducible

```powershell
python herramientas/validar_material_general.py
```

El verificador distingue la ruta canónica de la biblioteca extendida y exige
exactamente 26 notebooks, dos ejercicios normales por subsección y no más de
un problema General por notebook. También revisa JSON, metadatos, títulos,
salidas de error y recursos locales.

La estructura canónica se puede reconstruir de forma determinista con:

```powershell
python herramientas/construir_ruta_canonica.py
```

Consulta la [auditoría técnica](AUDITORIA_TECNICA.md) para el alcance y los
criterios de animación.
