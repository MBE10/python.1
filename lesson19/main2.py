import pandas as pd
import streamlit as st
import ploty.express as px

book_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title('Bestselling book analysis')
st.write("This is a simple app for getting to now the best books")


#sidebar

st.sidebar.header("add a new book")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author Name")
    new_user_rating = st.slider("user rating", 0.5, 5.0, 0.0, 0.1)
    new_reviews = st.number_input("Num Inputs", min_value=0, step=1)
    new_price = st.number_input("Price", min_value=1, step=1)
    new_year = st.number_input("Year", min_value=2009, max_value=2025)
    new_ganre = st.selections("Ganre", book_df['Ganre'].unique())
    submit_button = st.form_submit_button(label="Add book")


    if submit_button:
        new_data = {
            'Name': new_name,
            'Author': new_author,
            'Rating': new_user_rating,
            'Reviews': new_reviews,
            'Price': new_price,
            'Year': new_year,
            'Ganre': new_ganre
        }

        book_df = pd.concat([pd.DataFrame(new_data, index=[0]), book_df], ignore_index=True)
        book_df.to_csv('bestsellers_with_categories_2022_03_27.csv', index=False)
        st.sidebar.success("New book is added")

