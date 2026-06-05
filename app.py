import streamlit as st

st.set_page_config(
    page_title="Rationneur INRAE",
    page_icon="🐄",
    layout="wide"
)

st.title("🐄 Rationneur INRAE")

st.markdown("""
## Bienvenue

Application de rationnement bovin laitier basée sur les références INRAE.

### Modules prévus

- Besoins INRAE
- Bibliothèque MP
- Formulation Ration Actuelle
- Diagnostic
- Formulation Ration Optimisée
- Comparaison
- Formulation Aliment

Utilisez le menu situé à gauche pour naviguer dans l'application.
""")
