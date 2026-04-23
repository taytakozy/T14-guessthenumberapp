import streamlit as st
import random

# 1. Setup the "Secret Number" so it stays the same while playing
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0

st.title("🎯 Guess the Number!")
st.write("I'm thinking of a number between 1 and 100.")

# 2. The Input Box
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# 3. The Button
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    
    if guess < st.session_state.secret_number:
        st.warning("Too low! Try again. 👇")
    elif guess > st.session_state.secret_number:
        st.warning("Too high! Try again. 👆")
    else:
        st.success(f"🏆 Correct! you LOVE DAMLA and You got it in {st.session_state.attempts} tries!")
        # Reset button
        if st.button("Play Again"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.rerun()
