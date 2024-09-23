import streamlit as st

x = st.number_input("Masukan Angka")
sx = st.text_input("Satuan C", "C")
st.write ("Anda memasukkan", x, ' ',sx)
