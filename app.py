from dotenv import load_dotenv
load_dotenv() #load all the env variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#Configure API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#Fuction to Load Google Gemini Model that provide SQL Query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])

    return response.text

#Function to retrieve query from SQL database
def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    
    return rows

#Defining Prompt 
prompt = [
    '''
        Imagine you are an expert in converting natural language text into SQL queries. You have a table named e_com with the following columns:

user_id (INTEGER): The unique identifier for each user, automatically incremented.
username (VARCHAR(50)): The name of the user, required and cannot be null.
email (VARCHAR(100)): The email address of the user, also required and cannot be null.
address (VARCHAR(255)): The address of the user.
order_quantity (VARCHAR(255)): The quantity of orders placed by the user.
order_date (TIMESTAMP): The date and time of when the order was placed, with a default value set to the current timestamp.
Your task is to convert the natural language descriptions into SQL queries that operate on the E_COM_DATA table.

EXAMPLES - 

Tell me the usernames and email addresses of all users whose order quantity is greater than 3.
Expected Response - SELECT username, email FROM e_com WHERE order_quantity > '3';


Tell me the usernames and addresses of users who have placed orders after a specific date, say '2023-01-01'.
Expected Response - SELECT username, address FROM e_com WHERE order_date > '2023-01-01';


ALSO, the sql response should not have ``` in the beginning or end and sql word in the output.

'''
]

#StreamLit App

st.set_page_config(page_title = "Hey! I can retriece any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question,prompt)
    print(response)

    data = read_sql_query(response, "e_com.db")
    st.subheader("The Response is ")

    for row in data:
        print(row)
        st.header(row)