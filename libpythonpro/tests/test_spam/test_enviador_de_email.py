import pytest as pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert None is not enviador


@pytest.mark.parametrize(
    'destinatario',
    ['olv.leo@outlook.com', 'kfernaadess@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'teste@gmail.com',
        'Curso Python Pro',
        'Corpo do email',
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['karine', 'leonardo']

)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'teste@gmail.com',
            'Curso Python Pro',
            'Corpo do email',
        )
