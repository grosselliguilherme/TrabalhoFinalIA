<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# Multiprogramação

## Introdução

A multiprogramação é uma técnica utilizada pelos sistemas operacionais para aumentar a utilização da CPU e melhorar o desempenho geral do sistema.

Seu objetivo principal é permitir que vários programas permaneçam na memória principal ao mesmo tempo, possibilitando que a CPU execute outro programa quando o atual estiver aguardando alguma operação de entrada e saída.

Essa técnica foi um marco importante na evolução dos sistemas operacionais modernos.

---

# O Problema dos Sistemas Antigos

Nos primeiros computadores, apenas um programa era executado por vez.

Fluxo:

```text
Programa
↓
CPU executa
↓
Operação de E/S
↓
CPU fica ociosa
```

Durante operações de:

- Leitura de disco
- Impressão
- Comunicação de rede

a CPU permanecia sem realizar trabalho útil.

Consequência:

```text
Baixo aproveitamento da CPU
```

---

# Conceito de Multiprogramação

Na multiprogramação, vários programas permanecem carregados simultaneamente na memória.

Exemplo:

```text
Memória

Programa A
Programa B
Programa C
Programa D
```

Quando um programa entra em espera por uma operação de entrada e saída, a CPU pode executar outro programa.

---

# Objetivos da Multiprogramação

Principais objetivos:

- Melhorar o aproveitamento da CPU.
- Reduzir períodos ociosos.
- Aumentar o número de tarefas executadas.
- Melhorar o desempenho do sistema.
- Aumentar a produtividade dos usuários.

---

# Funcionamento Básico

Considere três programas:

```text
Programa A
Programa B
Programa C
```

Fluxo:

```text
A executa
↓
A solicita E/S
↓
CPU executa B
↓
B solicita E/S
↓
CPU executa C
```

A CPU permanece ocupada durante a maior parte do tempo.

---

# Multiprogramação x Monoprogramação

## Monoprogramação

```text
Programa único
↓
Executa
↓
Espera E/S
↓
CPU ociosa
```

---

## Multiprogramação

```text
Programa A espera
↓
Programa B executa
↓
Programa C executa
```

Resultado:

```text
Maior utilização da CPU
```

---

# Processamento em Lote (Batch)

Antes da multiprogramação, tornou-se comum o processamento em lote.

Os trabalhos eram agrupados e executados automaticamente.

Exemplo:

```text
Job 1
Job 2
Job 3
Job 4
```

O operador carregava diversos trabalhos e o sistema os executava sequencialmente.

---

# Limitações do Processamento em Lote

Problemas:

- Longo tempo de espera.
- Baixa interação com usuários.
- CPU frequentemente ociosa.

Essas limitações motivaram o surgimento da multiprogramação.

---

# Multiprogramação e Memória

Para que a multiprogramação funcione, vários programas devem coexistir na memória.

Exemplo:

```text
Memória RAM

Sistema Operacional

Programa A
Programa B
Programa C
```

O sistema operacional gerencia o espaço ocupado por cada programa.

---

# Escalonamento

O sistema operacional precisa decidir qual processo utilizará a CPU.

Esse mecanismo é chamado de:

```text
Escalonamento
```

O responsável é o:

```text
Escalonador (Scheduler)
```

---

# Escalonador

O escalonador seleciona qual processo será executado.

Critérios comuns:

- Ordem de chegada.
- Prioridade.
- Tempo de execução.
- Justiça entre processos.

---

# Estados de um Processo

Durante a multiprogramação, os processos podem assumir diferentes estados.

---

## Novo (New)

Processo recém-criado.

---

## Pronto (Ready)

Aguardando CPU.

---

## Executando (Running)

Está utilizando a CPU.

---

## Espera (Waiting)

Aguardando algum evento.

Exemplos:

- Disco.
- Teclado.
- Rede.

---

## Finalizado (Terminated)

Execução concluída.

---

# Diagrama Simplificado

```text
Novo
 ↓
Pronto
 ↓
Executando
 ↓
Esperando
 ↓
Pronto
 ↓
Executando
 ↓
Finalizado
```

---

# Troca de Contexto

Quando a CPU passa de um processo para outro ocorre uma:

```text
Troca de Contexto
```

ou

```text
Context Switch
```

---

## O que é Salvo?

O sistema operacional armazena:

- Registradores.
- Contador de programa.
- Estado da CPU.

Posteriormente o processo pode continuar de onde parou.

---

# Context Switch

Exemplo:

```text
Processo A executa
↓
Interrupção
↓
Estado salvo
↓
Processo B executa
```

---

# Vantagens da Multiprogramação

## Melhor Utilização da CPU

Menos tempo ocioso.

---

## Maior Throughput

Throughput:

```text
Quantidade de trabalhos concluídos
```

em determinado período.

---

## Maior Produtividade

Mais programas podem ser executados simultaneamente.

---

## Melhor Aproveitamento dos Recursos

CPU, memória e dispositivos trabalham de forma mais eficiente.

---

# Desvantagens da Multiprogramação

## Maior Complexidade

O sistema operacional torna-se mais complexo.

---

## Necessidade de Gerenciamento de Memória

Vários programas compartilham a memória.

---

## Sobrecarga de Context Switch

Trocas frequentes de contexto consomem recursos.

---

## Possibilidade de Deadlocks

Processos podem competir por recursos.

---

# Multiprogramação x Multitarefa

Muitas vezes os conceitos são confundidos.

---

## Multiprogramação

Foco:

```text
Maximizar uso da CPU
```

O sistema alterna entre processos quando um deles fica bloqueado.

---

## Multitarefa

Foco:

```text
Interatividade
```

A CPU alterna rapidamente entre processos, dando a impressão de simultaneidade.

---

# Multiprogramação x Multiprocessamento

## Multiprogramação

```text
Uma CPU
Vários processos
```

---

## Multiprocessamento

```text
Múltiplas CPUs ou núcleos
```

Vários processos podem realmente executar ao mesmo tempo.

---

# Time-Sharing

O conceito de Time-Sharing evoluiu a partir da multiprogramação.

Cada processo recebe uma pequena fatia de tempo chamada:

```text
Quantum
```

Exemplo:

```text
A → B → C → A → B → C
```

A troca ocorre rapidamente.

---

# Benefícios do Time-Sharing

- Maior interatividade.
- Melhor experiência do usuário.
- Compartilhamento eficiente da CPU.

---

# Exemplo Prático

Imagine um usuário:

- Navegando na Internet.
- Ouvindo música.
- Editando um documento.

Embora pareça que tudo ocorre simultaneamente, o sistema operacional está alternando entre diversos processos.

---

# Multiprogramação nos Sistemas Modernos

Todos os sistemas operacionais modernos utilizam conceitos de multiprogramação.

Exemplos:

- Linux
- Windows
- macOS
- Android
- iOS

Esses sistemas executam centenas ou até milhares de processos simultaneamente.

---

# Resumo

A multiprogramação é uma técnica que permite manter vários programas na memória ao mesmo tempo, aumentando a utilização da CPU e melhorando o desempenho geral do sistema. Quando um processo fica aguardando operações de entrada e saída, outro pode utilizar a CPU. Esse conceito foi fundamental para a evolução dos sistemas operacionais modernos e serviu de base para mecanismos como multitarefa e time-sharing.

---

# Conclusão

A multiprogramação representa um dos avanços mais importantes da história dos sistemas operacionais. Ao permitir que múltiplos processos compartilhem os recursos do sistema de forma eficiente, ela reduz o desperdício de processamento e melhora significativamente o desempenho computacional. Seus princípios continuam presentes em praticamente todos os sistemas operacionais atuais.