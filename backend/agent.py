import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

df = pd.read_csv("backend/titanic_dataset.csv")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # or "gemini-2.0-flash"
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0
)


agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True )