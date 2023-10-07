import streamlit as st
import openai

openai.api_key=st.secrets['openai_key']
st.title("Generative AI")

prompt=st.text_area("Enter a Promt:")
def generate_text(promt):
    response=openai.Completion.create(
        engine="text-davinci-002",
        promt=promt,
        max_tokens=1200
    )
    return response.choices[0].text

if st.button("Generate"):
    if prompt:
        generate_text=generate_text(prompt)
        st.write("Generated Text")
        st.write(generate_text)
    else:
        st.warning("Please Enter a promt")