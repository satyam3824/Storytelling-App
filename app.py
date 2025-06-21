import streamlit as st
import hmac
import google.generativeai as genai  # ✅ Correct import


# -------- PASSWORD CHECK ----------
def check_password():
    def password_entered():
        username = st.session_state.get("username", "")
        password = st.session_state.get("password", "")
        if username in st.secrets["passwords"] and hmac.compare_digest(
            password, st.secrets.passwords[username]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["username"]
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    def login_form():
        with st.form("Login"):
            st.markdown("### 🔐 Secure Login")
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    if st.session_state.get("password_correct", False):
        return True

    login_form()
    if "password_correct" in st.session_state and not st.session_state["password_correct"]:
        st.error("😕 User not known or password incorrect")
    return False

if not check_password():
    st.stop()

# -------- GEMINI SETUP ----------
genai.configure(api_key=st.secrets["api_key"]["api_key"])
model = genai.GenerativeModel("gemini-1.5-flash")

# -------- APP UI ----------
st.set_page_config(page_title="AI Storyteller", layout="centered")
st.markdown("<h1 style='text-align: center;'>🧙‍♂️ AI Storyteller</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Turn your ideas into magical stories powered by Google Gemini</p>", unsafe_allow_html=True)
st.markdown("---")

# -------- STORY FUNCTION ----------
def story_telling(text):
    if not text.strip():
        return "Please enter a story idea."

    response = model.generate_content(
        [f"Generate a creative and engaging short story based on this input: {text}"]
    )
    return response.text

# -------- INPUT FORM ----------
user_input = st.text_area(
    "📌 Your Story Idea:",
    placeholder="e.g., A time-traveling elephant discovers an ancient mystery...",
    height=200
)

if st.button("Generate Story"):
    if user_input:
        with st.spinner("✨ Generating your story..."):
            result = story_telling(user_input)
        st.success("✅ Story generated!")
        st.subheader("📖 Your Story")
        st.markdown(result)
    else:
        st.warning("⚠️ Please enter a story idea first.")

st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>Made with ❤️ using Streamlit & Gemini AI</div>", unsafe_allow_html=True)
