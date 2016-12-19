from domain.email import ServicoEmail
from web.excecoes import FormatadorEmailNaoExistente

class ServicoEmailFormatado(ServicoEmail):
    def __init__(self, formatadores):
        self.formatadores = formatadores

    def formatador(self, email):
        formatadores = list(filter(lambda f: f.aceita(email), self.formatadores))
        if not formatadores:
            return None

        return formatadores[0]

    def formatar(self, email):
        formatador = self.formatador(email)
        if not formatador:
            return None

        return formatador(email)

    def enviar(self, destino, email):
        assunto, corpo = self.formatar(email)
        if not corpo:
            raise FormatadorEmailNaoExistente

        self.enviar_formatado(destino, assunto, corpo)
