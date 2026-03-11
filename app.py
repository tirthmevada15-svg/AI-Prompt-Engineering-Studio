import streamlit as st
from prompt_engine import generate_magic_prompt, improve_prompt, analyze_prompt
from pdf_export import create_pdf
from templates import templates

st.set_page_config(page_title="AI Prompt Engineering Studio",layout="wide")

st.markdown("""
<style>

.stApp{
background: radial-gradient(circle,#020617,#0f172a);
color:white;
}

.neon-title{
text-align:center;
font-size:42px;
color:#00e5ff;
text-shadow:0 0 15px #00e5ff;
}

.glass-card{
background:rgba(255,255,255,0.05);
padding:25px;
border-radius:15px;
border:1px solid rgba(255,255,255,0.15);
margin-bottom:20px;
}

.stButton>button{
background:linear-gradient(90deg,#00f5ff,#7c3aed);
border:none;
border-radius:8px;
color:white;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="neon-title">AI Prompt Engineering Studio</div>',unsafe_allow_html=True)

st.sidebar.title("AI Tools")

menu = st.sidebar.radio(
"Navigation",
[
"Prompt Generator",
"Prompt Improver",
"Prompt Analyzer",
"Prompt Library"
]
)

if menu=="Prompt Generator":

    col1,col2=st.columns(2)

    with col1:
        st.markdown('<div class="glass-card">',unsafe_allow_html=True)

        title=st.text_input("Enter Title")

        if st.button("Generate Prompt"):

            with st.spinner("Generating..."):
                result=generate_magic_prompt(title)

            st.session_state["result"]=result

        st.markdown('</div>',unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">',unsafe_allow_html=True)

        if "result" in st.session_state:

            st.code(st.session_state["result"])

            pdf=create_pdf(st.session_state["result"])

            with open(pdf,"rb") as f:

                st.download_button("Download PDF",f,"prompt.pdf")

        st.markdown('</div>',unsafe_allow_html=True)

elif menu=="Prompt Improver":

    prompt=st.text_area("Enter prompt")

    if st.button("Improve Prompt"):

        result=improve_prompt(prompt)

        st.code(result)

elif menu=="Prompt Analyzer":

    prompt=st.text_area("Enter prompt")

    if st.button("Analyze Prompt"):

        result=analyze_prompt(prompt)

        st.write(result)

elif menu=="Prompt Library":

    category=st.selectbox("Category",list(templates.keys()))

    for p in templates[category]:
        st.markdown(f"- {p}")

st.markdown("### Created by Tirth Mevada")