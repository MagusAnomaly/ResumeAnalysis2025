import google.generativeai as genai
from pdf import read_pdf
import streamlit as st
import os

genai.configure(api_key=os.getenv('GOOGLE-GEMINI-API'))
model = genai.GenerativeModel("gemini-2.0-flash")

def profile(resume, job_desc):
    if resume is not None:
        resume_doc = read_pdf(resume)
        st.markdown("Resume has been Uploaded")
    else:
        st.warning('Resume Missing')
        return

    response = model.generate_content(
        f"Act as a HR or Ops Head and analyse the resume:\n{resume_doc}\nwith the job description:\n{job_desc}\n and tell me am I a good fit."
    )

    st.write(response.text)
