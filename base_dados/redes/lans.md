<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# LANs (Local Area Networks)

## Introdução

LAN (Local Area Network) significa Rede Local.

É uma rede de computadores que conecta dispositivos dentro de uma área geográfica limitada, como:

- Residências
- Escritórios
- Empresas
- Escolas
- Universidades
- Laboratórios

As LANs são as redes mais comuns no dia a dia e permitem o compartilhamento de recursos e informações entre dispositivos próximos.

---

## Objetivos das LANs

As Redes Locais foram desenvolvidas para permitir:

- Compartilhamento de arquivos.
- Compartilhamento de impressoras.
- Compartilhamento de acesso à Internet.
- Comunicação entre usuários.
- Compartilhamento de aplicações.
- Redução de custos de infraestrutura.

---

## Características das LANs

As principais características são:

### Pequena Área Geográfica

A cobertura normalmente ocorre dentro de:

- Um cômodo.
- Um prédio.
- Um campus.

---

### Alta Velocidade

As LANs oferecem altas taxas de transmissão.

Exemplos:

```text
100 Mbps
1 Gbps
10 Gbps
```

---

### Baixa Latência

Como as distâncias são pequenas, o tempo de resposta costuma ser reduzido.

---

### Administração Local

A rede geralmente é administrada por uma única organização.

---

## Componentes de uma LAN

Uma rede local é composta por diversos elementos.

### Computadores

Podem atuar como:

- Clientes.
- Servidores.

---

### Switches

Responsáveis pela interconexão dos dispositivos.

Funções:

- Receber quadros.
- Consultar endereços MAC.
- Encaminhar dados.

---

### Roteadores

Responsáveis por conectar a LAN a outras redes.

Normalmente conectam:

```text
LAN
↓
Internet
```

---

### Pontos de Acesso (Access Points)

Permitem comunicação sem fio.

Exemplo:

```text
Wi-Fi
```

---

### Cabos

Utilizados para transmissão física.

Exemplos:

- UTP Cat5e
- UTP Cat6
- Fibra óptica

---

## Topologias de Rede

Topologia é a forma como os dispositivos estão conectados.

---

## Topologia em Barramento

Todos os dispositivos compartilham um único meio físico.

Exemplo:

```text
PC --- PC --- PC --- PC
```

### Vantagens

- Baixo custo.

### Desvantagens

- Muitas colisões.
- Baixa escalabilidade.

Atualmente pouco utilizada.

---

## Topologia em Anel

Cada dispositivo conecta-se ao próximo formando um círculo.

Exemplo:

```text
PC → PC → PC → PC
↑             ↓
└─────────────┘
```

### Vantagens

- Comunicação organizada.

### Desvantagens

- Falhas podem interromper a rede.

---

## Topologia em Estrela

É a mais utilizada atualmente.

Todos os dispositivos se conectam a um equipamento central.

Exemplo:

```text
      Switch
      / | \
     /  |  \
   PC  PC  PC
```

### Vantagens

- Fácil manutenção.
- Boa escalabilidade.
- Maior confiabilidade.

### Desvantagens

- Dependência do equipamento central.

---

## Ethernet

A tecnologia mais utilizada em LANs é a Ethernet.

Padronização:

```text
IEEE 802.3
```

Características:

- Baixo custo.
- Alta velocidade.
- Grande compatibilidade.

---

## Padrões Ethernet

### Fast Ethernet

```text
100 Mbps
```

---

### Gigabit Ethernet

```text
1 Gbps
```

---

### 10 Gigabit Ethernet

```text
10 Gbps
```

---

### 40 Gigabit Ethernet

```text
40 Gbps
```

---

### 100 Gigabit Ethernet

```text
100 Gbps
```

Utilizada principalmente em data centers.

---

## LAN com Fio

Utiliza meios físicos para transmissão.

Exemplos:

- Cabo UTP.
- Fibra óptica.

### Vantagens

- Maior estabilidade.
- Menor interferência.
- Maior segurança.

### Desvantagens

- Menor mobilidade.

---

## WLAN

WLAN significa:

```text
Wireless Local Area Network
```

É uma LAN sem fio.

Exemplo:

```text
Wi-Fi
```

---

## Wi-Fi

Tecnologia baseada na família IEEE 802.11.

Permite comunicação sem cabos.

### Benefícios

- Mobilidade.
- Facilidade de instalação.

### Limitações

- Interferências.
- Menor alcance.
- Maior vulnerabilidade.

---

## Padrões Wi-Fi

### 802.11n

Velocidades de centenas de Mbps.

---

### 802.11ac

Velocidades superiores a 1 Gbps.

---

### 802.11ax (Wi-Fi 6)

Maior eficiência e capacidade.

---

## Endereçamento em LANs

Em uma LAN os dispositivos possuem:

### Endereço MAC

Utilizado pela Camada de Enlace.

Exemplo:

```text
00:1A:2B:3C:4D:5E
```

---

### Endereço IP

Utilizado pela Camada de Rede.

Exemplo:

```text
192.168.1.10
```

---

## Comunicação Dentro da LAN

Considere dois computadores:

```text
PC1
↓
Switch
↓
PC2
```

Fluxo:

1. PC1 identifica o IP de destino.
2. Obtém o MAC através do ARP.
3. Envia um quadro Ethernet.
4. O switch encaminha o quadro.
5. PC2 recebe os dados.

---

## Domínio de Colisão

Representa uma área onde colisões podem ocorrer.

Em redes antigas com hubs:

```text
Toda a rede
```

era um único domínio de colisão.

Com switches:

```text
Cada porta
```

possui seu próprio domínio de colisão.

---

## Domínio de Broadcast

Representa o alcance de mensagens de broadcast.

Exemplo:

```text
FF:FF:FF:FF:FF:FF
```

Todos os dispositivos recebem.

---

## VLAN

VLAN significa:

```text
Virtual Local Area Network
```

Permite dividir logicamente uma LAN física.

Exemplo:

```text
VLAN 10 → Administração
VLAN 20 → Financeiro
VLAN 30 → TI
```

---

## Benefícios das VLANs

### Segurança

Separação de setores.

### Organização

Melhor gerenciamento.

### Desempenho

Redução do tráfego de broadcast.

---

## LANs Corporativas

Em empresas, as LANs costumam incluir:

- Switches gerenciáveis.
- VLANs.
- Servidores.
- Firewalls.
- Access Points.

Objetivos:

- Segurança.
- Escalabilidade.
- Desempenho.

---

## LANs Domésticas

Normalmente são compostas por:

- Roteador Wi-Fi.
- Smartphones.
- Notebooks.
- Smart TVs.
- Impressoras.

Exemplo:

```text
Internet
↓
Roteador
↓
Dispositivos da casa
```

---

## Segurança em LANs

As principais medidas incluem:

### Controle de Acesso

Definição de permissões.

### Firewalls

Filtragem de tráfego.

### Criptografia

Proteção de dados.

### Segmentação por VLAN

Isolamento de setores.

---

## Vantagens das LANs

- Alta velocidade.
- Baixo custo operacional.
- Compartilhamento de recursos.
- Fácil administração.
- Baixa latência.

---

## Desvantagens das LANs

- Alcance limitado.
- Dependência de infraestrutura local.
- Necessidade de manutenção.
- Possíveis riscos de segurança.

---

## LAN x MAN x WAN

### LAN

Local Area Network.

Abrangência:

```text
Prédio
Empresa
Residência
```

---

### MAN

Metropolitan Area Network.

Abrangência:

```text
Cidade
```

---

### WAN

Wide Area Network.

Abrangência:

```text
Países
Continentes
Internet
```

---

## Aplicações das LANs

As LANs são utilizadas em:

- Residências.
- Empresas.
- Universidades.
- Hospitais.
- Laboratórios.
- Data Centers.

Praticamente toda organização utiliza pelo menos uma rede local.

---

## Conclusão

As LANs (Local Area Networks) são redes responsáveis pela comunicação entre dispositivos em áreas geográficas reduzidas. Utilizando tecnologias como Ethernet, Wi-Fi, switches e VLANs, elas oferecem alta velocidade, baixa latência e compartilhamento eficiente de recursos. Seu entendimento é fundamental para compreender o funcionamento das redes modernas e a comunicação entre computadores em ambientes locais.