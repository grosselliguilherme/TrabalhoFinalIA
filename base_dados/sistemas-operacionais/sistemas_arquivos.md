<!--
ARQUIVO DE CONTEÚDO GERADO PELA INTELIGÊNCIA ARTIFICIAL APENAS PARA A DEMONSTRAÇÃO DO TRABALHO, ALERTO POIS ALGUMAS INFORMAÇÕES PODEM ESTAR INCORRETAS.
PROCURE BUSCAR CONHECIMENTO ATRAVÉS DE OUTRAS FONTES MAIS CONFIÁVEIS!
-->
# Sistema de Arquivos

## Introdução

O Sistema de Arquivos (File System) é o componente do sistema operacional responsável por organizar, armazenar, recuperar e gerenciar dados em dispositivos de armazenamento.

Sem um sistema de arquivos, os dados seriam armazenados apenas como sequências de bits, dificultando sua localização e utilização.

O sistema de arquivos fornece uma estrutura lógica que permite ao usuário e aos programas manipular informações através de arquivos e diretórios.

---

# O que é um Arquivo?

Um arquivo é uma unidade lógica de armazenamento utilizada para guardar informações.

Exemplos:

- Documentos
- Imagens
- Vídeos
- Programas
- Planilhas
- Bancos de Dados

Exemplos de arquivos:

```text
relatorio.pdf
foto.jpg
programa.py
dados.csv
```

---

# Características dos Arquivos

Um arquivo normalmente possui:

- Nome
- Extensão
- Tamanho
- Proprietário
- Data de criação
- Data de modificação
- Permissões

---

# Nome e Extensão

O nome identifica o arquivo.

Exemplo:

```text
trabalho_redes.pdf
```

Onde:

```text
Nome: trabalho_redes
Extensão: pdf
```

A extensão geralmente indica o tipo de conteúdo.

---

# Diretórios

Os diretórios (pastas) são estruturas utilizadas para organizar arquivos.

Exemplo:

```text
Documentos
├── Redes
│   └── tcp.pdf
├── IA
│   └── perceptron.pdf
└── SO
    └── memoria.pdf
```

---

# Estrutura Hierárquica

Os sistemas operacionais modernos organizam arquivos em forma de árvore.

Exemplo Linux:

```text
/
├── home
├── etc
├── usr
└── var
```

Exemplo Windows:

```text
C:\
├── Users
├── Windows
└── Program Files
```

---

# Caminhos (Paths)

Um caminho identifica a localização de um arquivo.

---

## Caminho Absoluto

Indica o caminho completo.

Linux:

```bash
/home/aluno/documento.txt
```

Windows:

```cmd
C:\Users\Aluno\documento.txt
```

---

## Caminho Relativo

Indica a localização em relação ao diretório atual.

Exemplo:

```text
documento.txt
```

ou

```text
../arquivo.pdf
```

---

# Operações com Arquivos

Os sistemas operacionais permitem diversas operações.

---

## Criar

```text
Criar Arquivo
```

---

## Abrir

```text
Open
```

---

## Ler

```text
Read
```

---

## Escrever

```text
Write
```

---

## Fechar

```text
Close
```

---

## Excluir

```text
Delete
```

---

# Métodos de Acesso

Existem diferentes formas de acessar dados em arquivos.

---

# Acesso Sequencial

Os dados são lidos em ordem.

Exemplo:

```text
Registro 1
Registro 2
Registro 3
Registro 4
```

Muito utilizado em arquivos de texto.

---

# Acesso Direto

Permite acessar qualquer posição diretamente.

Exemplo:

```text
Ir para posição 500
```

Muito utilizado em bancos de dados.

---

# Acesso Indexado

Utiliza índices para localizar informações rapidamente.

Exemplo:

```text
Índice
↓
Registro
```

Muito comum em sistemas de banco de dados.

---

# Organização Física dos Dados

Os dados são armazenados em blocos.

Exemplo:

```text
Bloco 1
Bloco 2
Bloco 3
Bloco 4
```

O sistema operacional controla a localização desses blocos.

---

# Alocação de Arquivos

Existem diferentes estratégias de armazenamento.

---

## Alocação Contígua

Os blocos ficam armazenados em sequência.

Exemplo:

```text
Bloco 10
Bloco 11
Bloco 12
Bloco 13
```

Vantagem:

```text
Leitura rápida
```

Desvantagem:

```text
Fragmentação
```

---

## Alocação Encadeada

Cada bloco aponta para o próximo.

Exemplo:

```text
10 → 25 → 40 → 52
```

---

## Alocação Indexada

Utiliza uma tabela de índices.

Exemplo:

```text
Índice
↓
10
25
40
52
```

---

# FAT (File Allocation Table)

O FAT foi um dos primeiros sistemas de arquivos amplamente utilizados.

Desenvolvido pela Microsoft.

---

## Funcionamento

Utiliza uma tabela que indica quais blocos pertencem a cada arquivo.

Estrutura:

```text
Arquivo
↓
Tabela FAT
↓
Blocos do Disco
```

---

# Versões do FAT

---

## FAT12

Utilizado em disquetes.

---

## FAT16

Utilizado em versões antigas do DOS e Windows.

---

## FAT32

Muito utilizado em:

- Pendrives
- Cartões de memória

---

# Vantagens do FAT32

- Simplicidade.
- Compatibilidade ampla.

---

# Desvantagens do FAT32

Limite de arquivo:

```text
4 GB
```

---

# NTFS (New Technology File System)

Sistema de arquivos padrão dos sistemas Windows modernos.

Introduzido pela Microsoft para substituir o FAT.

---

# Características do NTFS

- Journaling.
- Controle de permissões.
- Criptografia.
- Compressão.
- Suporte a arquivos grandes.

---

# Vantagens do NTFS

- Maior segurança.
- Melhor confiabilidade.
- Melhor recuperação após falhas.

---

# ext4

O ext4 é um dos sistemas de arquivos mais utilizados no Linux.

É sucessor do:

```text
ext
ext2
ext3
```

---

# Características do ext4

- Alto desempenho.
- Journaling.
- Suporte a arquivos grandes.
- Menor fragmentação.

---

# Vantagens do ext4

- Estabilidade.
- Eficiência.
- Excelente desempenho em Linux.

---

# Inodes

Nos sistemas Linux, as informações dos arquivos são armazenadas em estruturas chamadas:

```text
Inodes
```

---

# O que um Inode Armazena?

- Proprietário.
- Permissões.
- Tamanho.
- Datas.
- Ponteiros para blocos.

---

# O que NÃO é armazenado no Inode?

O nome do arquivo.

O nome fica armazenado no diretório.

---

# Exemplo Conceitual

```text
Diretório
↓
Nome do Arquivo
↓
Inode
↓
Dados
```

---

# Permissões no Linux

O Linux utiliza permissões para controlar acesso aos arquivos.

---

# Tipos de Usuários

Existem três categorias:

```text
Usuário (Owner)
Grupo (Group)
Outros (Others)
```

---

# Tipos de Permissões

---

## Leitura

```text
r
```

Valor:

```text
4
```

---

## Escrita

```text
w
```

Valor:

```text
2
```

---

## Execução

```text
x
```

Valor:

```text
1
```

---

# Exemplo

```text
rwxr-xr--
```

Significa:

```text
Usuário: rwx
Grupo: r-x
Outros: r--
```

---

# Notação Numérica

Exemplo:

```text
755
```

Representa:

```text
Usuário: rwx = 7
Grupo: r-x = 5
Outros: r-x = 5
```

---

# Comando chmod

Utilizado para alterar permissões.

Exemplo:

```bash
chmod 755 script.sh
```

---

# Journaling

Journaling é uma técnica utilizada para aumentar a confiabilidade dos sistemas de arquivos.

---

# Funcionamento

Antes de alterar dados:

```text
Operação
↓
Registro no Journal
↓
Execução
```

---

# Benefícios

- Recuperação após falhas.
- Menor risco de corrupção.
- Maior integridade dos dados.

---

# Sistemas que Utilizam Journaling

- NTFS
- ext3
- ext4

---

# Montagem de Sistemas de Arquivos

Antes de utilizar um dispositivo, o sistema operacional precisa montá-lo.

Linux:

```bash
mount /dev/sda1 /mnt
```

---

# Desmontagem

```bash
umount /mnt
```

A desmontagem correta evita perda de dados.

---

# Sistemas de Arquivos Modernos

Exemplos:

| Sistema | Plataforma |
|----------|------------|
| FAT32 | Windows/Pendrives |
| NTFS | Windows |
| ext4 | Linux |
| APFS | macOS |
| XFS | Linux |
| Btrfs | Linux |

---

# Resumo

O Sistema de Arquivos é responsável por organizar e armazenar informações em dispositivos de armazenamento. Ele utiliza arquivos e diretórios para estruturar os dados, além de mecanismos de alocação para controlar o armazenamento físico. Sistemas como FAT32, NTFS e ext4 possuem características específicas relacionadas a desempenho, compatibilidade e segurança. Conceitos como Inodes, permissões e Journaling são fundamentais para compreender o funcionamento dos sistemas modernos.

---

# Conclusão

Os sistemas de arquivos são componentes essenciais dos sistemas operacionais, pois permitem o armazenamento organizado e seguro das informações. Eles oferecem mecanismos para localização, proteção e recuperação de dados, sendo indispensáveis para o funcionamento de computadores, servidores e dispositivos modernos.