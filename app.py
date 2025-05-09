from dotenv import load_dotenv
load_dotenv() # activate the local env vars

import streamlit as st
import google.generativeai as genai

from pdf import read_pdf
from analysis import profile

# Create the front end...
st.header(":blue[Resume Analysis] Using AI",divider='green')
st.subheader('Tips for using the application')

st.sidebar.subheader('Upload the  resume')
resume = st.sidebar.file_uploader('',type=['pdf'])

st.balloons()
st.snow()

notes = f'''
* **Resume**: Please upload your resume.
* **Job Description**: Copy paste the job description from your sources.
* Let the AI do the magic for you !'''
st.write(notes)

# Job Desc
st.subheader("Enter the job description ",divider=True)
job_desc = st.text_area(label='',max_chars=10000)

button = st.button(label='Get Ai Powered Insights')
if button:
    st.markdown(profile(resume=resume,job_desc=job_desc))
    

