<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# Camada de Enlace de Dados

## Introdução

A Camada de Enlace de Dados é a segunda camada do Modelo OSI e tem como principal objetivo fornecer comunicação confiável entre dispositivos conectados ao mesmo meio físico.

Ela atua sobre os serviços oferecidos pela Camada Física, organizando os bits recebidos em estruturas chamadas quadros (frames), além de detectar erros de transmissão e controlar o acesso ao meio compartilhado.

Enquanto a Camada Física transmite apenas bits, a Camada de Enlace adiciona organização e controle à comunicação.

---

## Posição no Modelo OSI

```text
7. Aplicação
6. Apresentação
5. Sessão
4. Transporte
3. Rede
2. Enlace de Dados
1. Física
```

A Camada de Enlace atua entre a Camada Física e a Camada de Rede.

---

## Funções da Camada de Enlace

As principais funções são:

- Enquadramento dos dados.
- Controle de acesso ao meio.
- Detecção de erros.
- Controle de fluxo local.
- Endereçamento físico.
- Entrega entre dispositivos vizinhos.

---

## Unidade de Dados

A unidade de dados da Camada de Enlace é:

```text
Quadro (Frame)
```

Estrutura básica:

```text
Cabeçalho
↓
Dados
↓
Trailer
```

O quadro encapsula o pacote recebido da Camada de Rede.

---

## Processo de Encapsulamento

Durante a transmissão:

```text
Dados da Aplicação
↓
Segmento TCP/UDP
↓
Pacote IP
↓
Quadro Ethernet
↓
Bits
```

Cada camada adiciona suas informações de controle.

---

## Endereçamento Físico

A Camada de Enlace utiliza endereços físicos chamados MAC Addresses.

MAC significa:

```text
Media Access Control
```

Cada interface de rede possui um endereço MAC único.

Exemplo:

```text
00:1A:2B:3C:4D:5E
```

ou

```text
00-1A-2B-3C-4D-5E
```

---

## Estrutura do Endereço MAC

Um endereço MAC possui 48 bits.

Exemplo:

```text
00:1A:2B:3C:4D:5E
```

Divisão:

```text
00:1A:2B
↓
Fabricante

3C:4D:5E
↓
Identificador do dispositivo
```

---

## Tipos de Endereçamento

### Unicast

Comunicação entre dois dispositivos.

```text
A → B
```

---

### Broadcast

Mensagem enviada para todos os dispositivos da rede.

```text
A → Todos
```

Endereço especial:

```text
FF:FF:FF:FF:FF:FF
```

---

### Multicast

Mensagem enviada para um grupo específico de dispositivos.

```text
A → Grupo
```

---

## Controle de Acesso ao Meio

Em redes compartilhadas, múltiplos dispositivos podem tentar transmitir simultaneamente.

A Camada de Enlace define mecanismos para controlar esse acesso.

Objetivos:

- Evitar colisões.
- Melhorar eficiência.
- Garantir comunicação organizada.

---

## Colisão

Ocorre quando dois dispositivos transmitem ao mesmo tempo.

Exemplo:

```text
PC1
  ↘
   Meio Compartilhado
  ↗
PC2
```

Resultado:

```text
Colisão
```

Os dados precisam ser retransmitidos.

---

## CSMA/CD

Carrier Sense Multiple Access with Collision Detection.

Utilizado nas versões antigas da Ethernet.

Funcionamento:

1. Escuta o meio.
2. Verifica se está livre.
3. Transmite.
4. Detecta colisões.
5. Retransmite quando necessário.

---

## CSMA/CA

Carrier Sense Multiple Access with Collision Avoidance.

Utilizado em redes sem fio.

Objetivo:

Evitar colisões antes que elas ocorram.

Muito utilizado em:

```text
Wi-Fi
```

---

## Controle de Fluxo

Controla a velocidade de transmissão entre dispositivos vizinhos.

Objetivos:

- Evitar sobrecarga.
- Evitar perda de quadros.

---

## Controle de Erros

Durante a transmissão podem ocorrer falhas.

A Camada de Enlace detecta erros utilizando mecanismos específicos.

---

## Bit de Paridade

Método simples para detecção de erros.

Exemplo:

```text
1011001
```

Um bit adicional é inserido para verificar a integridade.

---

## Checksum

Valor calculado matematicamente a partir dos dados transmitidos.

Permite identificar alterações.

---

## CRC

CRC significa:

```text
Cyclic Redundancy Check
```

É o mecanismo mais utilizado nas redes modernas.

Características:

- Alta eficiência.
- Baixa taxa de erro não detectado.

---

## Subcamadas da Camada de Enlace

O padrão IEEE divide a Camada de Enlace em duas partes.

---

### LLC

Logical Link Control

Responsável por:

- Controle lógico da comunicação.
- Interface com a Camada de Rede.

---

### MAC

Media Access Control

Responsável por:

- Controle de acesso ao meio.
- Endereçamento físico.

---

## Ethernet

Ethernet é a tecnologia de enlace mais utilizada no mundo.

Padronizada pela norma:

```text
IEEE 802.3
```

Características:

- Alto desempenho.
- Baixo custo.
- Grande compatibilidade.

---

## Estrutura de um Quadro Ethernet

```text
Preâmbulo
↓
MAC Destino
↓
MAC Origem
↓
Tipo
↓
Dados
↓
CRC
```

---

## Campo MAC Destino

Identifica quem receberá o quadro.

Exemplo:

```text
00:1A:2B:3C:4D:5E
```

---

## Campo MAC Origem

Identifica quem enviou o quadro.

Exemplo:

```text
98:AB:45:11:AA:10
```

---

## Campo Tipo

Informa qual protocolo da Camada de Rede está encapsulado.

Exemplos:

```text
IPv4
IPv6
ARP
```

---

## Campo Dados

Contém o pacote recebido da Camada de Rede.

---

## Campo CRC

Utilizado para detecção de erros.

Permite verificar a integridade do quadro.

---

## Switch

O principal equipamento da Camada de Enlace é o switch.

Funções:

- Receber quadros.
- Analisar endereços MAC.
- Encaminhar quadros corretamente.

---

## Tabela MAC

O switch mantém uma tabela interna.

Exemplo:

```text
MAC                Porta

00:11:22:33:44:55   1
AA:BB:CC:DD:EE:FF   2
```

Essa tabela é construída automaticamente.

---

## Funcionamento do Switch

### Aprendizagem

O switch aprende os endereços MAC observando os quadros recebidos.

### Encaminhamento

Encaminha o quadro apenas para a porta correta.

### Filtragem

Evita transmissões desnecessárias.

---

## Hub x Switch

### Hub

```text
Recebe
↓
Reenvia para todas as portas
```

Problemas:

- Colisões.
- Baixa eficiência.

---

### Switch

```text
Recebe
↓
Consulta tabela MAC
↓
Encaminha apenas para o destino
```

Benefícios:

- Melhor desempenho.
- Menos colisões.

---

## VLAN

VLAN significa:

```text
Virtual Local Area Network
```

Permite dividir logicamente uma rede física.

Exemplo:

```text
VLAN 10 → Administração
VLAN 20 → Financeiro
VLAN 30 → TI
```

Benefícios:

- Segurança.
- Organização.
- Redução de tráfego.

---

## STP

Spanning Tree Protocol.

Padronizado pela norma:

```text
IEEE 802.1D
```

Objetivo:

Evitar loops em redes com múltiplos switches.

Sem STP:

```text
Loop
↓
Tempestade de Broadcast
↓
Rede indisponível
```

---

## Tempestade de Broadcast

Ocorre quando mensagens de broadcast circulam indefinidamente.

Consequências:

- Congestionamento.
- Queda de desempenho.
- Interrupção da rede.

---

## Comunicação Local

A Camada de Enlace atua apenas entre dispositivos diretamente conectados.

Exemplo:

```text
Computador
↓
Switch
↓
Roteador
```

Cada enlace utiliza quadros próprios.

Quando o pacote passa para outra rede, novos quadros são criados.

---

## Relação com a Camada de Rede

A Camada de Enlace entrega pacotes localmente.

A Camada de Rede entrega pacotes entre redes.

Exemplo:

```text
Enlace → MAC Address
Rede → Endereço IP
```

Ambas trabalham em conjunto.

---

## Importância da Camada de Enlace

A Camada de Enlace é responsável por garantir que dispositivos conectados ao mesmo meio consigam trocar informações de forma organizada e confiável.

Ela é fundamental para:

- Redes Ethernet.
- Redes Wi-Fi.
- Comunicação local.
- Detecção de erros.
- Controle de acesso ao meio.

---

## Conclusão

A Camada de Enlace de Dados é responsável pela comunicação local entre dispositivos conectados a uma mesma rede. Utilizando quadros, endereços MAC, mecanismos de detecção de erros e controle de acesso ao meio, ela garante uma transmissão eficiente e organizada. Tecnologias como Ethernet, VLANs e switches dependem diretamente dos serviços fornecidos por essa camada, tornando-a uma das mais importantes do Modelo OSI.