import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.callbacks import StreamlitCallbackHandler
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq


st.set_page_config(page_title="LangChain: Chat with SQL DB")
st.title("LangChain: Chat with SQL DB")

LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"

radio_opt = ["Use SQLite3 Database- student.db", "Connect To Your SQL Database"]
selected_opt = st.sidebar.radio(label="Choose the DB which you want to Chat", options=radio_opt)


if radio_opt.index(selected_opt)==1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("Provide mySQL Host")
    mysql_user = st.sidebar.text_input("Provide mySQL username")
    mysql_password = st.sidebar.text_input("Provide mySQL password", type="password")
    mysql_db = st.sidebar.text_input("Provide mySQL db")

else:
    db_uri= LOCALDB


api_key = st.sidebar.text_input(label="GRoq API Key", type="password")


if not db_uri:
    st.info("Please enter the Database informations")
if not api_key:
    st.info("Please provide the GRoq API Key")

## LLM Model

llm = ChatGroq(api_key=api_key, model_name = "Llama3-8-8192", streaming=True)
