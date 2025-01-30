import streamlit as st  
import matplotlib.pyplot as plt  
import matplotlib.font_manager as fm  
import pandas as pd  
from dotenv import load_dotenv  
import os  
import openai  

# Load environment variables from .env file  
load_dotenv()  

# Set your OpenAI API key from the environment variable  
openai.api_key = os.getenv("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")  

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

# Create a Sample Plot (Example with Matplotlib)  
st.header("Sample Chart")  
data = pd.DataFrame({'Month': ['January', 'February', 'March', 'April'], 'Sales': [200, 300, 400, 500]})  
plt.figure(figsize=(8, 6))  

plt.plot(data['Month'], data['Sales'])  
plt.title("Sales Over Time", fontproperties=font_prop)  
plt.xlabel("Month", fontproperties=font_prop)  
plt.ylabel("Sales", fontproperties=font_prop)  

# Display the plot  
st.pyplot(plt)  

# Other sections...
