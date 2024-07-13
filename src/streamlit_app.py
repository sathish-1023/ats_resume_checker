import streamlit as st
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pypdf import PdfReader
# Initialize CountVectorizer
cv = CountVectorizer()


    
# Streamlit app
def main():
    
    with st.sidebar:
        st.title("Smart ATS for Resume")
        st.subheader("About")
        st.write("This sophisticated ATS project, developed with sklearn Pro and Streamlit, seamlessly incorporates advanced features including resume percentage.")
        
        st.markdown("""
        - [Streamlit](https://streamlit.io/)
        - [Github](https://github.com/sathish_1023/ats_project) Repository         
        """)
        
        st.write("developed by sathish ( incredible developer ).")

    st.title("Resume Selection App")
    eliglity = st.number_input('enter Eligity percentage in Numbers')
    # Job description file
    job_desc=st.text_area('paste Job description : ')
    #job_desc_file = st.file_uploader("Upload Job Description (.docx)", type=["docx","pdf"])
    resume_file = st.file_uploader("Upload Resume (.docx, .pdf)", type=["docx","pdf"])
    resume=""
    if resume_file is not None and resume_file.type == "application/pdf":
        reader = PdfReader(resume_file)
        resume=""
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            resume += page.extract_text()

       # st.write("file is pdf")
    if job_desc and resume_file:
        # Extract text from uploaded files 
        #job_desc = docx2txt.process(job_desc_file)
        if resume_file.type !="application/pdf":
            resume = docx2txt.process(resume_file)
        # Combine the job description and resume texts
        texts = [job_desc, resume]
        #st.write(texts)
      
        #st.write(texts)
        # Convert the texts into a matrix of token counts
        matrix = cv.fit_transform(texts)
        
        # Calculate cosine similarity between the texts
        tracker = cosine_similarity(matrix)[0][1]
        st.write(tracker)
        # Print the similarity score
        similarity_score = round(tracker * 100, 2)
        st.write(f"Similarity Score: {similarity_score}%")
        
        # Determine if the resume is selected based on the similarity score
        if similarity_score > eliglity:
            st.header("Resume Selected")
        else:
            st.header("Resume Not Selected")

if __name__ == "__main__":
    main()
    