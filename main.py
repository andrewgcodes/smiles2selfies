import re
import time
import json
import os
import selfies
import streamlit as st
import pandas as pd
import selfies as sf

st.set_page_config(page_title='Smiles2Selfies',
                   layout="centered",
                   initial_sidebar_state='auto')

st.title("Smiles2Selfies")
st.write(
    "Upload a CSV file with one column of SMILES and no header, i.e. 'Smiles'. One SMILES per line/cell."
)
st.write(
    "[Example file](https://drive.google.com/file/d/1UeiTqKxnO5BRjxVasqIpSr1BPaySJgRr/view?usp=sharing)"
)
uploaded_file = st.file_uploader("Choose a file")
if (st.button("Load example file")):
    uploaded_file = 'smilesfile.csv'
if (st.button("Convert")):
    if (uploaded_file is None):
        uploaded_file = 'smilesfile.csv'
    df = pd.read_csv(uploaded_file)
    df.columns = ['SMILES']
    df['SELFIES'] = ""
    for i in range(len(df)):
        try:
            selfiesFormat = sf.encoder(df['SMILES'][i])
            df['SELFIES'][i] = selfiesFormat
        except sf.EncoderError:
            df['SELFIES'][i] = "FAILED_TO_CONVERT"
            pass  # sf.encoder error!
    st.write("First 10 rows:")
    st.dataframe(df.head(10))
    df2 = df.to_csv()
    st.download_button(
        label="Download data as CSV",
        data=df2,
        file_name='smiles2selfies_df.csv',
        mime='text/csv',
    )
