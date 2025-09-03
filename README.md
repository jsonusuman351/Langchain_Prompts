# 🚀 Prompt Engineering with LangChain

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python) !
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit) ![LangChain](https://img.shields.io/badge/LangChain-0086CB?style=for-the-badge&logo=langchain) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy) ![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn) ![Python-Dotenv](https://img.shields.io/badge/Python--Dotenv-EFC538?style=for-the-badge)

Welcome to this in-depth exploration of advanced prompt engineering techniques using LangChain! This repository is a collection of curated scripts and examples designed to showcase how to effectively structure conversations and instructions for Large Language Models (LLMs).

The core focus is on moving from simple, static inputs to dynamic, context-aware conversational prompts. This is the key to building intelligent, stateful AI applications.

---

### ✨ Core Concepts Demonstrated

This repository is a journey through the essential prompting strategies in LangChain:

1.  **🤖 Basic Prompting (Static vs. Dynamic)**:
    -   **Static Messages**: Learn to invoke models with simple, hardcoded messages (`AIMessage`, `HumanMessage`, `SystemMessage`).
    -   **Dynamic Prompts**: Understand the power of `PromptTemplate` to create reusable and flexible prompts by injecting variables into a template.

2.  **💬 Advanced Chat Prompts**:
    -   **ChatPromptTemplate**: Master the art of creating structured conversational templates. This is crucial for chat applications where different roles (System, User, AI) interact.
    -   **Dynamic Chat Conversations**: See how to dynamically format a series of messages based on input variables, making your chat prompts powerful and adaptable.

3.  **🧠 Managing Conversation History**:
    -   **The Stateless Nature of LLMs**: This project addresses the core challenge that LLMs have no memory of past interactions.
    -   **Message Placeholders**: Discover how to use `MessagesPlaceholder` to dynamically insert a list of previous chat messages into your prompt. This is the foundation for building conversational memory.
    -   **Chat History Retrieval**: Implement a simple yet effective mechanism to load and append to a conversation's history, giving the LLM the context it needs to provide relevant and coherent responses.

4.  **💡 Building a Stateful Chatbot**:
    -   The `chatbot.py` script ties all these concepts together into a functional chatbot. It demonstrates how to manage a conversation buffer, append new messages, and feed the entire history back to the LLM for a truly conversational experience.

---

### 🛠️ Tech Stack

-   **Core Framework**: LangChain
-   **LLM/Chat Model Providers**: OpenAI, Hugging Face
-   **Core Libraries**: `langchain`, `python-dotenv`

---

### ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/jsonusuman351/Langchain_Prompts.git](https://github.com/jsonusuman351/Langchain_Prompts.git)
    cd Langchain_Prompts
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # It is recommended to use Python 3.10 or higher
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables:**
    To use API-based models (like OpenAI), you need to provide your API keys.
    -   Create a file named `.env` in the root directory of the project.
    -   Add your keys to this file:
        ```env
        OPENAI_API_KEY="your-openai-api-key"
        HF_TOKEN="your-huggingface-api-key"
        ```

---

### 🚀 Usage Guide

Each script in this repository is designed to be run independently to demonstrate a specific prompting technique.

#### 1. Basic Prompt Templates

-   **Create a dynamic prompt for a single message:**
    ```bash
    python prompt_template.py
    ```

#### 2. Advanced Chat Prompt Templates

-   **Invoke a chat model with a static list of messages:**
    ```bash
    python messages.py
    ```
-   **Use `ChatPromptTemplate` for dynamic, role-based conversations:**
    ```bash
    python chat_prompt_template.py
    ```

#### 3. Managing Chat History

-   **Use `MessagesPlaceholder` to dynamically insert conversation history:**
    ```bash
    python message_placeholder.py
    ```

#### 4. Simple Stateful Chatbot

-   **Run a conversational chatbot that remembers past interactions:**
    This script will prompt you for input in a loop, maintaining the conversation's history.
    ```bash
    python chatbot.py
    ```
    **Example Interaction:**
    ```
    > Hi, my name is Suman.
    AI: Hello Suman! It's a pleasure to meet you. How can I help you today?
    > What is my name?
    AI: Your name is Suman.
    >
    ```

---

### 🔬 Exploring the Concepts: A Tour of the Scripts

This repository is organized by concept, allowing you to explore each prompting technique step-by-step.

<details>
<summary>Click to view the code layout</summary>

```
Langchain_Prompts/
│
├── prompt_template.py         # Demonstrates fundamental prompt templates
├── messages.py                # Shows static, role-based messaging
├── chat_prompt_template.py    # Focuses on dynamic chat prompts
├── message_placeholder.py     # Implements chat history retrieval
├── chatbot.py                 # A simple chatbot with conversational memory
├── requirements.txt
├── .env                       # (need to create this for API keys)
└── README.md
```
</details>

---

---