<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# TCP (Transmission Control Protocol)

## Introdução

O TCP (Transmission Control Protocol) é um protocolo da Camada de Transporte do modelo TCP/IP e da Camada de Transporte do Modelo OSI.

Sua principal função é fornecer uma comunicação confiável entre aplicações executadas em dispositivos diferentes.

Diferentemente do UDP, o TCP garante que os dados sejam entregues corretamente, na ordem correta e sem perdas, tornando-o um dos protocolos mais importantes da Internet.

---

## Características do TCP

O TCP possui diversas características que garantem a confiabilidade da comunicação.

Principais características:

- Orientado à conexão.
- Confiável.
- Controle de fluxo.
- Controle de congestionamento.
- Entrega ordenada.
- Detecção de erros.
- Retransmissão de segmentos perdidos.

---

## Camada de Transporte

No Modelo OSI:

```text
7. Aplicação
6. Apresentação
5. Sessão
4. Transporte ← TCP
3. Rede
2. Enlace
1. Física
```

O TCP atua na Camada de Transporte.

---

## Unidade de Dados

A unidade de dados utilizada pelo TCP é:

```text
Segmento
```

Fluxo de encapsulamento:

```text
Dados
↓
Segmento TCP
↓
Pacote IP
↓
Quadro Ethernet
↓
Bits
```

---

# Comunicação Orientada à Conexão

Antes de transmitir dados, o TCP precisa estabelecer uma conexão entre origem e destino.

Esse processo é chamado de:

```text
Three-Way Handshake
```

ou

```text
Aperto de mão em três vias
```

---

# Three-Way Handshake

O estabelecimento da conexão ocorre em três etapas.

---

## Etapa 1 - SYN

O cliente envia uma solicitação de conexão.

```text
Cliente
↓
SYN
↓
Servidor
```

SYN significa:

```text
Synchronize
```

---

## Etapa 2 - SYN-ACK

O servidor responde aceitando a solicitação.

```text
Cliente
↑
SYN-ACK
↑
Servidor
```

ACK significa:

```text
Acknowledgment
```

(confirmação)

---

## Etapa 3 - ACK

O cliente confirma a resposta do servidor.

```text
Cliente
↓
ACK
↓
Servidor
```

A conexão é estabelecida.

---

## Resumo do Handshake

```text
Cliente                Servidor

SYN      ───────────►

          ◄─────────── SYN-ACK

ACK      ───────────►
```

Após essa etapa os dados podem ser transmitidos.

---

# Numeração de Sequência

Cada byte transmitido recebe um número de sequência.

Objetivo:

- Garantir entrega ordenada.
- Detectar perdas.
- Detectar duplicações.

Exemplo:

```text
Byte 1
Byte 2
Byte 3
...
```

---

# Confirmação (ACK)

Quando um segmento é recebido corretamente, o destino envia uma confirmação.

Exemplo:

```text
Recebi até o byte 1000.
```

ACK:

```text
1001
```

Significa:

```text
Espero receber o próximo byte.
```

---

# Retransmissão

Caso um segmento seja perdido:

```text
Origem
↓
Segmento perdido
↓
Sem ACK
↓
Retransmissão
```

O TCP envia novamente o segmento.

---

# Timeout

Após enviar um segmento, o TCP inicia um temporizador.

Se o ACK não chegar dentro do tempo esperado:

```text
Timeout
```

O segmento é retransmitido.

---

# Janela Deslizante (Sliding Window)

A Janela Deslizante permite que múltiplos segmentos sejam enviados sem esperar confirmação individual.

Exemplo:

```text
Enviar:

1
2
3
4
5

↓

Receber ACK depois
```

Isso aumenta significativamente o desempenho.

---

# Controle de Fluxo

O controle de fluxo evita que o receptor seja sobrecarregado.

O receptor informa quanto espaço possui disponível.

Exemplo:

```text
Janela = 5000 bytes
```

O transmissor respeita esse limite.

---

# Controle de Congestionamento

Além do controle de fluxo, o TCP tenta evitar congestionamentos na rede.

Objetivos:

- Reduzir perdas.
- Melhorar desempenho.
- Evitar saturação da rede.

---

# Slow Start

Quando a conexão inicia:

```text
Janela pequena
```

A taxa de transmissão aumenta gradualmente.

Isso reduz o risco de congestionamento.

---

# Congestion Avoidance

Após determinado limite:

```text
Aumento mais lento
```

Permitindo estabilidade da rede.

---

# Fast Retransmit

Quando múltiplos ACKs duplicados são recebidos:

```text
ACK duplicado
ACK duplicado
ACK duplicado
```

O TCP presume perda de pacote e realiza retransmissão imediata.

---

# Fast Recovery

Após detectar congestionamento:

```text
Redução controlada
```

evitando reiniciar totalmente a transmissão.

---

# Entrega Ordenada

Mesmo que segmentos cheguem fora de ordem:

```text
3
1
2
```

o TCP reorganiza:

```text
1
2
3
```

antes de entregar à aplicação.

---

# Multiplexação por Portas

O TCP utiliza números de porta para identificar aplicações.

Exemplo:

```text
IP + Porta
```

---

## Exemplos de Portas

### HTTP

```text
80
```

---

### HTTPS

```text
443
```

---

### FTP

```text
21
```

---

### SSH

```text
22
```

---

### SMTP

```text
25
```

---

### DNS

```text
53
```

Pode utilizar TCP ou UDP.

---

# Estrutura do Cabeçalho TCP

O cabeçalho TCP contém informações importantes.

Campos principais:

- Porta de origem.
- Porta de destino.
- Número de sequência.
- Número de ACK.
- Flags.
- Janela.
- Checksum.

---

# Flags TCP

As flags controlam o comportamento da conexão.

---

## SYN

Inicia conexão.

---

## ACK

Confirma recebimento.

---

## FIN

Finaliza conexão.

---

## RST

Reinicia conexão.

---

## PSH

Entrega imediata dos dados.

---

## URG

Dados urgentes.

---

# Encerramento da Conexão

O encerramento utiliza um processo chamado:

```text
Four-Way Handshake
```

---

## Etapa 1

```text
FIN
```

---

## Etapa 2

```text
ACK
```

---

## Etapa 3

```text
FIN
```

---

## Etapa 4

```text
ACK
```

---

## Resumo

```text
Cliente                Servidor

FIN      ───────────►

          ◄─────────── ACK

          ◄─────────── FIN

ACK      ───────────►
```

A conexão é encerrada.

---

# Vantagens do TCP

- Comunicação confiável.
- Entrega ordenada.
- Controle de fluxo.
- Controle de congestionamento.
- Recuperação de erros.
- Amplamente suportado.

---

# Desvantagens do TCP

- Maior overhead.
- Maior consumo de recursos.
- Maior latência.
- Processo de conexão obrigatório.

---

# Aplicações que Utilizam TCP

Diversos protocolos utilizam TCP.

---

## HTTP

Transferência de páginas web.

---

## HTTPS

Navegação segura.

---

## FTP

Transferência de arquivos.

---

## SSH

Acesso remoto seguro.

---

## SMTP

Envio de e-mails.

---

## IMAP

Recebimento de e-mails.

---

## POP3

Recebimento de e-mails.

---

# TCP x UDP

| Característica | TCP | UDP |
|---------------|------|------|
| Orientado à conexão | Sim | Não |
| Confiável | Sim | Não |
| Controle de fluxo | Sim | Não |
| Controle de congestionamento | Sim | Não |
| Retransmissão | Sim | Não |
| Velocidade | Menor | Maior |
| Overhead | Maior | Menor |

---

# Exemplo de Comunicação TCP

```text
Navegador
↓
TCP
↓
IP
↓
Internet
↓
Servidor Web
```

Fluxo:

```text
1. Handshake
2. Troca de dados
3. Confirmações
4. Encerramento
```

---

# Importância do TCP

O TCP é um dos pilares da Internet moderna.

Ele garante que informações importantes sejam entregues corretamente, mesmo em redes sujeitas a falhas.

Serviços como:

- Navegação Web.
- E-mails.
- Transferência de arquivos.
- Acesso remoto.

dependem diretamente do TCP.

---

# Conclusão

O TCP (Transmission Control Protocol) é um protocolo da Camada de Transporte responsável por fornecer comunicação confiável entre aplicações. Utilizando mecanismos como Three-Way Handshake, números de sequência, ACKs, retransmissão, controle de fluxo e controle de congestionamento, o TCP garante que os dados sejam entregues corretamente e na ordem correta. Por sua confiabilidade, é amplamente utilizado nos principais serviços da Internet.