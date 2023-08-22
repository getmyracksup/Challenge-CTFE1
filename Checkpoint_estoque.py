estoque = {}

def adicionarEstoque():
    nome = input("Digite o nome do produto: ")
    if nome in estoque:
        print("Produto já existente no estoque")
        return
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade no estoque: "))
    estoque[nome] = [preco, quantidade]
    return
    
def baixaEstoque():
    nome = input("Digite o nome do produto: ")
    if not nome in estoque:
        print("Produto não existe no estoque!")
        return
    quantidadeBaixa = int(input("Digite a quantidade da baixa: "))
    quantidadeAtual = estoque[nome][1]
    if not quantidadeAtual >= quantidadeBaixa:
        print("Quantidade no estoque insuficiente para baixa.")
        return
    estoque[nome][1] -= quantidadeBaixa
    return
    
def mostrarEstoque():
    chavesEstoque = estoque.keys()
    i = 1
    print("Estoque\n\n")
    for chave in chavesEstoque:
        print("%i - %s Preco: R$%.2f Quantidade: %i\n" %(i, chave, estoque[chave][0], estoque[chave][1]))
        i += 1
    return

opcoes = {1:adicionarEstoque, 2:baixaEstoque, 3:mostrarEstoque}
while True:
    escolha = int(input("Escolha uma opcao para continuar:\n\n1 - Adicionar produto ao estoque\n2 - Dar baixa em um produto\n3 - Mostrar estoque\n4 - Sair\n\nOpcao: "))
    if escolha in opcoes:
        opcoes[escolha]()
    elif escolha == 4:
        break
    else:
        print("Opcao invalida!")