# Auditoría técnica de la ruta compacta

Fecha de referencia: 23 de julio de 2026.

## Resultado de la reestructuración

- Se creó [`GENERAL/`](GENERAL/README.md) como única ruta activa.
- Hay **26 notebooks canónicos**, uno por subsección.
- La práctica activa contiene **52 ejercicios normales** y **8 problemas
  tipo General**.
- Cada notebook tiene exactamente dos ejercicios normales y como máximo un
  problema General.
- Las carpetas originales se conservan como biblioteca extendida para no
  romper animaciones, referencias ni material de consulta.

La cuenta anterior basada en encabezados de celdas no representaba todos los
incisos enumerados dentro de notebooks extensos. El nuevo validador cuenta
cada encabezado individual de la ruta canónica y deja fuera de la carga
obligatoria toda la biblioteca histórica.

## Correspondencia con el General

Se revisaron el temario y los exámenes 2023-1, 2023-2, 2025-1, 2025-2 y
2026-1. Los ocho problemas tipo General se concentran en los patrones más
recurrentes:

- cuasilineales/ruptura y Riemann–Burgers–LWR;
- d'Alembert/soporte y Huygens/Hadamard;
- máximo/unicidad y Dirichlet/Perron;
- núcleo del calor/asintótica y problemas de frontera.

Los demás temas siguen cubiertos mediante teoría, interpretación, ejemplo y
dos ejercicios normales.

## Visualizaciones

Las animaciones existentes siguen en sus carpetas originales y los notebooks
canónicos las enlazan mediante rutas relativas. El estándar didáctico es:
4 segundos para el estado inicial, 25–75 segundos de duración conceptual,
leyendas legibles, capas sin superposición y 3 segundos para el cierre.

Los videos previamente corregidos incluyen:

| Video | Duración verificada |
|---|---:|
| `animaciones/03.1.B_membrana_relajacion.mp4` | 15.0 s |
| `lAPLACE/animaciones/03.3.A_principio_debil_maximo.mp4` | 15.0 s |
| `ONDA/animaciones/02_01_dAlembert_2K_120fps.mp4` | 15.0 s |

## Reproducibilidad

```powershell
python herramientas/construir_ruta_canonica.py
python herramientas/validar_material_general.py
python herramientas/regenerar_animaciones_cortas.py
```

El primer comando reconstruye la ruta compacta; el segundo comprueba conteos,
títulos, metadatos, recursos y salud estructural de todos los notebooks; el
tercero regenera las animaciones cuya duración fue corregida.
