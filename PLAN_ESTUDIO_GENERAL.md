# Plan de estudio para el Examen General de EDP

Este documento organiza el repositorio según el temario oficial del Examen
General de Ecuaciones Diferenciales Parciales y los exámenes disponibles de
2023-1, 2023-2, 2025-1, 2025-2 y 2026-1.

## Criterio de selección

Los cinco exámenes revisados contienen problemas de los cuatro bloques
principales: primer orden, onda, elípticas y calor. Por ello no conviene omitir
ningún bloque completo. Sin embargo, tampoco conviene poner un problema de
nivel general en cada subsección.

Cada notebook canónico debe terminar, como máximo, con:

1. un ejercicio normal de cálculo o aplicación directa;
2. un ejercicio normal de demostración, interpretación o diagnóstico;
3. únicamente en temas de prioridad alta, un problema
   **GENERAL - VARIACIÓN** de 45 a 60 minutos.

Los problemas de nivel general son variaciones del tipo de razonamiento
observado en los exámenes, no copias literales.

## Prioridades observadas

| Bloque | Prioridad alta | Prioridad media | Prioridad de consulta |
|---|---|---|---|
| Primer orden | características y transversalidad; conservación, entropía, Riemann, Burgers/LWR | flujo característico, compatibilidad | jacobiano del flujo y desarrollos auxiliares |
| Onda | d'Alembert y soporte; intervalo y separación; Poisson/Huygens y ondas esféricas | reflexión, Duhamel, energía | identidades complementarias |
| Elípticas | solución fundamental/Green; máximo y unicidad; Dirichlet/Perron; espectro y resonancia | series en cuadrados, energía y principio de Dirichlet | estimaciones avanzadas y analiticidad |
| Calor | núcleo y comportamiento asintótico; máximo/comparación; Duhamel; problemas iniciales y de frontera | Fourier en intervalos, regularidad, energía | Tychonoff y Widder como temas avanzados |

## Patrones de los exámenes anteriores

### Primer orden

- 2023-1: características con datos sobre una curva y solución entrópica.
- 2023-2: características lineales con coeficientes variables.
- 2025-1: ecuación semilineal y explosión en tiempo finito.
- 2025-2: solución entrópica de Burgers.
- 2026-1: existencia/unicidad según transversalidad y modelo LWR.

### Onda

- 2023-1: fórmula de Poisson en dimensión dos y principio de Huygens.
- 2023-2: problema periódico y comparación entre dimensiones.
- 2025-1: separación de variables en un intervalo.
- 2025-2: reducción de una onda esférica tridimensional.
- 2026-1: d'Alembert, propagación finita y soporte.

### Elípticas

- 2023-1: unicidad exterior mediante el principio del máximo.
- 2023-2: Perron, función de Green y propiedades armónicas.
- 2025-1: soluciones fundamentales, Green, espectro y resonancia.
- 2025-2: unicidad con datos de Cauchy en una porción de la frontera.
- 2026-1: estimación a priori para Poisson-Dirichlet.

### Calor

- 2023-1: propagación del máximo en un dominio con obstáculos.
- 2023-2: asintótica del núcleo del calor.
- 2025-1: problema en el semieje y función error.
- 2025-2: problema no homogéneo con frontera variable.
- 2026-1: comparación para una ecuación semilineal con término de orden cero.

## Ruta corta sugerida

1. **Primera vuelta:** definiciones, fórmulas de representación, hipótesis y
   una interpretación geométrica o física por tema.
2. **Segunda vuelta:** los dos ejercicios normales de cada notebook canónico.
3. **Tercera vuelta:** sólo los problemas marcados
   **GENERAL - VARIACIÓN**.
4. **Simulacro:** elegir un problema de cada bloque y resolver los cuatro en
   cuatro horas, justificando hipótesis, dominio y unicidad.

## Estándar para visualizaciones y animaciones

- El dato, perfil o geometría inicial debe permanecer estático al menos
  **4 segundos** antes de comenzar la evolución.
- Una animación conceptual debe durar normalmente entre **25 y 75 segundos**.
  Las piezas de menos de 8 segundos se consideran incompletas.
- Cada fórmula o leyenda importante debe permanecer legible entre 2.5 y
  4 segundos.
- Antes de introducir una nueva capa conceptual se debe retirar o atenuar la
  anterior; no se deben acumular textos, ejes y fórmulas hasta empalmarlos.
- El último estado debe permanecer visible al menos 3 segundos.
- Para estudio basta 1080p30/60 o 1440p60. Se reserva 120 fps para movimientos
  que realmente lo necesiten.
- Toda animación debe cerrar con una lista breve de qué observar y qué
  afirmación matemática representa.

## Lista de control por notebook

- [ ] Coincide el título con el contenido real.
- [ ] Las hipótesis de cada teorema están completas.
- [ ] Se distingue transcripción, aclaración y resultado añadido.
- [ ] Hay una interpretación geométrica o física cuando aporta comprensión.
- [ ] Hay como máximo dos ejercicios normales.
- [ ] Sólo hay un problema general cuando el tema es prioritario.
- [ ] Las referencias locales existen.
- [ ] El notebook es JSON válido y no conserva errores de ejecución.
- [ ] El código de animación muestra primero los datos y evita superposiciones.
- [ ] Los archivos temporales de Manim no se versionan.
