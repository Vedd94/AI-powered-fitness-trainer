import ai_trainer as at
import streamlit as st
import os
import tempfile
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables


st.title("Your AI powered fitness assistant")
st.write("Welcome, lets begin.....")



# st.image('https://tse3.mm.bing.net/th/id/OIP.rorikgO4OLLgPTxbqmX3NAHaEK?rs=1&pid=ImgDetMain&o=7&rm=3', width = 1000)
tab1, tab2 = st.tabs(["Fitness Trainer", "Chatbot"])

with tab1:
    
    col1, col2 = st.columns(2)

    with col1:
        workout = st.selectbox("Select what you are performing",['select', 'Bicep-Curl','Squats', 'Push-Ups'])
    with col2:
        camera_option = st.selectbox("Select your video type", ['select', 'Open-webcam', 'Upload video'])

    video_path = None
    if camera_option == "Upload video":
        uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
        if uploaded_file is not None:
            # Save uploaded file to a temp path
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
                temp_file.write(uploaded_file.read())
                video_path = temp_file.name 


    if st.button("Letss goo!!!"):
        para1 = video_path

        match workout:
            case 'Bicep-Curl':
                at.bicepCurls(para1)
            case 'Squats':
                at.squats(para1)
            case 'Push-Ups': 
                # st.write(str(para1))
                at.pushUps(para1)


with tab2:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    ## function to load Gemini Pro model and get repsonses
    model=genai.GenerativeModel("gemini-pro") 
    chat = model.start_chat(history=[])
    def get_gemini_response(question):
        
        response=chat.send_message(question,stream=True)
        return response

    ##initialize our streamlit app

    st.set_page_config(page_title="Q&A Demo")

    st.header("Gemini LLM Application")

    # Initialize session state for chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    input=st.text_input("Input: ",key="input")
    submit=st.button("Ask the question")

    if submit and input:
        response=get_gemini_response(input)
        # Add user query and response to session state chat history
        st.session_state['chat_history'].append(("You", input))
        st.subheader("The Response is")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))
    st.subheader("The Chat History is")
        
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")
    