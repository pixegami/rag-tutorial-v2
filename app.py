
import streamlit as st
import os
import tempfile
from populate_database import ingest_file, clear_database
from query_data import query_rag

# Minimalistic page config
st.set_page_config(
    page_title="RAG Chat",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for minimalistic design
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 1rem;
        max-width: 700px;
    }
    
    /* Chat message styling */
    .chat-message {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        border-left: 3px solid #e0e0e0;
    }
    
    .user-message {
        background-color: #f8f9fa;
       
    }
    
    .assistant-message {
        background-color: #ffffff;
        border-left-color: #28a745;
        border: 1px solid #e9ecef;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
   
        border: 1px solid #e0e0e0;
        padding: 0.5rem 1rem;
      
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 20px;
        border: none;
        background-color: #007bff;
        color: white;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #0056b3;
        transform: translateY(-1px);
    }
    
    /* Upload area styling */
    .upload-section {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px dashed #e0e0e0;
        text-align: center;
        margin: 1rem 0;
    }
    
    /* Hide upload section when not needed */
    .minimize-upload {
        padding: 0.5rem;
        background-color: transparent;
        border: 1px solid #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'show_upload' not in st.session_state:
    st.session_state['show_upload'] = True

# App title - minimalistic
st.markdown("<h1 style='text-align: center; color: #333; font-weight: 300; margin-bottom: 2rem;'>💬 RAG Chat</h1>", unsafe_allow_html=True)

# Toggle upload section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("📄 " + ("Hide Upload" if st.session_state['show_upload'] else "Add Document"), 
                 use_container_width=True, type="secondary"):
        st.session_state['show_upload'] = not st.session_state['show_upload']

# Upload section - collapsible
if st.session_state['show_upload']:
    with st.container():
        st.markdown('<div class="upload-section">', unsafe_allow_html=True)
        st.markdown("##### 📄 Upload PDF Document")
        uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")
        
        if uploaded_file is not None:
            temp_dir = tempfile.gettempdir()
            file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            with st.spinner("Processing document..."):
                result = ingest_file(file_path)
            st.success(f"✅ {uploaded_file.name} added successfully")
            # Auto-hide upload section after successful upload
            st.session_state['show_upload'] = False
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

# Chat Interface
st.markdown("---")

# Chat input at the bottom
with st.form(key="chat_form", clear_on_submit=True):
    col1, col2 = st.columns([4, 1])
    with col1:
        user_input = st.text_input("", placeholder="Ask a question about your documents...", label_visibility="collapsed")
    with col2:
        submit_button = st.form_submit_button("Send", use_container_width=True)

if submit_button and user_input:
    with st.spinner("Thinking..."):
        try:
            answer = query_rag(user_input)
        except Exception as e:
            answer = f"I encountered an error: {str(e)}"
    
    st.session_state['chat_history'].append((user_input, answer))
    st.rerun()

# Display chat history with minimalistic design
if st.session_state['chat_history']:
    st.markdown("### Conversation")
    
    # Reverse order to show latest messages first
    for i, (question, answer) in enumerate(reversed(st.session_state['chat_history'])):
        # User message
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>You:</strong> {question}
        </div>
        """, unsafe_allow_html=True)
        
        # Assistant message
        st.markdown(f"""
        <div class="chat-message assistant-message">
            <strong>Assistant:</strong> {answer}
        </div>
        """, unsafe_allow_html=True)
        
        if i < len(st.session_state['chat_history']) - 1:
            st.markdown("<br>", unsafe_allow_html=True)

# Settings in sidebar for advanced users
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state['chat_history'] = []
        st.rerun()
    
    st.markdown("---")
    
    if st.button("�️ Clear Database", use_container_width=True, type="secondary"):
        with st.spinner("Clearing database..."):
            clear_database()
            st.session_state['chat_history'] = []
        st.success("Database cleared!")
        st.rerun()
    
    st.markdown("---")
    st.markdown("*Made with Streamlit*")
