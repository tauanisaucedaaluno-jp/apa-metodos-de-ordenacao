# TP1: Métodos de Ordenação Autorais — IGIS

Trabalho Prático 1 da disciplina de **Análise e Projetos de Algoritmos (APA)** — Curso de Engenharia de Software.

Este repositório contém a concepção, formalização, implementação e validação experimental do algoritmo de ordenação autoral **IGIS (*Interpolation-Guided Insertion Sort*)**, além de implementações instrumentadas dos algoritmos clássicos da literatura para fins de comparação empírica.

---

## Sobre o Algoritmo: IGIS

O **IGIS (*Interpolation-Guided Insertion Sort*)** é uma evolução estrutural do método de ordenação por inserção (*Insertion Sort*).

### Raciocínio Projetual
No Insertion Sort clássico, a localização da posição correta de inserção do $i$-ésimo elemento é realizada por busca linear reversa, exigindo $O(i)$ comparações a cada iteração ($O(n^2)$ no caso médio). 

O **IGIS** substitui essa busca ingênua por uma **busca guiada por interpolação linear** (inspirada na busca interpolada de Perl-Reingold-Shamir):
1. **Estimativa Proporcional:** O índice provável do elemento é calculated com base na amplitude de valores entre os extremos do prefixo ordenado ($a[\text{low}]$ e $a[\text{high}]$).
2. **Estabilidade Garantida (Upper Bound):** A busca estreita o intervalo assegurando semântica de *upper bound*, de modo que elementos de mesmo valor permaneçam em sua ordem relativa original.
3. **Fallback Robusto (Princípio de Liskov):** Em intervalos degenerados ($a[\text{low}] == a[\text{high}]$) ou em coleções não-aritméticas (como strings ou objetos customizados), o algoritmo degrada graciosamente para ponto médio (`(low + high) // 2`), comportando-se com a robustez de uma busca binária.

### Complexidade Teórica
* **Comparações de Chaves:** $\Omega(n)$ no melhor caso, $\Theta(n \log \log n)$ no caso médio (distribuição uniforme) e $O(n^2)$ no pior caso adversarial.
* **Movimentações Físicas:** $\Theta(n^2)$ no caso médio e pior caso (devido aos deslocamentos contíguos em array).
* **Espaço Auxiliar:** $\Theta(1)$ (*in-place* e iterativo).
* **Estabilidade:** Sim.

---

## Estrutura do Repositório

```text
.
├── .gitignore                    # Arquivo de exclusão do Git
├── AGENTS.md                     # Diretrizes de arquitetura, SOLID e regras de desenvolvimento
├── CONTEXT.md                    # Documento de contexto, decisões de projeto e invariantes
├── README.md                     # Visão geral do repositório e guia de execução
├── TP1-Metodos-de-Ordenacao-Autorais.md  # Enunciado oficial do trabalho prático
├── codigo/                       # Implementações e infraestrutura de testes/benchmark
│   ├── Makefile                  # Automação de testes e benchmarks (make test_python, etc.)
│   ├── README.md                 # Instruções técnicas da pasta de código
│   ├── cpp/                      # Infraestrutura de suporte em C++17
│   │   ├── authorial.cpp         # Algoritmo DPES em C++
│   │   ├── authorial.hpp         # Cabeçalho do DPES
│   │   ├── benchmark.cpp         # Benchmark em C++
│   │   ├── classical.cpp         # Algoritmos clássicos em C++
│   │   ├── classical.hpp         # Cabeçalhos dos clássicos
│   │   └── test_runner.cpp       # Executor de testes em C++
│   └── python/                   # Implementação principal e oficial em Python 3
│       ├── authorial.py          # Algoritmo de referência do professor (DPES)
│       ├── benchmark.py          # Framework de benchmark e gerador de gráficos PNG
│       ├── classical.py          # Algoritmos clássicos instrumentados (Bubble, Insertion, Quick, etc.)
│       ├── metrics.py            # Contadores e métricas de instrumentação
│       ├── student_template.py   # Implementação do algoritmo autoral IGIS
│       └── test_suite.py         # Suíte oficial de testes de corretude
└── docs/                         # Documentação final, relatórios e artefatos gerados
    ├── analise_comparativa.md    # Análise Teórica e Empírica aprofundada (IGIS vs Clássicos)
    ├── benchmark_authorials_direct_comparison.png # Gráfico: confronto direto IGIS vs DPES
    ├── benchmark_authorials_side_by_side.png       # Gráfico: visualização lado a lado IGIS vs DPES
    ├── benchmark_results.md      # Tabelas brutas consolidadas do benchmark
    ├── benchmark_results.png     # Gráfico: panorama geral de todos os algoritmos
    ├── issues.md                 # Registro e rastreamento das 6 issues do projeto
    └── relatorio_tecnico.md      # Relatório Técnico Completo (Entregável Principal)
```

---

## Como Executar e Reproduzir os Testes e Benchmarks

### Pré-requisitos
* Python 3.10 ou superior.
* Biblioteca `matplotlib` para geração de gráficos (`pip install matplotlib`).

### 1. Testes Unitários do Algoritmo Autoral (IGIS)
Para rodar os testes de sanidade locais específicos do IGIS:
```bash
python codigo/python/student_template.py
```

### 2. Suíte Oficial Completa de Corretude
Para rodar a bateria oficial completa com todos os cenários obrigatórios (vazio, unitário, ordenado, invertido, idênticos, repetidos, negativos/floats, aleatórios e estabilidade):
```bash
python codigo/python/test_suite.py
```
*(ou via Makefile: `cd codigo && make test_python`)*

### 3. Reprodução do Benchmark e Geração dos Gráficos
Para rodar os experimentos quantitativos (variando $N$ e distribuições) e atualizar as tabelas e gráficos:
```bash
python codigo/python/benchmark.py
```
*(ou via Makefile: `cd codigo && make benchmark_python`)*

> **Nota:** Todos os artefatos de saída do benchmark (tabelas `.md` e os gráficos `.png`) são gerados e salvos automaticamente na pasta `docs/`.

---

## Status do Backlog de Issues

O desenvolvimento foi concluído seguindo o plano de 6 issues sequenciais:

- [x] **Issue #01:** Implementação Modular do Algoritmo Autoral (IGIS) com Instrumentação e SOLID.
- [x] **Issue #02:** Integração e Validação na Suíte Oficial de Corretude (100% de aprovação e estabilidade).
- [x] **Issue #03:** Integração no Framework de Benchmark e Coleta Experimental.
- [x] **Issue #04:** Análise Comparativa Empírica e Teórica vs. Métodos Clássicos (`docs/analise_comparativa.md`).
- [x] **Issue #05:** Redação do Relatório Técnico Completo (`docs/relatorio_tecnico.md`).
- [x] **Issue #06:** Revisão de Conformidade, Reprodutibilidade e Pacote de Entrega.
