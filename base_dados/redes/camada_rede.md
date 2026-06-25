<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# Camada de Rede

## Introdução

A Camada de Rede é a terceira camada do Modelo OSI e tem como principal função permitir a comunicação entre dispositivos localizados em redes diferentes.

Enquanto a Camada de Enlace realiza a comunicação dentro de uma rede local, a Camada de Rede é responsável por determinar caminhos, encaminhar pacotes e garantir que os dados consigam chegar ao destino mesmo atravessando múltiplas redes intermediárias.

A Internet moderna depende fortemente dos serviços fornecidos por essa camada.

---

## Posição no Modelo OSI

```text
7. Aplicação
6. Apresentação
5. Sessão
4. Transporte
3. Rede
2. Enlace
1. Física
```

A Camada de Rede está localizada entre as camadas de Transporte e Enlace.

---

## Funções da Camada de Rede

As principais funções são:

- Endereçamento lógico.
- Encaminhamento de pacotes.
- Determinação de rotas.
- Interconexão de redes.
- Fragmentação de pacotes.
- Controle básico de tráfego.

---

## Unidade de Dados

A unidade de dados da Camada de Rede é:

```text
Pacote
```

Estrutura simplificada:

```text
Cabeçalho
↓
Dados
```

O pacote encapsula os segmentos recebidos da Camada de Transporte.

---

## Comunicação entre Redes

Considere a seguinte situação:

```text
PC A
↓
Rede A
↓
Roteador
↓
Rede B
↓
PC B
```

A Camada de Rede permite que os pacotes atravessem as diferentes redes até alcançar o destino final.

---

## Endereçamento Lógico

A Camada de Rede utiliza endereços lógicos.

O principal exemplo é:

```text
Endereço IP
```

Exemplo:

```text
192.168.1.10
```

Diferentemente do endereço MAC, o endereço IP pode ser alterado.

---

## Diferença entre IP e MAC

### Endereço MAC

```text
Camada de Enlace
```

Características:

- Físico.
- Associado à interface de rede.
- Utilizado localmente.

Exemplo:

```text
00:1A:2B:3C:4D:5E
```

---

### Endereço IP

```text
Camada de Rede
```

Características:

- Lógico.
- Configurável.
- Utilizado para comunicação entre redes.

Exemplo:

```text
192.168.0.100
```

---

## Protocolos da Camada de Rede

Os principais protocolos são:

### IPv4

Responsável pelo endereçamento lógico na Internet.

---

### IPv6

Versão mais recente do protocolo IP.

---

### ICMP

Utilizado para mensagens de controle e diagnóstico.

---

### ARP

Responsável pela resolução entre IP e MAC.

---

## IPv4

IPv4 significa:

```text
Internet Protocol Version 4
```

É o protocolo mais utilizado na Internet.

Possui endereços de:

```text
32 bits
```

Exemplo:

```text
192.168.1.10
```

---

## Estrutura do Endereço IPv4

Um endereço IPv4 possui quatro octetos.

Exemplo:

```text
192.168.1.10
```

Divisão:

```text
192
168
1
10
```

Cada valor varia entre:

```text
0 e 255
```

---

## Endereço de Rede e Host

Um endereço IP é dividido em:

### Parte da Rede

Identifica a rede.

### Parte do Host

Identifica o dispositivo.

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

## Máscara de Rede

A máscara define quais bits pertencem à rede e quais pertencem ao host.

Exemplo:

```text
255.255.255.0
```

Representação CIDR:

```text
/24
```

---

## CIDR

CIDR significa:

```text
Classless Inter-Domain Routing
```

Permite representar redes utilizando o número de bits da parte de rede.

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

---

## Classes de Endereços IPv4

Historicamente os endereços eram divididos em classes.

### Classe A

```text
1.0.0.0
até
126.255.255.255
```

---

### Classe B

```text
128.0.0.0
até
191.255.255.255
```

---

### Classe C

```text
192.0.0.0
até
223.255.255.255
```

---

### Classe D

Utilizada para multicast.

---

### Classe E

Reservada para pesquisas.

---

## Endereços Privados

São utilizados em redes internas.

Faixas:

### Classe A Privada

```text
10.0.0.0/8
```

---

### Classe B Privada

```text
172.16.0.0/12
```

---

### Classe C Privada

```text
192.168.0.0/16
```

---

## Endereços Públicos

São endereços válidos na Internet.

Precisam ser únicos globalmente.

São atribuídos por provedores e organizações responsáveis pela distribuição de endereços IP.

---

## IPv6

IPv6 foi criado para solucionar a escassez de endereços IPv4.

Possui:

```text
128 bits
```

Exemplo:

```text
2001:db8::1
```

---

## Vantagens do IPv6

- Quantidade enorme de endereços.
- Melhor eficiência de roteamento.
- Configuração simplificada.
- Melhor suporte à mobilidade.

---

## Pacotes IP

Os dados transmitidos na Camada de Rede são organizados em pacotes.

Estrutura simplificada:

```text
Cabeçalho IP
↓
Dados
```

O cabeçalho contém informações utilizadas pelos roteadores.

---

## Fragmentação

Algumas redes possuem limites para o tamanho dos pacotes.

Quando necessário, um pacote pode ser dividido em partes menores.

Esse processo é chamado de:

```text
Fragmentação
```

O destino posteriormente reconstrói o pacote original.

---

## Encaminhamento de Pacotes

O encaminhamento consiste em mover pacotes de uma rede para outra.

Exemplo:

```text
Origem
↓
Roteador
↓
Roteador
↓
Destino
```

Cada roteador decide o próximo salto.

---

## Roteadores

O principal equipamento da Camada de Rede é o roteador.

Funções:

- Encaminhar pacotes.
- Escolher rotas.
- Interligar redes.

Exemplo:

```text
LAN
↓
Roteador
↓
Internet
```

---

## Tabela de Roteamento

Os roteadores mantêm uma tabela contendo informações sobre os caminhos disponíveis.

Exemplo simplificado:

```text
Rede Destino      Próximo Salto

192.168.1.0       Interface 1
10.0.0.0          Interface 2
```

Essa tabela é utilizada para tomar decisões de encaminhamento.

---

## Próximo Salto (Next Hop)

É o próximo dispositivo para o qual o pacote será enviado.

Exemplo:

```text
PC
↓
Roteador A
↓
Roteador B
↓
Destino
```

Para o Roteador A, o próximo salto é o Roteador B.

---

## Gateway Padrão

É o roteador utilizado quando o destino está fora da rede local.

Exemplo:

```text
192.168.1.1
```

Praticamente todos os computadores possuem um gateway configurado.

---

## ICMP

ICMP significa:

```text
Internet Control Message Protocol
```

Utilizado para mensagens de controle e diagnóstico.

Exemplos:

- Erro de destino inacessível.
- Tempo excedido.
- Testes de conectividade.

---

## Ping

O comando Ping utiliza ICMP.

Exemplo:

```bash
ping 8.8.8.8
```

Função:

- Verificar conectividade.
- Medir latência.

---

## Traceroute

Permite identificar os roteadores percorridos por um pacote.

Exemplo:

```bash
tracert google.com
```

ou

```bash
traceroute google.com
```

Mostra cada salto até o destino.

---

## Comunicação Fim a Fim

Exemplo simplificado:

```text
Aplicação
↓
TCP
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
TCP
↓
Aplicação
```

A Camada de Rede é responsável pela entrega dos pacotes através das diversas redes intermediárias.

---

## Relação com a Camada de Enlace

A Camada de Rede utiliza os serviços da Camada de Enlace.

Exemplo:

```text
Rede → IP
Enlace → MAC
```

IP identifica o destino final.

MAC identifica o próximo dispositivo local.

---

## Importância da Camada de Rede

A Camada de Rede é responsável por permitir que dispositivos localizados em diferentes redes possam se comunicar.

Sem ela:

- Não existiria Internet.
- Não haveria roteamento.
- Não seria possível comunicação global.

Ela conecta milhões de redes ao redor do mundo.

---

## Conclusão

A Camada de Rede é responsável pelo endereçamento lógico e pelo encaminhamento de pacotes entre redes distintas. Utilizando protocolos como IPv4, IPv6 e ICMP, além de equipamentos como roteadores, essa camada permite que computadores localizados em qualquer parte do mundo possam trocar informações. Seu entendimento é fundamental para compreender IP, ARP, roteamento, TCP, UDP e o funcionamento da Internet moderna.