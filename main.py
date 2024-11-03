import streamlit as st
from scrape import extract_data, chunkify, CONTEXT_LENGTH
from parse import parse_with_llm


st.title("Web Scraper")
url = st.text_input("Enter a URL")

if st.button("Scrape URL"):
    if not url.startswith("https://"):
        url = "https://" + url
    st.write("Scraping URL:", url)

    result = extract_data(url)
    st.session_state.dom_context = result

    with st.expander("Show Content"):
        st.text_area("Content", result, height=300)

if 'dom_context' in st.session_state:
    parse_description = st.text_area('Describe what you want from the content', height=100)

    if st.button('Parse Content'):
        if parse_description:
            st.write('Parsing content...')

            chunks = chunkify(st.session_state.dom_context, CONTEXT_LENGTH)

            st.write(parse_with_llm(chunks, parse_description))
