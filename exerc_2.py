import json
from unittest import case

dados = '''
{
	"estoque":
	[
	  {
		"codigoProduto": 101,
		"descricaoProduto": "Caneta Azul",
		"estoque": 150
	  },
	  {
		"codigoProduto": 102,
		"descricaoProduto": "Caderno Universitário",
		"estoque": 75
	  },
	  {
		"codigoProduto": 103,
		"descricaoProduto": "Borracha Branca",
		"estoque": 200
	  },
	  {
		"codigoProduto": 104,
		"descricaoProduto": "Lápis Preto HB",
		"estoque": 320
	  },
	  {
		"codigoProduto": 105,
		"descricaoProduto": "Marcador de Texto Amarelo",
		"estoque": 90
	  }
	]
}'''

estoque = json.loads(dados)

parar = None
resposta = None


def cadastrar():
    while True:
        codItem = int(input('Digite o código do item: '))

        codigo_repetido = False

        for i in estoque['estoque']:
            if codItem == i['codigoProduto']:
                print('Já existe um item com este código. Tente outro\n')
                codigo_repetido = True
                break

        if codigo_repetido:
            continue
        else:
            break


    descricao = input('Digite a descrição do item: ')
    qtdEstoque = int(input('Digite a quantidade de estoque do item: '))
    estoque['estoque'].append({'codigoProduto': codItem, 'descricaoProduto': descricao, 'estoque': qtdEstoque})

def excluir():
  while True:
    codItem = int(input('Digite o código do item: '))


    for produto in estoque['estoque']:
      if produto['codigoProduto'] == codItem:
        estoque['estoque'].remove(produto)

        print(estoque['estoque'])
      break
    break

def mostrarItens():
  for item in estoque['estoque']:
    print(f"Código: {item['codigoProduto']}")
    print(f"Descrição: {item['descricaoProduto']}")
    print(f"Quantidade: {item['estoque']}")
    print('-' * 30)

while parar is None:
  try:
    resposta = int(input('Qual operação desejar realizar? (somente números)\n'
    '1 - Cadastrar no estoque\n' 
	  '2 - Excluir do estoque\n'
    '3 - ver itens\n'
    '4 - Sair do programa\n'))

    match resposta:
        case 1:
            cadastrar()

        case 2:
          excluir()

        case 3:
          mostrarItens()
          continue

        case 4:
          break

        case _:
          print('Digite uma opção válida.')
          print()
          continue

  except ValueError:
    continue

