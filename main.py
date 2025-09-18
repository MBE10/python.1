import streamlit as st
import pandas as pd





# tab1, tab2, tab3 = st.tabs(["News", "Sport", "Economy"])

# with tab1:
#     st.header = ("News")
#     st.write = ("Latest News")

# with tab2:
#     st.header = ("Sport")
#     st.write = ("Latest sport news")

# with tab3:
#     st.header = ("Economy") 
#     st.write = ("Latest economy news")     

# df = pd.DataFrame({
#     'Name':['Alice', 'John', 'Josh'],
#     'Age':[20,21,25],
#     'City':['New York', 'Paris', 'Berlin']
# })    

# st.write(df)


books_df = pd.read_csv('books.csv')
st.title('Best Selling Books')
st.write('This app analyzes the Amazon Top selling books from 2009-2022')

st.subheader("Summary statistics")

total_books = books_df.shape[0]
unique_titles = books_df['Name'].unique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1,col2,col3,col4 = st.columns(4)
col1.metric("Total Books",total_books)
col2.metric("Unique Titles",unique_titles)
col3.metric("Average Rating",average_rating)
col4.metric("Average Price",average_price )
