import pandas as pd
import matplotlib.pyplot as plt

urls = [
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"
]
"""Criando a identificação das lojas"""
lojasDados = [pd.read_csv(url) for url in urls]
lojasNomes = [f'Loja {i + 1}' for i in range(len(lojasDados))]
"""Faturamento de cada loja"""
faturamentosTotais = [dadosFaturamento['Preço'].sum() for dadosFaturamento in lojasDados]
for i in range(len(lojasDados)):
    print(f'{lojasNomes[i]}: R${faturamentosTotais[i]}')
#Gráfico de barras referente ao faturamento de cada loja
plt.bar(lojasNomes, faturamentosTotais)
plt.title('Faturamento por Loja')
plt.xlabel('Lojas')
plt.ylabel('Faturamento Total Em Milhões de Reais')
plt.ylim(1350000,1550000)
plt.show()
#Gráfico de pizza referente ao faturamento de cada loja
plt.pie(faturamentosTotais, labels=lojasNomes, startangle=180)
plt.show()
"""Quantidade por categoria"""
for i, lojaDados in enumerate(lojasDados, 1):
    plt.figure(figsize=(8, 5))
    contagemDasCategorias = lojaDados['Categoria do Produto'].value_counts()
    print(f'\n{"-"*40}')
    print(f'Loja {i} - Quantidade por Categoria:')
    for categoria, quantidade in contagemDasCategorias.items():
        print(f'{categoria}: {quantidade} unidades')
    print('-'*40)
#Gerando o gráfico de barras referente a quantidade por categoria de cada loja
    contagemDasCategorias.plot.bar(color='skyblue')
    plt.title(f'Vendas por Categoria - Loja {i}')
    plt.xlabel('Categorias')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
"""Avaliações médias"""
avaliacoesMedias = []
for i, loja in enumerate(lojasDados):
    media = loja["Avaliação da compra"].mean()
    avaliacoesMedias.append(media)
    print(f"{lojasNomes[i]}: {media:.2f}")
#Gerando o gráfico de barras das avaliações médias de cada loja
plt.bar(lojasNomes, avaliacoesMedias)
plt.title('Média de Avaliação por Loja')
plt.ylabel('Média de Avaliação')
plt.ylim(3.9, 4.10)
plt.show()
"""Produtos Mais e Menos Vendidos de cada loja"""
for dados, nome in zip(lojasDados, lojasNomes):
    contagemProdutos = dados['Produto'].value_counts()
    produtoMaisVendido = contagemProdutos.idxmax()
    quantidadeMaisVendido = contagemProdutos.max()
    produtoMenosVendido = contagemProdutos.idxmin()
    quantidadeMenosVendido = contagemProdutos.min()
    print(f"\n{nome}:")
    print(f"Produto mais vendido: {produtoMaisVendido} ({quantidadeMaisVendido} vendas)")
    print(f"Produto menos vendido: {produtoMenosVendido} ({quantidadeMenosVendido} vendas)")
#Gerando o gráfico de linhas dos produtos mais e menos vendidos por cada loja
for i, dados in enumerate(lojasDados, start=1):
    plt.figure(figsize=(10, 5))
    contagemDosProdutos = dados['Produto'].value_counts()
    maisVendidos = contagemDosProdutos.head(3)
    menosVendidos = contagemDosProdutos.tail(3)
    pareandoTops3 = pd.concat([maisVendidos, menosVendidos])
    pareandoTops3.plot(kind='line', marker='o', color='green', linewidth=2, markersize=8)
    plt.title(f'Loja {i} - Desempenho de Produtos', fontsize=14)
    plt.xlabel('Produtos', fontsize=12)
    plt.ylabel('Quantidade Vendida', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
"""Frete médio por loja"""
mediasFretes = []
for dados, nome in zip(lojasDados, lojasNomes):
    mediaFrete = dados['Frete'].mean()
    mediasFretes.append(mediaFrete)
    print(f"{nome}:")
    print(f"Média de frete → R${mediaFrete:.2f}\n")
#Gerando o gráfico de barras dos valores de frete médio de cada uma das lojas
plt.bar(lojasNomes,mediasFretes)
plt.title('Médias de Frete por Loja')
plt.ylabel('Valor médio do frete em R$')
plt.ylim(30,35)
plt.show()
#Gerando mapa de dispersão com as informações de latitude e longitude
#Não consegui, fica para depois ;-;