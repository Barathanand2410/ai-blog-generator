import streamlit as st
from groq import Groq

# API Key (temporary - replace later with env variable)
client = Groq(api_key="YOUR_API_KEY")

st.title("AI Blog Generator")

# Inputs
topic = st.text_input("Enter blog topic:")
tone = st.selectbox("Select tone", ["Professional", "Casual", "Marketing"])
word_limit = st.selectbox("Select word limit", [200, 500, 800])
keywords = st.text_input("Enter SEO keywords (comma separated)")

# Button
if st.button("Generate Blog"):

    if topic:

        prompt = f"""
        Write a blog on the topic: {topic}

        Tone: {tone}
        Word Limit: {word_limit}

        Include these SEO keywords: {keywords}

        Structure:
        - Title
        - Introduction
        - 3 main sections with headings
        - Conclusion

        Return output in clean markdown format with proper headings.
        """

        # Loading spinner
        with st.spinner("Generating blog..."):

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a professional SEO content writer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            content = response.choices[0].message.content

        # Display output
        st.subheader("Generated Blog:")
        st.markdown(content)

        # Download option
        st.download_button(
            label="Download Blog",
            data=content,
            file_name="blog.txt",
            mime="text/plain"
        )

    else:
        st.warning("Please enter a blog topic.")
