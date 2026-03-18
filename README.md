# 📊 Sales AI Chatbot

# 🚀 Project Overview

The **Sales AI Chatbot** is an AI-powered data analysis assistant that allows users to ask questions about a sales dataset using **natural language**.

Instead of writing SQL queries or Python code, users can simply ask questions like:

- Which country has the highest sales?
- Top 5 customers by revenue
- Average quantity ordered
- Total sales by product line

The chatbot automatically analyzes the dataset and provides answers instantly.

This project demonstrates how **Artificial Intelligence and Data Analysis can be combined to build smart business tools.**

---

# 🎯 Project Goal

The main goal of this project is to create an **AI-powered data analyst** that:

✔ Understands natural language questions  
✔ Converts questions into data analysis queries  
✔ Executes those queries on a dataset  
✔ Returns meaningful answers instantly  

This removes the need for technical knowledge like **SQL or Python** to analyze data.

---

# 🧠 How the Chatbot Works

The system works in the following steps:

User Question
↓
AI Model (LLM) understands the question
↓
AI generates pandas code
↓
The code runs on the dataset
↓
Result is returned to the user

Example:
User asks: Top 5 customers by SALES
The AI converts this into something like:

```python
df.groupby("CUSTOMERNAME")["SALES"].sum().sort_values(ascending=False).head(5)
```
 
# 🛠️ Technologies Used
1. Python

- Python is the main programming language used to build this project.

It is widely used for:

Data Science
Artificial Intelligence
Machine Learning
Data Analysis

2. Pandas

- Pandas is a Python library used for data analysis and manipulation.

It allows us to:
filter data
group data
calculate statistics
analyze large datasets easily

Example: df.groupby("COUNTRY")["SALES"].sum()


3. Streamlit
- Streamlit is used to build the interactive web interface.
It allows us to quickly create web apps using Python without writing HTML or JavaScript.

Streamlit is responsible for:
the chatbot interface
user input box
displaying results

4. Groq LLM
- Groq provides access to a Large Language Model (LLM).

The LLM is responsible for:
understanding natural language questions
converting them into pandas code

Example:
User question: Which country has the highest sales?
The LLM translates it into a data analysis query.

📂 Project Structure

The project contains the following files:

sales_ai_chatbot
│
├── app.py
├── sales_data.xlsx
├── requirements.txt
└── README.md

# app.py

Main Python file containing the chatbot logic.

sales_data.xlsx

The dataset used for analysis.

requirements.txt

Contains the list of required Python libraries.

# README.md

Documentation explaining the project.

# ⚙️ Installation & Setup Guide

Follow these steps to run the chatbot.

Step 1 — Install Python

Make sure Python is installed on your system.

Download from:
https://www.python.org/downloads/

Step 2 — Install Required Libraries

Open a terminal and run:

pip install -r requirements.txt

This installs all required libraries automatically.

Step 3 — Add Your Groq API Key

Open the file:

app.py

Find this line:

groq_api_key = "YOUR_API_KEY_HERE"

Replace it with your Groq API key.

You can generate an API key here:
https://console.groq.com/keys

Step 4 — Run the Chatbot

Run this command:

streamlit run app.py

The chatbot will open in your browser.

# 💬 Example Questions to Try

You can ask questions such as:

Which country has highest SALES?
Top 5 customers by SALES
Total SALES by PRODUCTLINE
Average QUANTITYORDERED
Top 10 orders by SALES

# ⚠️ Challenges Faced
1. AI generating incorrect queries

Sometimes the LLM produced incorrect pandas code.

This was solved by improving prompts and adding error handling.

2. Slow responses using AI agents

Initially the system used a LangChain agent which caused delays.

The architecture was improved by directly generating pandas code.

# 🌟 Key Features

Natural language data analysis
AI-powered query generation
Real-time dataset analysis
Interactive chatbot interface
Business insight generation


👩‍💻 Author

Ayesha Lubna

AI / Data Science Project
