import sreamlit as st

name= st.text_input("enter your name")

st.title("take the input name")
if st.bottom("submit Name"):
   sr.write(f"print the name : (name)")
