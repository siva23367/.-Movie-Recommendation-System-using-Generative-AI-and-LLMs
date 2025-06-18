import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Setup LLM
llm = ChatOpenAI(openai_api_key=api_key, model_name="gpt-3.5-turbo", temperature=0.8)

# Streamlit UI
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")
st.title("🎬 AI Movie Recommender")
st.markdown("Get personalized movie recommendations based on your mood or preferences!")

# Input from user
user_input = st.text_input("Tell me what you're in the mood for:")

if st.button("Recommend Movies"):
    if user_input.strip() == "":
        st.warning("Please enter a mood or preference.")
    else:
        with st.spinner("Thinking... 🎥"):
            prompt = f"""
            You are a helpful movie recommendation assistant. Based on the user's input, suggest 3 relevant movies.
            For each movie, include:
            - Title
            - Genre
            - Release year
            - A one-line reason why it's a good match

            User input: "{user_input}"
            """
            response = llm([HumanMessage(content=prompt)])
            st.success("Here are your movie picks:")
            st.markdown(response.content)
