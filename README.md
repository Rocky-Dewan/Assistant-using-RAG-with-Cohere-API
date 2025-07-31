# Assistant-using-RAG-with-Cohere-API
📌 Project Description:
This project implements a Retrieval-Augmented Generation (RAG) pipeline using the LangChain framework and Cohere API. It allows users to ask questions about real estate properties (e.g., "What is the rental yield of Greenview Estate?"), and answers are generated based on document data stored in a local directory.

The system works by:

Loading local .txt documents

Splitting them into chunks

Embedding them using Cohere's embedding model

Storing them in a FAISS vector database

Retrieving relevant chunks based on a user's query

Generating answers using Cohere's command-r LLM

🛠️ Tech Stack:
Component	Tool
Embedding Model	CohereEmbeddings (command-r)
Vector Store	FAISS
Framework	LangChain
Language	Python 3.13
API Key Management	.env + dotenv
Dependencies	langchain, cohere, langchain-cohere, faiss-cpu, etc.

🚀 How to Set Up and Run the Project
✅ Step-by-Step Instructions:
Clone or Prepare Your Project Directory

Create folder rag_pipeline

Add your .txt documents inside a data/ folder

Create a .env file

env
Edit
COHERE_API_KEY=your_api_key_here
Install Required Dependencies

bash
Edit
pip install langchain langchain-cohere faiss-cpu cohere python-dotenv
Your rag_pipeline.py Should Look Like:


Run the Script:

bash
python rag_pipeline.py
Ask Questions!

Example: "What is the expected ROI of Riverside Apartments?"
In my time Output look like:

<img width="897" height="465" alt="image" src="https://github.com/user-attachments/assets/0073a458-3d84-4a9f-812f-de01dd5fd7d2" />


🧩 Problems I Faced & How I Solved Them
Problem	Solution
❌ Used OpenAI API by default	✅ Switched to Cohere embeddings and LLM
❌ Used deprecated imports from langchain	✅ Updated to langchain_community and langchain_cohere
❌ Forgot to pass required model param to CohereEmbeddings	✅ Passed model="embed-english-v3.0"
❌ Used invalid LLM model "xlarge"	✅ Changed to "command-r"
❌ Used deprecated .run() method	✅ Replaced with .invoke()
❌ Chat model import errors	✅ Installed correct version of cohere, langchain-cohere

📄 Summary for Assessment Report
This RAG-based AI assistant uses LangChain and Cohere to answer natural language questions from a vectorized knowledge base. Documents are embedded, stored in FAISS, and queried using Cohere's chat LLM. The system was debugged by resolving deprecations, ensuring proper model usage, and upgrading dependencies.
