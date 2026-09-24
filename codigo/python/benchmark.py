"""
Framework de Benchmarking e Comparação de Algoritmos de Ordenação.
Gera tabelas estatísticas em Markdown, CSV e gráficos comparativos PNG.
"""

import argparse
from collections import defaultdict
import os
import random
import sys
import time
from typing import Callable, Dict, List, Tuple

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from authorial import dpes_sort
from classical import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort,
)
from student_template import my_authorial_sort


def generate_dataset(n: int, distribution: str) -> List[int]:
    """Gera vetores para testes com diferentes distribuições de dados."""
    if distribution == "random":
        return [random.randint(0, 10 * n) for _ in range(n)]
    elif distribution == "sorted":
        return list(range(n))
    elif distribution == "reverse":
        return list(range(n, 0, -1))
    elif distribution == "duplicates":
        return [random.choice([1, 2, 3, 5, 8]) for _ in range(n)]
    elif distribution == "almost_sorted":
        arr = list(range(n))
        swaps = max(1, n // 20)  # ~5% de trocas aleatórias
        for _ in range(swaps):
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    else:
        raise ValueError(f"Distribuição desconhecida: {distribution}")


def run_benchmark(
    algorithms: Dict[str, Callable[[List], Tuple[List, int, int]]],
    sizes: List[int],
    distributions: List[str],
    trials: int = 3,
) -> Dict[str, Dict[str, Dict[int, Dict[str, float]]]]:
    """
    Executa medições de tempo, comparações e movimentações para cada algoritmo,
    tamanho e distribuição.
    """
    # results[dist][alg_name][size] = {'time_ms': ..., 'comps': ..., 'moves': ...}
    results = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))

    for dist in distributions:
        print(f"\n[BENCHMARK] Executando testes para distribuicao: [{dist.upper()}]")
        for size in sizes:
            print(f"  -> Tamanho N = {size}...")
            # Gera datasets fixos por repetição para garantir comparação justa
            datasets = [generate_dataset(size, dist) for _ in range(trials)]

            for name, fn in algorithms.items():
                # Para métodos quadráticos em movimentação, evita tamanhos excessivos se N > 1500
                if size > 1500 and name in ("Bubble Sort", "Selection Sort", "Insertion Sort", "Authorial (IGIS)") and dist in ("random", "reverse"):
                    continue

                times = []
                comps = []
                moves = []

                for data in datasets:
                    data_copy = list(data)
                    start = time.perf_counter()
                    res, c, m = fn(data_copy)
                    elapsed_ms = (time.perf_counter() - start) * 1000.0

                    # Validação de sanidade
                    assert res == sorted(data), f"Erro de ordenação em {name}!"

                    times.append(elapsed_ms)
                    comps.append(c)
                    moves.append(m)

                results[dist][name][size] = {
                    "time_ms": sum(times) / len(times),
                    "comps": sum(comps) / len(comps),
                    "moves": sum(moves) / len(moves),
                }

    return results


def print_markdown_summary(results: dict, sizes: List[int], output_file: str = None):
    """
    Imprime e opcionalmente exporta tabelas formatadas em Markdown com os resultados comparativos:
    Tempo de Execução (ms), Número de Comparações e Número de Movimentações.
    """
    lines = []
    lines.append("# Relatório Experimental de Benchmarks — APA (TP1)")
    lines.append("")

    for dist, algs in results.items():
        lines.append(f"## Distribuição: `{dist.upper()}`")
        lines.append("")

        # 1. Tabela de Tempo de Execução
        lines.append("### 1. Tempo Médio de Execução (ms)")
        lines.append("")
        header = "| Algoritmo | " + " | ".join(f"N={s}" for s in sizes) + " |"
        sep = "| :--- | " + " | ".join(":---:" for _ in sizes) + " |"
        lines.append(header)
        lines.append(sep)
        for alg_name, size_data in algs.items():
            row = [alg_name]
            for s in sizes:
                if s in size_data:
                    row.append(f"{size_data[s]['time_ms']:.3f} ms")
                else:
                    row.append("—")
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")

        # 2. Tabela de Comparações
        lines.append("### 2. Número Médio de Comparações de Chaves")
        lines.append("")
        lines.append(header)
        lines.append(sep)
        for alg_name, size_data in algs.items():
            row = [alg_name]
            for s in sizes:
                if s in size_data:
                    row.append(f"{int(round(size_data[s]['comps'])):,}".replace(",", "."))
                else:
                    row.append("—")
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")

        # 3. Tabela de Movimentações
        lines.append("### 3. Número Médio de Movimentações de Elementos")
        lines.append("")
        lines.append(header)
        lines.append(sep)
        for alg_name, size_data in algs.items():
            row = [alg_name]
            for s in sizes:
                if s in size_data:
                    row.append(f"{int(round(size_data[s]['moves'])):,}".replace(",", "."))
                else:
                    row.append("—")
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")
        lines.append("---")
        lines.append("")

    content = "\n".join(lines)
    print(content)

    if output_file:
        os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\n[ARQUIVO] Tabelas completas salvas em Markdown em: {output_file}")


def plot_benchmark_results(results: dict, output_path: str = "benchmark_results.png"):
    """Gera gráficos consolidados com todos os algoritmos para Tempo, Comparações e Movimentações."""
    distributions = list(results.keys())
    fig, axes = plt.subplots(len(distributions), 3, figsize=(18, 4 * len(distributions)))

    if len(distributions) == 1:
        axes = [axes]

    for idx, dist in enumerate(distributions):
        ax_time = axes[idx][0]
        ax_comps = axes[idx][1]
        ax_moves = axes[idx][2]

        for alg_name, size_map in results[dist].items():
            sizes = sorted(size_map.keys())
            times = [size_map[s]["time_ms"] for s in sizes]
            comps = [size_map[s]["comps"] for s in sizes]
            moves = [size_map[s]["moves"] for s in sizes]

            is_student = "IGIS" in alg_name
            is_prof = "DPES" in alg_name
            lw = 2.5 if (is_student or is_prof) else 1.2
            alpha = 1.0 if (is_student or is_prof) else 0.7

            ax_time.plot(sizes, times, marker="o", label=alg_name, linewidth=lw, alpha=alpha)
            ax_comps.plot(sizes, comps, marker="s", label=alg_name, linewidth=lw, alpha=alpha)
            ax_moves.plot(sizes, moves, marker="^", label=alg_name, linewidth=lw, alpha=alpha)

        ax_time.set_title(f"Tempo de Execução (ms) — [{dist.title()}]", fontweight="bold")
        ax_time.set_xlabel("Tamanho da Entrada (N)")
        ax_time.set_ylabel("Tempo Médio (ms)")
        ax_time.grid(True, linestyle="--", alpha=0.6)
        ax_time.legend(fontsize=8)

        ax_comps.set_title(f"Comparações — [{dist.title()}]", fontweight="bold")
        ax_comps.set_xlabel("Tamanho da Entrada (N)")
        ax_comps.set_ylabel("Comparações")
        ax_comps.grid(True, linestyle="--", alpha=0.6)
        ax_comps.legend(fontsize=8)

        ax_moves.set_title(f"Movimentações — [{dist.title()}]", fontweight="bold")
        ax_moves.set_xlabel("Tamanho da Entrada (N)")
        ax_moves.set_ylabel("Movimentações")
        ax_moves.grid(True, linestyle="--", alpha=0.6)
        ax_moves.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"\n[GRAFICO] Grafico geral salvo com sucesso em: {output_path}")


def plot_authorials_side_by_side(results: dict, output_path: str = "benchmark_authorials_side_by_side.png"):
    """
    Gera gráficos comparativos separando o algoritmo autoral do aluno (IGIS)
    e o algoritmo autoral do professor (DPES) lado a lado para cada distribuição.
    """
    distributions = list(results.keys())
    # 5 distribuições (linhas) x 2 colunas principais (Esquerda: IGIS do Aluno, Direita: DPES do Professor)
    fig, axes = plt.subplots(len(distributions), 2, figsize=(16, 4.5 * len(distributions)))

    if len(distributions) == 1:
        axes = [axes]

    for idx, dist in enumerate(distributions):
        ax_student = axes[idx][0]
        ax_prof = axes[idx][1]

        # Dados do IGIS (Aluno)
        if "Authorial (IGIS)" in results[dist]:
            size_map = results[dist]["Authorial (IGIS)"]
            sizes = sorted(size_map.keys())
            times = [size_map[s]["time_ms"] for s in sizes]
            comps = [size_map[s]["comps"] for s in sizes]
            moves = [size_map[s]["moves"] for s in sizes]

            ax_student.plot(sizes, comps, marker="o", color="#1f77b4", label="Comparações", linewidth=2.0)
            ax_student.plot(sizes, moves, marker="s", color="#ff7f0e", label="Movimentações", linewidth=2.0)
            ax_student.set_ylabel("Operações (Comparações / Movimentações)", color="#333333")
            ax_student.tick_params(axis="y")

            # Eixo secundário para tempo em ms
            ax_student_t = ax_student.twinx()
            ax_student_t.plot(sizes, times, marker="^", color="#2ca02c", linestyle="--", label="Tempo (ms)", linewidth=2.0)
            ax_student_t.set_ylabel("Tempo de Execução (ms)", color="#2ca02c")
            ax_student_t.tick_params(axis="y", labelcolor="#2ca02c")

            # Junção de legendas
            lines1, labels1 = ax_student.get_legend_handles_labels()
            lines2, labels2 = ax_student_t.get_legend_handles_labels()
            ax_student.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=8)

        ax_student.set_title(f"NOSSO ALGORITMO: IGIS — [{dist.title()}]", fontweight="bold", color="#0b4f6c")
        ax_student.set_xlabel("Tamanho da Entrada (N)")
        ax_student.grid(True, linestyle="--", alpha=0.6)

        # Dados do DPES (Professor)
        if "Authorial (DPES)" in results[dist]:
            size_map_p = results[dist]["Authorial (DPES)"]
            sizes_p = sorted(size_map_p.keys())
            times_p = [size_map_p[s]["time_ms"] for s in sizes_p]
            comps_p = [size_map_p[s]["comps"] for s in sizes_p]
            moves_p = [size_map_p[s]["moves"] for s in sizes_p]

            ax_prof.plot(sizes_p, comps_p, marker="o", color="#d62728", label="Comparações", linewidth=2.0)
            ax_prof.plot(sizes_p, moves_p, marker="s", color="#9467bd", label="Movimentações", linewidth=2.0)
            ax_prof.set_ylabel("Operações (Comparações / Movimentações)", color="#333333")
            ax_prof.tick_params(axis="y")

            # Eixo secundário para tempo em ms
            ax_prof_t = ax_prof.twinx()
            ax_prof_t.plot(sizes_p, times_p, marker="^", color="#8c564b", linestyle="--", label="Tempo (ms)", linewidth=2.0)
            ax_prof_t.set_ylabel("Tempo de Execução (ms)", color="#8c564b")
            ax_prof_t.tick_params(axis="y", labelcolor="#8c564b")

            lines1_p, labels1_p = ax_prof.get_legend_handles_labels()
            lines2_p, labels2_p = ax_prof_t.get_legend_handles_labels()
            ax_prof.legend(lines1_p + lines2_p, labels1_p + labels2_p, loc="upper left", fontsize=8)

        ax_prof.set_title(f"PROFESSOR: DPES — [{dist.title()}]", fontweight="bold", color="#780000")
        ax_prof.set_xlabel("Tamanho da Entrada (N)")
        ax_prof.grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"[GRAFICO] Grafico Lado a Lado (IGIS vs DPES) salvo com sucesso em: {output_path}")


def plot_authorials_direct_comparison(results: dict, output_path: str = "benchmark_authorials_direct_comparison.png"):
    """
    Gera comparação direta lado a lado entre IGIS e DPES para cada métrica:
    Tempo (ms), Comparações e Movimentações em cada distribuição.
    """
    distributions = list(results.keys())
    fig, axes = plt.subplots(len(distributions), 3, figsize=(18, 4 * len(distributions)))

    if len(distributions) == 1:
        axes = [axes]

    for idx, dist in enumerate(distributions):
        ax_time = axes[idx][0]
        ax_comps = axes[idx][1]
        ax_moves = axes[idx][2]

        # Comparação direta apenas entre IGIS (Aluno) e DPES (Professor)
        algs_to_compare = ["Authorial (IGIS)", "Authorial (DPES)"]
        colors = {"Authorial (IGIS)": "#0b4f6c", "Authorial (DPES)": "#c1121f"}
        markers = {"Authorial (IGIS)": "o", "Authorial (DPES)": "s"}

        for alg_name in algs_to_compare:
            if alg_name in results[dist]:
                size_map = results[dist][alg_name]
                sizes = sorted(size_map.keys())
                times = [size_map[s]["time_ms"] for s in sizes]
                comps = [size_map[s]["comps"] for s in sizes]
                moves = [size_map[s]["moves"] for s in sizes]

                ax_time.plot(sizes, times, marker=markers[alg_name], label=alg_name,
                             color=colors[alg_name], linewidth=2.2)
                ax_comps.plot(sizes, comps, marker=markers[alg_name], label=alg_name,
                              color=colors[alg_name], linewidth=2.2)
                ax_moves.plot(sizes, moves, marker=markers[alg_name], label=alg_name,
                              color=colors[alg_name], linewidth=2.2)

        ax_time.set_title(f"Tempo (ms) [IGIS vs DPES] — [{dist.title()}]", fontweight="bold")
        ax_time.set_xlabel("Tamanho N")
        ax_time.set_ylabel("Tempo (ms)")
        ax_time.grid(True, linestyle="--", alpha=0.6)
        ax_time.legend(fontsize=9)

        ax_comps.set_title(f"Comparações [IGIS vs DPES] — [{dist.title()}]", fontweight="bold")
        ax_comps.set_xlabel("Tamanho N")
        ax_comps.set_ylabel("Comparações")
        ax_comps.grid(True, linestyle="--", alpha=0.6)
        ax_comps.legend(fontsize=9)

        ax_moves.set_title(f"Movimentações [IGIS vs DPES] — [{dist.title()}]", fontweight="bold")
        ax_moves.set_xlabel("Tamanho N")
        ax_moves.set_ylabel("Movimentações")
        ax_moves.grid(True, linestyle="--", alpha=0.6)
        ax_moves.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"[GRAFICO] Grafico de Confronto Direto (IGIS vs DPES) salvo com sucesso em: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Benchmark de Algoritmos de Ordenação — APA")
    parser.add_argument("--trials", type=int, default=3, help="Número de repetições por teste")
    parser.add_argument("--plot", type=str, default="benchmark_results.png", help="Caminho para salvar o gráfico geral")
    parser.add_argument("--side-by-side", type=str, default="benchmark_authorials_side_by_side.png", help="Caminho para gráfico lado a lado dos autorais")
    parser.add_argument("--direct-comparison", type=str, default="benchmark_authorials_direct_comparison.png", help="Caminho para confronto direto IGIS vs DPES")
    parser.add_argument("--export-md", type=str, default="../../docs/benchmark_results.md", help="Exportar tabelas Markdown")
    args = parser.parse_args()

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Authorial (DPES)": dpes_sort,
        "Authorial (IGIS)": my_authorial_sort,
    }

    sizes = [10, 50, 100, 250, 500, 1000]
    distributions = ["random", "sorted", "reverse", "duplicates", "almost_sorted"]

    random.seed(42)
    results = run_benchmark(algorithms, sizes, distributions, trials=args.trials)

    # Determina caminho de exportação do markdown
    script_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.normpath(os.path.join(script_dir, args.export_md))

    print_markdown_summary(results, sizes, output_file=md_path)

    # 1. Gráfico Geral (Todos os algoritmos)
    plot_benchmark_results(results, args.plot)

    # 2. Gráfico Lado a Lado: O nosso (IGIS) à esquerda e o do Professor (DPES) à direita
    plot_authorials_side_by_side(results, args.side_by_side)

    # 3. Gráfico de Confronto Direto métrica a métrica (IGIS vs DPES)
    plot_authorials_direct_comparison(results, args.direct_comparison)


if __name__ == "__main__":
    main()
