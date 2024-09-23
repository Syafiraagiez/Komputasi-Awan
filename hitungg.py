import streamlit as st

x = st.number_input("Masukan Angka")
sx = st.text_input("Satuan C", "C")
st.write ("Anda memasukkan", x, ' ',sx)
sy = st.text_input("Dikonversi ke", "C")
y = 0
if (sx == 'C');
  if(sy == 'C');
    y = x
  elif(sy == 'F'):
   F = (9/5) * x + 32

st.write (x,' ',sx, ' = ',y, sy)
