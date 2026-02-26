import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dotenv import load_dotenv
load_dotenv()

st.title("🚢 Titanic Insight Bot")
st.markdown("Ask me anything about the Titanic passengers!")

query = st.text_input("Example: What was the survival rate of females?")

if st.button("Analyze"):
    if query:
        # 1. Get Text Answer from Backend using POST
        try:
            # We send a JSON object with the key "question" to match the Pydantic model
            payload = {"question": query}
            response = requests.post(f"{os.getenv('BASE_API_URL')}/ask", json=payload)
            
            if response.status_code == 200:
                result = response.json()
                st.write(result["response"])
            else:
                st.error(f"Error: Backend returned status code {response.status_code}")
        except Exception as e:
            st.error(f"Could not connect to backend: {e}")
        
        # 2. Logic for Visualizations
        if "histogram" in query.lower() or "show me" in query.lower() or "plot" in query.lower():
            st.subheader("Visual Insight")
            # Load data (Ensure titanic.csv is in your project root or backend folder)
            try:
                df = pd.read_csv("titanic.csv") 
                fig, ax = plt.subplots()
                
                if "age" in query.lower():
                    sns.histplot(df['Age'].dropna(), kde=True, ax=ax, color="skyblue")
                    st.pyplot(fig)
                elif "survival" in query.lower() or "survived" in query.lower():
                    sns.countplot(data=df, x='Survived', ax=ax, palette="viridis")
                    st.pyplot(fig)
            except FileNotFoundError:
                st.warning("Titanic.csv not found. Please ensure the file is in the correct directory.")