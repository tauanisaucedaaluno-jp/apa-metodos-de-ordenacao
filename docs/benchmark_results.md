# Relatório Experimental de Benchmarks — APA (TP1)

## Distribuição: `RANDOM`

### 1. Tempo Médio de Execução (ms)

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 0.011 ms | 0.141 ms | 0.563 ms | 3.598 ms | 14.206 ms | 73.147 ms |
| Selection Sort | 0.008 ms | 0.084 ms | 0.323 ms | 3.207 ms | 6.399 ms | 55.176 ms |
| Insertion Sort | 0.007 ms | 0.077 ms | 0.301 ms | 1.625 ms | 7.986 ms | 32.471 ms |
| Merge Sort | 0.024 ms | 0.093 ms | 0.210 ms | 0.540 ms | 1.480 ms | 2.405 ms |
| Quick Sort | 0.017 ms | 0.067 ms | 0.137 ms | 0.349 ms | 0.791 ms | 2.576 ms |
| Authorial (DPES) | 0.013 ms | 0.084 ms | 0.169 ms | 0.448 ms | 1.075 ms | 2.626 ms |
| Authorial (IGIS) | 0.040 ms | 0.154 ms | 0.367 ms | 1.619 ms | 7.081 ms | 26.780 ms |

### 2. Número Médio de Comparações de Chaves

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 45 | 1.159 | 4.845 | 30.989 | 124.659 | 498.275 |
| Selection Sort | 45 | 1.225 | 4.950 | 31.125 | 124.750 | 499.500 |
| Insertion Sort | 32 | 666 | 2.555 | 16.204 | 60.948 | 254.445 |
| Merge Sort | 24 | 215 | 540 | 1.665 | 3.847 | 8.727 |
| Quick Sort | 57 | 421 | 931 | 2.812 | 6.135 | 14.001 |
| Authorial (DPES) | 32 | 410 | 1.015 | 3.380 | 8.005 | 18.152 |
| Authorial (IGIS) | 30 | 256 | 544 | 1.492 | 3.370 | 7.018 |

### 3. Número Médio de Movimentações de Elementos

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 50 | 1.246 | 4.916 | 31.924 | 120.910 | 506.908 |
| Selection Sort | 12 | 90 | 188 | 494 | 984 | 1.980 |
| Insertion Sort | 43 | 721 | 2.656 | 16.460 | 61.453 | 255.452 |
| Merge Sort | 34 | 286 | 672 | 1.994 | 4.488 | 9.976 |
| Quick Sort | 18 | 172 | 364 | 1.140 | 2.424 | 5.298 |
| Authorial (DPES) | 43 | 255 | 613 | 1.760 | 3.852 | 8.497 |
| Authorial (IGIS) | 43 | 721 | 2.656 | 16.460 | 61.453 | 255.452 |

---

## Distribuição: `SORTED`

### 1. Tempo Médio de Execução (ms)

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 0.017 ms | 0.010 ms | 0.130 ms | 0.013 ms | 0.060 ms | 0.066 ms |
| Selection Sort | 0.012 ms | 0.205 ms | 0.230 ms | 2.466 ms | 8.847 ms | 35.637 ms |
| Insertion Sort | 0.006 ms | 0.015 ms | 0.012 ms | 0.053 ms | 0.066 ms | 0.190 ms |
| Merge Sort | 0.046 ms | 0.137 ms | 0.217 ms | 0.829 ms | 0.971 ms | 3.422 ms |
| Quick Sort | 0.025 ms | 0.068 ms | 0.085 ms | 0.193 ms | 0.464 ms | 1.822 ms |
| Authorial (DPES) | 0.018 ms | 0.083 ms | 0.097 ms | 0.295 ms | 0.767 ms | 2.070 ms |
| Authorial (IGIS) | 0.028 ms | 0.078 ms | 0.082 ms | 0.431 ms | 0.813 ms | 0.885 ms |

### 2. Número Médio de Comparações de Chaves

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 9 | 49 | 99 | 249 | 499 | 999 |
| Selection Sort | 45 | 1.225 | 4.950 | 31.125 | 124.750 | 499.500 |
| Insertion Sort | 9 | 49 | 99 | 249 | 499 | 999 |
| Merge Sort | 15 | 133 | 316 | 983 | 2.216 | 4.932 |
| Quick Sort | 49 | 348 | 795 | 2.138 | 4.773 | 10.542 |
| Authorial (DPES) | 9 | 315 | 751 | 2.701 | 7.013 | 14.191 |
| Authorial (IGIS) | 18 | 98 | 198 | 498 | 998 | 1.998 |

### 3. Número Médio de Movimentações de Elementos

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 0 | 0 | 0 | 0 | 0 | 0 |
| Selection Sort | 0 | 0 | 0 | 0 | 0 | 0 |
| Insertion Sort | 18 | 98 | 198 | 498 | 998 | 1.998 |
| Merge Sort | 34 | 286 | 672 | 1.994 | 4.488 | 9.976 |
| Quick Sort | 0 | 0 | 0 | 0 | 0 | 0 |
| Authorial (DPES) | 18 | 86 | 182 | 446 | 838 | 1.838 |
| Authorial (IGIS) | 18 | 98 | 198 | 498 | 998 | 1.998 |

---

## Distribuição: `REVERSE`

### 1. Tempo Médio de Execução (ms)

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 0.011 ms | 0.169 ms | 0.667 ms | 4.261 ms | 21.593 ms | 103.990 ms |
| Selection Sort | 0.005 ms | 0.061 ms | 0.231 ms | 1.737 ms | 9.170 ms | 38.465 ms |
| Insertion Sort | 0.006 ms | 0.115 ms | 0.648 ms | 4.585 ms | 19.849 ms | 66.539 ms |
| Merge Sort | 0.018 ms | 0.068 ms | 0.161 ms | 0.455 ms | 1.647 ms | 2.079 ms |
| Quick Sort | 0.011 ms | 0.040 ms | 0.088 ms | 0.212 ms | 0.832 ms | 1.094 ms |
| Authorial (DPES) | 0.011 ms | 0.063 ms | 0.114 ms | 0.690 ms | 1.473 ms | 1.755 ms |
| Authorial (IGIS) | 0.012 ms | 0.117 ms | 0.420 ms | 2.238 ms | 20.954 ms | 42.719 ms |

### 2. Número Médio de Comparações de Chaves

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 45 | 1.225 | 4.950 | 31.125 | 124.750 | 499.500 |
| Selection Sort | 45 | 1.225 | 4.950 | 31.125 | 124.750 | 499.500 |
| Insertion Sort | 45 | 1.225 | 4.950 | 31.125 | 124.750 | 499.500 |
| Merge Sort | 19 | 153 | 356 | 1.011 | 2.272 | 5.044 |
| Quick Sort | 55 | 351 | 799 | 2.143 | 4.779 | 10.549 |
| Authorial (DPES) | 45 | 450 | 886 | 2.965 | 7.501 | 15.218 |
| Authorial (IGIS) | 18 | 98 | 198 | 498 | 998 | 1.998 |

### 3. Número Médio de Movimentações de Elementos

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 90 | 2.450 | 9.900 | 62.250 | 249.500 | 999.000 |
| Selection Sort | 10 | 50 | 100 | 250 | 500 | 1.000 |
| Insertion Sort | 63 | 1.323 | 5.148 | 31.623 | 125.748 | 501.498 |
| Merge Sort | 34 | 286 | 672 | 1.994 | 4.488 | 9.976 |
| Quick Sort | 14 | 54 | 104 | 254 | 504 | 1.004 |
| Authorial (DPES) | 63 | 240 | 336 | 731 | 1.347 | 2.892 |
| Authorial (IGIS) | 63 | 1.323 | 5.148 | 31.623 | 125.748 | 501.498 |

---

## Distribuição: `DUPLICATES`

### 1. Tempo Médio de Execução (ms)

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 0.009 ms | 0.108 ms | 0.474 ms | 2.821 ms | 15.790 ms | 99.102 ms |
| Selection Sort | 0.005 ms | 0.064 ms | 0.322 ms | 1.559 ms | 6.745 ms | 54.374 ms |
| Insertion Sort | 0.004 ms | 0.043 ms | 0.260 ms | 1.273 ms | 7.073 ms | 25.624 ms |
| Merge Sort | 0.019 ms | 0.081 ms | 0.180 ms | 0.492 ms | 1.135 ms | 6.194 ms |
| Quick Sort | 0.014 ms | 0.055 ms | 0.120 ms | 0.342 ms | 0.753 ms | 2.435 ms |
| Authorial (DPES) | 0.009 ms | 0.045 ms | 0.087 ms | 1.294 ms | 0.418 ms | 1.554 ms |
| Authorial (IGIS) | 0.014 ms | 0.199 ms | 0.470 ms | 4.514 ms | 12.884 ms | 53.605 ms |

### 2. Número Médio de Comparações de Chaves

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 44 | 1.134 | 4.779 | 29.997 | 118.972 | 478.179 |
| Selection Sort | 45 | 1.225 | 4.950 | 31.125 | 124.750 | 499.500 |
| Insertion Sort | 21 | 461 | 2.103 | 13.367 | 50.985 | 214.437 |
| Merge Sort | 21 | 215 | 512 | 1.570 | 3.628 | 8.218 |
| Quick Sort | 63 | 410 | 955 | 2.528 | 5.501 | 11.847 |
| Authorial (DPES) | 21 | 321 | 749 | 1.881 | 3.808 | 7.723 |
| Authorial (IGIS) | 34 | 490 | 1.452 | 7.516 | 28.870 | 121.784 |

### 3. Número Médio de Movimentações de Elementos

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 28 | 828 | 4.008 | 26.240 | 100.972 | 426.880 |
| Selection Sort | 12 | 76 | 152 | 374 | 782 | 1.638 |
| Insertion Sort | 32 | 512 | 2.202 | 13.618 | 51.484 | 215.438 |
| Merge Sort | 34 | 286 | 672 | 1.994 | 4.488 | 9.976 |
| Quick Sort | 20 | 196 | 462 | 1.494 | 3.326 | 7.748 |
| Authorial (DPES) | 32 | 194 | 244 | 502 | 1.066 | 2.228 |
| Authorial (IGIS) | 32 | 512 | 2.202 | 13.618 | 51.484 | 215.438 |

---

## Distribuição: `ALMOST_SORTED`

### 1. Tempo Médio de Execução (ms)

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 0.005 ms | 0.033 ms | 0.192 ms | 1.562 ms | 9.784 ms | 44.928 ms |
| Selection Sort | 0.004 ms | 0.057 ms | 0.234 ms | 2.332 ms | 9.622 ms | 45.541 ms |
| Insertion Sort | 0.002 ms | 0.008 ms | 0.028 ms | 0.427 ms | 1.119 ms | 4.304 ms |
| Merge Sort | 0.018 ms | 0.067 ms | 0.153 ms | 0.576 ms | 1.493 ms | 4.905 ms |
| Quick Sort | 0.011 ms | 0.036 ms | 0.081 ms | 0.235 ms | 0.739 ms | 2.313 ms |
| Authorial (DPES) | 0.007 ms | 0.043 ms | 0.093 ms | 0.506 ms | 1.316 ms | 2.986 ms |
| Authorial (IGIS) | 0.011 ms | 0.050 ms | 0.238 ms | 2.136 ms | 8.298 ms | 21.135 ms |

### 2. Número Médio de Comparações de Chaves

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 24 | 595 | 3.120 | 26.274 | 119.899 | 494.144 |
| Selection Sort | 45 | 1.225 | 4.950 | 31.125 | 124.750 | 499.500 |
| Insertion Sort | 12 | 73 | 294 | 2.311 | 7.846 | 32.055 |
| Merge Sort | 18 | 148 | 402 | 1.422 | 3.337 | 7.578 |
| Quick Sort | 49 | 358 | 822 | 2.138 | 5.042 | 10.969 |
| Authorial (DPES) | 12 | 319 | 784 | 2.902 | 7.353 | 15.807 |
| Authorial (IGIS) | 22 | 176 | 990 | 6.030 | 18.990 | 52.804 |

### 3. Número Médio de Movimentações de Elementos

| Algoritmo | N=10 | N=50 | N=100 | N=250 | N=500 | N=1000 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | 6 | 48 | 390 | 4.124 | 14.694 | 62.112 |
| Selection Sort | 2 | 4 | 10 | 24 | 50 | 100 |
| Insertion Sort | 21 | 122 | 393 | 2.560 | 8.345 | 33.054 |
| Merge Sort | 34 | 286 | 672 | 1.994 | 4.488 | 9.976 |
| Quick Sort | 2 | 4 | 50 | 64 | 166 | 372 |
| Authorial (DPES) | 21 | 105 | 282 | 943 | 1.936 | 5.189 |
| Authorial (IGIS) | 21 | 122 | 393 | 2.560 | 8.345 | 33.054 |

---
