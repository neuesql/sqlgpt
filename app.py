from io import StringIO

import pandas as pd
import streamlit as st
import os

from src.client import SQLTransformer

st.set_page_config(
    page_title='A SQL Generative Pre-trained Transformer',
    layout='wide',
    initial_sidebar_state='expanded'
)

databases = ['Oracle', 'DB2', 'SQLServer', 'PostgreSQL']
# -------------

st.sidebar.header('A SQL Transformer')

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

input_text = st.sidebar.text_area(
    label='Insert SQL',
    placeholder='select * from now()'
)

input_file = st.sidebar.file_uploader(
    label="Choose a SQL file",
    accept_multiple_files=False)

st.subheader("Target SQL")

client = SQLTransformer(
    organization=os.getenv('openapi-org'),
    api_key=os.getenv('openapi-key')
)


def transform():
    code = input_text
    if code:
        st.code(code, language='sql')
    else:
        if input_file is not None:
            # To convert to a string based IO:
            stringio = StringIO(input_file.getvalue().decode("utf-8"))
            # To read file as string:
            source_sql = stringio.read()
            target_sql = client.generate(source_sql)
            st.code(target_sql)


transform_button = st.sidebar.button(
    label='Transform', type='primary',
    on_click=transform()
)

# ---------------------------------------
