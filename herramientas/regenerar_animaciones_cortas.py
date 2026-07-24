"""Regenera las tres animaciones que la auditoría detectó como demasiado breves.

Cada video usa la cronología didáctica 4 s + 8 s + 3 s:
perfil/estado inicial, evolución y estado final. Requiere NumPy, Matplotlib y
FFmpeg. El ejecutable de FFmpeg puede indicarse con la variable FFMPEG_BINARY.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# El entorno de Codex instala estas dependencias fuera del repositorio para no
# contaminarlo. En un entorno normal este bloque no cambia nada.
WORK_DIR = Path(__file__).resolve().parents[2]
LOCAL_PACKAGES = WORK_DIR / "python-packages"
if LOCAL_PACKAGES.exists():
    sys.path.insert(0, str(LOCAL_PACKAGES))
os.environ.setdefault("MPLCONFIGDIR", str(WORK_DIR / "mplconfig"))

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FFMpegWriter, FuncAnimation

try:
    import imageio_ffmpeg

    os.environ.setdefault("FFMPEG_BINARY", imageio_ffmpeg.get_ffmpeg_exe())
except ImportError:
    pass


ROOT = Path(__file__).resolve().parents[1]
# 15 fps es suficiente para estas evoluciones lentas y mantiene los archivos
# ligeros para abrirlos dentro de Jupyter.
FPS = 15
INITIAL_FRAMES = 4 * FPS
CORE_FRAMES = 8 * FPS
FINAL_FRAMES = 3 * FPS
TOTAL_FRAMES = INITIAL_FRAMES + CORE_FRAMES + FINAL_FRAMES

if binary := os.environ.get("FFMPEG_BINARY"):
    matplotlib.rcParams["animation.ffmpeg_path"] = binary


def timeline(last_state: int) -> np.ndarray:
    return np.concatenate(
        (
            np.zeros(INITIAL_FRAMES, dtype=int),
            np.rint(np.linspace(0, last_state, CORE_FRAMES)).astype(int),
            np.full(FINAL_FRAMES, last_state, dtype=int),
        )
    )


def save(animation: FuncAnimation, path: Path, title: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    writer = FFMpegWriter(
        fps=FPS,
        bitrate=2600,
        metadata={"title": title, "artist": "EDPs-Completo"},
    )
    animation.save(path, writer=writer, dpi=80)
    plt.close(animation._fig)
    print(path.relative_to(ROOT), "15.0 s", flush=True)


def membrane() -> None:
    n = 120
    x = np.linspace(-1.0, 1.0, n)
    xx, yy = np.meshgrid(x, x)
    h = x[1] - x[0]
    load = 8 * np.exp(-18 * ((xx - 0.25) ** 2 + (yy + 0.15) ** 2))
    load += 4 * np.exp(-25 * ((xx + 0.45) ** 2 + (yy - 0.35) ** 2))
    state = np.zeros_like(load)
    snapshots = [state.copy()]
    steps = [0]
    for iteration in range(1, 721):
        new = state.copy()
        new[1:-1, 1:-1] = 0.25 * (
            state[2:, 1:-1]
            + state[:-2, 1:-1]
            + state[1:-1, 2:]
            + state[1:-1, :-2]
            + h * h * load[1:-1, 1:-1]
        )
        state = 0.18 * state + 0.82 * new
        if iteration % 6 == 0:
            snapshots.append(state.copy())
            steps.append(iteration)
    snapshots = np.asarray(snapshots)
    playback = timeline(len(snapshots) - 1)

    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    image = ax.imshow(
        snapshots[0],
        origin="lower",
        extent=[-1, 1, -1, 1],
        cmap="viridis",
        vmin=0,
        vmax=float(snapshots[-1].max()),
    )
    fig.colorbar(image, ax=ax, label=r"desplazamiento $u(x,y)$")
    status = ax.text(
        0.02,
        0.97,
        "",
        transform=ax.transAxes,
        va="top",
        color="white",
        bbox={"boxstyle": "round", "facecolor": "black", "alpha": 0.68},
    )
    ax.set(
        title="Membrana elástica: relajación hacia el equilibrio",
        xlabel=r"$x$",
        ylabel=r"$y$",
    )

    def update(frame: int):
        index = int(playback[frame])
        image.set_data(snapshots[index])
        phase = (
            "condición inicial"
            if frame < INITIAL_FRAMES
            else "equilibrio"
            if frame >= INITIAL_FRAMES + CORE_FRAMES
            else "relajación"
        )
        status.set_text(f"{phase}\niteración {steps[index]}")
        return image, status

    animation = FuncAnimation(
        fig, update, frames=TOTAL_FRAMES, interval=1000 / FPS, blit=False
    )
    fig.tight_layout()
    save(
        animation,
        ROOT / "animaciones" / "03.1.B_membrana_relajacion.mp4",
        "Membrana elástica: relajación",
    )


def maximum_principle() -> None:
    n = 120
    boundary = np.linspace(0, 1, n)
    state = np.zeros((n, n), dtype=float)
    state[-1, :] = 0.25 + 0.75 * np.sin(np.pi * boundary) ** 2
    state[0, :] = 0.10 + 0.15 * boundary
    state[:, 0] = np.linspace(state[0, 0], state[-1, 0], n)
    state[:, -1] = np.linspace(state[0, -1], state[-1, -1], n)
    snapshots = [state.copy()]
    steps = [0]
    for iteration in range(1, 961):
        new = state.copy()
        new[1:-1, 1:-1] = 0.25 * (
            state[2:, 1:-1]
            + state[:-2, 1:-1]
            + state[1:-1, 2:]
            + state[1:-1, :-2]
        )
        state = new
        if iteration % 8 == 0:
            snapshots.append(state.copy())
            steps.append(iteration)
    snapshots = np.asarray(snapshots)
    playback = timeline(len(snapshots) - 1)
    boundary_values = np.concatenate(
        (
            snapshots[0][0, :],
            snapshots[0][-1, :],
            snapshots[0][1:-1, 0],
            snapshots[0][1:-1, -1],
        )
    )
    boundary_min = float(boundary_values.min())
    boundary_max = float(boundary_values.max())

    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    image = ax.imshow(
        snapshots[0],
        origin="lower",
        extent=[0, 1, 0, 1],
        cmap="plasma",
        vmin=boundary_min,
        vmax=boundary_max,
    )
    fig.colorbar(image, ax=ax, label=r"$u(x,y)$")
    status = ax.text(
        0.02,
        0.97,
        "",
        transform=ax.transAxes,
        va="top",
        color="white",
        bbox={"boxstyle": "round", "facecolor": "black", "alpha": 0.72},
    )
    ax.set(
        title="Principio del máximo: los extremos los controla la frontera",
        xlabel=r"$x$",
        ylabel=r"$y$",
    )

    def update(frame: int):
        index = int(playback[frame])
        values = snapshots[index]
        image.set_data(values)
        interior = values[1:-1, 1:-1]
        phase = (
            "dato de frontera e inicialización"
            if frame < INITIAL_FRAMES
            else "estado armónico"
            if frame >= INITIAL_FRAMES + CORE_FRAMES
            else "relajación armónica"
        )
        status.set_text(
            f"{phase}\n"
            f"frontera: [{boundary_min:.2f}, {boundary_max:.2f}]\n"
            f"interior: [{interior.min():.2f}, {interior.max():.2f}]"
        )
        return image, status

    animation = FuncAnimation(
        fig, update, frames=TOTAL_FRAMES, interval=1000 / FPS, blit=False
    )
    fig.tight_layout()
    save(
        animation,
        ROOT / "lAPLACE" / "animaciones" / "03.3.A_principio_debil_maximo.mp4",
        "Principio débil del máximo",
    )


def dalembert() -> None:
    c = 1.0
    x = np.linspace(-7.0, 7.0, 1400)

    def bump(z: np.ndarray, radius: float = 1.0) -> np.ndarray:
        q = np.asarray(z) / radius
        result = np.zeros_like(q)
        mask = np.abs(q) < 1.0
        result[mask] = np.exp(-1.0 / (1.0 - q[mask] ** 2) + 1.0)
        return result

    def f(z: np.ndarray) -> np.ndarray:
        return bump(z)

    def g(z: np.ndarray) -> np.ndarray:
        step = 1.0e-4
        return 0.32 * (bump(z + step, 0.8) - bump(z - step, 0.8)) / (2 * step)

    extended = np.linspace(-12.0, 12.0, 12000)
    velocity = g(extended)
    primitive = np.zeros_like(extended)
    primitive[1:] = np.cumsum(
        0.5 * (velocity[:-1] + velocity[1:]) * np.diff(extended)
    )

    def integral_g(z: np.ndarray) -> np.ndarray:
        return np.interp(z, extended, primitive)

    def right(z: np.ndarray) -> np.ndarray:
        return 0.5 * f(z) - integral_g(z) / (2 * c)

    def left(z: np.ndarray) -> np.ndarray:
        return 0.5 * f(z) + integral_g(z) / (2 * c)

    core_times = np.linspace(0.0, 4.2, CORE_FRAMES)
    times = np.concatenate(
        (
            np.zeros(INITIAL_FRAMES),
            core_times,
            np.full(FINAL_FRAMES, core_times[-1]),
        )
    )
    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    line_right, = ax.plot([], [], lw=1.8, label=r"$W(x-ct)$")
    line_left, = ax.plot([], [], lw=1.8, label=r"$V(x+ct)$")
    line_total, = ax.plot([], [], lw=2.8, color="black", label=r"$u(x,t)$")
    status = ax.text(
        0.02,
        0.94,
        "",
        transform=ax.transAxes,
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.85},
    )
    ax.set(
        xlim=(-7, 7),
        ylim=(-0.35, 1.15),
        xlabel=r"$x$",
        ylabel="amplitud",
        title="Fórmula de d'Alembert: separación en dos ondas viajeras",
    )
    ax.grid(alpha=0.25)
    ax.legend(loc="upper right")

    def update(frame: int):
        time = float(times[frame])
        w = right(x - c * time)
        v = left(x + c * time)
        line_right.set_data(x, w)
        line_left.set_data(x, v)
        line_total.set_data(x, w + v)
        phase = (
            "perfil y velocidad iniciales"
            if frame < INITIAL_FRAMES
            else "perfil final"
            if frame >= INITIAL_FRAMES + CORE_FRAMES
            else "propagación"
        )
        status.set_text(f"{phase}\n$t={time:.2f}$")
        return line_right, line_left, line_total, status

    animation = FuncAnimation(
        fig, update, frames=TOTAL_FRAMES, interval=1000 / FPS, blit=True
    )
    fig.tight_layout()
    save(
        animation,
        ROOT / "ONDA" / "animaciones" / "02_01_dAlembert_2K_120fps.mp4",
        "d'Alembert: ondas viajeras",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "animations",
        nargs="*",
        choices=("membrane", "maximum", "dalembert"),
        default=("membrane", "maximum", "dalembert"),
    )
    requested = parser.parse_args().animations
    if "membrane" in requested:
        membrane()
    if "maximum" in requested:
        maximum_principle()
    if "dalembert" in requested:
        dalembert()
