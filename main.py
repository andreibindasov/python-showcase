import streamlit as st

# st.set_page_config(layout="wide")

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image("images/photo.jpg")

    with col2:
        st.title("Andrei Bindasov")
        content = """
        Hi, I am a man: Andrei! I am a programmer, linguist, coach and a teacher. I graduated in 1996 with 
        MD in Computer Science & BD in Linguistics.
        """
        st.write(content)

st.write("Below you can find python showcase projects. Feel free to contact me.")

