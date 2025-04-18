import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Análise Alura Store')

urls = [
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"
]

lojasDados = [pd.read_csv(url) for url in urls]
lojasNomes = [f'Loja {i + 1}' for i in range(len(lojasDados))]

# Faturamento de cada loja
st.header("Faturamento Total por Loja")
faturamentosTotais = [dados['Preço'].sum() for dados in lojasDados]
for nome, faturamento in zip(lojasNomes, faturamentosTotais):
    st.write(f'{nome}: R${faturamento:,.2f}')

# Gráfico de Barras - Faturamento
fig, ax = plt.subplots()
ax.bar(lojasNomes, faturamentosTotais)
ax.set_title('Faturamento por Loja')
ax.set_xlabel('Lojas')
ax.set_ylabel('Faturamento Total (R$)')
ax.set_ylim(1350000, 1550000)
st.pyplot(fig)

# Gráfico de Pizza - Faturamento
fig, ax = plt.subplots()
ax.pie(faturamentosTotais, labels=lojasNomes, startangle=180, autopct='%.1f%%')
ax.set_title('Participação no Faturamento Total')
st.pyplot(fig)

# Quantidade por Categoria
st.header("Quantidade Vendida por Categoria")
for i, dados_loja in enumerate(lojasDados, 1):
    st.subheader(f'Loja {i}')
    contagem = dados_loja['Categoria do Produto'].value_counts()

    # Exibe tabela de quantidades
    for categoria, qtd in contagem.items():
        st.write(f'{categoria}: {qtd} unidades')

    # Gráfico de Barras
    fig, ax = plt.subplots(figsize=(8, 5))
    contagem.plot.bar(ax=ax, color='skyblue')
    ax.set_title(f'Vendas por Categoria - Loja {i}')
    ax.set_xlabel('Categorias')
    ax.set_ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Avaliações Médias
st.header("Avaliações Médias por Loja")
avaliacoes_medias = [dados['Avaliação da compra'].mean() for dados in lojasDados]

fig, ax = plt.subplots()
ax.bar(lojasNomes, avaliacoes_medias)
ax.set_title('Média de Avaliação por Loja')
ax.set_ylabel('Média de Avaliação')
ax.set_ylim(3.9, 4.1)
st.pyplot(fig)

# Produtos Mais/Menos Vendidos
st.header("Desempenho de Produtos")
for i, dados in enumerate(lojasDados, 1):
    st.subheader(f'Loja {i}')
    contagem = dados['Produto'].value_counts()

    # Top 3 e Bottom 3
    top3 = contagem.head(3)
    bottom3 = contagem.tail(3)

    st.write("**Mais vendidos:**")
    for produto, qtd in top3.items():
        st.write(f"- {produto}: {qtd} unidades")

    st.write("**Menos vendidos:**")
    for produto, qtd in bottom3.items():
        st.write(f"- {produto}: {qtd} unidades")

    # Gráfico de Linha
    fig, ax = plt.subplots(figsize=(10, 5))
    pd.concat([top3, bottom3]).plot(kind='line', marker='o', ax=ax, color='green')
    ax.set_title(f'Desempenho de Produtos - Loja {i}')
    ax.set_xlabel('Produtos')
    ax.set_ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Frete Médio
st.header("Média de Frete por Loja")
medias_frete = [dados['Frete'].mean() for dados in lojasDados]

fig, ax = plt.subplots()
ax.bar(lojasNomes, medias_frete)
ax.set_title('Média de Frete por Loja')
ax.set_ylabel('Valor Médio (R$)')
ax.set_ylim(30, 35)
st.pyplot(fig)