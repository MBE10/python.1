import pandas as pd
import streamlit as st
import ploty.express as px

book_df = pd.read_csv('books.csv')

st.title('Bestselling book analysis')
st.write("This is a simple app for getting to now the best books")


#sidebar

st.sidebar.header("add a new book")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author Name")
    new_user_rating = st.slider("user rating", 0.5, 5.0, 0.0, 0.1)
    new_reviews = st.number_input("Num Inputs" min_value=0, step=1)
    new_price = st.number_input("Price", min_value=1, step=1)
    new_year = st.number_input("Year", min_value=2009, max_value=2025)
    new_ganre = st.selections("Ganre", books_df['Ganre'].unique())
    submit_button = st.form_submit_button(label="Add book")
