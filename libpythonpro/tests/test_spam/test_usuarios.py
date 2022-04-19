from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Leonardo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(conexao, sessao):
    usuarios = [Usuario(nome='Leonardo'), Usuario(nome='Karine')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
