"""Construye la ruta canónica compacta para el Examen General de EDP.

Cada subsección oficial produce exactamente un notebook autocontenido con:
teoría esencial, interpretación geométrica/física, ejemplo guiado, dos
ejercicios normales y, sólo en ocho temas recurrentes, una variación General.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERAL = ROOT / "GENERAL"


SECTIONS = [
    {
        "folder": "01_PRIMER_ORDEN",
        "id": "01.01",
        "slug": "Transporte_y_caracteristicas",
        "title": "Transporte y método de características",
        "priority": "ALTA",
        "history": "Aparece de forma directa o como paso inicial en 2023-1, 2023-2 y 2026-1.",
        "core": r"""Para
\[
u_t+b(x,t)\cdot\nabla u=f(x,t,u),\qquad u(x,0)=g(x),
\]
las características satisfacen \(X'(s)=b(X(s),s)\). Sobre ellas,
\[
\frac{d}{ds}u(X(s),s)=f(X(s),s,u(X(s),s)).
\]
Si \(b\equiv c\) y \(f=0\), entonces \(u(x,t)=g(x-ct)\). Antes de calcular,
identifica siempre la curva de datos, su parametrización y qué
características la atraviesan.""",
        "visual": r"""Las características son las trayectorias de partículas. El valor de \(u\)
se transporta sobre cada trayectoria; por eso el soporte del dato inicial se
desplaza sin deformarse cuando la velocidad es constante.""",
        "media": "../../LINEALES/media/videos/LINEALES/1440p120/TransporteConstanteCaracteristicas.mp4",
        "example": r"""Para \(u_t+2u_x=0\), \(u(x,0)=e^{-x^2}\), se tiene
\(x(s)=\xi+2s\) y \(u(x(s),s)=e^{-\xi^2}\). Como \(\xi=x-2t\),
\[
u(x,t)=e^{-(x-2t)^2}.
\]""",
        "exercises": [
            r"""Resuelve \(u_t+(1+t)u_x=0\), \(u(x,0)=\sin x\), y verifica el dato inicial.""",
            r"""Si \(g\) está soportada en \([-1,1]\), determina exactamente el soporte de la solución de \(u_t+cu_x=0\).""",
        ],
    },
    {
        "folder": "01_PRIMER_ORDEN",
        "id": "01.02",
        "slug": "Flujo_caracteristico_y_transversalidad",
        "title": "Flujo característico, jacobiano y transversalidad",
        "priority": "ALTA",
        "history": "La condición de transversalidad fue el núcleo del problema de 2026-1.",
        "core": r"""El flujo \(X(s;\xi)\) resuelve \(X'=b(X,s)\). Su jacobiano
\(J=\det D_\xi X\) satisface la fórmula de Liouville
\[
J'(s)=(\nabla\cdot b)(X(s),s)J(s).
\]
Para datos prescritos sobre una curva \(\gamma(r)\), la condición local de
buena posición es que el campo característico no sea tangente:
\[
\det\big(\gamma'(r),\,b(\gamma(r))\big)\neq0.
\]""",
        "visual": r"""Transversalidad significa que las características cruzan la curva de datos.
Si son tangentes, la curva no etiqueta de manera única las trayectorias y
puede haber incompatibilidad o falta de unicidad.""",
        "media": "../../LINEALES/media/videos/LINEALES/1440p120/ProblemaMixtoCompatibilidad.mp4",
        "example": r"""Para \(b(x,y)=(1,y)\), el sistema \(x'=1,\ y'=y\) da
\(x=r+s,\ y=y_0e^s\). Por tanto \(J=e^s\), coherente con
\(\nabla\cdot b=1\).""",
        "exercises": [
            r"""Calcula el flujo y su jacobiano para \(b(x,y)=(x,-y)\). Interpreta la conservación de área.""",
            r"""Para \(u_x+xu_y=0\) con datos sobre \(\gamma(r)=(0,r)\), verifica transversalidad y encuentra la solución local.""",
        ],
    },
    {
        "folder": "01_PRIMER_ORDEN",
        "id": "01.03",
        "slug": "Cuasilineales_y_perdida_de_regularidad",
        "title": "Ecuaciones cuasilineales y pérdida de regularidad",
        "priority": "ALTA",
        "history": "Características no lineales y tiempo de ruptura aparecen repetidamente; 2025-1 pidió explosión.",
        "core": r"""Para
\[
a(x,t,u)u_x+b(x,t,u)u_t=c(x,t,u),
\]
se resuelve \(x'=a,\ t'=b,\ u'=c\). En Burgers,
\[
u_t+uu_x=0,\qquad u(x,0)=g(x),
\]
resulta \(u=g(\xi)\), \(x=\xi+t g(\xi)\). La solución clásica existe mientras
\[
\partial_\xi x=1+t g'(\xi)\neq0.
\]""",
        "visual": r"""La ruptura ocurre cuando dos características se intersectan. La función
puede seguir acotada, pero su pendiente se hace infinita: la gráfica se
vuelve vertical antes de formar un choque.""",
        "example": r"""Si \(g(\xi)=-\xi\), entonces \(x=(1-t)\xi\) y
\(u(x,t)=-x/(1-t)\). El primer tiempo de ruptura es \(t_*=1\).""",
        "exercises": [
            r"""Para Burgers con \(g(x)=e^{-x^2}\), expresa el tiempo de ruptura mediante \(\min g'\) y localiza dónde comienza.""",
            r"""Resuelve \(u_t+u_x=u^2\), \(u(x,0)=g(x)\), y determina cuándo explota una característica.""",
        ],
        "general": r"""Considere \(u_t+(1+u)u_x=u^2\), \(u(x,0)=\alpha e^{-x^2}\).
Construya el sistema característico, obtenga la representación implícita,
distinga explosión de \(u\) y cruce de características, y determine cuál
mecanismo limita primero la solución clásica en función de \(\alpha>0\).""",
    },
    {
        "folder": "01_PRIMER_ORDEN",
        "id": "01.04",
        "slug": "No_lineales_y_caracteristicas_generalizadas",
        "title": "Ecuaciones completamente no lineales y características generalizadas",
        "priority": "MEDIA",
        "history": "Es herramienta del temario; suele evaluarse mediante compatibilidad y geometría, no como bloque aislado.",
        "core": r"""Para \(F(x,y,u,p,q)=0\), con \(p=u_x,\ q=u_y\), el sistema de
Charpit puede escribirse
\[
x'=F_p,\quad y'=F_q,\quad
u'=pF_p+qF_q,
\]
\[
p'=-F_x-pF_u,\qquad q'=-F_y-qF_u.
\]
Los datos iniciales deben satisfacer \(F=0\) y ser compatibles con la
derivada tangencial de \(u\) sobre la curva inicial.""",
        "visual": r"""La solución es una superficie; \((p,q)\) describe su plano tangente.
Las características generalizadas evolucionan simultáneamente el punto, la
altura y la inclinación.""",
        "example": r"""Para la eikonal \(p^2+q^2=1\), \(F_p=2p,\ F_q=2q\) y
\(p,q\) son constantes sobre cada característica. La proyección al plano es
una recta.""",
        "exercises": [
            r"""Escribe el sistema de Charpit para \(u_xu_y=u\) y señala qué variables permanecen constantes si las hay.""",
            r"""Para \(u_x^2+u_y^2=1\) con \(u(x,0)=x\), verifica compatibilidad y describe las características iniciales.""",
        ],
    },
    {
        "folder": "01_PRIMER_ORDEN",
        "id": "01.05",
        "slug": "Soluciones_debiles_entropia_y_Rankine_Hugoniot",
        "title": "Soluciones débiles, entropía y Rankine-Hugoniot",
        "priority": "ALTA",
        "history": "Los generales 2023-1 y 2025-2 exigen seleccionar la solución entrópica.",
        "core": r"""Una solución débil de \(u_t+f(u)_x=0\) satisface
\[
\iint (u\varphi_t+f(u)\varphi_x)\,dxdt+\int u_0\varphi(\cdot,0)\,dx=0.
\]
Un salto \(u_L\to u_R\) que viaja con velocidad \(s\) debe cumplir
\[
s[u]=[f(u)],\qquad
s=\frac{f(u_L)-f(u_R)}{u_L-u_R}.
\]
Para flujo convexo, un choque entrópico satisface
\(f'(u_L)>s>f'(u_R)\).""",
        "visual": r"""Rankine-Hugoniot es balance de masa a través de un frente móvil. La
condición de Lax exige que las características entren al choque desde ambos
lados; un frente del que salen características no es físicamente admisible.""",
        "example": r"""Para Burgers \(f(u)=u^2/2\), \(u_L=2,\ u_R=0\),
\(s=(2-0)/(2)=1\). Como \(f'(2)=2>1>0=f'(0)\), el choque es entrópico.""",
        "exercises": [
            r"""Para \(f(u)=u^3/3\), \(u_L=2,\ u_R=1\), calcula \(s\) y verifica la condición de Lax.""",
            r"""Demuestra desde la formulación débil que una función constante a cada lado de \(x=st\) exige Rankine-Hugoniot.""",
        ],
    },
    {
        "folder": "01_PRIMER_ORDEN",
        "id": "01.06",
        "slug": "Riemann_Burgers_y_LWR",
        "title": "Problema de Riemann, Burgers y modelo LWR",
        "priority": "ALTA",
        "history": "Burgers apareció en 2025-2 y el modelo de tráfico LWR en 2026-1.",
        "core": r"""Con datos de Riemann \(u_L,u_R\), la solución entrópica es
autosemejante \(u(x,t)=U(x/t)\). Para flujo convexo: si \(u_L>u_R\) hay
choque; si \(u_L<u_R\), rarefacción
\[
U(\xi)=
\begin{cases}
u_L,&\xi<f'(u_L),\\
(f')^{-1}(\xi),&f'(u_L)\le\xi\le f'(u_R),\\
u_R,&\xi>f'(u_R).
\end{cases}
\]
En LWR, \(f(\rho)=v_{\max}\rho(1-\rho/\rho_{\max})\) es cóncavo, por lo que
se invierte el criterio geométrico habitual del flujo convexo.""",
        "visual": r"""En el plano \((x,t)\), una rarefacción abre un abanico de
características; un choque las concentra en una sola recta. En tráfico, una
velocidad de choque negativa representa una onda de congestión que retrocede.""",
        "example": r"""Burgers con \(u_L=0,\ u_R=1\) produce el abanico
\(u=x/t\) para \(0<x<t\), con estados constantes fuera.""",
        "exercises": [
            r"""Resuelve el problema de Riemann de Burgers con \(u_L=1,\ u_R=-1\) y dibuja las características.""",
            r"""Para \(f(\rho)=\rho(1-\rho)\), calcula la velocidad del frente entre \(\rho_L=0.8\) y \(\rho_R=0.2\).""",
        ],
        "general": r"""Para \(u_t+(u(1-u))_x=0\), combine tres estados
\(u_0=0.8\) si \(x<0\), \(0.2\) si \(0<x<1\) y \(0.6\) si \(x>1\).
Construya las ondas iniciales, determine su interacción y describa la solución
entrópica después del primer tiempo de interacción.""",
    },
    {
        "folder": "02_ONDA",
        "id": "02.01",
        "slug": "Cauchy_dAlembert_y_propagacion_finita",
        "title": "Problema de Cauchy, d'Alembert y propagación finita",
        "priority": "ALTA",
        "history": "d'Alembert y soporte fueron el centro del General 2026-1.",
        "core": r"""Para \(u_{tt}-c^2u_{xx}=0\), \(u(x,0)=f(x)\),
\(u_t(x,0)=g(x)\),
\[
u(x,t)=\frac{f(x-ct)+f(x+ct)}2+
\frac1{2c}\int_{x-ct}^{x+ct}g(y)\,dy.
\]
El valor en \((x,t)\) sólo depende del intervalo \([x-ct,x+ct]\), la base de
su cono pasado.""",
        "visual": r"""La perturbación viaja a velocidad finita \(c\). El dato de desplazamiento
se separa en ondas derecha e izquierda y el dato de velocidad llena el
interior del cono.""",
        "media": "../../ONDA/animaciones/02_01_dAlembert_2K_120fps.mp4",
        "example": r"""Si \(g=0\) y \(f\) está soportada en \([-1,1]\), entonces
el soporte de \(u(\cdot,t)\) está contenido en
\([-1-ct,1+ct]\).""",
        "exercises": [
            r"""Usa d'Alembert para \(f(x)=e^{-x^2}\), \(g=0\), y verifica ambos datos iniciales.""",
            r"""Si \(f,g\) se anulan en \([x_0-ct_0,x_0+ct_0]\), demuestra que \(u(x_0,t_0)=0\).""",
        ],
        "general": r"""Sean \(f,g\) suaves y soportadas en \([-a,a]\).
Determine el soporte máximo de \(u(\cdot,t)\), demuestre la afirmación desde
d'Alembert y construya datos no triviales para los que la inclusión sea
estricta en un tiempo dado.""",
    },
    {
        "folder": "02_ONDA",
        "id": "02.02",
        "slug": "Fronteras_reflexion_y_compatibilidad",
        "title": "Semirrecta, reflexión y compatibilidad",
        "priority": "MEDIA",
        "history": "Es técnica necesaria para los problemas de semieje y frontera.",
        "core": r"""En \(x>0\), Dirichlet homogénea se obtiene extendiendo \(f,g\) de manera
impar; Neumann homogénea, de manera par. Después se aplica d'Alembert en toda
la recta. En la esquina se requiere compatibilidad: para Dirichlet,
\(f(0)=0\); para Neumann, \(f'(0)=0\), además de condiciones de orden superior
si se busca mayor regularidad.""",
        "visual": r"""La frontera actúa como un espejo. La reflexión impar cambia el signo del
pulso y fuerza \(u(0,t)=0\); la reflexión par conserva el signo y fuerza
\(u_x(0,t)=0\).""",
        "example": r"""Para Dirichlet, \(f(x)=xe^{-x}\), \(g=0\), se define
\(\tilde f(x)=xe^{-|x|}\), que es impar, y se usa d'Alembert con \(\tilde f\).""",
        "exercises": [
            r"""Resuelve el problema de Dirichlet homogéneo con \(f(x)=xe^{-x}\), \(g=0\), y determina cuándo el pulso reflejado aparece en \(x=1\).""",
            r"""Deriva la fórmula de Neumann homogénea por extensión par y comprueba \(u_x(0,t)=0\).""",
        ],
    },
    {
        "folder": "02_ONDA",
        "id": "02.03",
        "slug": "Intervalo_separacion_y_Fourier",
        "title": "Intervalo finito, separación de variables y series de Fourier",
        "priority": "ALTA",
        "history": "La separación en intervalo fue evaluada en 2025-1 y la periodicidad en 2023-2.",
        "core": r"""En \(0<x<L\) con extremos fijos, \(u(0,t)=u(L,t)=0\), se busca
\(u=X(x)T(t)\). Resulta
\[
X_n=\sin(n\pi x/L),\qquad \omega_n=cn\pi/L,
\]
\[
u=\sum_{n\ge1}\left(A_n\cos\omega_nt+B_n\sin\omega_nt\right)
\sin(n\pi x/L).
\]
Los coeficientes se obtienen de las series seno de \(f\) y \(g\).""",
        "visual": r"""Los modos normales son patrones estacionarios con nodos en la frontera.
Cada modo oscila con frecuencia propia; la solución total es su
superposición.""",
        "example": r"""Si \(f(x)=\sin(\pi x/L)\), \(g=0\), sólo se excita el primer modo:
\(u=\cos(c\pi t/L)\sin(\pi x/L)\).""",
        "exercises": [
            r"""Resuelve el problema con \(f=0\), \(g(x)=\sin(2\pi x/L)\).""",
            r"""Expande \(f(x)=x(L-x)\) en serie seno y escribe la solución formal con velocidad inicial nula.""",
        ],
    },
    {
        "folder": "02_ONDA",
        "id": "02.04",
        "slug": "Problema_no_homogeneo_y_Duhamel",
        "title": "Problema no homogéneo y principio de Duhamel",
        "priority": "MEDIA",
        "history": "Duhamel conecta las versiones no homogéneas en una y varias dimensiones.",
        "core": r"""Para
\[
u_{tt}-c^2u_{xx}=F(x,t),\qquad u(\cdot,0)=u_t(\cdot,0)=0,
\]
Duhamel superpone soluciones homogéneas creadas en cada tiempo \(s\):
\[
u(x,t)=\frac1{2c}\int_0^t\int_{x-c(t-s)}^{x+c(t-s)}
F(y,s)\,dy\,ds.
\]
Con datos no nulos se suma la solución de d'Alembert.""",
        "visual": r"""Cada punto de la fuerza emite una onda elemental. Sólo contribuyen los
puntos del soporte de \(F\) contenidos en el cono pasado de \((x,t)\).""",
        "example": r"""Para \(F(x,t)=e^{-t}\cos(kx)\), se usa la identidad trigonométrica
en la integral espacial y queda una integral temporal escalar con frecuencia
\(ck\).""",
        "exercises": [
            r"""Reduce explícitamente la fórmula de Duhamel para \(F=e^{-t}\cos(kx)\) y verifica la ecuación.""",
            r"""Si \(F\) está soportada en \(|x|\le a,\ 0\le t\le T\), describe una región donde la respuesta forzada es cero.""",
        ],
    },
    {
        "folder": "02_ONDA",
        "id": "02.05",
        "slug": "Energia_y_unicidad",
        "title": "Método de energía, conservación y unicidad",
        "priority": "MEDIA",
        "history": "La energía es una herramienta de demostración transversal del temario.",
        "core": r"""Para una solución en \([0,L]\),
\[
E(t)=\frac12\int_0^L(u_t^2+c^2u_x^2)\,dx.
\]
Multiplicar la ecuación por \(u_t\) e integrar da
\[
E'(t)=c^2[u_xu_t]_0^L+\int_0^L Fu_t\,dx.
\]
Con frontera homogénea y \(F=0\), \(E\) se conserva. Aplicada a la diferencia
de dos soluciones, la identidad prueba unicidad.""",
        "visual": r"""La energía interior cambia por potencia inyectada en la frontera y por el
trabajo de la fuerza. No debe eliminarse el término de frontera sin justificar
las condiciones impuestas.""",
        "example": r"""Si \(u(0,t)=u(L,t)=0\), entonces \(u_t=0\) en los extremos y el flujo
de energía \(c^2u_xu_t\) se anula.""",
        "exercises": [
            r"""Deriva cuidadosamente la identidad de energía en \([0,L]\) e indica dónde se usa cada condición de frontera.""",
            r"""Aplica la energía a \(w=u-v\) para demostrar unicidad con los mismos datos iniciales y de frontera.""",
        ],
    },
    {
        "folder": "02_ONDA",
        "id": "02.06",
        "slug": "Ondas_en_Rn_Huygens_y_Hadamard",
        "title": "Ondas en dimensiones superiores, Huygens y descenso de Hadamard",
        "priority": "ALTA",
        "history": "Poisson/Huygens apareció en 2023-1 y ondas esféricas en 2025-2.",
        "core": r"""En \(\mathbb R^3\), Kirchhoff promedia datos sobre la esfera
\(|y-x|=ct\); en \(\mathbb R^2\), Poisson integra sobre todo el disco
\(|y-x|<ct\) con peso \((c^2t^2-|y-x|^2)^{-1/2}\). El descenso de Hadamard
obtiene la fórmula bidimensional a partir de la tridimensional usando datos
independientes de una coordenada.""",
        "visual": r"""En dimensión tres la señal ideal viaja sobre el frente esférico (Huygens
fuerte). En dimensión dos queda una cola dentro del cono: el observador puede
seguir registrando señal después de pasar el frente.""",
        "media": "../../ONDA/animaciones/videos/1440p60/ParalelogramoCaracteristico.mp4",
        "example": r"""Para una onda radial 3D, \(v(r,t)=ru(r,t)\) satisface la ecuación
de onda 1D; se aplica d'Alembert a \(v\) y luego se divide entre \(r\).""",
        "exercises": [
            r"""Justifica mediante descenso de Hadamard el núcleo \((c^2t^2-r^2)^{-1/2}\) y especifica el intervalo de la coordenada adicional.""",
            r"""Para datos compactamente soportados, compara el soporte permitido por las fórmulas en \(\mathbb R^2\) y \(\mathbb R^3\).""",
        ],
        "general": r"""Compare datos suaves y compactamente soportados en
\(\mathbb R^2\) y \(\mathbb R^3\): escriba las regiones de integración,
demuestre propagación finita, explique la falla de Huygens fuerte en dimensión
dos y proponga una observación física que distinga ambos casos.""",
    },
    {
        "folder": "03_ELIPTICAS",
        "id": "03.01",
        "slug": "Laplace_Poisson_y_solucion_fundamental",
        "title": "Ecuaciones de Laplace y Poisson; solución fundamental",
        "priority": "ALTA",
        "history": "Soluciones fundamentales y representación aparecieron en 2025-1.",
        "core": r"""Las ecuaciones básicas son \(\Delta u=0\) y
\(-\Delta u=f\). Una solución fundamental de \(-\Delta\) es
\[
\Phi(x)=
\begin{cases}
\frac1{2\pi}\log\frac1{|x|},&n=2,\\
\frac1{(n-2)\omega_n}|x|^{2-n},&n\ge3.
\end{cases}
\]
En distribuciones, \(-\Delta\Phi=\delta_0\), por lo que
\(u=\Phi*f\) resuelve Poisson en todo el espacio bajo hipótesis apropiadas.""",
        "visual": r"""La solución fundamental es el potencial creado por una fuente puntual.
El gradiente es el campo asociado y el flujo a través de cualquier esfera que
encierra el origen es constante.""",
        "example": r"""Fuera del origen, para \(r=|x|\),
\(\Delta r^\alpha=\alpha(\alpha+n-2)r^{\alpha-2}\). Tomar
\(\alpha=2-n\) produce una función armónica.""",
        "exercises": [
            r"""Verifica que \(\Delta\log|x|=0\) en \(n=2\) y que \(\Delta|x|^{2-n}=0\) en \(n\ge3\), fuera del origen.""",
            r"""Usa el teorema de la divergencia para fijar la constante de \(\Phi\) en dimensión \(n\ge3\).""",
        ],
    },
    {
        "folder": "03_ELIPTICAS",
        "id": "03.02",
        "slug": "Funciones_armonicas_promedio_Harnack_Liouville",
        "title": "Funciones armónicas: promedio, Harnack, Liouville y regularidad",
        "priority": "ALTA",
        "history": "Propiedades armónicas, Green y Perron se combinaron en 2023-2.",
        "core": r"""Si \(u\) es armónica,
\[
u(x_0)=\fint_{\partial B_r(x_0)}u\,dS
=\fint_{B_r(x_0)}u\,dx.
\]
De la fórmula de Poisson se obtienen Harnack y estimaciones de derivadas. Una
función armónica y acotada en todo \(\mathbb R^n\) es constante (Liouville).
La propiedad del promedio también caracteriza la armonicidad bajo
continuidad.""",
        "visual": r"""El valor central no es un pico aislado: es exactamente el promedio de
cualquier esfera o bola contenida en el dominio. Ésta es la geometría detrás
del máximo y de la rigidez de Liouville.""",
        "media": "../../lAPLACE/media_propiedad_promedio/videos/propiedad_promedio_manim/1440p120/PromedioDisco.mp4",
        "example": r"""Para \(u(x,y)=x^2-y^2\), el promedio sobre
\((r\cos\theta,r\sin\theta)\) es
\(r^2\fint_0^{2\pi}\cos(2\theta)\,d\theta=0=u(0)\).""",
        "exercises": [
            r"""Verifica directamente la propiedad del promedio para \(u(x,y)=x^2-y^2\) en circunferencias centradas en el origen.""",
            r"""Demuestra Liouville usando una estimación interior para \(|\nabla u(0)|\) y haciendo \(R\to\infty\).""",
        ],
    },
    {
        "folder": "03_ELIPTICAS",
        "id": "03.03",
        "slug": "Maximo_comparacion_y_unicidad",
        "title": "Principios del máximo, comparación, unicidad y estabilidad",
        "priority": "ALTA",
        "history": "Máximo exterior en 2023-1, unicidad de Cauchy en 2025-2 y estimación de Poisson en 2026-1.",
        "core": r"""Si \(\Delta u\ge0\), el máximo de \(u\) en un dominio acotado se alcanza
en la frontera. Aplicar el resultado a \(u-v\) produce comparación y
unicidad. Para \(-\Delta u=f\), una barrera \(w\) con
\(-\Delta w\ge|f|\) y control de frontera da una estimación a priori.""",
        "visual": r"""Una membrana sin fuentes no puede formar un máximo interior estricto.
Las fuentes curvan la membrana; las barreras superior e inferior encierran la
solución.""",
        "media": "../../lAPLACE/animaciones/03.3.A_principio_debil_maximo.mp4",
        "example": r"""En \(B_1\), \(-\Delta(1-|x|^2)=2n\). Por ello múltiplos de
\(1-|x|^2\) sirven como barreras para fuentes acotadas.""",
        "exercises": [
            r"""Demuestra unicidad del problema de Dirichlet para \(\Delta u=0\) aplicando el máximo a \(u-v\).""",
            r"""Si \(-\Delta u=f\) en \(B_1\) y \(u=0\) en la frontera, usa \(1-|x|^2\) para acotar \(\|u\|_\infty\) por \(\|f\|_\infty\).""",
        ],
        "general": r"""Sea \(\Omega\subset B_R\) y
\(-\Delta u+\lambda u=f\), \(\lambda\ge0\), con \(u=g\) en
\(\partial\Omega\). Construya barreras explícitas y pruebe una estimación
\(\|u\|_\infty\le C(R,n,\lambda)\|f\|_\infty+\|g\|_\infty\). Indique dónde
se usa el signo de \(\lambda\).""",
    },
    {
        "folder": "03_ELIPTICAS",
        "id": "03.04",
        "slug": "Green_Poisson_y_representacion",
        "title": "Función de Green, núcleo de Poisson y representación",
        "priority": "ALTA",
        "history": "Green aparece explícitamente en 2023-2 y 2025-1.",
        "core": r"""La función de Green satisface
\[
-\Delta_xG(x,y)=\delta_y,\qquad G(\cdot,y)=0\text{ en }\partial\Omega.
\]
La segunda identidad de Green conduce a
\[
u(x)=\int_\Omega G(x,y)f(y)\,dy
-\int_{\partial\Omega}g(y)\partial_{\nu_y}G(x,y)\,dS_y.
\]
El núcleo de Poisson es \(P(x,y)=-\partial_{\nu_y}G(x,y)\).""",
        "visual": r"""Green es la respuesta del dominio a una fuente puntual con la frontera
fijada. El núcleo de Poisson reparte la influencia de cada punto de la
frontera sobre el punto interior.""",
        "example": r"""En el semiespacio, el método de imágenes resta la fuente reflejada para
anular \(G\) en el plano frontera.""",
        "exercises": [
            r"""Deriva la simetría \(G(x,y)=G(y,x)\) usando la segunda identidad de Green fuera de pequeñas bolas.""",
            r"""Obtén el núcleo de Poisson del semiespacio a partir de la solución fundamental y una fuente imagen.""",
        ],
    },
    {
        "folder": "03_ELIPTICAS",
        "id": "03.05",
        "slug": "Dirichlet_barreras_y_Perron",
        "title": "Problema de Dirichlet, barreras y método de Perron",
        "priority": "ALTA",
        "history": "Perron fue parte central de 2023-2 y la frontera irregular reaparece en problemas de existencia.",
        "core": r"""Perron toma el supremo de las subsoluciones por debajo del dato de
frontera. El máximo garantiza orden; el levantamiento armónico garantiza que
el supremo es armónico. Una barrera en \(\xi\in\partial\Omega\) obliga a que la
envolvente adopte el valor \(g(\xi)\). La condición de esfera exterior es un
criterio suficiente de regularidad.""",
        "visual": r"""Las subsoluciones forman perfiles que empujan desde abajo. La envolvente
superior es la mayor configuración admisible; las barreras sujetan esa
envolvente al dato en cada punto regular de la frontera.""",
        "example": r"""Si existe una bola exterior tangente en \(\xi\), una combinación de
\(|x-y|^{2-n}\) (o \(\log|x-y|\) en 2D) produce una barrera que se anula sólo
en \(\xi\).""",
        "exercises": [
            r"""Construye una barrera en un punto que satisface la condición de esfera exterior.""",
            r"""Explica por qué el máximo de dos subarmónicas es subarmónica y cómo se usa en Perron.""",
        ],
        "general": r"""Desarrolle el método de Perron para un dominio acotado con condición de
esfera exterior: defina la familia inferior, pruebe que su envolvente es
armónica y use barreras para recuperar datos continuos en la frontera.
Separe claramente existencia y unicidad.""",
    },
    {
        "folder": "03_ELIPTICAS",
        "id": "03.06",
        "slug": "Energia_y_principio_de_Dirichlet",
        "title": "Energía y principio de Dirichlet",
        "priority": "MEDIA",
        "history": "Es una vía variacional importante y soporte de unicidad, aunque aparece menos como problema aislado.",
        "core": r"""Para datos de frontera fijados se minimiza
\[
\mathcal E[v]=\frac12\int_\Omega|\nabla v|^2\,dx-\int_\Omega fv\,dx.
\]
La primera variación en dirección \(\varphi\in H_0^1(\Omega)\) es
\[
\int_\Omega\nabla u\cdot\nabla\varphi-\int_\Omega f\varphi.
\]
Su anulación es la formulación débil de \(-\Delta u=f\). La convexidad
estricta da unicidad.""",
        "visual": r"""La solución de Poisson es la configuración de menor energía entre todas
las superficies con la misma frontera. Las perturbaciones admisibles se
anulan en el borde.""",
        "example": r"""Si \(u\) resuelve el problema homogéneo y \(v=u+w\) con
\(w\in H_0^1\), entonces
\(\mathcal E[v]=\mathcal E[u]+\frac12\int|\nabla w|^2\).""",
        "exercises": [
            r"""Calcula la primera variación de \(\mathcal E[u+\varepsilon\varphi]\) y recupera la ecuación de Euler-Lagrange.""",
            r"""Demuestra unicidad del minimizador usando la identidad del paralelogramo o convexidad estricta.""",
        ],
    },
    {
        "folder": "03_ELIPTICAS",
        "id": "03.07",
        "slug": "Valores_propios_armonicos_esfericos_y_resonancia",
        "title": "Valores propios, armónicos esféricos y resonancia",
        "priority": "ALTA",
        "history": "Espectro y resonancia fueron evaluados en 2025-1.",
        "core": r"""El problema de Dirichlet
\[
-\Delta\phi_k=\lambda_k\phi_k
\]
produce una base ortogonal en \(L^2(\Omega)\). Para
\((-\Delta-\lambda)u=f\), si \(\lambda\neq\lambda_k\),
\[
u=\sum_k\frac{\langle f,\phi_k\rangle}{\lambda_k-\lambda}\phi_k.
\]
En resonancia \(\lambda=\lambda_j\), se requiere
\(\langle f,\phi_j\rangle=0\) (alternativa de Fredholm). En la esfera, las
funciones propias angulares son armónicos esféricos.""",
        "visual": r"""Cada función propia es un modo natural. Cerca de una frecuencia propia,
la respuesta se amplifica; exactamente en resonancia sólo hay solución si la
fuerza no excita el modo resonante.""",
        "example": r"""En \((0,\pi)\), \(\phi_k=\sin(kx)\), \(\lambda_k=k^2\).
Para \(-u''-4u=\sin x\), \(u=\sin x/(1-4)=-\sin x/3\).""",
        "exercises": [
            r"""Resuelve \(-u''-\lambda u=\sin(2x)\) en \((0,\pi)\) con Dirichlet para \(\lambda\neq4\).""",
            r"""Analiza existencia y no unicidad cuando \(\lambda=4\) y \(f\) es ortogonal a \(\sin(2x)\).""",
        ],
    },
    {
        "folder": "04_CALOR",
        "id": "04.01",
        "slug": "Nucleo_del_calor_y_Cauchy_global",
        "title": "Núcleo del calor y problema de Cauchy global",
        "priority": "ALTA",
        "history": "El comportamiento asintótico del núcleo fue evaluado en 2023-2.",
        "core": r"""El núcleo fundamental es
\[
\psi(x,t)=(4\pi t)^{-n/2}e^{-|x|^2/(4t)},\qquad t>0.
\]
La solución global es \(u(x,t)=(\psi_t*g)(x)\). El núcleo tiene masa uno,
escala parabólicamente y aproxima la identidad cuando \(t\downarrow0\).
Además \(\|\psi_t\|_\infty=(4\pi t)^{-n/2}\).""",
        "visual": r"""El calor tiene propagación instantánea: una masa puntual se vuelve una
gaussiana positiva en todo el espacio. Su anchura crece como \(\sqrt t\) y su
altura decrece como \(t^{-n/2}\).""",
        "media": "../../calor/media/videos/01_04_01_nucleo_fundamental/1440p120/HeatKernelEvolution.mp4",
        "example": r"""Por simetría, \(\int x_i\psi\,dx=0\). Cada coordenada tiene varianza
\(2t\), por lo que \(\int|x|^2\psi\,dx=2nt\).""",
        "exercises": [
            r"""Demuestra \(\int x_i\psi(x,t)\,dx=0\) y \(\int|x|^2\psi(x,t)\,dx=2nt\).""",
            r"""Prueba \(\|u(\cdot,t)\|_\infty\le(4\pi t)^{-n/2}\|g\|_1\).""",
        ],
        "general": r"""Sea \(g\in L^1(\mathbb R^n)\) con masa \(M\) y primer momento finito.
Demuestre que \(t^{n/2}u(\sqrt t\,y,t)\) converge al perfil gaussiano de masa
\(M\), y obtenga una estimación del error usando el primer momento.""",
    },
    {
        "folder": "04_CALOR",
        "id": "04.02",
        "slug": "Maximo_comparacion_y_unicidad",
        "title": "Principio débil del máximo, comparación y unicidad",
        "priority": "ALTA",
        "history": "Comparación y términos de orden cero fueron evaluados en 2026-1.",
        "core": r"""En \(\Omega_T=\Omega\times(0,T]\), la frontera parabólica es
\[
\Gamma_T=(\overline\Omega\times\{0\})\cup
(\partial\Omega\times[0,T]).
\]
Si \(u_t-\Delta u\le0\), entonces
\(\max_{\overline{\Omega_T}}u=\max_{\Gamma_T}u\). Aplicar el principio a
\(u-v\) da comparación, estabilidad en norma supremo y unicidad.""",
        "visual": r"""El tiempo tiene orientación: la frontera relevante incluye el instante
inicial y la pared lateral, no la tapa \(t=T\). El máximo sólo puede entrar
desde el pasado o la pared.""",
        "example": r"""Si \(u,v\) tienen la misma fuente, entonces
\(w=u-v\) satisface la ecuación homogénea y
\(\|w\|_{\infty,\Omega_T}\le\|w\|_{\infty,\Gamma_T}\).""",
        "exercises": [
            r"""Escribe \(\Gamma_T\) para \(\Omega=B_1(0)\) y explica por qué la tapa superior no se incluye.""",
            r"""Demuestra la estabilidad supremo para dos soluciones con igual fuente y datos de frontera distintos.""",
        ],
    },
    {
        "folder": "04_CALOR",
        "id": "04.03",
        "slug": "Principio_fuerte_y_positividad",
        "title": "Principio fuerte del máximo y positividad",
        "priority": "ALTA",
        "history": "La propagación del máximo en dominios con obstáculos apareció en 2023-1.",
        "core": r"""Si una solución del calor alcanza un máximo global en un punto interior
\((x_0,t_0)\), entonces es constante en la región espacial conectada para
tiempos anteriores hasta \(t_0\). Aplicado a \(-u\) da la versión de mínimos.
Con datos no negativos y no nulos, el núcleo del calor implica positividad
instantánea en dominios apropiados.""",
        "visual": r"""El calor comunica valores hacia adelante en el tiempo. Un máximo interior
no queda aislado: fuerza una meseta que se propaga hacia el pasado dentro de
la componente accesible.""",
        "example": r"""Si \(u\ge0\), \(u\not\equiv0\) y \(u=\psi_t*g\) en todo el espacio,
entonces \(u(x,t)>0\) para todo \(x\) y \(t>0\) porque \(\psi>0\).""",
        "exercises": [
            r"""Deduce la versión fuerte para mínimos aplicando el teorema a \(-u\).""",
            r"""Prueba positividad instantánea de \(\psi_t*g\) cuando \(g\ge0\), \(g\not\equiv0\).""",
        ],
    },
    {
        "folder": "04_CALOR",
        "id": "04.04",
        "slug": "Problema_no_homogeneo_y_Duhamel",
        "title": "Problema no homogéneo y principio de Duhamel",
        "priority": "ALTA",
        "history": "La fuente y la frontera variable aparecieron en 2025-2.",
        "core": r"""Para
\[
u_t-\Delta u=F,\qquad u(\cdot,0)=g
\]
en todo el espacio,
\[
u(x,t)=\psi_t*g(x)+\int_0^t\psi_{t-s}*F(\cdot,s)(x)\,ds.
\]
La derivación usa el semigrupo del calor y requiere justificar el límite en
\(s=t\). En dominios con frontera se combina con levantamientos o con el
semigrupo del operador con condiciones de frontera.""",
        "visual": r"""La fuente deposita calor continuamente. Cada depósito hecho en tiempo
\(s\) evoluciona durante \(t-s\), no durante \(t\).""",
        "example": r"""Si \(F(x,t)=e^{-t}h(x)\), la respuesta forzada es
\(\int_0^te^{-s}\psi_{t-s}*h\,ds\).""",
        "exercises": [
            r"""Verifica formalmente que la fórmula de Duhamel satisface la ecuación y el dato inicial.""",
            r"""Prueba una cota supremo de la respuesta forzada en términos de \(\int_0^t\|F(\cdot,s)\|_\infty ds\).""",
        ],
    },
    {
        "folder": "04_CALOR",
        "id": "04.05",
        "slug": "Frontera_semirrecta_intervalo_y_Fourier",
        "title": "Problemas de frontera: semirrecta, intervalo y Fourier",
        "priority": "ALTA",
        "history": "El semieje apareció en 2025-1 y la frontera no homogénea en 2025-2.",
        "core": r"""En el semieje, Dirichlet homogénea usa extensión impar del dato y
Neumann homogénea usa extensión par. En \((0,L)\), separación de variables
produce modos seno para Dirichlet y coseno para Neumann. Para frontera
variable se escribe \(u=v+\ell\), donde \(\ell\) interpola los datos de borde;
\(v\) tiene frontera homogénea y una fuente modificada.""",
        "visual": r"""La reflexión construye fuentes imagen; el levantamiento separa la
geometría de la frontera de la difusión interior. Los modos altos decaen como
\(e^{-\lambda_kt}\), mucho más rápido que los bajos.""",
        "example": r"""Para \(u(0,t)=a(t)\), \(u(L,t)=b(t)\), toma
\(\ell(x,t)=a(t)+(b(t)-a(t))x/L\). Entonces
\(v=u-\ell\) tiene frontera cero y fuente \(-\ell_t\).""",
        "exercises": [
            r"""Obtén la solución del semieje con Dirichlet homogénea y dato \(g(x)=e^{-x}\) mediante extensión impar.""",
            r"""Para frontera \(u(0,t)=0,\ u(L,t)=t\), construye un levantamiento y escribe el problema homogéneo resultante.""",
        ],
        "general": r"""Resuelva en \(0<x<L\) el problema
\(u_t-u_{xx}=F(x,t)\), \(u(0,t)=a(t)\), \(u(L,t)=b(t)\), \(u(x,0)=g(x)\).
Establezca compatibilidad, haga un levantamiento explícito, obtenga la serie
de Fourier-Duhamel y justifique unicidad e interpretación del balance de
calor.""",
    },
    {
        "folder": "04_CALOR",
        "id": "04.06",
        "slug": "Regularidad_y_propiedad_de_las_medias",
        "title": "Suavizamiento, regularidad y propiedad de las medias",
        "priority": "MEDIA",
        "history": "La regularidad sostiene máximo fuerte y estimaciones, pero suele evaluarse integrada con otros temas.",
        "core": r"""Para \(t>0\), derivar la convolución da
\[
D_x^\alpha u=(D_x^\alpha\psi_t)*g,
\]
de modo que datos poco regulares producen soluciones suaves. El escalamiento
parabólico es \((x,t)\mapsto(rx,r^2t)\). Las bolas de calor y su propiedad de
las medias respetan esta geometría y producen estimaciones interiores.""",
        "visual": r"""La difusión borra escalas pequeñas primero. Espacio y tiempo no escalan
igual: duplicar la longitud multiplica por cuatro el tiempo característico.""",
        "example": r"""Como \(\|\nabla\psi_t\|_1=Ct^{-1/2}\),
\(\|\nabla u(\cdot,t)\|_\infty\le Ct^{-1/2}\|g\|_\infty\).""",
        "exercises": [
            r"""Calcula \(\partial_{x_i}\psi\) y deduce su escalamiento \(L^1\).""",
            r"""Verifica que \(u_r(x,t)=u(rx,r^2t)\) satisface la ecuación del calor cuando \(u\) la satisface.""",
        ],
    },
    {
        "folder": "04_CALOR",
        "id": "04.07",
        "slug": "Tychonoff_y_Widder",
        "title": "No unicidad de Tychonoff y representación de Widder",
        "priority": "CONSULTA",
        "history": "Son resultados avanzados del curso; no fueron problema principal en los generales revisados.",
        "core": r"""Tychonoff construye soluciones no triviales con dato inicial cero si no se
impone control de crecimiento espacial; usa funciones planas en \(t=0\).
Esto muestra que la unicidad global requiere una clase de crecimiento.
Widder afirma, bajo positividad, que una solución global del calor se
representa como convolución del núcleo con una medida positiva.""",
        "visual": r"""Tychonoff explota crecimiento extremadamente rápido en el infinito para
ocultar una solución no trivial en el dato inicial. Widder restaura rigidez:
la positividad convierte la solución en una superposición de fuentes
puntuales positivas.""",
        "example": r"""La serie
\(u=\sum_{k\ge0}f^{(k)}(t)x^{2k}/(2k)!\) satisface formalmente
\(u_t-u_{xx}=f^{(N+1)}(t)x^{2N}/(2N)!\) al truncarse en \(N\).""",
        "exercises": [
            r"""Calcula el residuo del truncamiento de Tychonoff y explica por qué desaparece al pasar a la serie formal.""",
            r"""Demuestra que \(e^{-1/t^\alpha}\), prolongada por cero para \(t\le0\), es plana en el origen.""",
        ],
    },
]


def video_cell(path: str) -> str:
    return f"""<video controls preload="metadata" style="max-width: 100%; height: auto;">
  <source src="{path}" type="video/mp4">
</video>

> Si el reproductor no carga en GitHub, abre el notebook localmente; la ruta es relativa al repositorio."""


def make_notebook(section: dict) -> dict:
    practice = [
        "## Práctica esencial\n",
        "\n",
        "La cuenta es literal: dos ejercicios normales. Sólo los temas marcados llevan un tercero de nivel General.\n",
        "\n",
    ]
    for index, exercise in enumerate(section["exercises"], start=1):
        practice.extend(
            [
                f"### Ejercicio normal {section['id']}.{index}\n",
                "\n",
                exercise.strip() + "\n",
                "\n",
            ]
        )
    if section.get("general"):
        practice.extend(
            [
                f"### Problema tipo General {section['id']}.G\n",
                "\n",
                section["general"].strip() + "\n",
            ]
        )

    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": (
                f"# {section['id']} — {section['title']}\n\n"
                f"**Prioridad para el General:** {section['priority']}  \n"
                f"**Patrón histórico:** {section['history']}\n\n"
                "> Notebook canónico de la ruta compacta. Para estudiar el examen, "
                "usa éste en lugar de las versiones extensas o legadas."
            ).splitlines(keepends=True),
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ("## Núcleo teórico\n\n" + section["core"].strip()).splitlines(
                keepends=True
            ),
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": (
                "## Interpretación geométrica o física\n\n"
                + section["visual"].strip()
            ).splitlines(keepends=True),
        },
    ]
    if section.get("media"):
        cells.append(
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": (
                    "## Visualización\n\n" + video_cell(section["media"])
                ).splitlines(keepends=True),
            }
        )
    cells.extend(
        [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": (
                    "## Ejemplo guiado\n\n" + section["example"].strip()
                ).splitlines(keepends=True),
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": practice,
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": (
                    "## Autochequeo\n\n"
                    "- ¿Puedo enunciar las hipótesis antes de usar la fórmula?\n"
                    "- ¿Puedo dibujar o explicar la geometría relevante?\n"
                    "- ¿Puedo verificar ecuación, datos y frontera al terminar?\n"
                    "- ¿Sé por qué este método es preferible a los otros del bloque?"
                ).splitlines(keepends=True),
            },
        ]
    )
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3"},
            "general_edp": {
                "canonical": True,
                "section": section["id"],
                "priority": section["priority"],
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    written = []
    for section in SECTIONS:
        folder = GENERAL / section["folder"]
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"{section['id']}_{section['slug']}.ipynb"
        path.write_text(
            json.dumps(make_notebook(section), ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )
        written.append(path)

    print(f"Notebooks canónicos escritos: {len(written)}")
    print(f"Ejercicios normales: {sum(len(s['exercises']) for s in SECTIONS)}")
    print(f"Problemas General: {sum(bool(s.get('general')) for s in SECTIONS)}")


if __name__ == "__main__":
    main()
