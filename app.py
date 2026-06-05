import streamlit as st

st.set_page_config(
    page_title="Rationneur INRAE",
    layout="wide"
)

st.title("🐄 Rationneur INRAE")

st.markdown(
    """
    ## Bienvenue

    Application de rationnement bovin laitier
    basée sur les références INRAE.

    Sélectionnez un module dans le menu de gauche.
    """
)
