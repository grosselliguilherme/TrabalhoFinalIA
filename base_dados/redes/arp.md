<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# ARP (Address Resolution Protocol)

## Introdução

O ARP (Address Resolution Protocol) é um protocolo utilizado para descobrir o endereço físico (MAC Address) associado a um determinado endereço IP dentro de uma rede local.

Ele atua como uma ponte entre a Camada de Rede e a Camada de Enlace do Modelo OSI.

Embora a comunicação entre redes utilize endereços IP, a transmissão local de quadros Ethernet depende de endereços MAC. O ARP é responsável por realizar essa conversão.

---

## O Problema que o ARP Resolve

Considere a seguinte situação:

```text
Computador A

IP: 192.168.1.10
```

Deseja enviar dados para:

```text
Computador B

IP: 192.168.1.20
```

O computador conhece o IP de destino, mas a Ethernet exige que o quadro seja enviado para um endereço MAC.

Pergunta:

```text
Qual é o MAC associado ao IP 192.168.1.20?
```

O ARP responde essa pergunta.

---

## Posição no Modelo OSI

O ARP atua entre:

```text
Camada de Rede
(IP)

e

Camada de Enlace
(MAC)
```

Por isso costuma ser considerado um protocolo intermediário.

---

## Funcionamento Geral

O funcionamento do ARP ocorre em duas etapas:

### 1. ARP Request

O dispositivo envia uma mensagem para toda a rede perguntando:

```text
Quem possui o IP 192.168.1.20?
```

---

### 2. ARP Reply

O dispositivo que possui aquele IP responde:

```text
Eu possuo esse IP.

Meu MAC é:
00:1A:2B:3C:4D:5E
```

---

## Exemplo Completo

Considere:

```text
PC A

IP:
192.168.1.10

MAC:
AA:AA:AA:AA:AA:AA
```

e

```text
PC B

IP:
192.168.1.20

MAC:
BB:BB:BB:BB:BB:BB
```

---

### Passo 1

PC A deseja enviar dados para:

```text
192.168.1.20
```

---

### Passo 2

PC A verifica sua tabela ARP.

Se não encontrar o endereço correspondente:

```text
Inicia ARP Request
```

---

### Passo 3

Mensagem enviada em broadcast:

```text
Quem possui o IP 192.168.1.20?
```

---

### Passo 4

Todos os dispositivos recebem a solicitação.

---

### Passo 5

Somente PC B responde:

```text
192.168.1.20
=
BB:BB:BB:BB:BB:BB
```

---

### Passo 6

PC A armazena essa informação em sua tabela ARP.

---

### Passo 7

Os quadros Ethernet passam a ser enviados para:

```text
BB:BB:BB:BB:BB:BB
```

---

## ARP Request

O ARP Request é enviado utilizando:

### Endereço MAC de Destino

```text
FF:FF:FF:FF:FF:FF
```

Esse endereço representa:

```text
Broadcast
```

Todos os dispositivos da LAN recebem a mensagem.

---

## ARP Reply

A resposta é enviada diretamente para o solicitante.

Tipo:

```text
Unicast
```

Somente o dispositivo que fez a solicitação recebe a resposta.

---

## Tabela ARP

Os dispositivos mantêm uma tabela contendo associações entre IPs e MACs.

Exemplo:

```text
IP               MAC

192.168.1.1      11:11:11:11:11:11
192.168.1.20     BB:BB:BB:BB:BB:BB
192.168.1.50     CC:CC:CC:CC:CC:CC
```

Essa tabela reduz a quantidade de consultas ARP necessárias.

---

## Cache ARP

A tabela ARP normalmente é armazenada em memória.

Por isso também é chamada de:

```text
Cache ARP
```

As entradas possuem tempo de vida limitado.

Após determinado período:

```text
São removidas
```

e poderão ser descobertas novamente.

---

## Visualizando a Tabela ARP

### Windows

```cmd
arp -a
```

---

### Linux

```bash
arp -a
```

ou

```bash
ip neigh
```

---

## Exemplo de Saída

```text
Interface: 192.168.1.10

Internet Address      Physical Address

192.168.1.1           00-11-22-33-44-55
192.168.1.20          BB-BB-BB-BB-BB-BB
```

---

## ARP Gratuito (Gratuitous ARP)

É uma mensagem ARP enviada por um dispositivo para anunciar seu próprio endereço IP e MAC.

Objetivos:

- Atualizar caches ARP.
- Detectar conflitos de IP.
- Informar alterações de endereço físico.

---

## Proxy ARP

Permite que um roteador responda solicitações ARP em nome de outro dispositivo.

Exemplo:

```text
Host A
↓
Roteador
↓
Host B
```

O roteador pode responder ao ARP mesmo sem ser o destino final.

---

## ARP e Comunicação Local

O ARP funciona apenas dentro da rede local.

Exemplo:

```text
192.168.1.10
↓
192.168.1.20
```

O ARP pode resolver o MAC diretamente.

---

## ARP e Comunicação Externa

Considere:

```text
192.168.1.10
↓
8.8.8.8
```

O computador não procura o MAC do Google.

Ele procura o MAC do:

```text
Gateway Padrão
```

Exemplo:

```text
192.168.1.1
```

Assim os pacotes são enviados ao roteador.

---

## Relação entre ARP e IP

O IP identifica:

```text
Quem receberá o pacote
```

O ARP descobre:

```text
Para qual MAC o quadro deve ser enviado
```

Exemplo:

```text
IP:
192.168.1.20

↓

ARP

↓

MAC:
BB:BB:BB:BB:BB:BB
```

---

## Estrutura de uma Mensagem ARP

Uma mensagem ARP contém informações como:

```text
Tipo de Hardware
Tipo de Protocolo
MAC de Origem
IP de Origem
MAC de Destino
IP de Destino
Operação
```

---

## Operações ARP

Existem dois tipos principais.

### Request

```text
Pergunta
```

Quem possui determinado IP?

---

### Reply

```text
Resposta
```

Eu possuo esse IP.

---

## Limitações do ARP

O ARP possui algumas limitações.

### Broadcast Excessivo

Em redes grandes podem existir muitas solicitações.

---

### Segurança

O protocolo não possui autenticação.

Isso permite ataques de falsificação.

---

## ARP Spoofing

Também conhecido como:

```text
ARP Poisoning
```

O atacante envia respostas ARP falsas.

Exemplo:

```text
IP do Gateway
↓

MAC do Atacante
```

Consequência:

Os pacotes podem ser redirecionados para o invasor.

---

## Ataque Man-in-the-Middle

Um dos ataques mais comuns envolvendo ARP.

Fluxo:

```text
Computador
↓
Atacante
↓
Roteador
```

O atacante intercepta a comunicação sem que os usuários percebam.

---

## Medidas de Segurança

Algumas formas de proteção incluem:

### Entradas ARP Estáticas

Mapeamentos configurados manualmente.

---

### Switches Gerenciáveis

Recursos como:

```text
Dynamic ARP Inspection (DAI)
```

---

### Segmentação da Rede

Utilização de VLANs.

---

### Monitoramento

Ferramentas de detecção de anomalias.

---

## ARP x DNS

São protocolos diferentes.

### ARP

Converte:

```text
IP → MAC
```

---

### DNS

Converte:

```text
Nome → IP
```

Exemplo:

```text
google.com
↓

142.250.190.78
```

---

## Importância do ARP

Sem o ARP, dispositivos Ethernet não conseguiriam descobrir para qual endereço físico enviar seus quadros.

Ele é essencial para:

- Redes locais.
- Comunicação Ethernet.
- Funcionamento do IPv4.
- Encaminhamento de pacotes.

---

## Conclusão

O ARP (Address Resolution Protocol) é responsável por associar endereços IP a endereços MAC dentro de uma rede local. Ele permite que dispositivos descubram o endereço físico necessário para a transmissão de quadros Ethernet, tornando possível a comunicação entre hosts em uma LAN. Apesar de simples, o ARP desempenha papel fundamental no funcionamento das redes IPv4 modernas e na integração entre as camadas de Rede e Enlace do Modelo OSI.