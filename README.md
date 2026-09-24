# TP1: Métodos de Ordenação Autorais — IGIS

Trabalho Prático 1 da disciplina de **Análise e Projetos de Algoritmos (APA)** — Curso de Engenharia de Software.

Este repositório contém a concepção, formalização, implementação e validação experimental do algoritmo de ordenação autoral **IGIS (*Interpolation-Guided Insertion Sort*)**, além de implementações instrumentadas dos algoritmos clássicos da literatura para fins de comparação empírica.

---

## Sobre o Algoritmo: IGIS

O **IGIS (*Interpolation-Guided Insertion Sort*)** é uma evolução estrutural do método de ordenação por inserção (*Insertion Sort*).

### Raciocínio Projetual
No Insertion Sort clássico, a localização da posição correta de inserção do $i$-ésimo elemento é realizada por busca linear reversa, exigindo $O(i)$ comparações a cada iteração ($O(n^2)$ no caso médio). 

O **IGIS** substitui essa busca ingênua por uma **busca guiada por interpolação linear** (inspirada na busca interpolada de Perl-Reingold-Shamir):
1. **Estimativa Proporcional:** O índice provável do elemento é calculado com base na amplitude de valores entre os extremos do prefixo ordenado ($a[\text{low}]$ e $a[\text{high}]$).
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
├── codigo/
│   ├── Makefile                  # Comandos de automação
│   ├── README.md                 # Guia técnico da infraestrutura de código
│   ├── python/
│   │   ├── student_template.py   # Implementação oficial do algoritmo autoral (IGIS)
│   │   ├── test_suite.py         # Suíte de testes com todos os cenários obrigatórios
│   │   ├── classical.py          # Baselines clássicos (Bubble, Selection, Insertion, Merge, Quick)
│   │   ├── authorial.py          # DPES (Algoritmo de referência do professor)
│   │   ├── benchmark.py          # Framework de medição empírica e gráficos
│   │   └── metrics.py            # Utilitários de instrumentação
│   └── cpp/                      # Equivalentes em C++17
├── docs/
│   └── issues.md                 # Backlog organizado das 6 issues do projeto
├── CONTEXT.md                    # Documento unificado de contexto, decisões e invariantes
└── TP1-Metodos-de-Ordenacao-Autorais.md  # Enunciado oficial da disciplina
```

---

## Como Executar e Reproduzir os Testes

### Pré-requisitos
* Python 3.10 ou superior.

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
*(ou via Makefile: `make test_python` a partir do diretório `codigo/`)*

---

## Status do Backlog de Issues

O desenvolvimento está estruturado em 6 issues sequenciais:

- [x] **Issue #01:** Implementação Modular do Algoritmo Autoral (IGIS) com Instrumentação e SOLID.
- [x] **Issue #02:** Integração e Validação na Suíte Oficial de Corretude (100% de aprovação e estabilidade).
- [x] **Issue #03:** Integração no Framework de Benchmark e Coleta Experimental.
- [ ] **Issue #04:** Análise Comparativa Empírica e Teórica vs. Métodos Clássicos.
- [ ] **Issue #05:** Redação do Relatório Técnico Completo.
- [ ] **Issue #06:** Revisão de Conformidade, Reprodutibilidade e Pacote de Entrega.
