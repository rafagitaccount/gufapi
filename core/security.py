from passlib.context import CryptContext

CRYPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(password: str, password_hash: str) -> bool:
    """
    Função para verificar se a senha está correta, comparando
    a senha em texto puro, informada pelo usuário, e o hash da senha
    que estará salvo no banco de dados durante a criação da conta.
    """
    return CRYPTO.verify(password, password_hash)


def make_password_hash(password: str) -> str:
    """
    Função que gera e retorna o hash da senha
    """
    return CRYPTO.hash(password)
