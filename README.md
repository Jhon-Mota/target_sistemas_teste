# Exercício 1 — Cálculo de Comissão

## Descrição

Programa desenvolvido em Python para calcular a comissão de vendedores a partir dos registros de vendas.

## Regras de Comissão

| Valor da venda           | Comissão |
| ------------------------ | -------: |
| Abaixo de R$ 100,00      |       0% |
| De R$ 100,01 a R$ 500,00 |       1% |
| Acima de R$ 500,00       |       5% |

> **Obs.:** no código, uma venda de exatamente R$ 500,00 recebe 1%.

## Tecnologias utilizadas

* Python
* Pandas

## Funcionamento

Os dados das vendas são armazenados em uma estrutura semelhante a JSON e convertidos em um `DataFrame`.

A função `calcula_comissao()` verifica o valor de cada venda e calcula a comissão correspondente:

```python
def calcula_comissao(valor):
    if valor > 500:
        return valor * 0.05
    elif valor > 100:
        return valor * 0.01
    return 0.0
```

A função é aplicada à coluna de valores:

```python
df['comissao'] = df['valor'].astype(float).apply(calcula_comissao)
```

O programa também filtra e exibe as vendas de acordo com suas faixas de comissão.

## Objetivos

Praticar:

* Manipulação de dados com Pandas;
* Funções e estruturas condicionais;
* `apply()`;
* Conversão de tipos com `astype()`;
* Filtragem de dados com `between()`.

---
# Exercício 2 — Controle de Estoque

## Descrição

Programa desenvolvido em Python para controlar produtos de um estoque, permitindo cadastrar, excluir e visualizar itens.

Os produtos possuem:

* Código;
* Descrição;
* Quantidade em estoque.

## Funcionalidades

### Cadastrar produto

Adiciona um novo produto ao estoque e verifica se o código já está cadastrado.

### Excluir produto

Remove um produto utilizando seu código.

### Visualizar produtos

Exibe todos os produtos cadastrados, com código, descrição e quantidade.

### Sair

Encerra o programa.

## Tecnologias utilizadas

* Python
* JSON
* Funções
* Listas e dicionários
* `match/case`
* Estruturas de repetição
* Tratamento de exceções

## Funcionamento

Os dados são armazenados em uma estrutura JSON e convertidos com `json.loads()`.

O programa utiliza funções para organizar as operações:

```python
cadastrar()
excluir()
mostrarItens()
```

O menu principal utiliza `match/case` para executar a operação escolhida pelo usuário.

## Objetivos

Praticar:

* Manipulação de JSON;
* Listas e dicionários;
* Funções;
* Estruturas condicionais e de repetição;
* Validação de dados;
* Tratamento de exceções.

---

# Exercício 3 — Cálculo de Juros por Atraso

## Descrição

Programa desenvolvido em Python para calcular os juros de uma dívida em atraso, considerando uma taxa de **2,5% ao dia**.

O programa solicita:

* Valor da dívida;
* Data de vencimento.

E apresenta:

* Dias de atraso;
* Valor dos juros;
* Valor total da dívida.

## Regra de cálculo

```text
Juros = Valor da dívida × 0,025 × Dias de atraso
Valor total = Valor da dívida + Juros
```

## Tecnologias utilizadas

* Python
* `datetime`

## Funcionamento

A data informada é convertida utilizando `strptime()`, enquanto `datetime.now()` obtém a data atual.

```python
data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")
data_hoje = datetime.now()
dias_atraso = (data_hoje - data_vencimento).days
```

Depois, os juros e o valor total são calculados.

## Objetivos

Praticar:

* Entrada e conversão de dados;
* Manipulação de datas;
* Diferença entre datas;
* Operações matemáticas;
* Formatação de valores com `:.2f`.
