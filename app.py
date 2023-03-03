import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')
import streamlit as st
import pandas as pd
from io import StringIO

databases = ['Oracle', 'DB2', 'SQLServer', 'PostgreSQL']

source_database = st.sidebar.selectbox(
    label='Source Database',
    options=databases,
    index=0
)

target_database = st.sidebar.selectbox(
    label='Target Database',
    options=databases,
    index=3
)

input_files = st.sidebar.file_uploader("Choose a SQL file", accept_multiple_files=True)
for uploaded_file in input_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

input_text = st.sidebar.text_area(
    label='Insert SQL',
    placeholder='select * from now()'
)
transform_button = st.sidebar.button(
    label='Transform', type='primary')

col1, col2 = st.columns(2)

with col1:
    st.header("Source SQL")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col2:
    st.header("Target SQL")
    st.image("https://static.streamlit.io/examples/dog.jpg")
