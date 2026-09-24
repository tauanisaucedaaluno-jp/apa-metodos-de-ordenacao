# Backlog de Issues — TP1 APA: Algoritmo de Ordenação Autoral (IGIS)

Este documento organiza as tarefas e entregáveis do projeto em **6 issues (número par)** sequenciais e incrementais, mapeadas a partir das exigências do enunciado (`TP1-Metodos-de-Ordenacao-Autorais.md`), do algoritmo planejado em `CONTEXT.md` (IGIS — *Interpolation-Guided Insertion Sort*) e das diretrizes de arquitetura/SOLID em `AGENTS.md`.

> **Formato de Entrega Escolhido:** Opção A — **Relatório Técnico Completo (sem defesa oral)**. As issues refletem todo o ciclo desde a codificação até a consolidação do relatório formal e validação final do pacote de entrega.

---

## Resumo do Status Geral

- [x] **Concepção e Formalização Inicial:** Ideia do algoritmo (IGIS), pseudocódigo, invariantes e análise teórica preliminar documentados no [CONTEXT.md](../CONTEXT.md).
- [x] **Benchmarking e Análise Empírica (Issue #03):** Bateria de testes de desempenho concluída com geração de tabelas e gráficos comparativos lado a lado (IGIS vs DPES e baselines).
- [ ] **Análise Comparativa Teórica vs Empírica (Issue #04):** Elaboração da discussão técnica confrontando as ordens de grandeza.
- [ ] **Relatório Técnico e Empacotamento (Issues #05 e #06):** Redação formal, gráficos e auditoria final do pacote.

---

## Issue #01: Implementação Modular do Algoritmo Autoral (IGIS) com Instrumentação

- **Status:** Concluída
- **Tipo:** Funcionalidade / Implementação
- **Componente:** `codigo/python/student_template.py`
- **Contexto:**
  O algoritmo já foi projetado no [CONTEXT.md](../CONTEXT.md), mas o arquivo [student_template.py](../codigo/python/student_template.py) ainda contém apenas um rascunho temporário de Insertion Sort padrão.
- **Objetivos e Critérios de Aceite:**
  1. Implementar `my_authorial_sort(arr: List[Any]) -> Tuple[List[Any], int, int]` seguindo o pseudocódigo do IGIS.
  2. Aplicar princípios **SOLID**:
     - `_estimar_guess(a, low, high, key)`: cálculo por interpolação com fallback para ponto médio (OCP/LSP) caso tipos não suportem subtração ou intervalo seja degenerado (`a[low] == a[high]`).
     - `_encontrar_posicao_insercao(a, low, high, key, ...)`: busca upper-bound para preservar estabilidade (SRP).
     - `_deslocar_e_inserir(a, i, pos, ...)`: deslocamento contíguo dos elementos (SRP).
  3. Contabilização rigorosa de métricas:
     - `comps`: incrementado em toda comparação de valores para decisão de ordenação.
     - `moves`: incrementado em todo shift/atribuição física de elementos.
  4. Tratar explicitamente casos-limite: vetor vazio (`N=0`) e elemento único (`N=1`).
  5. Aprovação total nos testes locais do template (`python3 python/student_template.py`).

---

## Issue #02: Integração e Validação na Suíte Oficial de Corretude

- **Status:** Concluída
- **Tipo:** Testes / QA
- **Componente:** `codigo/python/test_suite.py` e `codigo/Makefile`
- **Contexto:**
  A suíte oficial do professor testa todos os cenários obrigatórios (vazio, 1 elemento, ordenado, invertido, idênticos, duplicados, aleatório). O algoritmo autoral precisa ser registrado e aprovado sem alteração dos testes pré-existentes.
- **Objetivos e Critérios de Aceite:**
  1. Adicionar a classe de teste `TestIGISSort` em [test_suite.py](../codigo/python/test_suite.py) herdando de `BaseSortMixin` e apontando para `my_authorial_sort`.
  2. **Regra inegociável:** não remover nem afrouxar nenhum teste existente (critério de reprovação).
  3. Validar se a busca upper-bound mantém chaves idênticas em ordem estável.
  4. Executar via linha de comando `make test_python` (ou `python -m unittest python/test_suite.py`) e garantir 100% de aprovação (zero erros / zero falhas).

---

## Issue #03: Integração no Framework de Benchmark e Coleta Experimental

- **Status:** Concluída
- **Tipo:** Benchmark / Experimentos
- **Componente:** `codigo/python/benchmark.py`, `docs/benchmark_results.md`, gráficos PNG
- **Contexto:**
  O framework avalia tempo de CPU, comparações e movimentações para diferentes distribuições (aleatório, ordenado, reverso, quase ordenado, duplicados) variando $N$.
- **Objetivos e Critérios de Aceite:**
  1. [x] Registrar `my_authorial_sort` no dicionário `algorithms` do script [benchmark.py](../codigo/python/benchmark.py).
  2. [x] Executar baterias completas de testes com repetições (`trials=3`).
  3. [x] Gerar os artefatos de saída:
     - Tabelas estatísticas completas de Tempo, Comparações e Movimentações salvas em [docs/benchmark_results.md](benchmark_results.md).
     - Gráficos comparativos gerados e organizados:
       - `benchmark_results.png`: Visão geral completa de todos os algoritmos para as 3 métricas.
       - `benchmark_authorials_side_by_side.png`: Gráfico separando o IGIS (Aluno) à esquerda e o DPES (Professor) à direita para cada distribuição.
       - `benchmark_authorials_direct_comparison.png`: Confronto direto entre IGIS e DPES métrica por métrica.
  4. [x] Salvar e organizar os dados brutos e imagens na pasta `docs/` para inclusão direta no relatório.

---

## Issue #04: Análise Comparativa Empírica e Teórica vs. Métodos Clássicos

- **Status:** A Fazer
- **Tipo:** Análise Algorítmica / Conteúdo do Relatório
- **Componente:** `docs/relatorio/` (Seção 5 do Relatório)
- **Contexto:**
  O enunciado exige comparar o algoritmo com ao menos 2 métodos clássicos (Insertion Sort — baseline direto de mesma família — e Quick Sort — divisão e conquista).
- **Objetivos e Critérios de Aceite:**
  1. Construir tabela comparativa detalhando: modelo assintótico (melhor, médio, pior caso), espaço auxiliar, estabilidade e in-place.
  2. Analisar a redução substancial de comparações proporcionada pela interpolação ($O(n \log \log n)$ vs $O(n^2)$ no caso uniforme).
  3. Demonstrar matematicamente e via dados experimentais por que o ganho de comparações não altera o tempo de CPU total ($O(n^2)$), dominado pelo deslocamento em memória contígua.
  4. Avaliar cenários adversariais (distribuição reversa e duplicados em massa) e a eficácia do fallback.

---

## Issue #05: Redação do Relatório Técnico Completo

- **Status:** A Fazer
- **Tipo:** Documentação / Relatório
- **Componente:** `docs/relatorio_tecnico.md` (ou PDF equivalente)
- **Contexto:**
  O relatório técnico é o entregável principal avaliado da disciplina (1,0 ponto), devendo conter todas as seções obrigatórias estipuladas no enunciado.
- **Objetivos e Critérios de Aceite:**
  1. Estruturar o documento com rigor acadêmico contendo as 7 seções obrigatórias:
     - **1. Concepção e Raciocínio Projetual:** motivação do IGIS, analogia com busca telefônica/dicionário e invariantes formais de laço.
     - **2. Especificação Formal:** pseudocódigo detalhado e rastreamento passo a passo com exemplo numérico ilustrado.
     - **3. Análise Assintótica Teórica:** demonstração formal de tempo (melhor $\Omega(n)$, médio $\Theta(n \log \log n)$ comps / $\Theta(n^2)$ moves, pior $O(n^2)$) e espaço auxiliar ($\Theta(1)$).
     - **4. Propriedades Estruturais:** demonstração da estabilidade (upper bound) e caráter in-place.
     - **5. Comparação com a Literatura:** análise e tabela contrastando IGIS contra Insertion Sort e Quick Sort.
     - **6. Resultados Experimentais:** discussão aprofundada das curvas dos gráficos e tabelas consolidadas.
     - **7. Declaração Obrigatória de Autoria e IA:** discriminação transparente do uso de ferramentas (IA para formalização, escrita e scripts), limitações identificadas e pensamento crítico do autor.
  2. Revisar formatação matemática (KaTeX/LaTeX) e legendas de figuras e tabelas.

---

## Issue #06: Revisão de Conformidade, Reprodutibilidade e Pacote de Entrega

- **Status:** A Fazer
- **Tipo:** Release / QA Final
- **Componente:** Todo o repositório (`codigo/`, `docs/`, `README.md`)
- **Contexto:**
  O edital prevê critérios de reprovação automática (nota 0,0) por problemas de reprodutibilidade, ausência de declaração de IA, código quebrado ou dependências não documentadas.
- **Objetivos e Critérios de Aceite:**
  1. Fazer auditoria contra todos os critérios de rejeição do edital:
     - [ ] Código funcional e 100% aprovado nos testes oficiais (`make test_python`).
     - [ ] Ausência de plágio ou variação puramente cosmética.
     - [ ] Declaração formal de autoria e uso de IA presente e preenchida.
     - [ ] Reprodutibilidade: comandos do `Makefile` e dependências claramente instruídos no README.
  2. Atualizar o `README.md` principal com instruções claras para o professor reproduzir os testes e o benchmark.
  3. Validar se os arquivos finais do relatório (Markdown/PDF) e os gráficos gerados estão íntegros e devidamente organizados na pasta `docs/`.
