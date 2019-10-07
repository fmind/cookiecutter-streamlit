#!/usr/bin/env python3

"""Documentation of the app."""

import numpy as np
import pandas as pd
import streamlit as st

df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'],
)

st.title('My Title')

st.header('My Header')

st.subheader('My Chart')

threshold = st.sidebar.selectbox(
    'Threshold on 1st column',
     df['a'],
)

st.line_chart(df[df['a'] >= threshold])
