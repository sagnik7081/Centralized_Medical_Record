from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

def summarize_text(text, api_key):
    llm = ChatGroq(api_key=api_key, model_name="llama-3.3-70b-versatile")  # or another Groq-supported model
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following medical report in plain language for a patient:\n\n{text}"
    )
    docs = [Document(page_content=text)]
    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
    result = chain.run(docs)
    return result
