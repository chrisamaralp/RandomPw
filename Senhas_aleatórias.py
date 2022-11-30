import random
import string


def criador_senha(tamanho, quantidade):
    # criaremos uma lista para juntar todas as senhas criadas nos loops
    senha = []
    # aqui iremos definir as nossas variáveis de caracteres que vão compor as nossas senhas
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    special = string.punctuation
    alphabet = lower + upper + num + special
    # primeiro vamos criar uma variável 'pw' para guardar nossas senhas
    for _ in range(quantidade):
        pw = ''
        # cada loop que iremos dar vamos juntar um conjunto de strings do nosso "alfabeto", colocar na variável pw e dps
        # dar append nela para adicionarmos na nossa lista senha
        for i in range(tamanho):
            pw += random.choice(alphabet)
        senha.append(pw)
    # para isso criamos nossa variavel senha como lista, para resultar em algo que não seja None
    return senha


quantidade = input("How many passwords? ")
quantidade = int(quantidade)

tamanho = input("What's the lenght? ")
tamanho = int(tamanho)

print(criador_senha(tamanho, quantidade))
