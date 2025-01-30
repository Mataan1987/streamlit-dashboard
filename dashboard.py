import streamlit as st  
import openai  

# Set your OpenAI API key  
openai.api_key = "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"  # Replace with your actual API key  

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
            response = openai.Completion.create(  
                engine="text-davinci-003",  
                prompt=user_input,  
                max_tokens=50  
            )  
            st.write("AI Response:")  
            st.write(response.choices[0].text.strip())  
        except Exception as e:  
            st.error(f"An error occurred: {e}")  
    else:  
        st.write("Please enter a question.")  

st.header("Agency Tools")  
st.write("Manage CRM, analytics, and marketing tools here.")  
tools = st.selectbox("Select a tool to manage:", ["CRM", "Analytics", "Marketing"])  
st.write(f"You selected: {tools}")  

st.header("Notifications")  
st.write("Here are your latest updates:")  
notifications = ["New AI agent added", "CRM updated", "Marketing campaign launched"]  
for notification in notifications:  
    st.write(f"- {notification}")  

st.header("Reports")  
st.write("Visualize key metrics here.")  
import pandas as pd  

# Sample data for visualization  
data = pd.DataFrame({  
    'Month': ['January', 'February', 'March', 'April'],  
    'Sales': [200, 300, 400, 500]  
})  

st.line_chart(data.set_index('Month'))