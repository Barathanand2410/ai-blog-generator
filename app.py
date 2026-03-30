import streamlit as st
from groq import Groq
import os

# Use environment variable for security
client = Groq(api_key="YOUR_API_KEY")
st.title("AI Blog Generator")

# Inputs
topic = st.text_input("Enter blog topic:")
tone = st.selectbox("Select tone", ["Professional", "Casual", "Marketing"])

# Button to trigger generation
if st.button("Generate Blog"):

    if topic:
        prompt = f"""
        Write a blog on the topic: {topic}

        Tone: {tone}

        Structure:
        - Title
        - Introduction
        - 3 main sections with headings
        - Conclusion

        Keep it clear, engaging, and well formatted.
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a professional content writer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        st.subheader("Generated Blog:")
        st.write(response.choices[0].message.content)

    else:
        st.warning("Please enter a blog topic.")