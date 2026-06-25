<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# Programação Concorrente

## Introdução

A Programação Concorrente é uma técnica que permite que múltiplas tarefas sejam executadas de forma sobreposta ao longo do tempo.

Nos sistemas operacionais modernos, diversos processos e threads executam simultaneamente ou aparentemente simultaneamente, compartilhando recursos do sistema.

A concorrência é fundamental para melhorar a utilização dos recursos computacionais e aumentar a capacidade de resposta das aplicações.

---

# Conceito de Concorrência

Concorrência é a capacidade de um sistema lidar com múltiplas tarefas durante um mesmo intervalo de tempo.

Exemplo:

```text
Tarefa A
Tarefa B
Tarefa C
```

O sistema alterna rapidamente entre elas.

---

# Concorrência x Paralelismo

Embora os termos sejam frequentemente confundidos, eles possuem significados diferentes.

---

## Concorrência

Múltiplas tarefas progridem ao mesmo tempo.

Exemplo:

```text
CPU Única

A → B → C → A → B → C
```

A CPU alterna rapidamente entre as tarefas.

---

## Paralelismo

Múltiplas tarefas executam exatamente ao mesmo tempo.

Exemplo:

```text
CPU 1 → Tarefa A
CPU 2 → Tarefa B
CPU 3 → Tarefa C
```

Ocorre em sistemas com múltiplos núcleos ou processadores.

---

# Processos

Um processo é um programa em execução.

Cada processo possui:

- Espaço de memória próprio.
- Registradores próprios.
- Contador de programa.
- Recursos associados.

---

## Exemplo

Programas abertos simultaneamente:

```text
Google Chrome
Visual Studio Code
Spotify
```

Cada um representa um processo diferente.

---

# Estados de um Processo

Um processo pode assumir diferentes estados.

---

## Novo (New)

Processo criado.

---

## Pronto (Ready)

Aguardando CPU.

---

## Executando (Running)

Utilizando a CPU.

---

## Esperando (Waiting)

Aguardando algum evento.

Exemplos:

- Leitura de disco.
- Entrada do teclado.
- Resposta da rede.

---

## Finalizado (Terminated)

Execução concluída.

---

# Threads

Uma thread é uma unidade de execução dentro de um processo.

Um processo pode possuir:

```text
1 ou mais threads
```

---

## Exemplo

Navegador Web:

```text
Processo Chrome

├── Thread Interface
├── Thread Rede
├── Thread Renderização
└── Thread Downloads
```

---

# Vantagens das Threads

- Menor consumo de memória.
- Maior desempenho.
- Compartilhamento de dados.
- Melhor capacidade de resposta.

---

# Processos x Threads

| Característica | Processo | Thread |
|---------------|-----------|---------|
| Memória própria | Sim | Não |
| Isolamento | Alto | Baixo |
| Criação | Mais custosa | Mais rápida |
| Comunicação | Mais complexa | Mais simples |

---

# Recursos Compartilhados

Quando várias threads executam simultaneamente, elas podem compartilhar:

- Variáveis.
- Arquivos.
- Conexões de rede.
- Estruturas de dados.

Isso aumenta o desempenho, mas também cria desafios.

---

# Região Crítica

Uma Região Crítica é um trecho do programa que acessa recursos compartilhados.

Exemplo:

```python
saldo = saldo + 100
```

Se várias threads modificarem a variável ao mesmo tempo, problemas podem ocorrer.

---

# Condição de Corrida (Race Condition)

Uma Condição de Corrida ocorre quando o resultado da execução depende da ordem em que as threads acessam um recurso compartilhado.

---

## Exemplo

Saldo inicial:

```text
1000
```

Thread A:

```text
Lê 1000
Adiciona 100
```

Thread B:

```text
Lê 1000
Subtrai 50
```

Resultado esperado:

```text
1050
```

Resultado possível:

```text
950
1100
1050
```

Dependendo da ordem de execução.

---

# Exclusão Mútua

A Exclusão Mútua garante que apenas uma thread por vez acesse uma região crítica.

Objetivo:

```text
Evitar condições de corrida
```

---

# Locks

Um Lock é um mecanismo utilizado para implementar exclusão mútua.

Fluxo:

```text
Thread A
↓
Obtém Lock
↓
Executa
↓
Libera Lock
```

Enquanto isso:

```text
Thread B
↓
Espera
```

---

# Mutex

Mutex significa:

```text
Mutual Exclusion
```

É um dos mecanismos mais utilizados para proteger regiões críticas.

---

## Exemplo Conceitual

```text
Mutex Livre
↓
Thread A entra
↓
Mutex Ocupado
↓
Thread B espera
```

---

# Semáforos

Semáforos são mecanismos de sincronização criados por Edsger Dijkstra.

Controlam o acesso a recursos compartilhados.

---

## Semáforo Binário

Possui apenas dois valores:

```text
0
1
```

Funciona de forma semelhante a um Mutex.

---

## Semáforo Contador

Permite controlar múltiplas instâncias de um recurso.

Exemplo:

```text
5 conexões disponíveis
```

Cada utilização reduz o contador.

---

# Operações dos Semáforos

---

## wait()

Solicita acesso ao recurso.

```text
Contador--
```

---

## signal()

Libera o recurso.

```text
Contador++
```

---

# Problema do Produtor-Consumidor

Exemplo clássico de sincronização.

---

## Produtor

Adiciona itens ao buffer.

---

## Consumidor

Remove itens do buffer.

---

## Objetivo

Garantir que:

- O buffer não transborde.
- O consumidor não leia dados inexistentes.

---

# Monitores

Monitores são mecanismos de sincronização de alto nível.

Eles combinam:

- Variáveis compartilhadas.
- Procedimentos.
- Exclusão mútua automática.

---

# Deadlock

Deadlock ocorre quando dois ou mais processos ficam bloqueados indefinidamente aguardando recursos uns dos outros.

---

## Exemplo

```text
Processo A
possui Recurso 1
aguarda Recurso 2

Processo B
possui Recurso 2
aguarda Recurso 1
```

Nenhum consegue prosseguir.

---

# Condições Necessárias para Deadlock

Segundo Coffman, quatro condições devem existir simultaneamente.

---

## Exclusão Mútua

Um recurso só pode ser utilizado por um processo de cada vez.

---

## Posse e Espera

Processo mantém recursos enquanto aguarda outros.

---

## Não Preempção

Recursos não podem ser retirados à força.

---

## Espera Circular

Existe um ciclo de dependências.

---

# Prevenção de Deadlocks

Estratégias:

- Eliminar espera circular.
- Limitar aquisição de recursos.
- Utilizar ordenação de recursos.

---

# Starvation

Starvation ocorre quando um processo espera indefinidamente por recursos.

Exemplo:

```text
Processo de baixa prioridade
nunca recebe CPU
```

---

# Concorrência em Sistemas Operacionais

Os sistemas modernos utilizam concorrência em diversas situações.

Exemplos:

- Navegadores.
- Bancos de dados.
- Sistemas distribuídos.
- Servidores Web.
- Aplicações móveis.

---

# Benefícios da Programação Concorrente

- Melhor utilização da CPU.
- Maior desempenho.
- Maior responsividade.
- Melhor aproveitamento de múltiplos núcleos.

---

# Desafios da Programação Concorrente

- Race Conditions.
- Deadlocks.
- Starvation.
- Complexidade de implementação.
- Dificuldade de depuração.

---

# Exemplo Prático

Em um navegador moderno:

```text
Thread Interface
Thread Rede
Thread Renderização
Thread Downloads
```

Todas trabalham de forma concorrente para melhorar a experiência do usuário.

---

# Resumo

A Programação Concorrente permite que múltiplas tarefas sejam executadas de forma sobreposta, aumentando o desempenho e a eficiência dos sistemas computacionais. Os principais conceitos incluem processos, threads, regiões críticas, exclusão mútua, mutexes, semáforos, monitores e deadlocks. Esses mecanismos são essenciais para garantir a sincronização correta de recursos compartilhados em sistemas modernos.

---

# Conclusão

A Programação Concorrente é um dos pilares dos sistemas operacionais modernos. Ela possibilita que diversas atividades sejam executadas simultaneamente ou de forma intercalada, aproveitando melhor os recursos computacionais. Embora ofereça grandes benefícios de desempenho e escalabilidade, também introduz desafios relacionados à sincronização e ao compartilhamento de recursos, tornando fundamental o entendimento de conceitos como mutexes, semáforos e deadlocks.