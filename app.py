import streamlit as st
import pandas as pd
from langchain_groq import ChatGroq

# ---------------- PAGE ----------------
st.set_page_config(page_title="Sales AI Analyst", layout="wide")

st.title("📊 Neysa AI Analyst")

st.markdown("""
### 👋 Hey!

I'm **Neysa** 🤖  

Your intelligent assistant for analyzing sales data and generating business insights.

Ask me anything about your data — I’ll help you uncover meaningful patterns and insights instantly!
""")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_excel("sales_data.xlsx")

df = load_data()

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.header("📌 About")
    st.write(
        "This AI chatbot analyzes sales data using natural language queries. "
        "It converts your questions into pandas code and generates insights."
    )

    st.header("💡 Example Questions")
    st.write("""
    - Top 10 customers by sales  
    - Sales by country  
    - Best product line  
    - Which customers should we focus on?  
    - which year had highest sales  
    """)

    st.markdown("---")
    st.write("Built using Python, Pandas & LLM")

# ---------------- LLM -----------
groq_api_key = st.secrets["GROQ_API_KEY"]

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant",
    temperature=0
)

# ---------------- CLEAN CODE ----------------
def clean_code(code):
    code = code.replace("```python", "")
    code = code.replace("```", "")
    code = code.replace("Here is the code:", "")
    code = code.replace("Here is the pandas code:", "")
    code = code.replace("The pandas code is:", "")
    return code.strip()

# ---------------- SMART QUESTION HANDLING ----------------
def improve_question(question):
    prompt = f"""
Rewrite this question into a clear data analysis query:

Question: {question}

Make it specific for a sales dataset.
"""
    response = llm.invoke(prompt)
    return response.content.strip()

# ---------------- GENERATE CODE ----------------
def generate_code(question):

    columns = list(df.columns)

    prompt = f"""
You are a Python pandas expert.

A dataframe named df already exists.

Columns:
{columns}

User question:
{question}

Rules:
- Return ONLY one line of pandas code
- Store result in variable named result
- No explanation
- No print
"""

    response = llm.invoke(prompt)
    return clean_code(response.content)

# ---------------- EXECUTE ----------------
def run_code(code):
    local_env = {"df": df, "pd": pd}
    exec(code, {}, local_env)
    return local_env["result"]

# ---------------- ANALYST EXPLANATION ----------------
def explain_result(question, result):

    prompt = f"""
You are a business data analyst.

User question:
{question}

Data result:
{result}

Explain this clearly in a professional way.
Also give a short business insight.

Keep it simple.
"""

    response = llm.invoke(prompt)
    return response.content

# ---------------- INPUT ----------------
st.markdown("### 💬 — Ask a Question")
question = st.text_input("Type your question here...")

if question:

    # ---------------- GREETING HANDLING ----------------
    greetings = ["hi", "hello", "hey", "hii", "helo"]

    if question.lower().strip() in greetings:
        st.markdown("### 🤖 Hey there!")
        st.write("I'm **Neysa** — ready to help you with your data 📊")
        st.write("Ask me anything like *top customers*, *sales trends*, or *best products*!")
        st.stop()

    if "who are you" in question.lower():
        st.markdown("### 🤖 About Me")
        st.write("I'm **Neysa**, your AI assistant built to analyze sales data and generate insights.")
        st.stop()

    if "thank" in question.lower():
        st.markdown("### 😊 You're welcome!")
        st.write("Happy to help! Let me know if you need more insights 📊")
        st.stop()

    # ---------------- MAIN LOGIC ----------------
    with st.spinner("🔍 Analyzing data and generating insights..."):

        try:
            improved_q = improve_question(question)
            code = generate_code(improved_q)
            result = run_code(code)

        except Exception:

            try:
                code = generate_code(question)
                result = run_code(code)

            except Exception:
                st.error("😅 Oops! I couldn’t fully understand that question.\n\nTry asking in a slightly different way — I’m still learning!")
                st.stop()

        st.markdown("---")

        # ---------------- SHOW RESULT ----------------
        st.markdown("### 📊 Result")

        if isinstance(result, pd.DataFrame) or isinstance(result, pd.Series):
            st.dataframe(result)
        else:
            st.write(result)

        # ---------------- INSIGHT ----------------
        try:
            st.markdown("### 🧠 Smart Insight")
            explanation = explain_result(question, result)
            st.write(explanation)
        except:
            pass