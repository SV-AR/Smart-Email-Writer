import streamlit as st
import google.generativeai as gen
gen.configure(api_key = "YOUR API KEY")
model = gen.GenerativeModel("gemini-2.5-flash")
prompt = st.text_input("Answer any questions asked by the user")
if st.button("Submit"):
    res = model.generate_content(prompt+"you are a smart email writer.write or replay to email with tone adjustment and quick replies")
    st.write(res.text)