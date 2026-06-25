<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# Modelo OSI

## Introdução

O Modelo OSI (Open Systems Interconnection) é um modelo de referência criado pela ISO (International Organization for Standardization) para padronizar a comunicação entre sistemas computacionais.

Seu principal objetivo é dividir o processo de comunicação em camadas independentes, facilitando o desenvolvimento, manutenção e interoperabilidade dos sistemas de rede.

O modelo não define protocolos específicos, mas estabelece funções que devem ser desempenhadas por cada camada.

O Modelo OSI é amplamente utilizado no ensino de Redes de Computadores porque fornece uma visão organizada de como os dados trafegam de um dispositivo para outro.

---

## Objetivos do Modelo OSI

O Modelo OSI foi criado para:

- Padronizar a comunicação entre sistemas.
- Permitir interoperabilidade entre fabricantes.
- Facilitar o desenvolvimento de protocolos.
- Simplificar o estudo de redes.
- Dividir funções complexas em módulos menores.

---

## Estrutura em Camadas

O Modelo OSI possui sete camadas:

```text
7. Aplicação
6. Apresentação
5. Sessão
4. Transporte
3. Rede
2. Enlace de Dados
1. Física
```

Cada camada executa funções específicas e se comunica apenas com as camadas adjacentes.

---

## Conceito de Encapsulamento

Quando uma aplicação envia dados pela rede, cada camada adiciona informações de controle.

Esse processo é chamado de encapsulamento.

Exemplo:

```text
Dados
↓
Segmento
↓
Pacote
↓
Quadro
↓
Bits
```

Ao chegar ao destino ocorre o desencapsulamento.

---

## Camada Física

A Camada Física é responsável pela transmissão dos bits através do meio físico.

Funções:

- Transmissão de sinais elétricos.
- Transmissão óptica.
- Transmissão por rádio.
- Definição de conectores.
- Definição de cabos.

Unidade de dados:

```text
Bits
```

Equipamentos:

- Cabos.
- Repetidores.
- Hubs.

---

## Camada de Enlace de Dados

Responsável pela comunicação entre dispositivos diretamente conectados.

Funções:

- Controle de acesso ao meio.
- Detecção de erros.
- Enquadramento dos dados.
- Endereçamento físico.

Unidade de dados:

```text
Quadro (Frame)
```

Endereço utilizado:

```text
MAC Address
```

Equipamentos:

- Switches.

Protocolos:

- Ethernet.
- PPP.

---

## Camada de Rede

Responsável pelo encaminhamento de pacotes entre redes diferentes.

Funções:

- Endereçamento lógico.
- Escolha de rotas.
- Encaminhamento de pacotes.

Unidade de dados:

```text
Pacote
```

Endereço utilizado:

```text
Endereço IP
```

Equipamentos:

- Roteadores.

Protocolos:

- IPv4.
- IPv6.
- ICMP.

---

## Camada de Transporte

Responsável pela comunicação fim a fim entre aplicações.

Funções:

- Controle de fluxo.
- Controle de congestionamento.
- Segmentação.
- Confiabilidade.

Unidade de dados:

```text
Segmento
```

Protocolos:

- TCP.
- UDP.

---

## Camada de Sessão

Responsável por estabelecer, manter e encerrar sessões de comunicação.

Funções:

- Controle de diálogo.
- Sincronização.
- Gerenciamento de sessões.

Exemplos:

- Sessões remotas.
- Comunicação entre aplicações distribuídas.

---

## Camada de Apresentação

Responsável pela representação dos dados.

Funções:

- Conversão de formatos.
- Compressão.
- Criptografia.
- Descriptografia.

Exemplos:

- JPEG.
- PNG.
- ASCII.
- UTF-8.

---

## Camada de Aplicação

É a camada mais próxima do usuário.

Fornece serviços diretamente às aplicações.

Exemplos:

- Navegadores.
- Clientes de e-mail.
- Sistemas de mensagens.

Protocolos:

- HTTP.
- HTTPS.
- FTP.
- SMTP.
- DNS.

---

## Processo de Comunicação

Considere o envio de uma página web.

### Origem

```text
Aplicação → HTTP
Transporte → TCP
Rede → IP
Enlace → Ethernet
Física → Bits
```

### Destino

```text
Bits
↑
Ethernet
↑
IP
↑
TCP
↑
HTTP
```

Cada camada interpreta apenas suas próprias informações.

---

## Encapsulamento

Durante o envio:

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

Cada camada adiciona seu cabeçalho.

---

## Desencapsulamento

No destino:

```text
Bits
↓
Quadro Ethernet
↓
Pacote IP
↓
Segmento TCP
↓
Dados
```

Os cabeçalhos são removidos progressivamente.

---

## Vantagens do Modelo OSI

### Modularidade

Cada camada possui funções específicas.

### Interoperabilidade

Equipamentos de fabricantes diferentes podem se comunicar.

### Facilidade de Desenvolvimento

Protocolos podem evoluir independentemente.

### Facilidade de Diagnóstico

Problemas podem ser localizados por camada.

---

## Desvantagens do Modelo OSI

### Complexidade

Possui sete camadas distintas.

### Pouca Utilização Prática Completa

Na Internet utiliza-se principalmente o modelo TCP/IP.

### Algumas Funções Sobrepostas

Determinadas funcionalidades podem aparecer em mais de uma camada.

---

## Modelo OSI x Modelo TCP/IP

### Modelo OSI

```text
Aplicação
Apresentação
Sessão
Transporte
Rede
Enlace
Física
```

### Modelo TCP/IP

```text
Aplicação
Transporte
Internet
Acesso à Rede
```

O modelo TCP/IP é mais simples e corresponde à implementação real utilizada na Internet.

---

## Importância do Modelo OSI

Mesmo não sendo implementado integralmente na prática, o Modelo OSI continua sendo uma referência fundamental para:

- Estudo de redes.
- Projeto de protocolos.
- Diagnóstico de falhas.
- Certificações profissionais.

Ele fornece uma visão organizada do funcionamento das comunicações em redes de computadores.

---

## Conclusão

O Modelo OSI é uma arquitetura de referência composta por sete camadas que descrevem como ocorre a comunicação em redes de computadores. Cada camada possui responsabilidades específicas e contribui para a transmissão eficiente dos dados entre dispositivos. O entendimento do Modelo OSI é fundamental para compreender protocolos, equipamentos de rede e o funcionamento da Internet moderna.