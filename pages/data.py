import streamlit as st 
import pandas as pd
import module


def app():
	col1, col2 = st.beta_columns((1, 1))
	with col1:
		col1.write("data page")
		words = module.getAllWords()
		df = pd.DataFrame(words)
		col1.write(df)

	with col2:
		wordToDelete = st.text_input("Delete word")
		if st.button("Delete"):
			res = deleteWord(wordToDelete)
			msg = st.success("Word deleted") if res else st.error("Word not deleted")

def deleteWord(word):
	deletedCount = module.deleteWord(word)
	return deletedCount