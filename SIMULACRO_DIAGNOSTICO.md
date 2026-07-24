# Simulacro diagnóstico - 4 horas

Resuelve un problema por hoja. Justifica las hipótesis utilizadas y distingue
existencia, fórmula, regularidad y unicidad. Cada problema vale 25 puntos.

Los problemas son variaciones de los patrones de los exámenes 2023-2026; no
son copias de ellos.

## 1. Primer orden: características y pérdida de regularidad

Considera

\[
u_t+(1+u)u_x=0,\qquad x\in\mathbb R,\quad t>0,
\]

con

\[
u(x,0)=\frac{1}{1+x^2}.
\]

1. Construye la solución clásica mediante características.
2. Determina el intervalo temporal máximo en el que la parametrización
   característica es invertible.
3. Calcula el primer tiempo y la posición en que se pierde la regularidad
   clásica.
4. Explica qué tipo de solución debe buscarse después de ese instante y qué
   condición selecciona la solución físicamente relevante.

## 2. Onda: reducción esférica y propagación

Sea \(u=u(r,t)\) una solución radial en tres dimensiones:

\[
u_{tt}=c^2\left(u_{rr}+\frac{2}{r}u_r\right),
\qquad r>0,\quad t>0,
\]

con \(u_r(0,t)=0\),

\[
u(r,0)=f(r),\qquad u_t(r,0)=0,
\]

donde \(f\in C^2([0,\infty))\), \(f'(0)=0\) y
\(\operatorname{supp}f\subset[0,R]\).

1. Introduce \(v(r,t)=r\,u(r,t)\) y deduce el problema unidimensional que
   satisface \(v\).
2. Obtén una fórmula explícita para \(u\) usando una extensión impar.
3. Describe con precisión el soporte de \(u(\cdot,t)\).
4. Relaciona la respuesta con el principio fuerte de Huygens.

## 3. Elípticas: estimación a priori por comparación

Sea \(u\in C^2(B_1)\cap C(\overline{B_1})\) solución de

\[
-\Delta u+\lambda u=f\quad\text{en }B_1,
\qquad
u=g\quad\text{en }\partial B_1,
\]

donde \(\lambda\ge 0\), \(f\in C(\overline{B_1})\) y
\(g\in C(\partial B_1)\).

1. Construye barreras usando \(1-|x|^2\).
2. Demuestra una cota de la forma

   \[
   \|u\|_{L^\infty(B_1)}
   \le
   \|g\|_{L^\infty(\partial B_1)}
   C_n\|f\|_{L^\infty(B_1)},
   \]

   con una constante explícita \(C_n\).
3. Explica por qué la misma comparación implica unicidad.
4. Señala qué parte del argumento puede fallar si \(\lambda<0\).

## 4. Calor: positividad y control uniforme

Sea \(\Omega\subset\mathbb R^n\) un dominio acotado y suave. Supón que

\[
u_t-\Delta u+\theta(x,t)u=-u^3
\quad\text{en }\Omega\times(0,T],
\]

\[
u=0\quad\text{en }\partial\Omega\times(0,T],
\qquad
u(\cdot,0)=u_0\ge0,
\]

con \(\theta(x,t)\ge-\theta_0\).

1. Demuestra que \(u\ge0\).
2. Mediante un cambio exponencial o una barrera, prueba

   \[
   u(x,t)\le e^{\theta_0t}\|u_0\|_{L^\infty(\Omega)}.
   \]

3. Identifica con precisión dónde se utilizan el signo de \(-u^3\), la
   condición de frontera y el principio del máximo.
4. Explica cómo cambiaría la estimación si el lado derecho fuera
   \(h(x,t)-u^3\), con \(h\ge0\) acotada.

## Uso del resultado

- Menos de 40 puntos: regresar a fórmulas e hipótesis básicas.
- Entre 40 y 60: priorizar demostraciones y control del tiempo.
- Entre 60 y 80: practicar variaciones y problemas mixtos.
- Más de 80: hacer un segundo simulacro cambiando datos y geometrías.
