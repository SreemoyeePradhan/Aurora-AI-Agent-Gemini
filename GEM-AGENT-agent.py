import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env
load_dotenv()

# Check if API key is loaded
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in .env file.")

# Initialize Gemini 2.5 Pro model
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-pro",
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Set up prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}")
])

# Chain components together
chain = prompt | llm | StrOutputParser()

# REPL interface
print("🤖 Gemini Agent Ready! Type 'quit' to exit.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ("quit", "exit"):
        print("Goodbye!")
        break
    response = chain.invoke({"input": user_input})
    print(f"AI: {response}\n")
