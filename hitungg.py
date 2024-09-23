import streamlit as st

x = st.number_input("Masukan Angka")
sx = st.text_input("Satuan C", "C")
st.write ("Anda memasukkan", x, ' ',sx)
sy = st.text_input("Dikonversi ke", "C")
if(Satuan == "C"):
  if(konversi == "C"):
   print(x, " C = ", x, "C")
  elif(konversi == "F"):
    y = x*9/5+32
    print(x, " C = ", y,"R")
  elif(konversi == "K"):
    y = x*9/5+32
    print(x, " C = ", y,"K")
  else:
    print("Maaf, satuan konversi tidak di")

elif(satuan == "F"):
  if(konversi == "R"):
    y = (x-32)*4/9
    print(x, "F = ", y,"R")
else:
  print("Maaf, satuan tidak dikenali")
st.write (x, ' ',sx, '= ...', sy)
