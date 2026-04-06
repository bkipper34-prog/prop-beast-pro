import streamlit as st

# Title of the application
st.title('Prop Beast Pro Application')

# Sample input fields
user_input = st.text_input('Enter some data:')

# Display the input data
if st.button('Submit'):
    st.write('You entered:', user_input)