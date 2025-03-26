import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key with error handling
try:
    OPENROUTER_BASE_URL = os.getenv('OPENROUTER_BASE_URL')
    OPENROUTER_APIKEY = os.getenv('OPENROUTER_APIKEY')
    if not OPENROUTER_BASE_URL:
        baseurl='https://api.openai.com/v1'
        OPENAI_APIKEY = os.getenv('OPENAI_APIKEY')
        if not OPENAI_APIKEY:
            st.error("API key not found in environment variables")
            st.stop()
        apikey=OPENAI_APIKEY
    else:
        baseurl=OPENROUTER_BASE_URL
        apikey=OPENROUTER_APIKEY
    if not OPENROUTER_APIKEY:
        st.error("API key not found in environment variables")
        st.stop()
except Exception as e:
    st.error(f"Error loading environment variables: {e}")
    st.stop()
# Set page title
st.title("AI Trip planner")

client = OpenAI(
    base_url=baseurl,
    api_key=apikey,
)

# Initialize messages if not present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("What is up?"):
    # Check if prompt is not empty
    if prompt.strip():
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate and display assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                stream = client.chat.completions.create(
                    model="meta-llama/llama-3.2-11b-vision-instruct:free",  # Using consistent model
                    messages=[
                        {
                            "role": "system",
                            "content": """
                                You are a highly knowledgeable and friendly travel planner AI designed to assist users with all their travel needs. Your goal is to provide personalized recommendations for destinations, activities, accommodations, and transportation based on the user's preferences, budget, and any other specific requirements they have. You have access to up-to-date travel information, weather forecasts, local events, and can make suggestions for both popular and hidden gem destinations.

                                Your responses should always be clear, concise, and tailored to the user's desires. If they are unsure about where they want to go, help guide them with questions to narrow down their options. Offer a variety of options for flights, hotels, activities, and itineraries, and ensure all suggestions fit within their budget and interests.

                                Always be friendly, patient, and proactive in helping users plan memorable, stress-free trips. If you are unsure about an answer, let the user know and offer to find more information.
                            """
                        },
                        *[
                            {"role": m["role"], "content": m["content"]} 
                            for m in st.session_state.messages
                        ]
                    ],
                    stream=True
                )
                
                # Handle streaming response
                for response in stream:
                    if hasattr(response.choices[0].delta, 'content') and response.choices[0].delta.content:
                        full_response += response.choices[0].delta.content
                        message_placeholder.markdown(full_response + "|")
                message_placeholder.markdown(full_response)
                
            except Exception as e:
                st.error(f"Error communicating with AI service: {e}")
                full_response = "Sorry, I encountered an error. Please try again."
                message_placeholder.markdown(full_response)
        
        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    else:
        with st.chat_message("assistant"):
            st.markdown("Please enter a valid message to continue the conversation!")