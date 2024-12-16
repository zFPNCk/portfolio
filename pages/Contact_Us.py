import streamlit as st

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Yout email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")

    if button:
        st.write("Thanks for your message")

