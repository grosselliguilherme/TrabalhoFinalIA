from mcp_server.server import buscar_conteudo


class Researcher:

    def search(self, query):

        resultados = buscar_conteudo(query)

        return resultados