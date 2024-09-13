from gc import disable
import streamlit as st
import streamlit.components.v1 as components

def create_navigation_menu(pages):
    '''
    Função que cria o menu de navegação da aplicação
    '''
    page = st.sidebar.selectbox("Selecione a página", tuple(pages.keys()))
    return pages[page]

#end

def trends():
    '''
    Função que renderiza a página de Tendências
    '''   

    # st.code(st.session_state)

    tab1, tab2, tab3, tab4 = st.tabs(["YouTube", "TikTok", "Instagram", "Facebook"])

    with tab1:

        st.subheader('Tendências do segmento.') 
        
        html_code = """<iframe title="dash_trends" width="800" height="836" src="https://app.powerbi.com/view?r=eyJrIjoiNjI0ZjZjZmUtYTRkZC00YWQxLTk4MjItOWFjZDIwMzEwZDIyIiwidCI6Ijc5NWNjMjMzLWJkYzAtNGZkNC04NjZhLTgxYWJmZmY3MTQzNCJ9&pageName=cff75a1a2d0e35a03dcd" frameborder="0" allowFullScreen="true"></iframe>"""

        # Usando st.components.v1.html para incluir o HTML na aplicação
        components.html(html_code, height=600, width = 800)

    with tab2:

        st.subheader('Tendências do segmento.') 
        
        html_code = """<iframe title="tiktok_trends" width="800" height="836" src="https://app.powerbi.com/view?r=eyJrIjoiZGFmM2MxNDItYjQ0OC00N2FlLWE1MzQtMzRmNTM5OTIyYWE1IiwidCI6Ijc5NWNjMjMzLWJkYzAtNGZkNC04NjZhLTgxYWJmZmY3MTQzNCJ9" frameborder="0" allowFullScreen="true"></iframe>"""

        # Usando st.components.v1.html para incluir o HTML na aplicação
        components.html(html_code, height=600, width = 800)

    
#end

def brand():
    '''
    Função que renderiza a página de Sua Marca
    '''
    st.subheader('Sua Marca!') 
    st.write('Aqui você pode ver como está a sua marca nas redes sociais.')

#end

def competitors():
    '''
    Função que renderiza a página de Concorrência
    '''
    st.subheader('Concorrência') 
    st.write('Aqui você pode ver como está a concorrência.')

#end

def audience():
    '''
    Função que renderiza a página de Audiência
    '''
    st.subheader('Audiência') 
    st.write('Aqui você pode ver como está a audiência.')

#end
