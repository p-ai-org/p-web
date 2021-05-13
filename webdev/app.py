import tensorflow.compat.v1 as tf
import gpt_2_simple as gpt2

from gpt_2_simple.src import model, sample, encoder, memory_saving_gradients
import os
import json
import numpy as np

from bs4 import BeautifulSoup
import random
import streamlit as st

tf.reset_default_graph()

st.title("P-Web S2021 Model Demo")

modelpath = "/Users/andyliu/Downloads/checkpoint/355_10mb"

#@st.cache(allow_output_mutation=True, suppress_st_warning=True)

def complete(pre, maxlength, classes):
    output = gpt2.generate(sess, include_prefix=True, prefix=pre, length=maxlength, model_name = modelpath, return_as_list=True)[0]
    html = pre + output
    soup = BeautifulSoup(html)
    if len(classes) > 0 and soup.find("div") is not None:
        for ele in soup.find("div"):
            ele['class'] = random.choice(classes)
    processed = soup.prettify()
    return(processed)

textbox = st.text_area('Start your HTML:', '', height=200, max_chars=256)
classes = st.text_area('Classes (optional, separated by commas):', '', height=50, max_chars = 128)
slider = st.slider('Max text length (in tokens)', 1, 128)
button = st.button('Generate')

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, model_name = modelpath)

if button:
    st.subheader("Generated HTML Template:")
    class_list = classes.split(',')
    output_text = complete(textbox, slider, class_list)
    for line in output_text.split('\n'):
        st.markdown(line)

    st.button('Download')



