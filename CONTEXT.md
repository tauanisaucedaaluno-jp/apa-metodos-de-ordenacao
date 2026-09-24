# CONTEXT.md — TP1 Análise e Projetos de Algoritmos (Ordenação Autoral)

Este documento resume o estado atual do projeto: o que foi pedido, o que já foi decidido e o que falta fazer. Serve como ponto de partida único para retomar o trabalho (por humano ou por um agente de IA).

## 1. O que é o trabalho

Disciplina: **Análise e Projetos de Algoritmos (APA)** — Trabalho Prático 1 (TP1).

Objetivo: conceber, formalizar, implementar e validar experimentalmente um **algoritmo de ordenação autoral** (inédito, ou adaptação estrutural profunda de um método conhecido — nunca uma variação cosmética).

Peso: 1,0 ponto na nota final (bloco TP = 3,0).

Critérios de nota:

| Critério | Peso |
|---|---|
| Raciocínio Projetual e Originalidade | 30% |
| Análise Teórica de Complexidade | 25% |
| Corretude e Validação Experimental | 25% |
| Qualidade da Documentação e Defesa | 10% |
| Declaração de Autoria e Pensamento Crítico | 10% |

**Regra de ouro do enunciado:** performance bruta não é o foco. Um algoritmo O(n²) bem explicado vale mais que um algoritmo rápido que o autor não sabe justificar.

Critérios de reprovação automática (nota 0,0): plágio/cópia sem atribuição, falha em qualquer cenário de teste obrigatório, incapacidade de explicar o algoritmo em arguição oral, ausência da declaração de uso de IA, ou ausência de código-fonte executável.

Enunciado completo: `TP1-Metodos-de-Ordenacao-Autorais.md` (convertido do PDF original do professor).

## 2. Pacote de código fornecido pelo professor

Extraído em `codigo/`, já contém toda a infraestrutura — **não precisa ser recriada**:

```
codigo/
├── Makefile
├── README.md
├── python/
│   ├── classical.py          # Bubble, Selection, Insertion, Merge, Quick (baseline, instrumentados)
│   ├── authorial.py          # DPES (Dual-Pivot Extremes Sieve Sort) — algoritmo de referência do professor
│   ├── metrics.py            # utilitários de instrumentação
│   ├── test_suite.py         # suíte oficial de corretude (todos os cenários obrigatórios)
│   ├── benchmark.py          # gera tabelas/gráficos comparativos (benchmark_results.png)
│   └── student_template.py   # ARQUIVO A EDITAR — função my_authorial_sort(arr)
└── cpp/                       # equivalentes em C++17
```

Contrato de retorno obrigatório de `my_authorial_sort`:
```python
def my_authorial_sort(arr: List[Any]) -> Tuple[List[Any], int, int]:
    # retorna (lista_ordenada, total_comparacoes, total_movimentacoes)
```

## 3. Algoritmo escolhido: IGIS (Interpolation-Guided Insertion Sort)

**Ordenação por Inserção Guiada por Interpolação.**

### Ideia central
Insertion Sort clássico gasta O(i) comparações para achar a posição de inserção do i-ésimo elemento. O IGIS substitui a busca linear por uma **busca por interpolação** (adaptada da busca interpolada de Peterson/Perl-Reingold-Shamir): o próximo índice a testar é estimado pela posição *relativa do valor* da chave dentro do intervalo de valores do prefixo já ordenado — não pela posição relativa dos índices (como seria numa busca binária).

Técnica de origem declarada: busca interpolada em vetores ordenados. Modificação estrutural: aplicada como motor de localização do ponto de inserção dentro de um processo de shift estilo Insertion Sort, com fallback automático para ponto médio (comportamento de busca binária) quando os elementos não suportam subtração.

### Pseudocódigo

```
função encontrar_posicao_insercao(a, low, high, key):
    # Pré-condição: a[low..high] está ordenado
    # Pós-condição: retorna o menor índice pos em [low, high+1]
    #               tal que a[pos] > key (upper bound → garante estabilidade)
    enquanto low <= high:
        se a[low] == a[high]:
            se key < a[low]: retornar low
            senão: retornar high + 1

        guess = low + piso( (key - a[low]) / (a[high] - a[low]) * (high - low) )
        guess = limitar(guess, low, high)

        se a[guess] <= key:
            low = guess + 1
        senão:
            high = guess - 1

    retornar low


função IGIS_sort(a):
    n = tamanho(a)
    para i de 1 até n-1:
        key = a[i]
        pos = encontrar_posicao_insercao(a, 0, i-1, key)
        para j de i-1 até pos, decrescendo:
            a[j+1] = a[j]
        a[pos] = key
    retornar a
```

### Invariantes

- **Laço externo (i):** no início da iteração `i`, `a[0..i-1]` contém os mesmos elementos do array original nessas posições, está ordenado, e preserva ordem relativa de chaves iguais (estabilidade).
- **Laço de busca (estreitamento):** a qualquer momento, todo elemento em `a[0..low-1]` é `<= key` e todo elemento em `a[high+1..i-1]` é `> key`; a posição correta de inserção está sempre em `[low, high+1]`.

### Complexidade

| Caso | Comparações (busca) | Movimentações (shift) | Observação |
|---|---|---|---|
| Melhor (já ordenado) | Θ(n) | Θ(n) | interpolação acerta perto do fim |
| Médio (uniforme aleatório) | Θ(n log log n) | Θ(n²) | resultado clássico de Perl-Reingold-Shamir |
| Pior (adversarial/invertido) | Θ(n²) | Θ(n²) | interpolação degenera fora de distribuição uniforme |

- **Espaço auxiliar:** Θ(1) — busca iterativa, sem recursão.
- **Estabilidade:** sim (upper bound na busca).
- **In-place:** sim.
- **Fallback não-numérico:** se `key - a[low]` levantar `TypeError`, usa ponto médio `(low+high)//2` (degrada para Binary Insertion Sort).

**Ponto-chave da análise crítica:** a melhoria reduz comprovadamente o número de *comparações* no caso médio, mas não muda a ordem de grandeza do tempo total, porque o gargalo passa a ser o deslocamento de elementos (Θ(n²), inerente a arrays contíguos). Contribuição honesta, sem prometer milagre assintótico.

## 4. Status atual e próximos passos

- [x] Enunciado lido e resumido.
- [x] Pacote de código do professor explorado (README, `authorial.py`/DPES, `student_template.py`).
- [x] Mecanismo autoral escolhido e formalizado (IGIS): pseudocódigo, invariantes, complexidade.
- [x] Implementar `my_authorial_sort` em `codigo/python/student_template.py` seguindo o pseudocódigo acima, com contadores `comps`/`moves` fiéis à lógica.
- [x] Rodar `python3 python/student_template.py` (testes embutidos) e depois `make test_python` (suíte oficial completa) — cobrir vazio, único, ordenado, reverso, repetidos, aleatório.
- [x] Adicionar o algoritmo ao dicionário `algorithms` em `benchmark.py` e rodar `make benchmark_python` para gerar tabelas/gráficos vs. N crescente.
- [ ] Escrever a comparação crítica contra pelo menos 2 clássicos (sugestão: Insertion Sort — mesma família — e Quick Sort — para contraste de paradigma).
- [ ] Montar o entregável final (relatório ou slides) com todas as seções exigidas na seção 4 do enunciado, incluindo a declaração obrigatória de uso de IA (esta conversa deve ser referenciada nela: uso de IA para formalização do algoritmo e apoio à análise).
- [ ] Preparar a defesa oral (saber justificar cada escolha: por que interpolação, por que o fallback, por que o resultado médio não muda a ordem O(n²) total).
