<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# IP (Internet Protocol)

## Introdução

O IP (Internet Protocol) é o principal protocolo da Camada de Rede do Modelo OSI e da pilha TCP/IP.

Sua principal função é identificar dispositivos em uma rede e permitir o encaminhamento de pacotes entre diferentes redes até o destino final.

Praticamente toda comunicação realizada na Internet depende do protocolo IP.

---

## O que é um Endereço IP?

Um endereço IP é um identificador lógico atribuído a um dispositivo conectado a uma rede.

Assim como uma residência possui um endereço para receber correspondências, um dispositivo precisa de um endereço IP para enviar e receber dados.

Exemplo:

```text
192.168.1.10
```

Sem um endereço IP, um dispositivo não consegue participar da comunicação em rede.

---

## Funções do Protocolo IP

As principais funções são:

- Identificação de dispositivos.
- Encaminhamento de pacotes.
- Interconexão de redes.
- Roteamento entre origens e destinos.
- Fragmentação de pacotes.

O protocolo IP não garante entrega confiável dos dados.

Essa responsabilidade pertence ao TCP.

---

## Versões do Protocolo IP

Existem duas versões principais.

### IPv4

Versão mais utilizada atualmente.

Possui:

```text
32 bits
```

Exemplo:

```text
192.168.1.10
```

---

### IPv6

Criado para solucionar a escassez de endereços IPv4.

Possui:

```text
128 bits
```

Exemplo:

```text
2001:db8::1
```

---

# IPv4

## Estrutura do IPv4

Um endereço IPv4 possui 32 bits divididos em quatro grupos de 8 bits.

Exemplo:

```text
192.168.1.10
```

Representação binária:

```text
11000000.10101000.00000001.00001010
```

Cada grupo é chamado de octeto.

---

## Faixa de Valores

Cada octeto pode variar entre:

```text
0 e 255
```

Exemplos válidos:

```text
10.0.0.1
172.16.1.5
192.168.1.100
8.8.8.8
```

---

## Rede e Host

Todo endereço IPv4 possui duas partes:

### Parte da Rede

Identifica a rede.

### Parte do Host

Identifica o dispositivo dentro da rede.

Exemplo:

```text
192.168.1.25/24
```

Rede:

```text
192.168.1.0
```

Host:

```text
25
```

---

# Máscara de Rede

## Conceito

A máscara de rede determina quais bits pertencem à rede e quais pertencem ao host.

Exemplo:

```text
255.255.255.0
```

Representação binária:

```text
11111111.11111111.11111111.00000000
```

Os bits com valor 1 representam a rede.

Os bits com valor 0 representam os hosts.

---

## Exemplos de Máscaras

### Classe C

```text
255.255.255.0
```

CIDR:

```text
/24
```

---

### Classe B

```text
255.255.0.0
```

CIDR:

```text
/16
```

---

### Classe A

```text
255.0.0.0
```

CIDR:

```text
/8
```

---

# CIDR

## Conceito

CIDR significa:

```text
Classless Inter-Domain Routing
```

É a forma moderna de representar máscaras.

Exemplos:

```text
192.168.1.0/24
```

```text
10.0.0.0/8
```

```text
172.16.0.0/16
```

O número após a barra indica quantos bits pertencem à rede.

---

# Classes de Endereçamento

Historicamente os endereços IPv4 eram divididos em classes.

---

## Classe A

Faixa:

```text
1.0.0.0
até
126.255.255.255
```

Máscara padrão:

```text
255.0.0.0
```

CIDR:

```text
/8
```

---

## Classe B

Faixa:

```text
128.0.0.0
até
191.255.255.255
```

Máscara padrão:

```text
255.255.0.0
```

CIDR:

```text
/16
```

---

## Classe C

Faixa:

```text
192.0.0.0
até
223.255.255.255
```

Máscara padrão:

```text
255.255.255.0
```

CIDR:

```text
/24
```

---

## Classe D

Utilizada para multicast.

Faixa:

```text
224.0.0.0
até
239.255.255.255
```

---

## Classe E

Reservada para pesquisas.

Faixa:

```text
240.0.0.0
até
255.255.255.255
```

---

# Endereços Privados

São utilizados em redes internas.

Não podem ser roteados diretamente pela Internet.

---

## Faixa Privada Classe A

```text
10.0.0.0/8
```

---

## Faixa Privada Classe B

```text
172.16.0.0/12
```

---

## Faixa Privada Classe C

```text
192.168.0.0/16
```

---

# Endereços Públicos

São endereços únicos na Internet.

Exemplo:

```text
8.8.8.8
```

Servidor DNS público do Google.

---

# Endereço de Rede

Representa a própria rede.

Exemplo:

```text
192.168.1.0/24
```

Nesse caso:

```text
192.168.1.0
```

é o endereço da rede.

Não pode ser atribuído a dispositivos.

---

# Endereço de Broadcast

Utilizado para enviar mensagens a todos os dispositivos da rede.

Exemplo:

```text
192.168.1.255
```

para a rede:

```text
192.168.1.0/24
```

---

# Gateway Padrão

É o dispositivo responsável por encaminhar pacotes para outras redes.

Normalmente é o roteador da rede local.

Exemplo:

```text
192.168.1.1
```

Fluxo:

```text
PC
↓
Gateway
↓
Internet
```

---

# Sub-redes (Subnetting)

## Conceito

Subnetting consiste em dividir uma rede em redes menores.

Objetivos:

- Melhor organização.
- Maior segurança.
- Redução de broadcasts.
- Melhor aproveitamento dos endereços.

---

## Exemplo

Rede original:

```text
192.168.1.0/24
```

Pode ser dividida em:

```text
192.168.1.0/25
```

e

```text
192.168.1.128/25
```

---

# NAT

## Network Address Translation

Permite que vários dispositivos privados compartilhem um único IP público.

Exemplo:

```text
192.168.1.10
192.168.1.20
192.168.1.30
```

↓

```text
200.150.10.5
```

(IP público)

---

## Vantagens do NAT

- Economia de endereços IPv4.
- Maior segurança.
- Facilidade de administração.

---

# Estrutura de um Pacote IPv4

O cabeçalho IPv4 contém informações importantes.

Campos principais:

- Versão.
- Tamanho do cabeçalho.
- Tamanho total.
- TTL.
- Protocolo.
- IP de origem.
- IP de destino.

---

# TTL

TTL significa:

```text
Time To Live
```

Determina quantos roteadores um pacote pode atravessar.

Cada roteador reduz o valor em:

```text
1
```

Quando chega a:

```text
0
```

o pacote é descartado.

---

# Fragmentação

Algumas redes possuem limites máximos para o tamanho dos pacotes.

Quando necessário:

```text
Pacote grande
↓
Fragmentação
↓
Pacotes menores
```

O destino reconstrói os fragmentos.

---

# ICMP

O protocolo ICMP auxilia o IP com mensagens de controle e diagnóstico.

Exemplos:

- Ping.
- Traceroute.
- Destino inacessível.
- Tempo excedido.

---

# IPv6

## Motivações para o IPv6

O IPv4 possui aproximadamente:

```text
4,3 bilhões
```

de endereços.

Com o crescimento da Internet, essa quantidade tornou-se insuficiente.

---

## Estrutura do IPv6

Possui:

```text
128 bits
```

Exemplo:

```text
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

Forma abreviada:

```text
2001:db8::8a2e:370:7334
```

---

## Vantagens do IPv6

- Quantidade enorme de endereços.
- Melhor desempenho de roteamento.
- Configuração automática.
- Melhor suporte à mobilidade.
- Eliminação da necessidade de NAT em muitos cenários.

---

## Tipos de Endereços IPv6

### Unicast

Comunicação entre dois dispositivos.

---

### Multicast

Comunicação para grupos.

---

### Anycast

Entrega ao dispositivo mais próximo.

---

# IPv4 x IPv6

| Característica | IPv4 | IPv6 |
|---------------|-------|-------|
| Tamanho | 32 bits | 128 bits |
| Exemplo | 192.168.1.10 | 2001:db8::1 |
| Endereços disponíveis | ~4,3 bilhões | 340 undecilhões |
| NAT | Muito utilizado | Geralmente desnecessário |
| Configuração automática | Limitada | Nativa |

---

# Comunicação Utilizando IP

Fluxo simplificado:

```text
Aplicação
↓
TCP/UDP
↓
IP
↓
Ethernet
↓
Rede
↓
Ethernet
↓
IP
↓
TCP/UDP
↓
Aplicação
```

O IP é responsável por levar os pacotes entre as redes até o destino.

---

# Importância do IP

O protocolo IP é a base da comunicação moderna.

Sem ele:

- Não existiria Internet.
- Não haveria roteamento.
- Redes diferentes não poderiam se comunicar.

Praticamente todos os serviços de rede dependem do IP.

---

# Conclusão

O Internet Protocol (IP) é o principal protocolo da Camada de Rede, responsável pelo endereçamento lógico e pelo encaminhamento de pacotes entre redes. Por meio do IPv4 e IPv6, bilhões de dispositivos conseguem se comunicar diariamente. Conceitos como máscaras de rede, CIDR, subnetting, NAT, gateway e roteamento são fundamentais para compreender o funcionamento das redes modernas e da Internet.