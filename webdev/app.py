import tensorflow.compat.v1 as tf
import gpt_2_simple as gpt2

from gpt_2_simple.src import model, sample, encoder, memory_saving_gradients
import os
import json
import numpy as np

from bs4 import BeautifulSoup
import streamlit as st

tf.reset_default_graph()

st.title("P-Web S2021 Model Demo")

modelpath = "/Users/andyliu/Downloads/checkpoint/355_10mb"

#@st.cache(allow_output_mutation=True, suppress_st_warning=True)

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, model_name = modelpath)


def complete(pre, ml):
    output = gpt2.generate(sess, include_prefix=True, prefix=pre, length=ml, model_name = modelpath, return_as_list=True)[0]
    html = pre + output
    #you would add in classes here
    soup = BeautifulSoup(html)
    processed = soup.prettify()
    return(processed)

textbox = st.text_area('Start your HTML:', '', height=200, max_chars=256)
button = st.button('Generate')

slider = st.slider('Max text length (in tokens)', 16, 512)

st.subheader("Generated HTML Template:")

if button:
    output_text = complete(textbox, slider)
    for line in output_text.split('\n'):
        st.markdown(line)

st.button('Download')



