# Preparación para el Examen General de EDP

Colección de notebooks para estudiar el temario oficial del Examen General de
Ecuaciones Diferenciales Parciales.

## Cómo usar este repositorio

1. Empieza por [el plan de estudio](PLAN_ESTUDIO_GENERAL.md).
2. Consulta la [matriz de cobertura](MATRIZ_COBERTURA_TEMARIO.md).
3. Estudia los notebooks canónicos de cada bloque.
4. Resuelve primero los ejercicios normales.
5. Deja los problemas **GENERAL - VARIACIÓN** para la segunda vuelta.

## Bloques

- [`LINEALES/`](LINEALES/): transporte, características, conservación,
  entropía y problemas de Riemann.
- [`ONDA/`](ONDA/): d'Alembert, dependencia, fronteras, Duhamel, Huygens,
  descenso de Hadamard y energía.
- [`lAPLACE/`](lAPLACE/): Poisson-Laplace, funciones armónicas, máximo,
  Green, Dirichlet, Perron, energía y espectro.
- [`calor/`](calor/): núcleo, máximo, Duhamel, regularidad, problemas de
  frontera y series de Fourier.

## Validación

La colección incluye un verificador estructural:

```powershell
python herramientas/validar_material_general.py
```

El verificador revisa:

- que cada `.ipynb` sea JSON válido;
- que no se conserven salidas de error;
- que no haya celdas de código accidentales;
- que los recursos locales referenciados existan;
- que no se acumulen demasiados ejercicios;
- que no haya múltiples problemas de nivel general por notebook;
- que no existan duplicados exactos sin identificar.

Consulta también la [auditoría técnica](AUDITORIA_TECNICA.md).

Resultado de la auditoría del 23 de julio de 2026: **52/52 notebooks válidos,
54 ejercicios en la ruta activa, 8 de nivel General, 0 errores y 0
advertencias**.

## Animaciones

Las animaciones son material didáctico, no decoración. Deben mostrar el dato o
perfil inicial antes de evolucionar, mantener textos legibles, evitar
superposiciones y cerrar indicando qué propiedad matemática se observó.

Los archivos de caché de Manim no deben incluirse en Git. Sólo se conservan
fuentes y videos finales seleccionados.

Para regenerar las tres animaciones cuya duración fue corregida:

```powershell
python herramientas/regenerar_animaciones_cortas.py
```
