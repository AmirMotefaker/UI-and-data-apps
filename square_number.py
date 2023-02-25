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
with st.sidebar:
    my_component(greeting="Hello")
    
x = st.slider("Select a value")

# Answer
st.write(x, "squared is", x * x)

# --------------------------------------
# third step:
# and Now run it to open the app in browser with this code:
# $ streamlit run square_number.py
