import streamlit as st

x = st.number_input(
  "insert a number", value=None, placeholder="Type a number..."
)
st.write("The current number is ", x)
st.latex(r'''
    x^2 =
    ''')
st.write(x*x)
