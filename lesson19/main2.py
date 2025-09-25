import pandas as pd
import streamlit as st
import plotly.express as px

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
    new_genre = st.selectbox("Genre", book_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add book")


    if submit_button:
        new_data = {
            'Name': new_name,
            'Author': new_author,
            'Rating': new_user_rating,
            'Reviews': new_reviews,
            'Price': new_price,
            'Year': new_year,
            'Genre': new_genre
        }

        book_df = pd.concat([pd.DataFrame(new_data, index=[0]), book_df], ignore_index=True)
        book_df.to_csv('bestsellers_with_categories_2022_03_27.csv', index=False)
        st.sidebar.success("New book is added")


st.sidebar.header("Filter options")
selected_author = st.sidebar.selectbox("Select AUTHOR", ["All"] + list(book_df['Author'].unique()))
selected_year = st.sidebar.selectbox("Select Year", ["All"] + list(book_df['Year'].unique()))
selected_genre = st.sidebar.selectbox("Select Genre", ["All"] + list(book_df['Genre'].unique()))
min_rating = st.sidebar.slider("Minimum rating", 0.0 , 5.0 , 0.1)
max_price = st.sidebar.slider("Maximum price", 0 , book_df['Price'].max(), book_df['Price'].max())

filtered_book_df = book_df.copy()

if selected_author != "All":
    filtered_book_df = filtered_book_df[filtered_book_df['Author'] == selected_author]
if selected_year != "All":
    filtered_book_df = filtered_book_df[filtered_book_df['Year'] == int(selected_year)]
if selected_genre != "All":
    filtered_book_df = filtered_book_df[filtered_book_df['Genre'] == selected_genre]   

filtered_book_df = filtered_book_df[
     (filtered_book_df['User Rating'] >= min_rating) & (filtered_book_df['Price'] <= max_price)
]    


st.subheader(" Summary Statistic")

total_books = filtered_book_df.shape[0]
unique_titles = filtered_book_df['Name'].nunique()
average_rating = filtered_book_df['User Rating'].mean()
average_price = filtered_book_df['Price'].mean()

col1 , col2 , col3 , col4 = st.columns(4)
col1.metric("Total Books" , total_books)
col2.metric("Titles" , unique_titles)
col3.metric("Average Ratings", f"{average_rating:.2f}")
col4.metric("Average Price", f"{average_price:.2f}")

st.subheader("Dataset preview")
st.write(filtered_book_df.head())

col1 , col2  = st.columns(2)

with col1:
    st.subheader("Top 10 book Titles")
    top_titles = filtered_book_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)


with col2:
    st.subheader("Top 10 Authors")
    top_authors = filtered_book_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)


st.subheader("Genre")
fig = px.pie(filtered_book_df , names='Genre', title='Most liked genre(2009-2019)', color='Genre',
color_discrete_sequence=px.colors.sequential.Plasma)    
st.plotly_chart(fig)