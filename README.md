#📌 LangChain Search Agent — Streamlit App

This project is a conversational search-powered chatbot built with LangChain, Groq Llama 3.3, DuckDuckGo, Wikipedia, and ArXiv tools.
Users can chat with the assistant and get real-time search results from the web and scientific databases.

🚀 Features

✅ Conversational chatbot interface
✅ Uses Groq LLM for fast responses
✅ Integrates three external information sources:

🔍 DuckDuckGo Search

📚 Wikipedia

📄 ArXiv Research Papers

✅ Friendly UI with Streamlit
✅ Maintains full chat history

🧰 Tech Stack
Technology	Usage
Streamlit	UI & Chat Interface
LangChain	Agent + Tool Management
Groq Llama3.3	Response generation
Wikipedia API	Factual lookup
Arxiv API	Research lookup
DuckDuckGo	Web search
📦 Installation

Clone the repository:

git clone https://github.com/your-username/your-repo.git
cd your-repo


Create and activate virtual environment:

python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  (Mac/Linux)


Install dependencies:

pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the project root:

HUGGINGFACE_API_KEY=your_huggingface_key
GROQ_API_KEY=your_groq_key


✅ API keys must be valid or the app won't run.

▶️ Run the App
streamlit run app.py


✅ Open the browser — Streamlit UI will appear!
Enter Groq API key in sidebar → Start chatting with the bot 💬

📌 Sample Conversation

User: What is Machine Learning?
Bot: Machine learning is a branch of artificial intelligence where systems learn…

📁 Project Structure
📂 Langchain_Search_App
 ├── app.py
 ├── requirements.txt
 ├── .env (Not in Git — Sensitive)
 ├── README.md

🔒 Security Notes

✅ .env should not be pushed to GitHub
✅ API keys must remain private
✅ Add to .gitignore:

.env
venv/
__pycache__/

🙌 Author

👤 Laxman Sannu Gouda
📧 laxman.sg0104@gmail.com
