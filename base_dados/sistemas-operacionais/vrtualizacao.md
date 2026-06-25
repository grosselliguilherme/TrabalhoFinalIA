<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# Virtualização

## Introdução

A Virtualização é uma tecnologia que permite criar versões virtuais de recursos computacionais, como computadores, sistemas operacionais, redes e dispositivos de armazenamento.

Seu principal objetivo é permitir que múltiplos ambientes computacionais sejam executados em um mesmo hardware físico, aumentando o aproveitamento dos recursos disponíveis.

A virtualização é amplamente utilizada em:

- Data Centers
- Computação em Nuvem
- Ambientes de Desenvolvimento
- Testes de Software
- Consolidação de Servidores

---

# Conceito de Virtualização

Em um ambiente tradicional:

```text
Hardware
↓
Sistema Operacional
↓
Aplicações
```

Existe apenas um sistema operacional utilizando o hardware.

Com virtualização:

```text
Hardware
↓
Hypervisor
↓
VM 1
VM 2
VM 3
```

Vários sistemas operacionais podem compartilhar o mesmo hardware.

---

# Máquina Virtual (Virtual Machine)

Uma Máquina Virtual (VM) é um computador criado por software.

Ela possui seus próprios recursos virtuais:

- CPU virtual
- Memória virtual
- Disco virtual
- Placa de rede virtual

Para o sistema operacional convidado, a VM parece um computador real.

---

# Sistema Hospedeiro e Sistema Convidado

---

## Host (Hospedeiro)

Sistema operacional instalado diretamente no hardware.

Exemplo:

```text
Windows
```

---

## Guest (Convidado)

Sistema operacional executado dentro da máquina virtual.

Exemplo:

```text
Ubuntu Linux
```

---

# Exemplo de Virtualização

```text
Hardware Físico

CPU
RAM
SSD
Rede

↓

Hypervisor

↓

Windows Server
Ubuntu
Debian
Fedora
```

Todos executando simultaneamente.

---

# Hypervisor

O Hypervisor é o software responsável por criar e gerenciar máquinas virtuais.

Funções:

- Criar VMs.
- Distribuir recursos.
- Isolar ambientes.
- Gerenciar hardware virtual.

---

# Tipos de Hypervisor

Existem dois tipos principais.

---

# Hypervisor Tipo 1

Também chamado de:

```text
Bare Metal
```

Executa diretamente sobre o hardware.

Estrutura:

```text
Hardware
↓
Hypervisor
↓
Máquinas Virtuais
```

---

## Vantagens

- Melhor desempenho.
- Maior segurança.
- Menor overhead.
- Uso corporativo.

---

## Exemplos

- VMware ESXi
- Microsoft Hyper-V Server
- Xen
- KVM

---

# Hypervisor Tipo 2

Executa sobre um sistema operacional já instalado.

Estrutura:

```text
Hardware
↓
Sistema Operacional
↓
Hypervisor
↓
Máquinas Virtuais
```

---

## Vantagens

- Instalação simples.
- Ideal para estudos.
- Ideal para desenvolvimento.

---

## Desvantagens

- Menor desempenho.
- Maior consumo de recursos.

---

## Exemplos

- VirtualBox
- VMware Workstation
- Parallels Desktop

---

# Comparação entre Hypervisores

| Característica | Tipo 1 | Tipo 2 |
|---------------|---------|---------|
| Executa sobre hardware | Sim | Não |
| Executa sobre SO | Não | Sim |
| Desempenho | Maior | Menor |
| Segurança | Maior | Menor |
| Uso corporativo | Sim | Limitado |
| Facilidade de uso | Menor | Maior |

---

# Virtualização Completa

Na virtualização completa, o sistema operacional convidado não precisa ser modificado.

Ele acredita estar executando em hardware real.

Exemplo:

```text
Windows dentro do VirtualBox
```

---

# Paravirtualização

Na paravirtualização, o sistema operacional convidado é adaptado para interagir melhor com o hypervisor.

Vantagens:

- Menor overhead.
- Melhor desempenho.

Desvantagem:

- Requer modificações no sistema operacional.

---

# Recursos Virtualizados

---

## CPU

O hypervisor distribui tempo de processamento entre as VMs.

---

## Memória

Cada VM recebe uma quantidade específica de RAM.

Exemplo:

```text
VM 1 → 4 GB
VM 2 → 8 GB
VM 3 → 2 GB
```

---

## Armazenamento

Cada VM utiliza discos virtuais.

Exemplos:

```text
.vdi
.vmdk
.vhd
```

---

## Rede

O hypervisor cria interfaces de rede virtuais.

---

# Modos de Rede em Máquinas Virtuais

---

## NAT

A VM acessa a Internet utilizando o endereço IP do host.

---

## Bridge

A VM recebe um endereço IP próprio na rede.

---

## Host-Only

A comunicação ocorre apenas entre host e VM.

---

# Snapshots

Um Snapshot representa uma fotografia do estado da máquina virtual.

Armazena:

- Disco.
- Memória.
- Configurações.

---

## Utilização

Permite:

```text
Testar alterações
↓
Problema
↓
Restaurar Snapshot
```

---

# Clonagem de Máquinas Virtuais

Permite criar cópias completas de uma VM.

Vantagens:

- Rapidez.
- Padronização.
- Facilidade de implantação.

---

# Vantagens da Virtualização

---

## Melhor Aproveitamento de Hardware

Menor desperdício de recursos.

---

## Isolamento

Falhas em uma VM não afetam as demais.

---

## Flexibilidade

Permite executar diferentes sistemas operacionais simultaneamente.

---

## Facilidade de Backup

Snapshots e clones simplificam a recuperação.

---

## Redução de Custos

Menor quantidade de servidores físicos.

---

# Desvantagens da Virtualização

---

## Overhead

Existe perda de desempenho em comparação ao hardware físico.

---

## Consumo de Recursos

Múltiplas VMs exigem mais memória e processamento.

---

## Complexidade

Ambientes grandes podem ser difíceis de administrar.

---

# Containers

Containers são uma forma mais leve de virtualização.

Ao contrário das VMs, eles compartilham o Kernel do sistema operacional.

---

# Estrutura de uma Máquina Virtual

```text
Hardware
↓
Hypervisor
↓
Sistema Operacional
↓
Aplicação
```

---

# Estrutura de um Container

```text
Hardware
↓
Sistema Operacional
↓
Container Engine
↓
Containers
```

---

# Diferenças entre VM e Container

| Característica | VM | Container |
|---------------|----|------------|
| Possui SO próprio | Sim | Não |
| Consumo de memória | Alto | Baixo |
| Inicialização | Lenta | Rápida |
| Isolamento | Alto | Médio |
| Portabilidade | Boa | Excelente |

---

# Docker

Docker é a plataforma de containers mais utilizada atualmente.

Permite empacotar aplicações junto com todas as suas dependências.

---

## Componentes do Docker

### Imagem

Modelo utilizado para criar containers.

---

### Container

Instância em execução de uma imagem.

---

### Docker Hub

Repositório de imagens Docker.

---

# Exemplo de Fluxo Docker

```text
Dockerfile
↓
Imagem
↓
Container
↓
Aplicação Executando
```

---

# Benefícios dos Containers

- Inicialização rápida.
- Menor consumo de recursos.
- Facilidade de implantação.
- Escalabilidade.
- Portabilidade.

---

# Virtualização na Computação em Nuvem

Provedores de nuvem utilizam virtualização extensivamente.

Exemplos:

- Amazon Web Services (AWS)
- Microsoft Azure
- Google Cloud Platform (GCP)

---

# Casos de Uso

---

## Desenvolvimento

Ambientes isolados para testes.

---

## Laboratórios Acadêmicos

Execução de múltiplos sistemas operacionais em um único computador.

---

## Data Centers

Consolidação de servidores físicos.

---

## Computação em Nuvem

Hospedagem de aplicações e serviços.

---

# Exemplos Práticos

Você pode utilizar:

```text
Windows Host
↓
VirtualBox
↓
Ubuntu Linux
```

para estudar Linux sem alterar o sistema principal.

---

# Resumo

A virtualização é uma tecnologia que permite executar múltiplos sistemas operacionais em um único hardware físico através de máquinas virtuais gerenciadas por um hypervisor. Existem hypervisores do Tipo 1 e Tipo 2, cada um adequado para diferentes cenários. Além das máquinas virtuais, os containers surgiram como uma alternativa mais leve, compartilhando o kernel do sistema operacional hospedeiro. Tecnologias como Docker e plataformas de computação em nuvem dependem fortemente desses conceitos.

---

# Conclusão

A virtualização revolucionou a infraestrutura computacional moderna ao permitir melhor aproveitamento de recursos, isolamento de ambientes e maior flexibilidade operacional. Seu uso é fundamental em data centers, ambientes corporativos, laboratórios acadêmicos e serviços de computação em nuvem. O conhecimento sobre máquinas virtuais, hypervisores e containers tornou-se essencial para profissionais de Sistemas Operacionais, Redes de Computadores e Computação em Nuvem.