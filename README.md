# GEA - Guia de Estudos Acadêmicos

Trabalho final da disiciplina desenvolvido pelo aluno Guilherme Grosselli, matricula 199442, para a disciplina de Inteligência Artificial do Curso de Ciência da Computação - UPF.

## Descrição

O GEA - Guia de Estudos Acadêmicos é um assistente de estudos desenvolvido em linguagem Python, versão 3.14, para auxiliar estudantes universitários dos cursos de Ciência da Computação na consulta e revisão de conteúdos acadêmicos das disciplinas. O sistema utiliza uma arquitetura multiagente composta por Planejador, Pesquisador e Executor/Revisor, integrada a um mecanismo RAG (Retrieval-Augmented Generation) com ChromaDB e modelo local executado através do Ollama, versão 3.2. Seu funcionamento ocorre via terminal.

## Arquitetura

* Interface CLI
* Orquestrador Multiagente
* Agente Planejador
* Agente Pesquisador
* Agente Executor/Revisor
* MCP Server
* RAG + ChromaDB
* Modelo Local (Ollama)

## Tecnologias

* Python
* Ollama
* ChromaDB
* LangChain
* MCP
* FastMCP

## Estrutura do Projeto

agents/

* planner.py
* researcher.py
* executor.py
* orchestrator.py

rag/

* ingest.py
* query.py

mcp_server/

* server.py

base_dados/

* materiais de estudo, sobre os temas Redes de Computadores, Inteligência Artificial e Sistemas Operacionais.

vector_db/

* base vetorial gerada pelo ChromaDB


## Execução (Windows,Linux e macOS)

Após abrir o diretório onde estão salvos os arquivos pelo terminal:

Instalar os seguintes comandos Ollama na sua máquina:
```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

Instalar dependências:

```bash
pip install -r requirements.txt
```
ou em alguns modelos Linux:
```bash
pip3 install -r requirements.txt
```

Executar:

```bash
python main.py
```

ou em alguns modelos Linux:
```bash
python3 main.py
```

## Reindexação da Base (Opcional)

A pasta vector_db já acompanha o projeto.
Não é necessário executar rag/ingest.py para utilizar o sistema.
A reindexação só é necessária caso os arquivos da pasta base_dados sejam modificados ou novos materiais sejam adicionados

```bash
python rag/ingest.py
```

ou em alguns modelos Linux:
```bash
python3 rag/ingest.py
```

## Funcionalidades

* Perguntas sobre conteúdos acadêmicos
* Geração de resumos
* Busca semântica utilizando RAG
* Execução totalmente local