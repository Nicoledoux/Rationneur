import streamlit as st
import pandas as pd

from modules.database import (
    init_db,
    lire_mp,
    ajouter_mp
)

st.title("📚 Bibliothèque MP")

init_db()

st.subheader("Ajouter une matière première")

with st.form("ajout_mp"):

    categorie = st.text_input("Catégorie")
    sous_categorie = st.text_input("Sous-catégorie")
    mp = st.text_input("Matière première")

    ms = st.number_input("MS", value=0.0)
    ufl = st.number_input("UFL", value=0.0)
    ufv = st.number_input("UFV", value=0.0)

    pdin = st.number_input("PDIN", value=0.0)
    pdie = st.number_input("PDIE", value=0.0)

    mat = st.number_input("MAT", value=0.0)

    amidon = st.number_input("Amidon", value=0.0)
    sucres = st.number_input("Sucres", value=0.0)

    ndf = st.number_input("NDF", value=0.0)
    adf = st.number_input("ADF", value=0.0)

    mg = st.number_input("MG", value=0.0)

    ca = st.number_input("Ca", value=0.0)
    p = st.number_input("P", value=0.0)
    k = st.number_input("K", value=0.0)
    na = st.number_input("Na", value=0.0)

    cout = st.number_input(
        "Coût €/t",
        value=0.0
    )

    submit = st.form_submit_button(
        "Ajouter"
    )

    if submit:

        ajouter_mp((
            categorie,
            sous_categorie,
            mp,
            ms,
            ufl,
            ufv,
            pdin,
            pdie,
            mat,
            amidon,
            sucres,
            ndf,
            adf,
            mg,
            ca,
            p,
            k,
            na,
            cout
        ))

        st.success(
            "Matière première ajoutée"
        )

st.divider()

st.subheader("Bibliothèque")

df = lire_mp()

st.dataframe(
    df,
    use_container_width=True
)
