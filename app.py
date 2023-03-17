from io import StringIO

import streamlit as st

from src.client import SQLTransformer

st.set_page_config(
    page_title='A SQL Generative Pre-trained Transformer',
    layout='wide',
    initial_sidebar_state='expanded'
)

databases = ['Oracle', 'SQLServer', 'MySQL', 'DB2', 'PostgreSQL', 'Snowflake', 'Redshift']
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
    index=4
)

input_text = st.sidebar.text_area(
    label='Insert SQL',
    placeholder='select * from now()'
)

input_file = st.sidebar.file_uploader(
    label="Choose a SQL file",
    accept_multiple_files=False)

client = SQLTransformer(
    organization='org-LApth0Z5jom3MtfJQflCxXk6',
    api_key='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'
)


def transform():
    code = input_text
    source = source_database
    target = target_database
    if code:
        ts = client.generate(source, target, code)
        for solution in ts:
            st.code(solution, language='sql')
    else:
        if input_file is not None:
            # To convert to a string based IO:
            stringio = StringIO(input_file.getvalue().decode("utf-8"))
            # To read file as string:
            sql = stringio.read()
            ts = client.generate(source, target, sql)
            for solution in ts:
                st.code(solution, language='sql')


transform_button = st.sidebar.button(
    label='Transform', type='primary',
    on_click=transform()
)

# ---------------------------------------
