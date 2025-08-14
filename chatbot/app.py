import sys
import difflib
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware



# ---------- Load Knowledge Base ----------
def load_policies(file_path="policies.txt"):
    policies = {}
    try:
        with open(file_path, "r") as f:
            for line in f:
                if ":" in line:
                    key, value = line.strip().split(":", 1)
                    policies[key.strip().lower()] = value.strip()
    except FileNotFoundError:
        print("policies.txt not found! Please create it.")
    return policies

policies = load_policies()

# ---------- Search Function ----------
def get_answer(question):
    question_lower = question.lower()
    matches = difflib.get_close_matches(question_lower, policies.keys(), n=1, cutoff=0.4)
    if matches:
        return policies[matches[0]]
    else:
        return "Sorry, I couldn't find information about that."

# ---------- FastAPI ----------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to ["http://localhost:8501"] if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_endpoint(req: ChatRequest):
    answer = get_answer(req.message)
    return {"response": answer}

# ---------- Streamlit ----------
def run_streamlit():
    import streamlit as st
    st.title("📚 Education Policies Chatbot")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    user_input = st.text_input("Ask a question about policies:")
    if st.button("Send") and user_input:
        answer = get_answer(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", answer))
    
    for sender, message in st.session_state.chat_history:
        if sender == "You":
            st.markdown(f"**🧑‍🎓 {sender}:** {message}")
        else:
            st.markdown(f"**🤖 {sender}:** {message}")

# ---------- Terminal ----------
def run_terminal():
    print("📚 Education Policies Chatbot (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Bot: Goodbye!")
            break
        answer = get_answer(user_input)
        print(f"Bot: {answer}")

# ---------- Auto-detect mode ----------
if __name__ == "__main__":
    if "streamlit" in sys.argv[0]:
        run_streamlit()
    elif any("uvicorn" in arg for arg in sys.argv):
        # Running with uvicorn → FastAPI mode
        pass
    else:
        run_terminal()
