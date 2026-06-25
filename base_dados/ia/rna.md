<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# RNA - Redes Neurais Artificiais

## Introdução

As Redes Neurais Artificiais (RNAs) são modelos computacionais inspirados no funcionamento do cérebro humano. Elas constituem uma das principais técnicas utilizadas na Inteligência Artificial moderna e servem como base para diversas aplicações de Aprendizado de Máquina e Deep Learning.

O objetivo principal das Redes Neurais Artificiais é aprender padrões a partir de dados e utilizar esse conhecimento para realizar tarefas como classificação, previsão, reconhecimento de padrões, processamento de linguagem natural e visão computacional.

As RNAs são compostas por unidades de processamento chamadas neurônios artificiais, que trabalham de forma semelhante aos neurônios biológicos encontrados no sistema nervoso humano.

## Inspiração Biológica

O cérebro humano é formado por bilhões de neurônios conectados entre si.

Cada neurônio possui:

- Dendritos: recebem sinais.
- Corpo celular: processa informações.
- Axônio: transmite sinais.
- Sinapses: realizam a comunicação entre neurônios.

Quando um estímulo é recebido, o neurônio processa a informação e decide se deve transmitir um sinal para outros neurônios.

As Redes Neurais Artificiais tentam reproduzir esse comportamento utilizando estruturas matemáticas simplificadas.

## Conceito de Neurônio Artificial

O neurônio artificial é a unidade básica de uma RNA.

Seu funcionamento pode ser dividido em etapas:

1. Recebimento das entradas.
2. Multiplicação pelos pesos.
3. Soma ponderada.
4. Aplicação da função de ativação.
5. Produção da saída.

### Estrutura Matemática

Considere as entradas:

```text
x1, x2, x3
```

e os respectivos pesos:

```text
w1, w2, w3
```

O neurônio calcula:

```
z = (x1*w1) + (x2*w2) + (x3*w3) + b
```

onde:

- z = valor calculado
- b = viés (bias)

Após isso, aplica-se uma função de ativação para gerar a saída final.

## Pesos Sinápticos

Os pesos representam a importância de cada entrada.

Características:

- Pesos positivos reforçam a influência da entrada.
- Pesos negativos reduzem a influência da entrada.
- Durante o treinamento os pesos são ajustados.

O aprendizado da rede consiste justamente em encontrar os melhores pesos para resolver determinado problema.

## Bias (Viés)

O bias é um valor adicional utilizado para deslocar a função de ativação.

Ele aumenta a flexibilidade do modelo.

Sem o bias, a capacidade de aprendizado da rede seria reduzida.

## Funções de Ativação

A função de ativação determina a saída do neurônio.

Ela introduz não linearidade no modelo.

Sem funções de ativação, uma rede neural seria equivalente a uma simples combinação linear de variáveis.

### Função Degrau

Uma das primeiras funções utilizadas.

```text
Se z >= 0 → saída = 1
Se z < 0 → saída = 0
```

Muito utilizada no Perceptron original.

### Função Sigmoide

Produz valores entre 0 e 1.

Fórmula:

```text
f(z) = 1 / (1 + e^(-z))
```

Características:

- Fácil interpretação probabilística.
- Muito utilizada em classificações binárias.

### Tangente Hiperbólica (Tanh)

Produz valores entre -1 e 1.

Vantagens:

- Melhor centralização dos dados.
- Convergência mais rápida em alguns casos.

### ReLU (Rectified Linear Unit)

Uma das funções mais utilizadas atualmente.

```text
f(z) = max(0, z)
```

Vantagens:

- Simples.
- Computacionalmente eficiente.
- Facilita o treinamento de redes profundas.

## Arquitetura de uma Rede Neural

Uma RNA é organizada em camadas.

### Camada de Entrada

Recebe os dados do problema.

Exemplo:

- Idade.
- Peso.
- Altura.

Cada atributo corresponde a um neurônio de entrada.

### Camadas Ocultas

Realizam o processamento das informações.

São responsáveis por aprender padrões complexos.

Uma rede pode possuir:

- Uma camada oculta.
- Várias camadas ocultas.

### Camada de Saída

Produz o resultado final.

Exemplos:

- Classe prevista.
- Valor numérico.
- Probabilidade.

## Exemplo de Arquitetura

```text
Entradas
   ↓
Camada Oculta
   ↓
Camada Oculta
   ↓
Saída
```

Essa estrutura permite que a rede aprenda relações complexas entre os dados.

## Processo de Aprendizado

O aprendizado ocorre por meio do ajuste dos pesos da rede.

O objetivo é minimizar os erros entre as previsões realizadas e os resultados corretos.

## Aprendizado Supervisionado

É o método mais comum.

O treinamento utiliza:

- Dados de entrada.
- Respostas corretas (rótulos).

Exemplo:

```text
Imagem → Gato
Imagem → Cachorro
```

A rede aprende a associar padrões às classes corretas.

## Forward Propagation

Também chamado de propagação direta.

Consiste em:

1. Receber os dados de entrada.
2. Processar as informações nas camadas.
3. Produzir uma saída.

É a etapa de realização da previsão.

## Função de Perda

Após gerar uma previsão, a rede mede o erro cometido.

A função de perda quantifica essa diferença.

Exemplos:

### Erro Quadrático Médio (MSE)

Muito utilizado em regressão.

### Entropia Cruzada

Muito utilizada em classificação.

Quanto menor o valor da perda, melhor o desempenho da rede.

## Backpropagation

O Backpropagation é o algoritmo responsável por ajustar os pesos da rede.

Seu funcionamento ocorre em etapas:

1. Calcular o erro.
2. Propagar o erro para trás.
3. Atualizar os pesos.
4. Reduzir gradualmente o erro.

O Backpropagation é um dos algoritmos mais importantes da história das Redes Neurais.

## Gradiente Descendente

O Gradiente Descendente é utilizado para otimizar os pesos.

Objetivo:

Encontrar os valores que minimizam a função de perda.

O algoritmo ajusta os pesos em direção ao menor erro possível.

## Taxa de Aprendizado

A taxa de aprendizado controla o tamanho dos ajustes realizados nos pesos.

### Taxa Muito Alta

Pode causar instabilidade.

### Taxa Muito Baixa

Pode tornar o treinamento lento.

A escolha adequada é fundamental para o desempenho da rede.

## Épocas e Lotes

### Época (Epoch)

Corresponde a uma passagem completa pelos dados de treinamento.

Exemplo:

```text
100 épocas
```

significa que os dados foram utilizados 100 vezes.

### Batch

Quantidade de exemplos processados antes da atualização dos pesos.

### Mini-Batch

Processa pequenos grupos de exemplos.

É a estratégia mais utilizada atualmente.

## Capacidade de Generalização

O objetivo de uma RNA não é apenas memorizar os dados de treinamento.

Ela deve ser capaz de:

- Aprender padrões.
- Aplicar o conhecimento em novos dados.

Essa capacidade é chamada de generalização.

## Overfitting

Ocorre quando a rede aprende excessivamente os dados de treinamento.

Consequências:

- Excelente desempenho no treinamento.
- Baixo desempenho em dados novos.

Sinais de overfitting:

- Erro de treinamento muito baixo.
- Erro de teste elevado.

## Underfitting

Ocorre quando a rede não consegue aprender adequadamente.

Causas:

- Poucos neurônios.
- Poucas épocas.
- Arquitetura inadequada.

Resultado:

- Desempenho ruim tanto no treinamento quanto no teste.

## Vantagens das Redes Neurais

### Aprendizado Automático

Capacidade de aprender diretamente dos dados.

### Modelagem de Relações Complexas

Conseguem representar padrões altamente não lineares.

### Adaptabilidade

Podem ser aplicadas em diversos domínios.

### Escalabilidade

Funcionam bem com grandes volumes de dados.

## Desvantagens das Redes Neurais

### Alto Custo Computacional

Treinamentos podem exigir grande poder de processamento.

### Necessidade de Grandes Bases de Dados

Muitas aplicações dependem de milhares ou milhões de exemplos.

### Baixa Interpretabilidade

Nem sempre é fácil compreender como a rede tomou determinada decisão.

## Aplicações das RNAs

As Redes Neurais Artificiais possuem aplicações em diversas áreas.

### Visão Computacional

- Reconhecimento facial.
- Detecção de objetos.
- Diagnóstico por imagem.

### Processamento de Linguagem Natural

- Chatbots.
- Tradutores automáticos.
- Assistentes virtuais.

### Finanças

- Previsão de mercado.
- Detecção de fraudes.

### Saúde

- Diagnóstico médico.
- Análise de exames.

### Indústria

- Controle de qualidade.
- Manutenção preditiva.

## Relação entre RNA e Deep Learning

Toda técnica de Deep Learning utiliza Redes Neurais Artificiais.

A principal diferença é:

### RNA Tradicional

Poucas camadas ocultas.

### Deep Learning

Múltiplas camadas ocultas profundas.

Quanto maior a profundidade da rede, maior sua capacidade de aprender padrões complexos.

## Conclusão

As Redes Neurais Artificiais representam uma das tecnologias mais importantes da Inteligência Artificial moderna. Inspiradas no funcionamento do cérebro humano, elas utilizam neurônios artificiais, pesos e funções de ativação para aprender padrões a partir de dados. Seu sucesso em áreas como visão computacional, processamento de linguagem natural e aprendizado de máquina tornou as RNAs fundamentais para o desenvolvimento dos sistemas inteligentes atuais e para o avanço do Deep Learning.