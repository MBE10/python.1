import streamlit as st

with st.container():
    st.header("This is a container")
    st.subheader("The first container")
    st.write("This is my first container with streamlit")




tab1, tab2, tab3 = st.tabs(["News, Sport", "Economy"])

with tab1:
    st.header = ("News")
    st.write = ("Latest News")

with tab2:
    st.header = ("Sport")
    st.write = ("Latest sport news")

with tab3:
    st.header = ("Economy") 
    st.write = ("Latest economy news")       
