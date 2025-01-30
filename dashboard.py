import os  
import openai  
import pandas as pd  
import streamlit as st  
import matplotlib.pyplot as plt  
import matplotlib.font_manager as fm  
from dotenv import load_dotenv  

# Load environment variables from .env file  
load_dotenv()  

# Set your OpenAI API key from the environment variable  
openai.api_key = os.getenv("OPENAI_API_KEY")  

# Check if the API key is set  
if not openai.api_key:  
    st.error("OpenAI API key is not set. Please configure it as an environment variable.")  

# Load Custom Font  
font_path = '/mnt/data/file-ngwyeoEN29l1M3O1QpdxCwkj'  
font_prop = fm.FontProperties(fname=font_path)  

# Title  
st.title("Centralized Agency Dashboard")  

# Sections  
st.header("AI Agents")  
st.write("Manage your AI agents here.")  

# AI Interaction  
st.header("Ask the AI")  
user_input = st.text_input("What would you like to ask the AI?")  
if st.button("Get Response"):  
    if user_input:  
        try:  
            response = openai.ChatCompletion.create(  
                model="gpt-4",  
                messages=[  
                    {"role": "system", "content": "You are a helpful assistant."},  
                    {"role": "user", "content": user_input}  
                ],  
                max_tokens=100  
            )  
            # Display the AI's response  
            st.write("AI Response:")  
            st.write(response['choices'][0]['message']['content'].strip())  
        except Exception as e:  
            st.error(f"An error occurred: {e}")  
    else:  
        st.write("Please enter a question.")  

# Sample data for visualization  
data = pd.DataFrame({  
    'Month': ['January', 'February', 'March', 'April'],  
    'Sales': [200, 300, 400, 500]  
})  

# Sales Chart  
st.header("Sales Chart")  
plt.figure(figsize=(8, 6))  
plt.plot(data['Month'], data['Sales'], marker='o')  # Defaults to a line chart  
plt.title("Sales Over Time", fontproperties=font_prop)  
plt.xlabel("Months", fontproperties=font_prop)  
plt.ylabel("Sales", fontproperties=font_prop)  
st.pyplot(plt)  

# Additional Sections  
st.header("Agency Tools")  
st.write("Manage CRM, analytics, and marketing tools here.")  
tools = st.selectbox(  
    "Select a tool to manage:",  
    [  
        "CRM", "Analytics", "Marketing", "Legal Assistant", "Project Manager",  
        "Research Assistant", "Health & Wellness Coach", "Travel Planner",  
        "Learning & Development Coach", "Event Manager", "Inventory Manager",  
        "Risk Management Advisor", "Innovation Strategist"  
    ]  
)  
st.write(f"You selected: {tools}")  

# Notifications Section  
st.header("Notifications")  
st.write("Here are your latest updates:")  
notifications = ["New AI agent added", "CRM updated", "Marketing campaign launched"]  
for notification in notifications:  
    st.write(f"- {notification}")  

# Reports Section  
st.header("Reports")  
st.write("Visualize key metrics here.")  

# Sample data for another visualization  
another_data = pd.DataFrame({  
    'Category': ['A', 'B', 'C', 'D'],  
    'Value': [10, 20, 30, 25]  
})  

# Value Chart  
st.header("Value Chart")  
plt.figure(figsize=(8, 6))  
plt.bar(another_data['Category'], another_data['Value'])  
plt.title("Category Values", fontproperties=font_prop)  
plt.xlabel("Categories", fontproperties=font_prop)  
plt.ylabel("Values", fontproperties=font_prop)  
st.pyplot(plt)
