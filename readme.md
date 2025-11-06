# LangGraph AI Demo

## Overview

LangGraph AI Demo is a Streamlit application that simulates multi-step AI workflows using Groq LLM.

* Users can enter text.
* Choose a tool: Text Generator or Summarizer.
* Get instant AI-generated responses.

## Features

* Text generation
* Text summarization
* Streamlit UI
* Easy setup and use

## Setup Instructions

1. Install Python 3.10+.
2. Install required packages using pip:

```bash
pip install -r requirements.txt
```

3. Add your Groq API key in `langraph.py`:

```python
GROQ_KEY = "YOUR_GROQ_API_KEY"
```

4. Run the app:

```bash
streamlit run langgraph_app.py
```

5. Open your browser at `http://localhost:8501`

## Usage

* Select a tool from the sidebar.
* Enter text and click Submit.
* View AI-generated results.

---


