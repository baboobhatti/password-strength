import streamlit as st
import random
import string
import re

st.set_page_config(page_title="Strength Checker", page_icon="🔐")

st.title("🔒 Password Strength Checker")
st.markdown("<p style='margin-left: 60px; font-size: 20px; font-weight: bold;'>A tool is free to check password strength</p>",
               unsafe_allow_html=True)

# Function to check password strength
def password_strength(user_password):
    score = 0
    result = []  # Reset result every time function is called

    if len(user_password) >= 8:
        score += 1
        if re.search(r"[A-Z]", user_password) and re.search(r"[a-z]", user_password):
            score += 1
        else:
            result.append("❌ Include both uppercase and lowercase letters.")

        if re.search(r"\d", user_password):
            score += 1
        else:
            result.append("❌ Add at least one number (0-9).")

        if re.search(r"[@$#&*%^!]", user_password):
            score += 1
        else:
            result.append("❌ Include at least one special character (! @ # $ % ^ & *).")

        if score == 4:
            return "✅ Password strength status: Strong.", result
        elif score == 3:
            return "⚠️ Password strength status: Medium.", result
        else:
            return "❌ Password strength status: Weak 🌡.", result
    else:
        return "❌ Password should be at least 8 characters long.", result

# User input for password strength checking
user_password = st.text_input("Enter your password", type="password")

if st.button("Check Strength"): 
    st.write(f"🔑 Password: `{user_password}`")
    status, suggestions = password_strength(user_password)
    st.write(status)
    for suggestion in suggestions:
        st.write(suggestion)

# Divider
st.divider()
st.text("Free to Create a Strong Password")

# Define password generator function
def password_generator(length, digits, special_cha):
    characters_string = string.ascii_letters
    if digits:
        characters_string += string.digits
    if special_cha:
        characters_string += string.punctuation
    return ''.join(random.choice(characters_string) for _ in range(length))

# Password generator UI (Always Visible)
st.header("🔑 Strong Password Generator")

length = st.slider("Select number of characters in password", min_value=0, max_value=16, value=8)

if length <= 7:
    st.text("❌ Password is weak")
elif 8 <= length < 12:
    st.text("⚠️ Password is not strong")
else:
    st.text("✅ Password is strong")        

digits = st.checkbox('Include numbers')
special_cha = st.checkbox('Use special characters')

# Button to generate password
if st.button("Generate"):
    password = password_generator(length, digits, special_cha)
    st.write(f"🎉 Your Password: `{password}`")

