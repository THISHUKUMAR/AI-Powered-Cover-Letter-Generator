# cover_letter_generator.py
# cover_letter_generator.py

from langchain.chains import StuffDocumentsChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import Document

GEMINI_API_KEY = "AIzaSyB8mDOGyq4kfn5Re2zjygDTqyygxV3uWUg"

def generate_cover_letter(resume_data, jd_data):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=GEMINI_API_KEY
    )

    prompt_template = PromptTemplate(
        input_variables=["context"],
        template="""You are a professional career assistant. Based on the following combined content (resume and job description),
                    write a highly personalized and compelling cover letter.

                    Guidelines:
                    - Address the hiring manager (use "Dear Hiring Manager").
                    - Highlight relevant skills, experience, and achievements.
                    - Be concise (max 350 words).
                    - Use a professional and confident tone.

                    Content:
                    {context}

                    Output:
                    [Start your cover letter below]
                    """
    )

    llm_chain = LLMChain(llm=llm, prompt=prompt_template)

    resume_doc = Document(page_content=resume_data)
    jd_doc = Document(page_content=jd_data)

    chain = StuffDocumentsChain(llm_chain=llm_chain)
    combined_docs = [resume_doc, jd_doc]

    result = chain.invoke({"input_documents": combined_docs})
    
    return result['output_text']  # For compatibility with different return for
