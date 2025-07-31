import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_cohere import CohereEmbeddings
from langchain_cohere.chat_models import ChatCohere

from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA

load_dotenv()

def load_docs(directory):
    docs = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            loader = TextLoader(os.path.join(directory, filename))
            docs.extend(loader.load())
    return docs

def create_vector_store(docs):
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = splitter.split_documents(docs)
    embeddings = CohereEmbeddings(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    model="embed-english-v3.0"
   )

    vectorstore = FAISS.from_documents(split_docs, embeddings)
    return vectorstore

def build_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    llm = ChatCohere(cohere_api_key=os.getenv("COHERE_API_KEY"), model="command-r")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain


if __name__ == "__main__":
    docs = load_docs("data")
    vectorstore = create_vector_store(docs)
    qa = build_qa_chain(vectorstore)

    while True:
        query = input("\nAsk your property-related question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        answer = qa.invoke(query)
        print("\n🔍 Answer:", answer)
