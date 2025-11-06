import streamlit as st
from groq import Groq  # You can replace with OpenAI if preferred

# --- Groq Client Initialization ---
GROQ_KEY = "your_api_key"  # Replace with your actual Groq API key
GROQ_MODEL = "llama-3.1-8b-instant"

try:
    client = Groq(api_key=GROQ_KEY)
    groq_available = True
    st.success(f"✅ Groq client initialized using model: {GROQ_MODEL}")
except Exception as e:
    groq_available = False
    st.error(f"❌ Groq initialization failed: {e}")

# --- Streamlit UI ---
st.title("LangGraph AI Demo")
st.markdown("Simulated LangGraph workflow: text-generator and summarizer nodes")

# Sidebar for tool selection
st.sidebar.header("Select Tool")
tool = st.sidebar.selectbox("Choose tool", ["text-generator", "summarizer"])

# User input
user_input = st.text_area("Enter your text here:")

# Button to submit input
if st.button("Submit"):
    if not user_input:
        st.error("Input cannot be empty")
    elif not groq_available:
        st.error("Groq API not available")
    else:
        # Define node/system prompt
        if tool == "text-generator":
            system_prompt = "You are a helpful AI assistant. Answer directly."
            max_tokens_val = 300
        elif tool == "summarizer":
            system_prompt = "You are a summarizer. Condense the text into key points."
            max_tokens_val = 150
        else:
            st.error(f"Unknown tool: {tool}")
            st.stop()

        # --- Call Groq API ---
        try:
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=max_tokens_val,
                temperature=0.1
            )
            result = response.choices[0].message.content.strip()
            st.subheader("📝 Result")
            st.write(result)
        except Exception as e:
            st.error(f"Groq API call failed: {e}")
# User Input
#     │
#     ▼
# Text-Generation Node (Step 1)
#     │ output → generated_text
#     ▼
# Summarization Node (Step 2)
#     │ output → summary
#     ▼
# Final Result to User
