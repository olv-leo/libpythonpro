import requests


def buscar_avatar(usuario):
    """
    Busca um avatar de um usuário no Github
    :param usuario: str com o nome do usuário
    :return: str com o link para o avatar do usuário
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']
