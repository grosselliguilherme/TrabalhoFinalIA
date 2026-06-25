<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# System Calls (Chamadas de Sistema)

## Introdução

As System Calls (Chamadas de Sistema) são mecanismos que permitem que programas de usuário solicitem serviços ao sistema operacional.

Elas funcionam como uma interface entre aplicações e o Kernel.

Sem as System Calls, programas não poderiam acessar recursos protegidos do computador, como memória, arquivos, dispositivos de entrada e saída ou processos.

---

# O Problema que as System Calls Resolvem

Considere um programa que deseja:

- Criar um arquivo.
- Ler dados do disco.
- Criar um processo.
- Enviar dados pela rede.

Essas operações exigem acesso direto ao hardware ou a recursos críticos do sistema.

Por questões de segurança, aplicações comuns não possuem esse acesso.

Assim, elas precisam solicitar ao sistema operacional que execute essas tarefas.

---

# O que é uma System Call?

Uma System Call é uma solicitação feita por um programa ao Kernel para executar uma operação privilegiada.

Fluxo:

```text
Programa
↓
System Call
↓
Kernel
↓
Hardware
```

O Kernel executa a operação e devolve o resultado ao programa.

---

# Relação entre User Mode e Kernel Mode

Os processadores modernos trabalham em dois modos.

---

## User Mode

Modo utilizado por aplicações.

Características:

- Acesso restrito.
- Não pode acessar hardware diretamente.
- Não pode executar instruções privilegiadas.

Exemplos:

- Navegador.
- Editor de texto.
- Jogos.

---

## Kernel Mode

Modo utilizado pelo sistema operacional.

Características:

- Acesso total ao hardware.
- Controle da memória.
- Controle dos dispositivos.
- Controle dos processos.

---

# Fluxo de uma System Call

Exemplo:

```text
Aplicação deseja ler arquivo
↓
System Call read()
↓
Mudança para Kernel Mode
↓
Kernel acessa disco
↓
Retorna dados
↓
Volta para User Mode
```

---

# Transição de Modo

Quando uma System Call ocorre:

```text
User Mode
↓
Kernel Mode
↓
User Mode
```

Essa mudança é controlada pelo hardware e pelo sistema operacional.

---

# Categorias de System Calls

As chamadas de sistema geralmente são divididas em grupos.

---

## Controle de Processos

Responsáveis pela criação e gerenciamento de processos.

Exemplos:

- fork()
- exec()
- wait()
- exit()

---

## Gerenciamento de Arquivos

Permitem manipular arquivos.

Exemplos:

- open()
- read()
- write()
- close()

---

## Gerenciamento de Dispositivos

Controlam dispositivos de entrada e saída.

Exemplos:

- leitura de teclado
- impressão
- acesso à rede

---

## Gerenciamento de Informações

Obtêm informações sobre o sistema.

Exemplos:

- data
- hora
- informações de processos

---

## Comunicação

Permitem troca de informações entre processos.

Exemplos:

- pipes
- sockets
- memória compartilhada

---

# Principais System Calls do Linux

---

## fork()

Cria um novo processo.

Exemplo:

```c
pid = fork();
```

Após a execução:

```text
Processo Pai
↓
Processo Filho
```

Os dois continuam executando independentemente.

---

## Exemplo Conceitual

Antes:

```text
Processo A
```

Depois:

```text
Processo A
Processo B
```

---

# exec()

Substitui o código de um processo por outro programa.

Exemplo:

```c
exec("programa");
```

Muito utilizada após o fork().

---

## Fluxo Típico

```text
fork()
↓
Processo Filho
↓
exec()
↓
Novo Programa
```

---

# wait()

Permite que um processo aguarde o término de outro.

Exemplo:

```c
wait(NULL);
```

Muito utilizada pelo processo pai.

---

## Exemplo

```text
Pai
↓
Espera
↓
Filho termina
↓
Pai continua
```

---

# exit()

Finaliza um processo.

Exemplo:

```c
exit(0);
```

O valor informado normalmente indica sucesso ou erro.

---

# open()

Abre um arquivo.

Exemplo:

```c
fd = open("arquivo.txt");
```

O retorno geralmente é um descritor de arquivo.

---

# File Descriptor

Ao abrir um arquivo, o sistema retorna um identificador.

Exemplo:

```text
fd = 3
```

Esse número será utilizado em operações futuras.

---

# read()

Lê dados de um arquivo.

Exemplo:

```c
read(fd, buffer, tamanho);
```

---

## Funcionamento

```text
Arquivo
↓
Kernel
↓
Buffer
↓
Programa
```

---

# write()

Escreve dados em um arquivo.

Exemplo:

```c
write(fd, buffer, tamanho);
```

---

## Funcionamento

```text
Programa
↓
Buffer
↓
Kernel
↓
Arquivo
```

---

# close()

Fecha um arquivo.

Exemplo:

```c
close(fd);
```

Importância:

- Libera recursos.
- Evita vazamentos de descritores.

---

# Exemplo Completo de Arquivos

Fluxo típico:

```text
open()
↓
read()
↓
write()
↓
close()
```

---

# System Calls de Memória

Algumas chamadas manipulam memória.

Exemplos:

- mmap()
- brk()
- munmap()

---

# mmap()

Mapeia regiões de memória.

Utilizada para:

- Arquivos.
- Memória compartilhada.
- Bibliotecas.

---

# Comunicação entre Processos

System Calls também permitem comunicação.

---

## Pipe

Canal de comunicação entre processos.

Exemplo:

```text
Processo A
↓
Pipe
↓
Processo B
```

---

## Socket

Permite comunicação local ou pela rede.

Muito utilizado por:

- Servidores.
- Navegadores.
- Aplicações distribuídas.

---

# Exemplo de Uso Real

Ao abrir um navegador e acessar um site:

```text
Aplicação
↓
socket()
↓
Conexão TCP
↓
Envio de dados
↓
Recebimento de resposta
```

Diversas System Calls são utilizadas internamente.

---

# Interrupções e System Calls

As System Calls normalmente utilizam mecanismos de interrupção ou instruções especiais do processador para transferir o controle ao Kernel.

Exemplos modernos:

```text
syscall
sysenter
int 0x80
```

---

# Overhead das System Calls

As chamadas de sistema possuem custo.

Motivo:

```text
Troca User Mode
↓
Kernel Mode
↓
User Mode
```

Essa mudança exige processamento adicional.

---

# Segurança

As System Calls ajudam a proteger o sistema.

Benefícios:

- Controle de acesso.
- Isolamento de processos.
- Proteção do hardware.
- Prevenção de operações não autorizadas.

---

# Vantagens das System Calls

- Segurança.
- Controle centralizado.
- Abstração do hardware.
- Portabilidade.
- Facilidade para os programadores.

---

# Desvantagens

- Sobrecarga de execução.
- Troca de contexto.
- Dependência do sistema operacional.

---

# Exemplo Completo

Imagine que um editor de texto deseja salvar um arquivo.

Fluxo:

```text
Editor
↓
open()
↓
write()
↓
close()
↓
Kernel
↓
Disco
```

O programa não acessa o disco diretamente.

Todas as operações passam pelo sistema operacional.

---

# Resumo

As System Calls são mecanismos que permitem que aplicações solicitem serviços ao Kernel do sistema operacional. Elas constituem a principal interface entre programas e recursos protegidos do computador. Operações como criação de processos, manipulação de arquivos, gerenciamento de memória e comunicação em rede dependem diretamente dessas chamadas.

---

# Conclusão

As Chamadas de Sistema representam a ponte entre os programas de usuário e o núcleo do sistema operacional. Por meio delas, aplicações conseguem utilizar recursos de hardware e serviços do sistema de forma segura e controlada. Compreender System Calls é fundamental para entender o funcionamento interno dos sistemas operacionais modernos e a interação entre software e hardware.