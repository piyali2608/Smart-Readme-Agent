import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_agent_response(user_input, api_key, history, folder_context):
    # Use Gemini 2.5 Flash for advanced reasoning and large context
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        google_api_key=api_key,
        temperature=0.2
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are Gemini, a Senior Technical Architect. Analyze this project structure and files:\n\n{folder_context}"),
        *history,
        ("human", "{user_input}")
    ])
    
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"user_input": user_input})