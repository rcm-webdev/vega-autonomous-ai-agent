from langchain.schema import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import random
import pandas as pd

# Load environment variables from .env file
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

# you can use whaterver model you want.
llm_name = os.getenv("MODEL_CHOICE", "")
model = ChatOpenAI(api_key=openai_key, model=llm_name)

# read the csv file using pandas
df = pd.read_csv('data/hot_wheels.csv').fillna(value=0)

# verify that csv file is being read.
# print(df.head(15))