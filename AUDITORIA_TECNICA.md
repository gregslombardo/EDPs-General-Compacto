# Auditoría técnica final

Fecha de referencia: 23 de julio de 2026.

## Resultado

- 52/52 archivos `.ipynb` son notebooks JSON válidos.
- La ruta activa contiene 54 ejercicios: como máximo dos normales por
  notebook y sólo 8 variaciones de nivel General.
- El validador termina con 0 errores y 0 advertencias.
- No quedan referencias locales rotas.
- No quedan notebooks exactamente duplicados sin identificar como legados.
- Se repararon los dos archivos que no eran notebooks y la celda accidental
  cuyo único contenido era `as`.
- Se retiraron 87 ejercicios redundantes sólo de primer orden, onda y calor;
  la práctica elíptica se redujo por separado y se organizó mediante notebooks
  canónicos.
- Los videos finales demasiado breves se regeneraron y verificaron
  visualmente.

## Reparaciones estructurales

1. `LINEALES/2.5.1_Soluciones_debiles_y_Rankine_Hugoniot.ipynb` ahora contiene
   teoría matemática, interpretación geométrica, dos ejercicios y una
   variación General.
2. `ONDA/00_Indice_y_continuacion_automatica (1).ipynb` es ahora un índice
   navegable.
3. Los notebooks `02_04`, `02_05`, `02_08`, `02_10` y `02_11` de onda fueron
   reconstruidos para que el nombre coincida con Duhamel, reflexión, energía,
   Poisson/Hadamard y Duhamel multidimensional, respectivamente.
4. Las copias elípticas y la copia de calor se marcaron como archivos legados;
   las rutas canónicas están documentadas.
5. Las imágenes fuente ausentes se sustituyeron por notas explícitas que
   conservan la descripción y la referencia original, sin fabricar capturas.

## Videos corregidos

| Video | Antes | Después | Cronología |
|---|---:|---:|---|
| `animaciones/03.1.B_membrana_relajacion.mp4` | 0.95 s | 15.0 s | 4 s inicial + 8 s relajación + 3 s equilibrio |
| `lAPLACE/animaciones/03.3.A_principio_debil_maximo.mp4` | 1.48 s | 15.0 s | 4 s frontera + 8 s relajación + 3 s estado armónico |
| `ONDA/animaciones/02_01_dAlembert_2K_120fps.mp4` | 1.50 s | 15.0 s | 4 s perfil inicial + 8 s propagación + 3 s perfil final |

Los fotogramas de inicio, mitad y cierre se inspeccionaron mediante hojas de
contacto. Los títulos, ejes, leyendas y cartelas permanecen dentro del cuadro
y no se empalman. El código de la propiedad del promedio también se ajustó
para evitar títulos recortados y conservar una cartela inicial legible.

## Cobertura y selección

Se comparó la colección con el temario oficial y con los exámenes 2023-1,
2023-2, 2025-1, 2025-2 y 2026-1. Los cinco exámenes muestrean los cuatro
bloques: primer orden, onda, elípticas y calor. La selección final conserva
problemas General sólo en los núcleos que reaparecen históricamente:
características/conservación, d'Alembert-Huygens, Green-máximo-Dirichlet y
máximo-Duhamel-frontera para calor.

La correspondencia detallada está en `MATRIZ_COBERTURA_TEMARIO.md` y la ruta
de uso está en `PLAN_ESTUDIO_GENERAL.md`.

## Reproducibilidad

```powershell
python herramientas/validar_material_general.py
python herramientas/regenerar_animaciones_cortas.py
```

El primer comando comprueba notebooks, práctica, duplicados y recursos. El
segundo vuelve a producir los tres MP4 auditados con su cronología didáctica.
Los cachés nuevos de Manim, `__pycache__` y archivos parciales están excluidos
mediante `.gitignore`.
