import streamlit as st
import streamlit.components.v1 as components

from utils import create_navigation_menu

from config import pages

def main():
    
    #adding logo to sidebar at the center
    st.sidebar.markdown('<center><img src="https://d2kq0urxkarztv.cloudfront.net/59355fc54ac3e7290177e3e7/4244926/image-5f9e5fc3-116d-4f04-974c-3ca8ee69f86e.png?w=1148&e=webp&nll=true" width="100"></center>', unsafe_allow_html=True)
    # st.sidebar.image('baila_logo.png', width=100, )
    st.sidebar.header('Insights', divider='rainbow')

    #adding pages to sidebar from an hamburger menu
    page_function = create_navigation_menu(pages)
    page_function()

    # Chatbot inside the sidebar

    with st.sidebar:

        with st.expander('BAIL.AÍ 🤖'):
            prompt = st.chat_input("Say something")
            if prompt:
                st.write(f"User has sent the following prompt: {prompt}")

if __name__ == "__main__":
    main()