import streamlit as st
from bs4 import BeautifulSoup
import requests
st.markdown("<h1 style='text-align:center;'>Youtube Keyword Extractor</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Enter Youtube URL</h3>", unsafe_allow_html=True)
url=st.text_input(' Youtube URL')
if url:
    page = requests.get(url)
    soup=BeautifulSoup(page.content, 'lxml')
    meta_tag=soup.select("meta(name='keywords')")
    tit=soup.find('title')
    keywords=print(meta_tag[0]["content"])
    st.title("title")
    st.markdown(f"<h5 style='text-align:center;color:lightblue;'>[tit]</h5>", unsafe_allow_html=True)
    st.title("Tags")
    st.markdown(f"<h5 style='text-align:center;color:lightblue;'>)[keywords]</h5>", unsafe_allow_html=True)

