<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# Roteamento

## Introdução

O roteamento é o processo responsável por determinar o caminho que um pacote de dados deve seguir desde sua origem até seu destino.

Ele é uma das funções mais importantes da Camada de Rede do Modelo OSI e é fundamental para o funcionamento da Internet.

Sem o roteamento, computadores localizados em redes diferentes não conseguiriam se comunicar.

---

## Conceito de Roteamento

Quando um dispositivo envia um pacote para outro que está em uma rede diferente, é necessário definir qual caminho o pacote deverá percorrer.

Exemplo:

```text
Computador A
↓
Roteador 1
↓
Roteador 2
↓
Roteador 3
↓
Computador B
```

O roteamento é o mecanismo que escolhe esse caminho.

---

## Objetivos do Roteamento

Os principais objetivos são:

- Entregar pacotes ao destino correto.
- Encontrar caminhos eficientes.
- Evitar congestionamentos.
- Permitir comunicação entre redes distintas.
- Adaptar-se a falhas de rede.

---

## Equipamento Responsável

O principal dispositivo responsável pelo roteamento é o:

```text
Roteador
```

Funções do roteador:

- Receber pacotes.
- Analisar o endereço IP de destino.
- Consultar sua tabela de roteamento.
- Escolher o próximo salto.
- Encaminhar o pacote.

---

## Como Funciona o Roteamento

Quando um pacote chega a um roteador:

### Passo 1

O roteador lê o endereço IP de destino.

Exemplo:

```text
192.168.20.15
```

---

### Passo 2

Consulta sua tabela de roteamento.

---

### Passo 3

Determina o melhor caminho.

---

### Passo 4

Encaminha o pacote para o próximo salto.

---

## Tabela de Roteamento

A tabela de roteamento contém informações sobre as redes conhecidas pelo roteador.

Exemplo:

```text
Rede Destino       Próximo Salto

192.168.1.0/24     Interface 1
192.168.2.0/24     Interface 2
0.0.0.0/0          Gateway
```

---

## Componentes da Tabela de Roteamento

Cada entrada normalmente possui:

- Rede de destino.
- Máscara de rede.
- Próximo salto.
- Interface de saída.
- Métrica.

---

## Próximo Salto (Next Hop)

O próximo salto é o próximo dispositivo para o qual o pacote será enviado.

Exemplo:

```text
PC
↓
Roteador A
↓
Roteador B
↓
Servidor
```

Para o Roteador A:

```text
Próximo salto
=
Roteador B
```

---

## Métrica

A métrica é um valor utilizado para comparar rotas.

Normalmente representa:

- Número de saltos.
- Custo.
- Largura de banda.
- Atraso.
- Confiabilidade.

Quanto menor a métrica, melhor tende a ser a rota.

---

# Tipos de Roteamento

Existem dois tipos principais.

---

## Roteamento Estático

As rotas são configuradas manualmente pelo administrador.

Exemplo:

```text
ip route
```

ou configuração equivalente no equipamento.

---

### Vantagens

- Simplicidade.
- Baixo consumo de recursos.
- Maior controle.

---

### Desvantagens

- Pouca escalabilidade.
- Exige configuração manual.
- Não reage automaticamente a falhas.

---

## Roteamento Dinâmico

Os roteadores aprendem rotas automaticamente.

Utilizam protocolos de roteamento.

Exemplos:

- RIP
- OSPF
- EIGRP
- BGP

---

### Vantagens

- Atualização automática.
- Escalabilidade.
- Adaptação a mudanças.

---

### Desvantagens

- Maior complexidade.
- Consumo de recursos.

---

# Gateway Padrão

O gateway padrão é utilizado quando o destino não pertence à rede local.

Exemplo:

```text
192.168.1.1
```

Fluxo:

```text
Computador
↓
Gateway
↓
Internet
```

Sem gateway configurado corretamente, o acesso a outras redes não é possível.

---

# Rota Padrão

A rota padrão é utilizada quando não existe uma rota específica para determinado destino.

Representação:

```text
0.0.0.0/0
```

Significado:

```text
Qualquer destino
```

---

# Protocolos de Roteamento

Protocolos de roteamento permitem que roteadores troquem informações automaticamente.

---

## RIP

RIP significa:

```text
Routing Information Protocol
```

É um dos protocolos mais antigos.

---

### Características

Utiliza:

```text
Número de Saltos (Hop Count)
```

como métrica.

---

### Limitação

Máximo:

```text
15 saltos
```

Acima disso a rede é considerada inalcançável.

---

### Vantagens

- Simples.
- Fácil configuração.

---

### Desvantagens

- Baixa escalabilidade.
- Convergência lenta.

---

# OSPF

OSPF significa:

```text
Open Shortest Path First
```

É um dos protocolos mais utilizados em redes corporativas.

---

## Características

Utiliza algoritmo SPF:

```text
Shortest Path First
```

desenvolvido por Dijkstra.

---

## Métrica

Baseada em:

```text
Custo
```

geralmente relacionado à largura de banda.

---

## Vantagens

- Alta eficiência.
- Rápida convergência.
- Boa escalabilidade.

---

## Áreas OSPF

Grandes redes podem ser divididas em áreas.

Exemplo:

```text
Área 0
Área 1
Área 2
```

A Área 0 é conhecida como:

```text
Backbone Area
```

---

# EIGRP

EIGRP significa:

```text
Enhanced Interior Gateway Routing Protocol
```

Foi desenvolvido pela Cisco.

---

## Características

Utiliza múltiplos critérios:

- Banda.
- Atraso.
- Confiabilidade.

---

## Vantagens

- Convergência rápida.
- Boa eficiência.

---

# BGP

BGP significa:

```text
Border Gateway Protocol
```

É o protocolo responsável pelo roteamento da Internet.

---

## Função

Permitir a troca de rotas entre diferentes Sistemas Autônomos (AS).

---

## Sistema Autônomo

Um Sistema Autônomo é um conjunto de redes administradas por uma mesma organização.

Exemplos:

- Operadoras.
- Universidades.
- Grandes empresas.
- Provedores de Internet.

---

## Exemplo de Comunicação BGP

```text
Provedor A
↓
Internet
↓
Provedor B
```

O BGP troca informações entre essas organizações.

---

# Algoritmos de Roteamento

Os protocolos utilizam algoritmos para determinar rotas.

---

## Vetor de Distância

Exemplo:

```text
RIP
```

Baseia-se na distância até o destino.

---

## Estado de Enlace

Exemplo:

```text
OSPF
```

Mantém um mapa completo da topologia da rede.

---

## Vetor de Caminho

Exemplo:

```text
BGP
```

Considera o caminho completo percorrido.

---

# Convergência

Convergência é o tempo necessário para que todos os roteadores possuam informações consistentes sobre a rede.

Objetivo:

```text
Menor tempo possível
```

---

# Balanceamento de Carga

Alguns protocolos permitem utilizar múltiplos caminhos simultaneamente.

Benefícios:

- Melhor desempenho.
- Maior disponibilidade.

---

# Redundância

A redundância garante caminhos alternativos.

Exemplo:

```text
Rota Principal
↓
Falha
↓
Rota Secundária
```

Isso aumenta a disponibilidade da rede.

---

# Comunicação entre Redes

Exemplo simplificado:

```text
Rede A
↓
Roteador
↓
Rede B
↓
Roteador
↓
Rede C
```

Os roteadores trabalham continuamente encaminhando pacotes entre essas redes.

---

# Ferramentas de Diagnóstico

## Ping

Verifica conectividade.

Exemplo:

```bash
ping 8.8.8.8
```

---

## Traceroute

Mostra os roteadores percorridos.

Windows:

```cmd
tracert google.com
```

Linux:

```bash
traceroute google.com
```

---

# Relação com Outros Protocolos

O roteamento trabalha em conjunto com:

### IP

Identifica origem e destino.

### ARP

Resolve IP para MAC localmente.

### ICMP

Auxilia em diagnósticos e erros.

### TCP e UDP

Transportam os dados da aplicação.

---

# Importância do Roteamento

O roteamento é o mecanismo que conecta redes diferentes e permite a comunicação global.

Sem ele:

- Não existiria Internet.
- Redes permaneceriam isoladas.
- Serviços online seriam impossíveis.

---

# Exemplo Completo de Comunicação

```text
Computador
↓
Switch
↓
Roteador
↓
Internet
↓
Roteadores Intermediários
↓
Servidor
```

Em cada etapa, os roteadores analisam o endereço IP de destino e escolhem o próximo caminho.

---

# Conclusão

O roteamento é o processo responsável por determinar os caminhos percorridos pelos pacotes entre redes diferentes. Utilizando tabelas de roteamento, protocolos como RIP, OSPF e BGP e equipamentos como roteadores, ele torna possível a comunicação entre dispositivos em qualquer lugar do mundo. O entendimento de roteamento é essencial para compreender o funcionamento da Internet e das redes corporativas modernas.