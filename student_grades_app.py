import streamlit as st
import pandas as pd

st.title("Student Grade Calculator")

name = st.text_input("Enter your name")
math = st.number_input("Enter grade for Math", min_value=0.0, max_value=20.0)
english = st.number_input("Enter grade for English", min_value=0.0, max_value=20.0)
science = st.number_input("Enter grade for Science", min_value=0.0, max_value=20.0)

if st.button("Calculate"):
    average = (math + english + science) / 3
    if average >= 17:
        letter = "A"
    elif average >= 14:
        letter = "B"
    elif average >= 10:
        letter = "C"
    else:
        letter = "F"

    status = "You passed!" if letter != "F" else "You failed!"
    st.write(f"{name}, your average grade is {round(average,2)}")
    st.write(f"Your letter grade is {letter}")
    st.write(status)

data = {
    "Subject": ["Math", "English", "Science"],
    "Grade": [math, english, science]
}

df = pd.DataFrame(data)

st.bar_chart(df.set_index("Subject"))