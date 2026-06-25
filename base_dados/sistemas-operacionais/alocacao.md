<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# Alocação Contígua, Paginação e Segmentação

## Introdução

Um dos principais desafios do gerenciamento de memória é decidir como os processos serão armazenados na memória principal.

Ao longo da evolução dos sistemas operacionais, diversas técnicas foram desenvolvidas para organizar a memória de forma eficiente.

As principais são:

- Alocação Contígua
- Paginação
- Segmentação

Cada técnica possui vantagens, desvantagens e diferentes mecanismos para lidar com o problema da fragmentação.

---

# Alocação de Memória

Quando um processo é carregado para execução, o sistema operacional precisa reservar espaço na memória RAM.

Exemplo:

```text
Processo A → 100 MB
Processo B → 200 MB
Processo C → 150 MB
```

A forma como esse espaço é reservado depende da técnica utilizada.

---

# Alocação Contígua

Na alocação contígua, cada processo ocupa uma única região contínua da memória.

Exemplo:

```text
+----------------+
| Sistema Operac.|
+----------------+
| Processo A     |
+----------------+
| Processo B     |
+----------------+
| Processo C     |
+----------------+
```

Cada processo ocupa um bloco único.

---

# Vantagens da Alocação Contígua

- Simplicidade de implementação.
- Acesso rápido à memória.
- Fácil gerenciamento inicial.

---

# Desvantagens da Alocação Contígua

- Fragmentação externa.
- Dificuldade de expansão dos processos.
- Má utilização da memória ao longo do tempo.

---

# Fragmentação

A fragmentação ocorre quando parte da memória fica inutilizada.

Existem dois tipos principais:

- Fragmentação Interna
- Fragmentação Externa

---

# Fragmentação Interna

Ocorre quando um processo recebe mais memória do que realmente utiliza.

Exemplo:

```text
Bloco reservado: 100 MB
Uso real: 80 MB

20 MB desperdiçados
```

---

# Fragmentação Externa

Ocorre quando existem espaços livres, mas espalhados pela memória.

Exemplo:

```text
Livre
Ocupado
Livre
Ocupado
Livre
```

Mesmo havendo espaço suficiente, pode não existir um bloco contínuo para um novo processo.

---

# Exemplo de Fragmentação Externa

```text
+-----------+
| Processo A|
+-----------+
| Livre     |
+-----------+
| Processo B|
+-----------+
| Livre     |
+-----------+
| Processo C|
+-----------+
```

Se um novo processo precisar de um espaço maior do que qualquer bloco livre isolado, ele não poderá ser carregado.

---

# Estratégias de Alocação Contígua

Quando um processo solicita memória, o sistema operacional pode utilizar diferentes estratégias.

---

## First Fit

Seleciona o primeiro bloco livre suficientemente grande.

Exemplo:

```text
Memória:
100 MB livre
200 MB livre
300 MB livre

Pedido:
80 MB

Resultado:
Utiliza o bloco de 100 MB
```

---

## Best Fit

Seleciona o menor bloco livre capaz de acomodar o processo.

Objetivo:

```text
Reduzir desperdício
```

---

## Worst Fit

Seleciona o maior bloco disponível.

Objetivo:

```text
Manter blocos livres grandes
```

---

# Compactação

A compactação reorganiza os processos na memória para unir espaços livres.

Antes:

```text
Processo
Livre
Processo
Livre
Processo
```

Depois:

```text
Processo
Processo
Processo
Livre
Livre
```

---

# Limitações da Alocação Contígua

Com o aumento da multiprogramação, a fragmentação tornou-se um problema significativo.

Isso levou ao surgimento da:

```text
Paginação
```

---

# Paginação

A paginação divide a memória em blocos de tamanho fixo.

---

## Conceitos Fundamentais

A memória física é dividida em:

```text
Frames
```

ou

```text
Quadros
```

---

## Exemplo

```text
RAM

Frame 0
Frame 1
Frame 2
Frame 3
```

---

# Páginas

O espaço de memória de um processo é dividido em:

```text
Páginas
```

Cada página possui o mesmo tamanho de um frame.

---

## Exemplo

```text
Processo

Página 0
Página 1
Página 2
Página 3
```

---

# Mapeamento

As páginas não precisam ficar juntas na memória.

Exemplo:

```text
Página 0 → Frame 7
Página 1 → Frame 2
Página 2 → Frame 15
Página 3 → Frame 4
```

---

# Vantagem da Paginação

Os blocos podem ficar espalhados pela memória.

Isso elimina a fragmentação externa.

---

# Tabela de Páginas

Para localizar cada página, o sistema operacional utiliza uma:

```text
Tabela de Páginas
```

Exemplo:

| Página | Frame |
|----------|----------|
| 0 | 7 |
| 1 | 2 |
| 2 | 15 |
| 3 | 4 |

---

# Tradução de Endereços

Fluxo:

```text
Endereço Virtual
↓
Tabela de Páginas
↓
Frame
↓
Endereço Físico
```

---

# MMU e Paginação

A MMU (Memory Management Unit) realiza a tradução automaticamente.

Fluxo:

```text
CPU
↓
Endereço Virtual
↓
MMU
↓
Memória Física
```

---

# Fragmentação na Paginação

A paginação elimina a fragmentação externa.

Porém pode ocorrer:

```text
Fragmentação Interna
```

---

## Exemplo

Página:

```text
4 KB
```

Dados:

```text
3 KB
```

Espaço desperdiçado:

```text
1 KB
```

---

# Memória Virtual

A paginação é a base da memória virtual moderna.

Permite:

- Executar programas maiores que a RAM.
- Utilizar swap.
- Isolar processos.

---

# Segmentação

A segmentação organiza a memória com base na estrutura lógica dos programas.

Ao invés de páginas de tamanho fixo, utiliza segmentos de tamanho variável.

---

# Conceito de Segmento

Um processo pode ser dividido em:

```text
Código
Dados
Pilha
Heap
```

Cada parte forma um segmento.

---

# Exemplo

```text
Segmento Código
Segmento Dados
Segmento Pilha
Segmento Heap
```

Cada um possui tamanho próprio.

---

# Estrutura de um Endereço Segmentado

Um endereço é composto por:

```text
Número do Segmento
+
Deslocamento
```

---

# Tabela de Segmentos

O sistema operacional mantém uma tabela contendo:

- Endereço base.
- Limite do segmento.

Exemplo:

| Segmento | Base | Limite |
|-----------|--------|---------|
| Código | 1000 | 500 |
| Dados | 2000 | 300 |
| Pilha | 3000 | 400 |

---

# Tradução de Endereços na Segmentação

Fluxo:

```text
Segmento
↓
Tabela de Segmentos
↓
Endereço Físico
```

---

# Vantagens da Segmentação

- Organização lógica.
- Proteção independente.
- Compartilhamento facilitado.
- Flexibilidade.

---

# Desvantagens da Segmentação

- Fragmentação externa.
- Maior complexidade.

---

# Paginação x Segmentação

| Característica | Paginação | Segmentação |
|---------------|-----------|-------------|
| Tamanho dos blocos | Fixo | Variável |
| Fragmentação Externa | Não | Sim |
| Fragmentação Interna | Sim | Menor |
| Organização Lógica | Não | Sim |
| Complexidade | Menor | Maior |

---

# Segmentação com Paginação

Sistemas modernos frequentemente combinam ambas as técnicas.

Exemplo:

```text
Segmentos
↓
Páginas
↓
Frames
```

---

# Sistemas Operacionais Modernos

Atualmente:

- Windows
- Linux
- macOS

utilizam principalmente:

```text
Paginação
+
Memória Virtual
```

A segmentação é utilizada de forma limitada ou complementar.

---

# Exemplo Prático

Imagine um computador com:

```text
RAM = 8 GB
```

Um programa pode enxergar:

```text
Espaço Virtual = 128 TB
```

Isso é possível graças à paginação e à memória virtual.

---

# Benefícios das Técnicas Modernas

- Melhor utilização da memória.
- Proteção entre processos.
- Execução de programas grandes.
- Redução de desperdício.
- Maior estabilidade do sistema.

---

# Resumo

A alocação contígua foi uma das primeiras técnicas de gerenciamento de memória, mas apresenta problemas de fragmentação. A paginação surgiu para eliminar a fragmentação externa, dividindo memória e processos em blocos de tamanho fixo chamados páginas e frames. A segmentação organiza a memória de acordo com a estrutura lógica dos programas, utilizando segmentos de tamanho variável. Os sistemas operacionais modernos utilizam principalmente paginação associada à memória virtual para garantir eficiência e segurança.

---

# Conclusão

As técnicas de alocação contígua, paginação e segmentação representam etapas importantes na evolução do gerenciamento de memória. Cada uma busca resolver problemas específicos relacionados à utilização eficiente da RAM. Atualmente, a paginação é a técnica predominante nos sistemas operacionais modernos, permitindo a implementação de memória virtual e a execução segura de múltiplos processos simultaneamente.