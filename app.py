import streamlit as st
from firebase.auth import signup_user, login_user

st.set_page_config(page_title="TrackZen Login", layout="centered")

st.markdown("<h1 style='text-align: center; color: #ff80d5;'>TrackZen</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #fff;'>Sign up and get tracking!</h4>", unsafe_allow_html=True)

mode = st.radio("Choose Mode", ["Login", "Sign Up"], horizontal=True)

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if mode == "Sign Up":
    if st.button("Sign Up"):
        with st.spinner("Creating account..."):
            result = signup_user(email, password)
            if isinstance(result, dict):
                st.success("Account created! You can now log in.")
            else:
                st.error(result)

else:
    if st.button("Login"):
        with st.spinner("Logging in..."):
            result = login_user(email, password)
            if isinstance(result, dict):
                st.session_state["user"] = result
                st.success("Logged in!")
                st.switch_page("onboarding.py")  # Next page coming soon
            else:
                st.error(result)
