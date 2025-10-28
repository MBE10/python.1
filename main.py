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




from fastapi import FastAPI, HTTPException
from typing import List
import database
import models
from models import Movie, MovieCreate


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Movies CRUD API"}


 


 
@app.post("/movies/" , response_model=Movie)
def create_movie(movie:MovieCreate):
    """ Creates a new movie in the database """
    movie_id = database.create_movie(movie)
    return models.Movie(id=movie_id , **movie.diet())


@app.get("/movies/{movie_id}" , response_model=Movie)
def read_movie(movie_id: int):
    """ reads out movies from database single movies"""
    movie = database.read_movie(movie_id)
    if movie is None:
       raise HTTPException(status_code=404 , detail="MOVIE NOT FOUND ")
    return movie
@app.put("/movies/{movie_id}" , response_model=Movie)
def update_movie(movie_id: int , movie:MovieCreate):
    """ Updates the movies"""
    updated = database.update_movie(movie_id , movie)
    if not updated:
        raise HTTPException(status_code=404 , detail="Movie not found")
    return models.Movie(id=movie_id , **movie.diet())

@app.delete("/movies/{movie_id}" , response_model=dict)
def delete_movie(movie_id:int):
    """deletes a movie"""
    deleted = database.delete_movie(movie_id)
    if not deleted:
        raise HTTPException(status_code=404 , detail="Movie not found")
    return {"message": "Movie deleted successfully"}