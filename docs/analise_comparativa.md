# Análise Comparativa — IGIS vs. Métodos Clássicos (Issue #04)

> **Contexto:** Esta análise confronta o algoritmo autoral **IGIS** (*Interpolation-Guided Insertion Sort*) com dois métodos clássicos representativos — **Insertion Sort** (mesma família, baseline direto) e **Quick Sort** (paradigma divisão e conquista) — tanto do ponto de vista teórico quanto empírico, usando os dados coletados na Issue #03.

---

## 1. Tabela Comparativa Teórica

| Propriedade | IGIS | Insertion Sort | Quick Sort |
|:---|:---:|:---:|:---:|
| **Comparações — Melhor Caso** | $\Theta(n)$ | $\Theta(n)$ | $\Theta(n \log n)$ |
| **Comparações — Caso Médio** | $\Theta(n \log \log n)$ ¹ | $\Theta(n^2)$ | $\Theta(n \log n)$ |
| **Comparações — Pior Caso** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ ² |
| **Movimentações — Melhor Caso** | $\Theta(n)$ | $\Theta(n)$ | $\Theta(n \log n)$ |
| **Movimentações — Caso Médio** | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(n \log n)$ |
| **Movimentações — Pior Caso** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ |
| **Tempo Total — Caso Médio** | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(n \log n)$ |
| **Espaço Auxiliar** | $\Theta(1)$ | $\Theta(1)$ | $O(\log n)$ ³ |
| **Estabilidade** | Sim (upper-bound) | Sim | Não |
| **In-place** | Sim | Sim | Sim ⁴ |

**Notas:**
1. Resultado clássico de Perl, Itai & Avni (1978) para busca por interpolação em dados uniformemente distribuídos.
2. Pior caso do Quick Sort com pivô determinístico (ex.: array já ordenado sem aleatorização).
3. Pilha de recursão do Quick Sort.
4. Quick Sort é in-place no sentido de que não aloca um segundo array, mas usa $O(\log n)$ de pilha.

---

## 2. Análise Empírica: Comparações de Chaves

A contribuição central do IGIS é a **redução do número de comparações** em relação ao Insertion Sort clássico. Os dados experimentais confirmam isso de forma inequívoca:

### 2.1 Distribuição Aleatória (`random`)

| N | Insertion Sort | IGIS | Redução |
|---:|---:|---:|---:|
| 10 | 31 | 31 | 0% |
| 50 | 635 | 247 | **−61%** |
| 100 | 2.630 | 566 | **−78%** |
| 250 | 15.678 | 1.596 | **−90%** |
| 500 | 61.964 | 3.257 | **−95%** |
| 1.000 | 253.446 | 7.113 | **−97%** |

A redução é dramática: para $N = 1000$, o IGIS usa **apenas 2,8%** das comparações do Insertion Sort. Isso é consistente com a previsão teórica: o Insertion Sort faz $\Theta(n^2/4)$ comparações em média (busca linear), enquanto o IGIS faz $\Theta(n \log \log n)$ (busca por interpolação).

Para efeito de escala: $1000 \times \log_2(\log_2(1000)) \approx 1000 \times 3{,}32 \approx 3.322$, muito próximo dos 7.113 observados (que inclui o fator constante da contabilização de comparações na detecção de extremos iguais).

### 2.2 Distribuição Já Ordenada (`sorted`)

| N | Insertion Sort | IGIS |
|---:|---:|---:|
| 100 | 99 | 198 |
| 1.000 | 999 | 1.998 |

Aqui o IGIS faz exatamente **2n** comparações (uma para verificar `a[low] == a[high]` e outra para `key < a[low]` a cada iteração), enquanto o Insertion Sort faz apenas **n−1** (uma comparação por elemento que já está na posição correta). O IGIS paga um fator constante maior no melhor caso, mas ambos permanecem em $\Theta(n)$.

### 2.3 Distribuição Reversa (`reverse`)

| N | Insertion Sort | IGIS |
|---:|---:|---:|
| 100 | 4.950 | 198 |
| 1.000 | 499.500 | 1.998 |

Resultado **notável**: no caso reverso, o Insertion Sort degenera para $\Theta(n^2/2)$ comparações, mas o IGIS continua fazendo apenas **2n**. A interpolação calcula `guess = low` (porque o key é menor que todos os elementos do prefixo ordenado), e a busca converge em uma única iteração. Isso constitui uma vantagem prática significativa sobre o Insertion Sort clássico no pior caso de comparações.

### 2.4 Distribuição com Duplicados em Massa (`duplicates`)

| N | Insertion Sort | IGIS |
|---:|---:|---:|
| 100 | 2.014 | 1.520 |
| 1.000 | 203.588 | 122.521 |

A redução é mais modesta (~40%) com duplicados massivos. Quando `a[low] == a[high]` (intervalo degenerado), o IGIS faz fallback para a avaliação direta sem interpolação — o que é correto mas não reduz significativamente o número de iterações quando muitos segmentos do prefixo ordenado são formados por valores idênticos. Ainda assim, o IGIS permanece consistentemente melhor que o Insertion Sort.

---

## 3. Análise Empírica: Movimentações de Elementos

### O gargalo inalterável

Eis o ponto crucial — e a **limitação honesta** do IGIS: o número de movimentações é **idêntico** ao do Insertion Sort em todos os cenários.

| Distribuição | N=1000 | Insertion Sort (moves) | IGIS (moves) |
|:---|---:|---:|---:|
| Random | 1.000 | 254.451 | 254.451 |
| Sorted | 1.000 | 1.998 | 1.998 |
| Reverse | 1.000 | 501.498 | 501.498 |
| Duplicates | 1.000 | 204.588 | 204.588 |
| Almost Sorted | 1.000 | 33.545 | 33.545 |

**Explicação teórica:** O IGIS não altera o mecanismo de inserção — apenas muda *como encontra* a posição, não *como desloca* os elementos. O shift de $a[\text{pos}..i-1]$ uma posição à direita é inerente a qualquer Insertion Sort sobre arrays contíguos. No caso médio, cada elemento $i$ precisa ser deslocado $i/2$ posições em média, totalizando:

$$\sum_{i=1}^{n-1} \frac{i}{2} = \frac{n(n-1)}{4} = \Theta(n^2)$$

Nenhuma otimização na etapa de busca pode reduzir essa soma — ela depende apenas da *distância* entre a posição original e a posição final de cada elemento, que é uma propriedade da permutação de entrada, não do método de localização.

---

## 4. Análise Empírica: Tempo de Execução

### 4.1 IGIS vs. Insertion Sort — Tempo (ms)

| Distribuição | N=1000 | Insertion Sort | IGIS | Diferença |
|:---|---:|---:|---:|---:|
| Random | 1.000 | 23,96 ms | 18,44 ms | IGIS **23% mais rápido** |
| Sorted | 1.000 | 0,18 ms | 0,69 ms | IGIS 3,8× mais lento |
| Reverse | 1.000 | 80,29 ms | 81,89 ms | Virtualmente iguais |
| Duplicates | 1.000 | 108,58 ms | 84,64 ms | IGIS **22% mais rápido** |
| Almost Sorted | 1.000 | 3,72 ms | 18,21 ms | IGIS 4,9× mais lento |

**Interpretação:**

- **Caso aleatório:** O IGIS é ligeiramente mais rápido porque a redução de 97% em comparações compensa parcialmente o overhead constante da interpolação. O ganho é modesto (~23%) porque as movimentações — $\Theta(n^2)$ — dominam o tempo total.

- **Caso já ordenado e quase-ordenado:** O IGIS é **mais lento** que o Insertion Sort. O Insertion Sort clássico com busca linear detecta a posição correta em $O(1)$ (uma única comparação por elemento), enquanto o IGIS precisa avaliar `a[low] == a[high]`, calcular a interpolação e fazer o clamping — overhead constante por iteração que não compensa quando o array já está quase pronto.

- **Caso reverso:** Tempos virtualmente idênticos. O IGIS economiza enormemente em comparações ($2n$ vs $n^2/2$), mas as movimentações ($\Theta(n^2)$) continuam dominando. O ganho em comparações compensa o overhead aritmético da interpolação, resultando em empate prático.

### 4.2 IGIS vs. Quick Sort — Tempo (ms)

| Distribuição | N=1000 | Quick Sort | IGIS | Fator |
|:---|---:|---:|---:|---:|
| Random | 1.000 | 1,52 ms | 18,44 ms | Quick **12× mais rápido** |
| Sorted | 1.000 | 0,91 ms | 0,69 ms | Comparáveis |
| Reverse | 1.000 | 2,44 ms | 81,89 ms | Quick **34× mais rápido** |

O Quick Sort é dramaticamente mais rápido que o IGIS em quase todos os cenários. Isso é esperado: o Quick Sort tem complexidade de tempo $\Theta(n \log n)$ no caso médio, contra $\Theta(n^2)$ do IGIS. A diferença só tende a crescer com $N$.

A única vantagem do IGIS sobre o Quick Sort é a **estabilidade** (o Quick Sort padrão não é estável) e o **espaço auxiliar** constante (Quick Sort precisa de $O(\log n)$ para a pilha de recursão).

---

## 5. Síntese: Onde o IGIS Brilha e Onde Não

### ✅ Pontos fortes do IGIS

1. **Redução radical de comparações:** até 97% menos comparações que o Insertion Sort para dados aleatórios uniformes — confirmando a teoria de $\Theta(n \log \log n)$.
2. **Robustez no caso reverso:** mantém $\Theta(n)$ comparações mesmo no cenário que é o pior caso do Insertion Sort.
3. **Estabilidade garantida:** preserva a ordem relativa de chaves iguais (via upper-bound na busca), ao contrário do Quick Sort.
4. **In-place com $\Theta(1)$ de espaço auxiliar:** sem recursão nem alocação extra.
5. **Fallback gracioso:** para tipos não-numéricos (strings, objetos), degrada para Binary Insertion Sort em vez de quebrar.

### ❌ Limitações honestas

1. **O tempo total permanece $\Theta(n^2)$:** a redução de comparações não altera a ordem assintótica, porque o gargalo são as movimentações físicas em array contíguo.
2. **Overhead constante maior que o Insertion Sort:** para dados já ordenados ou quase-ordenados, a interpolação é desnecessária e adiciona custo.
3. **Não compete com algoritmos $O(n \log n)$:** Quick Sort e Merge Sort são categoricamente mais rápidos para $N$ grande.
4. **Sensível à distribuição dos dados:** a vantagem de $\Theta(n \log \log n)$ comparações só se materializa para distribuições razoavelmente uniformes; com dados adversariais (muitos duplicados, distribuições extremamente enviesadas), a busca por interpolação pode degenerar.

### 📊 Contribuição honesta

O IGIS demonstra que é possível **reduzir comprovadamente** o custo de localização na família de Insertion Sort, de $\Theta(n^2)$ comparações para $\Theta(n \log \log n)$, aplicando busca por interpolação como motor de localização. Porém, essa melhoria tem um **teto prático**: em arrays contíguos, o deslocamento físico dos elementos é o verdadeiro gargalo, e nenhuma otimização na busca pode eliminá-lo sem mudar a estrutura de dados subjacente (por exemplo, para listas ligadas — mas aí a localidade de cache degradaria o desempenho real).

A contribuição é real, mensurável e fundamentada, mas não promete revolução assintótica — apenas aprimora uma componente específica do Insertion Sort, e o faz de forma verificável.

---

## 6. Comparação com o Algoritmo do Professor (DPES)

Para completude, vale observar como o IGIS se compara ao DPES (*Dual-Pivot Extremes Sieve Sort*):

| Métrica (N=1000, Random) | IGIS | DPES |
|:---|---:|---:|
| Comparações | 7.113 | 18.147 |
| Movimentações | 254.451 | 8.606 |
| Tempo (ms) | 18,44 | 2,06 |

O DPES é um algoritmo de paradigma diferente (sieve/peneira com duplo pivô), que consegue $O(n \log n)$ movimentações. O IGIS faz **menos comparações**, mas o DPES faz **dramaticamente menos movimentações** — e como movimentações dominam o tempo, o DPES é ~9× mais rápido no caso aleatório. Isso reforça a conclusão central: **o gargalo do IGIS são as movimentações, não as comparações**.

---

*Documento gerado como parte da Issue #04 do TP1 APA — Análise Comparativa Empírica e Teórica.*
