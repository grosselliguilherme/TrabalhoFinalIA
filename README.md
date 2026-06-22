# GAE - Guia de Estudos Acadêmicos

## Descrição

O GAE - Guia de Estudos Acadêmicos é um assistente de estudos desenvolvido em linguagem Python para auxiliar estudantes universitários dos cursos de Ciência da Computação na consulta e revisão de conteúdos acadêmicos das disciplinas.

O sistema utiliza uma arquitetura multiagente composta por Planejador, Pesquisador e Executor/Revisor, integrada a um mecanismo RAG (Retrieval-Augmented Generation) com ChromaDB e modelo local executado através do Ollama.

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

* materiais de estudo

vector_db/

* base vetorial gerada pelo ChromaDB


## Execução

Instalar dependências:

pip install -r requirements.txt

Executar:

python main.py

## Funcionalidades

* Perguntas sobre conteúdos acadêmicos
* Geração de resumos
* Busca semântica utilizando RAG
* Execução totalmente local