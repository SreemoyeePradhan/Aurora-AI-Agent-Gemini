## Aurora-AI-Agent-Gemini
A lightweight AI-powered assistant built with Python and Streamlit, supporting real-time response streaming. Integrates LLMs like Gemini for intelligent task handling, conversational flow, and interactive user experience. Ideal for personal productivity and experimentation.
# 🧠 AI Agentic Assistant (Gemini 2.5 Pro + Streamlit)
This project is a web-based intelligent assistant powered by Google’s Gemini 2.5 Pro model. It leverages LangChain’s agentic capabilities to enable a responsive and interactive experience for end users. Designed for experimentation, this assistant can carry out conversational tasks, respond intelligently to inputs, and stream responses in real time through a user-friendly web interface built with Streamlit.

The key utility of this project lies in its ability to combine large language model (LLM) reasoning with agent workflows. It uses LangChain’s create_react_agent to manage the interaction logic and allows for future expansion with custom tools and memory integration. Gemini’s capabilities ensure high-quality language understanding, while the agentic system interprets and acts on queries step-by-step.

The assistant’s responses are streamed, not just statically displayed. That means users get a token-by-token visible typing effect, creating a natural conversational feel. This is particularly useful in real-time applications like personal assistants, chatbots, and AI companions.

Technologies used in this project include Python, LangChain, and Streamlit. The backend logic is handled in agent.py, where Gemini 2.5 Pro is integrated through the google.generativeai package. The frontend (app.py) uses Streamlit to capture user input and display streamed responses live. Configuration and sensitive data, such as your API key, are managed securely using dotenv.

To get started, users simply need to clone the repository, set up a Python virtual environment, install dependencies, and run the Streamlit app. The only configuration needed is adding your Gemini API key in a .env file as GOOGLE_API_KEY. The application is fully functional and renders locally in your browser at http://localhost:8501.

We plan to extend the assistant with memory support for context-aware responses, add custom tools (e.g., file handling, search), support multilingual conversations, and include a model switcher that lets users choose between different LLM providers like OpenAI, Gemini, and Claude.

The project currently uses Google Generative AI’s Gemini 2.5 Pro model. The API key must be obtained from Google AI Studio, and the model name in use is "models/gemini-2.5-pro". This ensures users get access to one of the most capable language models available publicly.

Overall, this assistant serves as a foundation for building smarter, more extensible AI-driven applications. Whether for personal productivity, educational use, or as a chatbot base, the modular structure allows for easy enhancements and experimentation. The entire project is free to use and modify for educational or research purposes
