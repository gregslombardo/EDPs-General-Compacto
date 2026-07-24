# Formulario de memorización para el General de EDP

Este documento reúne las fórmulas que conviene poder reconstruir sin apuntes.
No sustituye las hipótesis ni las demostraciones: junto a cada fórmula se
indica qué significa y cuándo debe usarse.

## Cómo memorizarlo

Para cada resultado intenta repetir cuatro cosas:

1. **Ecuación y datos:** qué problema resuelve.
2. **Fórmula o principio:** cuál es la herramienta.
3. **Geometría o física:** qué está ocurriendo.
4. **Verificación:** ecuación, datos, frontera y unicidad.

---

## 0. Mapa rápido

| Tipo | Modelo | Geometría dominante | Fenómeno |
|---|---|---|---|
| Primer orden | \(u_t+b\cdot\nabla u=f\) | curvas características | transporte, choque |
| Hiperbólica | \(u_{tt}-c^2\Delta u=F\) | conos de luz | propagación finita |
| Elíptica | \(-\Delta u=f\) | dominio completo y frontera | equilibrio, rigidez |
| Parabólica | \(u_t-\kappa\Delta u=F\) | frontera parabólica | difusión, suavizamiento |

Para

\[
Au_{xx}+2Bu_{xy}+Cu_{yy}+\text{términos de orden menor}=0,
\]

la clasificación local viene de \(B^2-AC\):

- \(B^2-AC>0\): hiperbólica;
- \(B^2-AC=0\): parabólica;
- \(B^2-AC<0\): elíptica.

> **Idea geométrica.** La parte principal determina las direcciones
> privilegiadas: dos familias reales en el caso hiperbólico, una dirección
> doble en el parabólico y ninguna dirección característica real en el
> elíptico.

---

# 1. Ecuaciones de primer orden

## 1.1 Transporte y características

Para

\[
u_t+b(x,t)\cdot\nabla u=f(x,t,u),\qquad u(x,0)=g(x),
\]

se introduce la característica \(X(s)\) y el valor \(U(s)\):

\[
\boxed{
\begin{aligned}
X'(s)&=b(X(s),s),\\
U'(s)&=f(X(s),s,U(s)),\\
U(s)&=u(X(s),s).
\end{aligned}}
\]

Si la característica termina en \((x,t)\), se usa
\(X(t;t,x)=x\). Cuando \(f\) no depende de \(u\),

\[
\boxed{
u(x,t)=g(X(0;t,x))
+\int_0^t f(X(s;t,x),s)\,ds.}
\]

Para velocidad constante \(b\equiv c\) y \(f=0\),

\[
\boxed{u(x,t)=g(x-ct).}
\]

> **Lectura física.** \(X(s)\) es la trayectoria de una partícula. En
> transporte puro, el valor de \(u\) viaja con la partícula sin deformarse.

### Qué verificar

- que \(X\) pase por el punto donde se pide la solución;
- que \(u(x,0)=g(x)\);
- que la derivada total sobre \(X\) reproduzca la EDP.

## 1.2 Sistema característico cuasilineal

Para una ecuación en dos variables

\[
a(x,y,u)u_x+b(x,y,u)u_y=c(x,y,u),
\]

el sistema característico es

\[
\boxed{
\frac{dx}{ds}=a,\qquad
\frac{dy}{ds}=b,\qquad
\frac{du}{ds}=c.}
\]

Para datos sobre una curva

\[
(x,y)=\gamma(r)=(x_0(r),y_0(r)),\qquad u(\gamma(r))=u_0(r),
\]

se inicializa

\[
x(r,0)=x_0(r),\quad y(r,0)=y_0(r),\quad u(r,0)=u_0(r).
\]

La condición de transversalidad es

\[
\boxed{
\det
\begin{pmatrix}
x_0'(r)&a(\gamma(r),u_0(r))\\
y_0'(r)&b(\gamma(r),u_0(r))
\end{pmatrix}
\neq0.}
\]

> **Lectura geométrica.** La curva de datos debe cortar las características.
> Si es tangente a ellas, no etiqueta de manera única las trayectorias y puede
> fallar existencia o unicidad.

## 1.3 Compatibilidad sobre una curva

Si \(p=u_x\) y \(q=u_y\), los datos iniciales deben satisfacer

\[
\boxed{
p_0x_0'(r)+q_0y_0'(r)=u_0'(r)}
\]

y también la ecuación original sobre la curva:

\[
\boxed{
a(\gamma,u_0)p_0+b(\gamma,u_0)q_0=c(\gamma,u_0).}
\]

Estas dos ecuaciones permiten determinar \(p_0,q_0\) cuando el determinante de
transversalidad no se anula.

> **Mnemotecnia.** Una ecuación viene de derivar el dato **a lo largo de la
> curva**; la otra viene de derivar **a lo largo de la característica**.

## 1.4 Flujo y jacobiano

Sea \(X(t;\xi)\) el flujo de

\[
\dot X=b(X,t),\qquad X(0;\xi)=\xi.
\]

Su jacobiano \(J(t,\xi)=\det D_\xi X(t;\xi)\) satisface la fórmula de
Liouville:

\[
\boxed{
J'(t,\xi)=(\nabla\cdot b)(X(t;\xi),t)J(t,\xi)}
\]

y por tanto

\[
\boxed{
J(t,\xi)=
\exp\left(\int_0^t(\nabla\cdot b)(X(s;\xi),s)\,ds\right).}
\]

Para la ecuación de continuidad

\[
\rho_t+\nabla\cdot(\rho b)=0,
\]

se conserva

\[
\boxed{\rho(X(t;\xi),t)J(t,\xi)=\rho_0(\xi).}
\]

> **Lectura física.** \(J\) mide cuánto se expande un pequeño volumen de
> partículas. Si el volumen crece, la densidad disminuye para conservar masa.

## 1.5 Pérdida de regularidad en Burgers

Para

\[
u_t+uu_x=0,\qquad u(x,0)=g(x),
\]

las características cumplen

\[
\boxed{u=g(\xi),\qquad x=\xi+t\,g(\xi).}
\]

La parametrización deja de ser invertible cuando

\[
\frac{\partial x}{\partial\xi}=1+t\,g'(\xi)=0.
\]

Si \(\min g'<0\), el primer tiempo de ruptura es

\[
\boxed{t_*=-\frac1{\min_\xi g'(\xi)}.}
\]

> **Lectura geométrica.** Las características se cruzan. \(u\) puede seguir
> acotada, pero su pendiente se vuelve infinita antes de formarse un choque.

## 1.6 Ecuaciones completamente no lineales: Charpit

Para

\[
F(x,y,u,p,q)=0,\qquad p=u_x,\quad q=u_y,
\]

el sistema de Charpit es

\[
\boxed{
\begin{aligned}
\dot x&=F_p,\\
\dot y&=F_q,\\
\dot u&=pF_p+qF_q,\\
\dot p&=-F_x-pF_u,\\
\dot q&=-F_y-qF_u.
\end{aligned}}
\]

> **Lectura geométrica.** Ya no basta mover el punto \((x,y,u)\): también se
> transporta el plano tangente, descrito por \((p,q)\).

## 1.7 Leyes de conservación y formulación débil

Para

\[
u_t+f(u)_x=0,
\]

la formulación débil es

\[
\boxed{
\iint_{\mathbb R\times(0,\infty)}
\big(u\varphi_t+f(u)\varphi_x\big)\,dx\,dt
+\int_{\mathbb R}u_0(x)\varphi(x,0)\,dx=0.}
\]

Un salto \(u_L\to u_R\) sobre \(x=st\) debe cumplir Rankine–Hugoniot:

\[
\boxed{
s[u]=[f(u)],\qquad
s=\frac{f(u_L)-f(u_R)}{u_L-u_R}.}
\]

> **Lectura física.** El flujo que entra y sale de un volumen móvil debe
> compensar la masa transportada por el frente.

## 1.8 Entropía y condición de Lax

Un par de entropía \((\eta,q)\) satisface

\[
\boxed{q'(u)=\eta'(u)f'(u)}
\]

y una solución entrópica obedece

\[
\boxed{\eta(u)_t+q(u)_x\le0}
\]

en distribuciones. Las entropías de Kruzhkov son

\[
\eta_k(u)=|u-k|,\qquad
q_k(u)=\operatorname{sgn}(u-k)\big(f(u)-f(k)\big).
\]

Para flujo estrictamente convexo, un choque de Lax cumple

\[
\boxed{f'(u_R)<s<f'(u_L).}
\]

> **Lectura geométrica.** Las características entran al choque desde ambos
> lados. Si salen del frente, el salto no es la solución física seleccionada.

## 1.9 Problema de Riemann

Con

\[
u_0(x)=
\begin{cases}
u_L,&x<0,\\
u_R,&x>0,
\end{cases}
\]

la solución es autosemejante: \(u(x,t)=U(\xi)\), \(\xi=x/t\).

Para flujo convexo:

- si \(u_L>u_R\), aparece un choque con velocidad Rankine–Hugoniot;
- si \(u_L<u_R\), aparece una rarefacción:

\[
\boxed{
U(\xi)=
\begin{cases}
u_L,&\xi<f'(u_L),\\
(f')^{-1}(\xi),&f'(u_L)\le\xi\le f'(u_R),\\
u_R,&\xi>f'(u_R).
\end{cases}}
\]

Para Burgers, \(f(u)=u^2/2\), de modo que

\[
s=\frac{u_L+u_R}{2},
\qquad
U(\xi)=\xi\quad\text{dentro de una rarefacción}.
\]

Para tráfico LWR,

\[
\boxed{f(\rho)=v_{\max}\rho\left(1-\frac{\rho}{\rho_{\max}}\right),}
\]

que es cóncavo: el criterio choque/rarefacción se invierte respecto del flujo
convexo.

---

# 2. Ecuación de onda

## 2.1 d'Alembert en una dimensión

Para

\[
u_{tt}-c^2u_{xx}=0,\qquad
u(x,0)=f(x),\quad u_t(x,0)=g(x),
\]

\[
\boxed{
u(x,t)=
\frac{f(x-ct)+f(x+ct)}2
+\frac1{2c}\int_{x-ct}^{x+ct}g(y)\,dy.}
\]

> **Lectura física.** El desplazamiento inicial se divide en dos ondas que
> viajan a velocidades \(\pm c\). La velocidad inicial llena el interior del
> cono.

El valor \(u(x,t)\) sólo depende de los datos en

\[
\boxed{[x-ct,x+ct].}
\]

Ésta es la base del cono pasado del punto \((x,t)\).

## 2.2 Variables características

Con

\[
\xi=x-ct,\qquad \eta=x+ct,
\]

se tiene

\[
u_{tt}-c^2u_{xx}=-4c^2u_{\xi\eta}.
\]

Así, la ecuación homogénea implica

\[
u_{\xi\eta}=0
\quad\Longrightarrow\quad
\boxed{u(x,t)=F(x-ct)+G(x+ct).}
\]

> **Lectura geométrica.** Las rectas \(x\mp ct=\text{constante}\) son las dos
> familias características.

## 2.3 Semirrecta y método de reflexión

En \(x>0\):

- Dirichlet homogénea \(u(0,t)=0\): extensión **impar** de \(f,g\);
- Neumann homogénea \(u_x(0,t)=0\): extensión **par** de \(f,g\).

Para el dato \(h\) definido en \(x>0\),

\[
h_{\rm impar}(x)=
\begin{cases}
h(x),&x>0,\\
-h(-x),&x<0,
\end{cases}
\qquad
h_{\rm par}(x)=h(|x|).
\]

> **Lectura física.** En Dirichlet el pulso reflejado cambia de signo; en
> Neumann conserva el signo.

Compatibilidad básica en la esquina:

\[
u(0,t)=0\Rightarrow f(0)=0,
\qquad
u_x(0,t)=0\Rightarrow f'(0)=0.
\]

## 2.4 Intervalo finito y series de Fourier

Para \(0<x<L\), extremos fijos y datos \(f,g\),

\[
u_{tt}-c^2u_{xx}=0,\qquad u(0,t)=u(L,t)=0,
\]

\[
\boxed{
u(x,t)=\sum_{n=1}^\infty
\left(
a_n\cos(\omega_nt)+\frac{b_n}{\omega_n}\sin(\omega_nt)
\right)
\sin\frac{n\pi x}{L},}
\]

donde

\[
\omega_n=\frac{cn\pi}{L},
\]

\[
\boxed{
a_n=\frac2L\int_0^L f(x)\sin\frac{n\pi x}{L}\,dx,\qquad
b_n=\frac2L\int_0^L g(x)\sin\frac{n\pi x}{L}\,dx.}
\]

> **Lectura física.** Cada seno es un modo normal con nodos en los extremos.
> La cuerda es la superposición de osciladores con frecuencias \(\omega_n\).

## 2.5 Duhamel en una dimensión

Para datos iniciales cero,

\[
u_{tt}-c^2u_{xx}=F(x,t),
\]

\[
\boxed{
u(x,t)=\frac1{2c}
\int_0^t
\int_{x-c(t-s)}^{x+c(t-s)}
F(y,s)\,dy\,ds.}
\]

Con datos no nulos se suma la solución de d'Alembert.

> **Lectura física.** La fuerza aplicada en el tiempo \(s\) genera una onda
> que evoluciona durante \(t-s\).

## 2.6 Energía

En \((0,L)\),

\[
\boxed{
E(t)=\frac12\int_0^L
\big(u_t^2+c^2u_x^2\big)\,dx.}
\]

Si \(u_{tt}-c^2u_{xx}=F\),

\[
\boxed{
E'(t)=c^2[u_xu_t]_0^L+\int_0^L Fu_t\,dx.}
\]

Con frontera homogénea apropiada y \(F=0\),

\[
\boxed{E(t)=E(0).}
\]

> **Lectura física.** La energía cambia por el flujo en la frontera y por el
> trabajo de la fuerza. No se debe borrar el término de frontera sin explicar
> por qué se anula.

## 2.7 Fórmula de Kirchhoff en \(\mathbb R^3\)

Sea

\[
M_rh(x)=\frac1{4\pi r^2}\int_{\partial B_r(x)}h(y)\,dS_y.
\]

Para datos \(f,g\),

\[
\boxed{
u(x,t)=\partial_t\big[tM_{ct}f(x)\big]+tM_{ct}g(x).}
\]

Equivalentemente,

\[
u(x,t)=
\partial_t\left[
\frac1{4\pi c^2t}
\int_{\partial B_{ct}(x)}f(y)\,dS_y
\right]
+\frac1{4\pi c^2t}
\int_{\partial B_{ct}(x)}g(y)\,dS_y.
\]

> **Lectura geométrica.** En tres dimensiones la información relevante está
> sobre la esfera \(|y-x|=ct\), no en todo su interior.

## 2.8 Fórmula de Poisson en \(\mathbb R^2\)

\[
\boxed{
\begin{aligned}
u(x,t)
&=\partial_t\left[
\frac1{2\pi c}
\int_{B_{ct}(x)}
\frac{f(y)}{\sqrt{c^2t^2-|x-y|^2}}\,dy
\right]\\
&\quad+
\frac1{2\pi c}
\int_{B_{ct}(x)}
\frac{g(y)}{\sqrt{c^2t^2-|x-y|^2}}\,dy.
\end{aligned}}
\]

> **Lectura geométrica.** En dos dimensiones contribuye todo el disco. Por
> eso puede quedar una cola después de pasar el frente: falla el principio
> fuerte de Huygens.

## 2.9 Ondas radiales tridimensionales

Si \(u=u(r,t)\) en \(\mathbb R^3\), entonces

\[
u_{tt}-c^2\left(u_{rr}+\frac2r u_r\right)=0.
\]

Definiendo

\[
\boxed{v(r,t)=r\,u(r,t),}
\]

se obtiene

\[
\boxed{v_{tt}-c^2v_{rr}=0,\qquad v(0,t)=0.}
\]

> **Mnemotecnia.** Una onda radial 3D se convierte en una onda 1D al
> multiplicar por \(r\).

---

# 3. Ecuaciones elípticas

## 3.1 Solución fundamental de \(-\Delta\)

\[
\boxed{
\Phi(x)=
\begin{cases}
\dfrac1{2\pi}\log\dfrac1{|x|},&n=2,\\[6pt]
\dfrac1{(n-2)|S^{n-1}|}|x|^{2-n},&n\ge3.
\end{cases}}
\]

En distribuciones,

\[
\boxed{-\Delta\Phi=\delta_0.}
\]

Por ello, en todo el espacio,

\[
\boxed{u=\Phi*f\quad\Longrightarrow\quad-\Delta u=f}
\]

bajo hipótesis que permitan la convolución.

> **Lectura física.** \(\Phi\) es el potencial producido por una fuente
> puntual. Su flujo a través de una esfera que encierra el origen es constante.

Identidad radial útil:

\[
\boxed{\Delta(r^\alpha)=\alpha(\alpha+n-2)r^{\alpha-2}.}
\]

## 3.2 Identidades de Green

Primera identidad:

\[
\boxed{
\int_\Omega
\big(\nabla u\cdot\nabla v+u\Delta v\big)\,dx
=\int_{\partial\Omega}u\,\partial_\nu v\,dS.}
\]

Segunda identidad:

\[
\boxed{
\int_\Omega(u\Delta v-v\Delta u)\,dx
=
\int_{\partial\Omega}
\big(u\partial_\nu v-v\partial_\nu u\big)\,dS.}
\]

> **Mnemotecnia.** Green es integración por partes para el Laplaciano; el
> precio de mover \(\Delta\) es un flujo normal en la frontera.

## 3.3 Propiedad del promedio

Si \(\Delta u=0\) y \(\overline{B_r(x_0)}\subset\Omega\),

\[
\boxed{
u(x_0)=
\fint_{\partial B_r(x_0)}u\,dS
=
\fint_{B_r(x_0)}u\,dx.}
\]

> **Lectura geométrica.** El valor central está perfectamente balanceado por
> sus alrededores. No puede ser un pico interior aislado.

Consecuencias que conviene asociar:

- principio fuerte del máximo;
- desigualdad de Harnack para funciones armónicas positivas;
- teorema de Liouville: armónica y acotada en \(\mathbb R^n\) implica
  constante;
- suavidad y analiticidad interior.

## 3.4 Principio del máximo y comparación

Si

\[
\Delta u\ge0\quad\text{en }\Omega,
\]

entonces \(u\) es subarmónica y

\[
\boxed{\max_{\overline\Omega}u=\max_{\partial\Omega}u}
\]

para \(\Omega\) acotado y con regularidad suficiente.

Equivalentemente, si \(-\Delta u\ge0\), el mínimo está en la frontera.

Para comparar \(u,v\):

\[
-\Delta u\le-\Delta v\ \text{en }\Omega,
\qquad
u\le v\ \text{en }\partial\Omega
\quad\Longrightarrow\quad
\boxed{u\le v\ \text{en }\Omega.}
\]

> **Lectura física.** Una membrana en equilibrio sin una fuente apropiada no
> puede formar un máximo interior estricto.

## 3.5 Harnack, Liouville y Perron

Si \(u>0\) es armónica y \(K\Subset\Omega\), la desigualdad de Harnack dice

\[
\boxed{
\sup_Ku\le C(K,\Omega)\inf_Ku.}
\]

Al aplicar estimaciones interiores sobre bolas cada vez más grandes se obtiene
Liouville:

\[
\boxed{
u\text{ armónica y acotada en }\mathbb R^n
\quad\Longrightarrow\quad
u\text{ constante}.}
\]

Para datos \(g\) en la frontera, la familia inferior de Perron es

\[
\mathcal S_g=
\left\{
v\text{ subarmónica en }\Omega:
\limsup_{x\to\xi}v(x)\le g(\xi)
\right\},
\]

y la candidata a solución es

\[
\boxed{u(x)=\sup_{v\in\mathcal S_g}v(x).}
\]

Una barrera en \(\xi\in\partial\Omega\) es una función superarmónica positiva
que tiende a cero en \(\xi\) y permanece separada de cero lejos de \(\xi\).
Su existencia obliga a que la envolvente de Perron recupere \(g(\xi)\).

> **Lectura geométrica.** Harnack impide oscilaciones extremas de una función
> armónica positiva. Perron apila todas las subsoluciones y las barreras
> sujetan la envolvente al dato de frontera.

## 3.6 Función de Green y representación

Para el operador \(-\Delta\),

\[
\boxed{
-\Delta_xG(x,y)=\delta_y,\qquad
G(x,y)=0\text{ para }x\in\partial\Omega.}
\]

Si

\[
-\Delta u=f\text{ en }\Omega,\qquad u=g\text{ en }\partial\Omega,
\]

entonces

\[
\boxed{
u(x)=
\int_\Omega G(x,y)f(y)\,dy
-\int_{\partial\Omega}
g(y)\partial_{\nu_y}G(x,y)\,dS_y.}
\]

El núcleo de Poisson es

\[
\boxed{P(x,y)=-\partial_{\nu_y}G(x,y).}
\]

Además, para el Laplaciano con condiciones simétricas,

\[
\boxed{G(x,y)=G(y,x).}
\]

> **Lectura física.** \(G(x,y)\) es la respuesta observada en \(x\) ante una
> fuente puntual colocada en \(y\), con la frontera fijada.

## 3.7 Núcleo de Poisson

Para la bola \(B_R(0)\), \(y\in\partial B_R\),

\[
\boxed{
P_R(x,y)=
\frac{R^2-|x|^2}
{R|S^{n-1}|\,|x-y|^n}.}
\]

La solución de Dirichlet es

\[
\boxed{
u(x)=\int_{\partial B_R}P_R(x,y)g(y)\,dS_y.}
\]

Para el semiespacio \(\mathbb R^n_+=\{x_n>0\}\),

\[
\boxed{
P(x',x_n;y')=
\frac{\Gamma(n/2)}{\pi^{n/2}}
\frac{x_n}
{\left(|x'-y'|^2+x_n^2\right)^{n/2}}.}
\]

> **Lectura probabilística.** \(P(x,y)dS_y\) es la distribución del punto de
> salida en la frontera de un movimiento browniano iniciado en \(x\).

## 3.8 Método de imágenes

En el semiespacio, si \(y^*=(y',-y_n)\),

\[
\boxed{G(x,y)=\Phi(x-y)-\Phi(x-y^*).}
\]

> **Lectura geométrica.** La fuente reflejada con signo opuesto hace que el
> potencial se anule en el plano frontera.

## 3.9 Energía y principio de Dirichlet

Para \(-\Delta u=f\) y datos de frontera fijados,

\[
\boxed{
\mathcal E[v]=
\frac12\int_\Omega|\nabla v|^2\,dx
-\int_\Omega fv\,dx.}
\]

La primera variación es

\[
\left.\frac d{d\varepsilon}
\mathcal E[u+\varepsilon\varphi]\right|_{\varepsilon=0}
=
\int_\Omega\nabla u\cdot\nabla\varphi\,dx
-\int_\Omega f\varphi\,dx.
\]

Por tanto, la formulación débil es

\[
\boxed{
\int_\Omega\nabla u\cdot\nabla\varphi\,dx
=\int_\Omega f\varphi\,dx
\qquad\forall\varphi\in H_0^1(\Omega).}
\]

> **Lectura física.** La solución es la configuración de mínima energía entre
> todas las superficies con la misma frontera.

## 3.10 Valores propios y resonancia

\[
\boxed{
-\Delta\phi_k=\lambda_k\phi_k,\qquad
\phi_k|_{\partial\Omega}=0.}
\]

Si \(\{\phi_k\}\) es una base ortonormal y

\[
(-\Delta-\lambda)u=f,
\]

entonces, fuera del espectro,

\[
\boxed{
u=\sum_k
\frac{\langle f,\phi_k\rangle}
{\lambda_k-\lambda}\phi_k.}
\]

En resonancia \(\lambda=\lambda_j\), se necesita

\[
\boxed{\langle f,\phi_j\rangle=0}
\]

para cada modo resonante. Si existe solución, no es única: puede sumarse un
elemento del autoespacio resonante.

> **Lectura física.** Cerca de una frecuencia propia la respuesta se
> amplifica. En resonancia, una fuerza con componente en ese modo impide el
> equilibrio.

---

# 4. Ecuación del calor

En esta sección se usa

\[
u_t-\kappa\Delta u=F,\qquad \kappa>0.
\]

## 4.1 Núcleo del calor

\[
\boxed{
\Gamma_\kappa(x,t)=
\frac1{(4\pi\kappa t)^{n/2}}
\exp\left(-\frac{|x|^2}{4\kappa t}\right),
\qquad t>0.}
\]

Para el problema de Cauchy homogéneo,

\[
\boxed{
u(x,t)=(\Gamma_\kappa(\cdot,t)*g)(x).}
\]

Propiedades que conviene memorizar:

\[
\int_{\mathbb R^n}\Gamma_\kappa(x,t)\,dx=1,
\qquad
\int x_i\Gamma_\kappa(x,t)\,dx=0,
\]

\[
\boxed{
\int_{\mathbb R^n}|x|^2\Gamma_\kappa(x,t)\,dx=2n\kappa t.}
\]

Semigrupo:

\[
\boxed{\Gamma_{\kappa,t}*\Gamma_{\kappa,s}
=\Gamma_{\kappa,t+s}.}
\]

> **Lectura física.** Una masa puntual se vuelve instantáneamente una
> gaussiana positiva. Su anchura es del orden de \(\sqrt{\kappa t}\).

## 4.2 Escalamiento parabólico

Si \(u_t-\kappa\Delta u=0\), entonces

\[
\boxed{u_r(x,t)=u(rx,r^2t)}
\]

también satisface la ecuación.

> **Mnemotecnia.** Duplicar la escala espacial multiplica por cuatro la escala
> temporal.

## 4.3 Duhamel

Para

\[
u_t-\kappa\Delta u=F,\qquad u(x,0)=g(x),
\]

en todo el espacio,

\[
\boxed{
u(x,t)=
\Gamma_{\kappa,t}*g(x)
+\int_0^t
\Gamma_{\kappa,t-s}*F(\cdot,s)(x)\,ds.}
\]

> **Lectura física.** El calor depositado en el instante \(s\) difunde
> durante \(t-s\).

## 4.4 Frontera parabólica y principio del máximo

Para \(\Omega_T=\Omega\times(0,T]\),

\[
\boxed{
\Gamma_T=
(\overline\Omega\times\{0\})
\cup
(\partial\Omega\times[0,T])}
\]

es la frontera parabólica.

Si

\[
u_t-\kappa\Delta u\le0,
\]

entonces

\[
\boxed{
\max_{\overline{\Omega_T}}u
=\max_{\Gamma_T}u.}
\]

> **Lectura geométrica.** La tapa \(t=T\) no es dato: el tiempo tiene
> orientación. Un máximo puede entrar desde el pasado o desde la pared
> lateral, no desde el futuro.

Comparación:

\[
u_t-\kappa\Delta u
\le
v_t-\kappa\Delta v,
\qquad
u\le v\text{ en }\Gamma_T
\quad\Longrightarrow\quad
\boxed{u\le v.}
\]

## 4.5 Principio fuerte y positividad

Si una solución alcanza un máximo interior global en \((x_0,t_0)\), entonces
es constante en la componente espacial accesible para tiempos anteriores a
\(t_0\).

En todo el espacio, si \(g\ge0\) y \(g\not\equiv0\),

\[
\boxed{
(\Gamma_{\kappa,t}*g)(x)>0
\qquad(t>0).}
\]

> **Lectura física.** El calor tiene velocidad de propagación infinita: una
> perturbación no negativa se siente inmediatamente en todo punto.

## 4.6 Semirrecta: fuentes imagen

Para \(x>0\), dato \(g\) y frontera Dirichlet homogénea,

\[
\boxed{
u(x,t)=
\int_0^\infty
\big[
\Gamma_\kappa(x-y,t)-\Gamma_\kappa(x+y,t)
\big]g(y)\,dy.}
\]

Para Neumann homogénea,

\[
\boxed{
u(x,t)=
\int_0^\infty
\big[
\Gamma_\kappa(x-y,t)+\Gamma_\kappa(x+y,t)
\big]g(y)\,dy.}
\]

> **Mnemotecnia.** Dirichlet resta la imagen; Neumann la suma.

## 4.7 Intervalo y Fourier

Para

\[
u_t-\kappa u_{xx}=0,\qquad
u(0,t)=u(L,t)=0,\qquad u(x,0)=g(x),
\]

\[
\boxed{
u(x,t)=
\sum_{n=1}^\infty
g_n e^{-\kappa(n\pi/L)^2t}
\sin\frac{n\pi x}{L},}
\]

\[
\boxed{
g_n=\frac2L\int_0^Lg(x)\sin\frac{n\pi x}{L}\,dx.}
\]

Con una fuente \(F\), cada coeficiente satisface

\[
\boxed{
u_n'(t)+\lambda_nu_n(t)=F_n(t),\qquad
\lambda_n=\kappa\left(\frac{n\pi}{L}\right)^2,}
\]

y

\[
\boxed{
u_n(t)=e^{-\lambda_nt}g_n+
\int_0^te^{-\lambda_n(t-s)}F_n(s)\,ds.}
\]

> **Lectura física.** Los modos altos tienen mayor curvatura y decaen mucho
> más rápido.

## 4.8 Frontera no homogénea: levantamiento

Si

\[
u(0,t)=a(t),\qquad u(L,t)=b(t),
\]

se toma

\[
\boxed{
\ell(x,t)=a(t)+\frac{x}{L}\big(b(t)-a(t)\big),\qquad v=u-\ell.}
\]

Entonces \(v\) tiene frontera homogénea y

\[
\boxed{
v_t-\kappa v_{xx}=F-\ell_t+\kappa\ell_{xx}
=F-\ell_t.}
\]

Compatibilidad de orden cero:

\[
\boxed{g(0)=a(0),\qquad g(L)=b(0).}
\]

## 4.9 Energía y decaimiento

Con frontera Dirichlet homogénea,

\[
\boxed{
E(t)=\frac12\int_\Omega u(x,t)^2\,dx,}
\]

\[
\boxed{
E'(t)=-\kappa\int_\Omega|\nabla u|^2\,dx\le0.}
\]

Usando Poincaré,

\[
\int_\Omega|\nabla u|^2\ge\lambda_1\int_\Omega u^2,
\]

se obtiene

\[
\boxed{
\|u(\cdot,t)\|_{L^2}
\le e^{-\kappa\lambda_1t}
\|u(\cdot,0)\|_{L^2}.}
\]

> **Lectura física.** La difusión disipa contrastes; la energía no se conserva,
> decrece.

## 4.10 Suavizamiento

Para \(t>0\),

\[
\boxed{
D_x^\alpha u=(D_x^\alpha\Gamma_{\kappa,t})*g.}
\]

Una estimación básica es

\[
\boxed{
\|D_x^\alpha u(\cdot,t)\|_{L^p}
\le
C_{\alpha,\kappa}\,
t^{-|\alpha|/2}\|g\|_{L^p}.}
\]

Más generalmente,

\[
\boxed{
\|u(\cdot,t)\|_{L^q}
\le
C\,t^{-\frac n2(\frac1p-\frac1q)}
\|g\|_{L^p},
\qquad 1\le p\le q\le\infty.}
\]

> **Lectura física.** El calor borra primero las escalas pequeñas; por eso
> aparecen derivadas instantáneamente y los modos altos decaen antes.

## 4.11 Tychonoff y Widder

- **Tychonoff:** sin una condición de crecimiento espacial pueden existir
  soluciones no triviales con dato inicial cero. La unicidad global necesita
  especificar la clase de crecimiento.
- **Widder:** una solución global no negativa del calor admite, bajo las
  hipótesis del teorema, una representación por el núcleo del calor contra
  una medida positiva.

> **Idea común.** Tychonoff muestra que el crecimiento en el infinito puede
> destruir la unicidad; la positividad de Widder devuelve rigidez.

---

# 5. Fórmulas que se confunden con frecuencia

| Situación | Fórmula correcta | Error típico |
|---|---|---|
| Burgers | \(x=\xi+tg(\xi)\) | poner \(x=\xi-tu\) |
| Ruptura | \(1+tg'(\xi)=0\) | buscar sólo que \(u\to\infty\) |
| Rankine–Hugoniot | \(s=[f]/[u]\) | usar \(s=f'(u)\) para un salto |
| Onda 1D | integra \(g\) en \([x-ct,x+ct]\) | intercambiar \(f\) y \(g\) |
| Duhamel de onda | radio \(c(t-s)\) | usar \(cs\) |
| Green para \(-\Delta\) | \(P=-\partial_{\nu_y}G\) | perder el signo normal |
| Calor con fuente | \(\Gamma_{t-s}*F(s)\) | usar \(\Gamma_t*F(s)\) |
| Frontera parabólica | base inicial + pared lateral | incluir sólo \(t=T\) |
| Reflexión Dirichlet | extensión impar / resta | usar suma |
| Reflexión Neumann | extensión par / suma | usar resta |

---

# 6. Guion de respuesta para un problema del General

Antes de calcular, escribe:

1. **Tipo de EDP y dominio.**
2. **Datos iniciales y de frontera.**
3. **Hipótesis necesarias:** regularidad, compatibilidad, transversalidad,
   convexidad, signo o crecimiento.
4. **Herramienta elegida:** características, energía, Green, máximo,
   Fourier, núcleo o Duhamel.
5. **Representación o estimación.**
6. **Verificación:** EDP, dato inicial, frontera.
7. **Unicidad o selección física:** máximo, energía o entropía.
8. **Interpretación geométrica/física en una frase.**

## Preguntas de memoria

- ¿Puedo escribir el sistema característico completo sin consultar?
- ¿Sé distinguir transversalidad de compatibilidad?
- ¿Recuerdo el signo de Rankine–Hugoniot y la condición de Lax?
- ¿Puedo dibujar el cono de dependencia de la onda?
- ¿Sé por qué Huygens cambia entre dos y tres dimensiones?
- ¿Puedo reconstruir Green desde la solución fundamental y la frontera?
- ¿Distingo máximo elíptico de máximo parabólico?
- ¿Recuerdo por qué el núcleo del calor usa \(t-s\) en Duhamel?
- ¿Puedo explicar qué se conserva en onda y qué se disipa en calor?

Si alguna respuesta es “no”, vuelve al notebook canónico correspondiente en
[`GENERAL/`](GENERAL/README.md).
