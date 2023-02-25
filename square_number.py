# Calculate the square of any number

# ---------------------------------------
# first step:
# Open a terminal and run:

# $ pip install streamlit
# $ streamlit hello

# If this opens our sweet Streamlit Hello app in your browser, you're all set! 

# ---------------------------------------
# second step:
# Create a new file square_number.py with the following code:

import streamlit as st

# Title
st.title('Calculate the square of any number')
   
# Slider
x = st.slider("Select a value")

# Answer
st.write(x, "squared is", x * x)
st.write(x, "multiply 1 is",  x * 1)
st.write(x, "multiply 2 is",  x * 2)
st.write(x, "multiply 3 is",  x * 3)
st.write(x, "multiply 4 is",  x * 4)
st.write(x, "multiply 5 is",  x * 5)
st.write(x, "multiply 6 is",  x * 6)
st.write(x, "multiply 7 is",  x * 7)
st.write(x, "multiply 8 is",  x * 8)
st.write(x, "multiply 9 is",  x * 9)


# --------------------------------------
# third step:
# and Now run it to open the app in browser with this code:
# $ streamlit run square_number.py
