import google.generativeai as genai 
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Select the model
model = genai.GenerativeModel('gemini-pro')

# Initialize session state
if 'project_ideas' not in st.session_state:
    st.session_state.project_ideas = []

# Title and description
st.title("Project Generator")
st.write("Generate project ideas and guidelines for their development.")

# User input
job_title = st.text_input("Enter your Target job title (e.g., data scientist, software engineer,front-end developer, etc..):")
tools = st.text_input("Enter tools for projects (e.g., PPython, Java, C, C++, Excel, etc..):")
technique = st.text_input("Enter a technique to showcase (e.g., Machine Learning, Deep Learning, AJAX, React.js, etc..)")
industry = st.text_input("Enter an industry for projects(e.g., E-Commerce , Retail , Finance , Healthcare etc..)")

# Button to generate project ideas
if st.button("Generate Project Ideas"):
    if job_title and tools and technique and industry:
        # Generate project ideas using Gemini AI
        prompt = f"Generate only top 10 project titles for a {job_title} using {tools} with a focus on {technique} in the {industry} industry."
        response = model.generate_content(prompt)

        # Store project ideas in session state
        st.session_state.project_ideas = response.text.split("\n")

        # Display the generated project ideas
        for idea in st.session_state.project_ideas:
            st.write(idea)

# Dropdown to select a project for detailed explanation
selected_project = st.selectbox("Select a project for detailed explanation:", st.session_state.project_ideas, key="selected_project")

# Button to generate detailed explanation
if st.button("Generate Detailed Explanation"):
    if selected_project:
        # Generate detailed explanation for the selected project
        explanation_prompt = f"Provide detailed explanation for {selected_project} project using {tools} with a focus on {technique} in the {industry} industry. give entire guidelines for project lifecycle step by step , start with stating the problem statement and then start solutions approcah problem solving"
        explanation_response = model.generate_content(explanation_prompt)

        # Display the detailed explanation
        st.write(explanation_response.text)
    else:
        st.warning("Please select a project first.")   
