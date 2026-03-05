from unicodedata import category

from pymysql import connect
import streamlit as st
from functions import insert_product, list_products, delete_products    , update_product

st.set_page_config(page_title= 'Sistema de estoque', layout='centered')
st.title('Sistema de estoque')

menu = st.sidebar.selectbox("Menu", ["Inserir produto", "Ver produtos", "Deletar produto", "Atualizar produto"])

#INSERIR PRODUTO
if menu == "Inserir produto":
    st.header("+Inserir produto")
    name = st.text_input("nome do produto")
    price = st.number_input("preço do produto", min_value=0.0, format='%2f')
    category = st.text_input("categoria do produto")
    quantity = st.number_input("quantidade do produto", min_value=1)
    provider = st.text_input("FORNECEDOR DO PRODUTO")


    if st.button("Salvar"):
        if name:
            insert_product(name, category, price, quantity, provider)
            st.success("produto salvo com sucesso")
        else:
            st.warning("digite o nome do produto")


if menu == "Ver produtos":
    st.header("Produtos cadastrados")
    products = list_products()
    st.table (products, columns=["ID", "Nome", "Categoria", "Preço", "Quantidade", "Fornecedor"])

if menu == "Deletar produto":
    id = st.number_input("ID do produto a ser deletado", min_value=1)
    if st.button("Deletar produto"):
        delete_products(id)
        st.success("produto deletado com sucesso")

if menu == "Atualizar produto":
    st.header("atualizar produto")
    id = st.number_input("ID do produto a ser atualizado ", min_value=1)
    name = st.text_input("nome do produto")
    price = st.number_input("preço do produto", min_value=0.0, format="%2f")
    category = st.text_input("categoria do produto")
    quantity = st.number_input("quantidade do produto", min_value=1)
    provider = st.text_input("Fornecedor do produto")
    if st.button("Atualizar produto"): 
        update_product(id, name, category, price, quantity, provider)
        st.success("produto atualizado com sucesso")