import os
from dotenv import load_dotenv
from agents import Agent,Runner , AsyncOpenAI ,RunConfig, OpenAIChatCompletionsModel

# Load .env file and get API Key / This will load variables from .env file

load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# Check Key Exists

if not openrouter_api_key:
        raise ValueError('OPENROUTER_API_KEY is not found. Please set API_KEY')


# ✅ Important: Tell OpenAI client to use that key
# os.environ["OPENAI_API_KEY"] = openrouter_api_key  # <- required by `openai-python`
        
# Set Openrouter Client

external_client = AsyncOpenAI(
    api_key = openrouter_api_key, 
    base_url = 'https://openrouter.ai/api/v1',
    timeout=60 # Seconds
   )

# Choose any OpenRouter-Supported model

model = OpenAIChatCompletionsModel(
        model = "deepseek/deepseek-r1-0528-qwen3-8b:free",
        openai_client= external_client,
    )

# Setup Config

config = RunConfig(
        model = model,
        model_provider  = external_client,
        tracing_disabled= True
    )

# Define Agent 

agent = Agent(
        name = 'Writer gent',
        instructions= 'You are a Writer Agent.Write Story , Essay , Poems and etc'  
    )

# Input and Run Agent 

response = Runner.run_sync(
        agent,
        input = 'Write an essay on Problems of Karachi.',
        run_config= config
    )


# Output

print(response.final_output)