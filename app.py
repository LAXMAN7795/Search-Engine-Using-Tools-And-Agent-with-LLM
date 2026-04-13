import streamlit as st
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain_groq import ChatGroq
from langchain.tools import Tool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ---------------- TOOLS ---------------- #

# Wikipedia Tool
api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

# DuckDuckGo Search Tool
search = DuckDuckGoSearchRun(name="Search")

# Arxiv Tool (SAFE WRAPPER to avoid 429 error)
api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)

def safe_arxiv(query):
    try:
        return api_wrapper_arxiv.run(query)
    except Exception:
        return "Arxiv is currently rate-limited. Please try again later."

arxiv = Tool(
    name="Arxiv",
    func=safe_arxiv,
    description="Search academic papers from Arxiv"
)

# ---------------- STREAMLIT UI ---------------- #

st.set_page_config(page_title="LangChain Chat with Search", page_icon="🔍")
st.title("🔍 LangChain Chat with Search")

st.sidebar.title("Settings")

# API Key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("⚠️ GROQ_API_KEY not found. Please set it in .env file.")
    st.stop()

# ---------------- CHAT MEMORY ---------------- #

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I am chatbot. How can I help you."}
    ]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

# ---------------- USER INPUT ---------------- #

if prompt := st.chat_input("Ask something..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # LLM
    llm = ChatGroq(
        groq_api_key=api_key,
        model="llama-3.3-70b-versatile"
    )

    # Tools
    tools = [search, wiki, arxiv]

    # Agent
    search_agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True
    )

    # Response
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)

        try:
            response = search_agent.run(prompt, callbacks=[st_cb])
        except Exception as e:
            response = "⚠️ Something went wrong. Please try again."

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
