import pytest as pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Leonardo', email='leonardo@gmail.com'),
            Usuario(nome='Lucas', email='lucas@gmail.com'),
            Usuario(nome='Karine', email='karine@gmail.com'),
        ],
        [
            Usuario(nome='Dilma', email='dilma@gmail.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'olv.leo@outlook.com',
        'Assunto Email',
        'Corpo email'
    )
    assert len(usuarios) == enviador.qtd_emails_enviados


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Leonardo', email='leonardo@gmail.com'),
            Usuario(nome='Lucas', email='lucas@gmail.com'),
            Usuario(nome='Karine', email='karine@gmail.com'),
        ],
        [
            Usuario(nome='Dilma', email='dilma@gmail.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'olv.leo@outlook.com',
        'Assunto Email',
        'Corpo email'
    )
    assert len(usuarios) == enviador.qtd_emails_enviados


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.parametros_de_envio = None
        self.qtd_emails_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_emails_enviados += 1


def test_paramentros_de_spam(sessao):
    usuario = Usuario(nome='Leo', email='leo@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'olv.leo@outlook.com',
        'Assunto Email',
        'Corpo email'
    )
    assert enviador.parametros_de_envio == (
        'olv.leo@outlook.com',
        'leo@gmail.com',
        'Assunto Email',
        'Corpo email'
    )
