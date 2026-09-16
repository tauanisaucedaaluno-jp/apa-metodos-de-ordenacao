# AGENTS.md

Instruções para qualquer agente de IA (Claude Code ou similar) que for editar código neste repositório do TP1 de Análise e Projetos de Algoritmos.

Leia `CONTEXT.md` primeiro — ele tem o enunciado resumido, o algoritmo autoral escolhido (IGIS), o pseudocódigo, os invariantes e a análise de complexidade já decididos. Este arquivo (`AGENTS.md`) trata só de como operar no repositório.

## Estrutura do repositório

```
codigo/
├── Makefile                  # atalhos de execução (ver "Comandos" abaixo)
├── README.md                 # guia original do professor
├── python/
│   ├── classical.py          # NÃO EDITAR — baseline instrumentado (Bubble/Selection/Insertion/Merge/Quick)
│   ├── authorial.py          # NÃO EDITAR — DPES, algoritmo de referência do professor (só leitura/inspiração)
│   ├── metrics.py            # utilitários de instrumentação
│   ├── test_suite.py         # suíte oficial de corretude — só editar para REGISTRAR o novo algoritmo, não para afrouxar testes
│   ├── benchmark.py          # framework de benchmark/gráficos — editar para adicionar o algoritmo ao dicionário `algorithms`
│   └── student_template.py   # ÚNICO arquivo onde a lógica do algoritmo autoral deve ser escrita
└── cpp/                       # equivalentes em C++17 (mesma lógica, se o aluno optar por C++)
```

## Comandos

```bash
make test_python          # roda a suíte oficial de corretude em Python
make test_cpp              # compila e roda os testes em C++
make benchmark_python       # gera tabelas + benchmark_results.png (python3 python/benchmark.py --trials 3 --plot benchmark_results.png)
make run_benchmark_cpp      # benchmark em C++
python3 python/student_template.py   # roda os testes rápidos embutidos no template
```

## Contrato de implementação (obrigatório)

Qualquer função de ordenação autoral deve seguir exatamente esta assinatura:

```python
def my_authorial_sort(arr: List[Any]) -> Tuple[List[Any], int, int]:
    """Retorna (lista_ordenada, total_comparacoes, total_movimentacoes)."""
```

- `comps` deve incrementar em **toda** comparação de valores usada para decisão de ordenação (inclusive dentro de sub-rotinas de busca).
- `moves` deve incrementar em **toda** atribuição que move um elemento de posição (shift, swap = 2 movimentações, etc.), seguindo o mesmo padrão usado em `authorial.py` e `classical.py` para manter as métricas comparáveis entre algoritmos.
- Não usar bibliotecas de ordenação prontas (`sorted()`, `.sort()`, `std::sort`) em nenhum ponto do algoritmo principal.
- Tratar explicitamente os casos-limite: array vazio (`N=0`) e de um elemento (`N=1`).

## Convenções de código (SOLID)

Mesmo em um script relativamente pequeno, aplique os princípios SOLID ao estruturar `student_template.py` (e o equivalente C++). Isso também ajuda na defesa oral, porque cada responsabilidade fica isolada e fácil de explicar separadamente.

1. **SRP (Responsabilidade Única)** — separe funções por responsabilidade, não amontoe tudo em `my_authorial_sort`:
   - `_encontrar_posicao_insercao(a, low, high, key, comps)` — só localiza a posição de inserção.
   - `_deslocar_e_inserir(a, i, pos, moves)` — só faz o shift físico dos elementos.
   - `my_authorial_sort(arr)` — só orquestra o laço externo e agrega os contadores.
   Isso espelha diretamente a separação já feita no pseudocódigo do `CONTEXT.md` entre `encontrar_posicao_insercao` e `IGIS_sort`.

2. **OCP (Aberto/Fechado)** — a estratégia de estimativa de posição (interpolação vs. fallback de ponto médio) deve ser isolada em uma função própria (`_estimar_guess(a, low, high, key)`), de forma que se um dia quiser testar outra heurística de estimativa, baste adicionar uma nova função/estratégia sem alterar `_encontrar_posicao_insercao` nem `my_authorial_sort`.

3. **LSP (Substituição de Liskov)** — qualquer variante alternativa de `_estimar_guess` deve manter o mesmo contrato (recebe `a, low, high, key`, devolve um índice válido dentro de `[low, high]`), para que possa substituir a implementação padrão sem quebrar `_encontrar_posicao_insercao`.

4. **ISP (Segregação de Interfaces)** — não force os contadores (`comps`, `moves`) para dentro de uma única estrutura "pesada" (ex: uma classe `Metrics` genérica com dezenas de campos não usados). Se for necessário agrupá-los, use uma estrutura mínima (`dataclass` com só os dois campos) — cada função só deve depender do que realmente usa.

5. **DIP (Inversão de Dependência)** — `my_authorial_sort` deve depender da *assinatura* de `_encontrar_posicao_insercao`/`_estimar_guess`, não da implementação concreta. Na prática em Python isso significa: evite hardcode de comportamento condicional espalhado pelo laço principal; centralize a decisão de estratégia nas funções auxiliares e injete-as por parâmetro (com valor padrão) se quiser permitir troca de estratégia nos testes/benchmark.

Regras gerais de estilo, independente de SOLID:
- Nomes de função em `snake_case`, privados a este módulo prefixados com `_`.
- Docstring em cada função pública/privada relevante, citando a pré/pós-condição (mesmo formato usado no pseudocódigo do `CONTEXT.md`).
- Nenhuma função deve exceder ~25 linhas; se a lógica crescer além disso, é sinal de que uma responsabilidade nova apareceu e merece ser extraída (SRP).
- Comentários devem explicar *por quê* (ex: por que o fallback existe), não *o quê* (o código já diz o que faz).

## Regras específicas deste trabalho (não negociáveis)

1. **Nunca transformar o algoritmo autoral numa variação cosmética de um clássico.** Se o agente perceber, ao implementar, que a lógica resultante é equivalente a Bubble/Selection/Insertion/Merge/Quick com apenas nomes/ordem trocados, deve avisar explicitamente antes de prosseguir — isso é critério de nota 0,0 no enunciado.
2. **Não gerar código integralmente e apresentá-lo como pronto sem revisão do aluno.** O aluno precisa entender e conseguir explicar cada linha (critério de rejeição do enunciado: "incapacidade de explicar a lógica durante arguição"). Ao gerar a implementação, comente o código explicando a correspondência com o pseudocódigo do `CONTEXT.md`.
3. **Qualquer uso de IA neste projeto deve ser registrado** na seção de "Declaração de Autoria e IA" do relatório/slides final — não deixe isso de fora do entregável.
4. **Não afrouxar nem remover testes** em `test_suite.py` para "fazer passar" — se um teste falhar, o algoritmo é que deve ser corrigido.
5. **Manter os invariantes formalizados no `CONTEXT.md`.** Se a implementação divergir do pseudocódigo (ex: por otimização), atualizar o `CONTEXT.md` para refletir a mudança real antes de seguir em frente — o documento de contexto e o código nunca podem descrever coisas diferentes.

## Fluxo de trabalho esperado

1. Implementar/editar apenas `python/student_template.py` (ou o equivalente C++) para a lógica do algoritmo.
2. Rodar `python3 python/student_template.py` para validação rápida.
3. Rodar `make test_python` para validação completa contra a suíte oficial.
4. Registrar o algoritmo em `python/benchmark.py` (dicionário `algorithms`) e rodar `make benchmark_python`.
5. Reportar resultados (tempos, comparações, movimentações) para alimentar a seção de resultados experimentais do entregável — não escrever essa seção sozinho sem o aluno revisar as conclusões.
