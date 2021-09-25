import streamlit as st
import numpy as np
import pandas as pd
import time

DATA_COLUMN = 'date/time'
DATA_URL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('loading data...')
data = load_data(10000)
data_load_state.text('done!')

data