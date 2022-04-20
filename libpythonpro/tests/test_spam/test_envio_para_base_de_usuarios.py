from unittest.mock import Mock

import pytest as pytest
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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'olv.leo@outlook.com',
        'Assunto Email',
        'Corpo email'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_paramentros_de_spam(sessao):
    usuario = Usuario(nome='Leo', email='leo@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'olv.leo@outlook.com',
        'Assunto Email',
        'Corpo email'
    )
    enviador.enviar.assert_called_once_with(
        'olv.leo@outlook.com',
        'leo@gmail.com',
        'Assunto Email',
        'Corpo email'
    )
