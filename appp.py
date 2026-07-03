import sreamlit as st

name= st.text_input("enter your name")

st.title("take the input name")
if st.botton("submit Name"):
   st.write(f"print the name :",name)
