import os
from dotenv import load_dotenv
from agents import Agent,Runner , AsyncOpenAI , OpenAIChatCompletionsModel

# Load .env file and get API Key
load_dotenv()