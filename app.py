import streamlit as st
import module
import pages.home
import pages.data
#import SessionState

st.set_page_config(layout="wide", page_icon="🇬🇧", page_title="British island")

#session_state = SessionState.get(checkboxed=False)

PAGES = {
	"home": pages.home,
	"data": pages.data
}

with st.sidebar:
	selection = st.radio("Go to", list(PAGES.keys()))
	page = PAGES[selection]

page.app()
