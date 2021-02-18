import streamlit as st
import module

def app():
	st.markdown("""
	# Vocabulary learning tool
	We gather weekly data here  
	=> you discovered a new word ?  
	=> you found a new expression ?  
	=> or a new gramatical rule ?  
	=> or something else you wanna write ?  
	""")

	refresh = ""

	save = st.button("Save")

	if save: 
		refresh = "blank"

	word = st.text_input("New word")

	if save:
		data = {}
		if word != "":
			_id = module.insertWord(word)
			msg = "Word saved" if _id else "Error"
			st.write(msg)
		else:
			st.write("Please write a word first")

