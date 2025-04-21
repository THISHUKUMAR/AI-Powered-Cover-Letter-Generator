# import streamlit as st
# import pdfplumber
# from cover_letter_generator import generate_cover_letter
# import tempfile
# import os

# def load_pdf_text(file):
#     with pdfplumber.open(file) as pdf:
#         text = ""
#         for page in pdf.pages:
#             text += page.extract_text() or ""
#     return text

# st.set_page_config(page_title="AI Cover Letter Generator", page_icon="📄", layout="centered")

# st.markdown("""
#     <style>
#         .main {
#             background-color: #f0f2f6;
#         }
#         .block-container {
#             padding-top: 2rem;
#             padding-bottom: 2rem;
#         }
#         .stButton > button {
#             background-color: #4CAF50;
#             color: white;
#             font-weight: bold;
#             border-radius: 8px;
#             padding: 0.5rem 1rem;
#         }
#     </style>
# """, unsafe_allow_html=True)

# st.title("📄 AI-Powered Cover Letter Generator")
# st.write("Upload your **resume** and **job description** PDFs to generate a personalized cover letter.")

# resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
# jd_file = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])

# if resume_file and jd_file:
#     if st.button("✨ Generate Cover Letter"):
#         with st.spinner("Generating your cover letter..."):
#             resume_text = load_pdf_text(resume_file)
#             jd_text = load_pdf_text(jd_file)
#             cover_letter = generate_cover_letter(resume_text, jd_text)

#         st.success("✅ Cover letter generated successfully!")
#         st.text_area("Generated Cover Letter", cover_letter, height=300)

#         # Provide a download button
#         tmp_file_path = os.path.join(tempfile.gettempdir(), "cover_letter.txt")
#         with open(tmp_file_path, "w", encoding="utf-8") as f:
#             f.write(cover_letter)

#         with open(tmp_file_path, "rb") as f:
#             st.download_button(
#                 label="📥 Download Cover Letter",
#                 data=f,
#                 file_name="cover_letter.txt",
#                 mime="text/plain"
#             )
# else:
#     st.warning("Please upload both your resume and job description PDFs.")

import streamlit as st
import pdfplumber
from cover_letter_generator import generate_cover_letter
import base64

# Page config
st.set_page_config(page_title="Cover Letter Generator", layout="centered")

# Custom styling
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        font-size: 16px;
        color: #333;
    }
    .main {
        background-color: #f9f9f9;
        padding: 2rem;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📝 AI-Powered Cover Letter Generator")
st.write("Upload your **Resume** and **Job Description** to get a tailored cover letter.")

# Upload section
resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
jd_file = st.file_uploader("🧾 Upload Job Description (PDF)", type=["pdf"])

def load_pdf_text(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])

# Generate section
if resume_file and jd_file:
    if st.button("🚀 Generate Cover Letter"):
        with st.spinner("Generating your personalized cover letter..."):
            resume_text = load_pdf_text(resume_file)
            jd_text = load_pdf_text(jd_file)
            output = generate_cover_letter(resume_text, jd_text)
            cover_letter = output.get("output_text", "")

        if cover_letter:
            st.success("✅ Cover Letter Generated!")
            st.subheader("📄 Your Cover Letter:")
            st.text_area("Preview", cover_letter, height=300)

            # Downloadable link
            b64 = base64.b64encode(cover_letter.encode()).decode()
            href = f'<a href="data:file/txt;base64,{b64}" download="cover_letter.txt">📥 Download Cover Letter</a>'
            st.markdown(href, unsafe_allow_html=True)
else:
    st.info("Please upload both Resume and Job Description PDFs.")

