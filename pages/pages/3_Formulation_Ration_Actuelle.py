import streamlit as st
import pandas as pd

from modules.database import (
    charger_bibliotheque_complete
)

st.title("🥣 Formulation Ration Actuelle")

df_mp = charger_bibliotheque_complete()

if "ration" not in st.session_state:
    st.session_state.ration = pd.DataFrame()

st.subheader("Ajouter un aliment")

col1, col2 = st.columns(2)

with col1:

    aliment = st.selectbox(
        "Matière première",
        df_mp["Matière première"]
    )

with col2:

    quantite = st.number_input(
        "Kg brut distribué",
        min_value=0.0,
        value=0.0,
        step=0.5
    )

if st.button("Ajouter à la ration"):

    ligne = df_mp[
        df_mp["Matière première"] == aliment
    ].copy()

    ligne["Kg brut"] = quantite

    st.session_state.ration = pd.concat(
        [
            st.session_state.ration,
            ligne
        ],
        ignore_index=True
    )

st.divider()

ration = st.session_state.ration.copy()

if len(ration):

    ration["MS kg"] = (
        ration["Kg brut"]
        * ration["MS"]
        / 100
    )

    ration["UFL total"] = (
        ration["MS kg"]
        * ration["UFL"]
    )

    ration["UFV total"] = (
        ration["MS kg"]
        * ration["UFV"]
    )

    ration["PDIN total"] = (
        ration["MS kg"]
        * ration["PDIN"]
    )

    ration["PDIE total"] = (
        ration["MS kg"]
        * ration["PDIE"]
    )

    ration["MAT total"] = (
        ration["MS kg"]
        * ration["MAT"]
        / 1000
    )

    ration["Amidon total"] = (
        ration["MS kg"]
        * ration["Amidon"]
        / 100
    )

    ration["Sucres total"] = (
        ration["MS kg"]
        * ration["Sucres"]
        / 100
    )

    ration["NDF total"] = (
        ration["MS kg"]
        * ration["NDF"]
        / 100
    )

    ration["ADF total"] = (
        ration["MS kg"]
        * ration["ADF"]
        / 100
    )

    ration["MG total"] = (
        ration["MS kg"]
        * ration["MG"]
        / 100
    )

    ration["Ca total"] = (
        ration["MS kg"]
        * ration["Ca"]
    )

    ration["P total"] = (
        ration["MS kg"]
        * ration["P"]
    )

    ration["K total"] = (
        ration["MS kg"]
        * ration["K"]
    )

    ration["Na total"] = (
        ration["MS kg"]
        * ration["Na"]
    )

    ration["Coût €"] = (
        ration["Kg brut"]
        * ration["Cout €/t"]
        / 1000
    )

    st.subheader("Ration")

    st.dataframe(
        ration,
        use_container_width=True
    )

    st.divider()

    st.subheader("Totaux")

    total_ms = ration["MS kg"].sum()

    total_ufl = ration["UFL total"].sum()

    total_ufv = ration["UFV total"].sum()

    total_pdin = ration["PDIN total"].sum()

    total_pdie = ration["PDIE total"].sum()

    total_mat = ration["MAT total"].sum()

    total_amidon = ration["Amidon total"].sum()

    total_sucres = ration["Sucres total"].sum()

    total_ndf = ration["NDF total"].sum()

    total_adf = ration["ADF total"].sum()

    total_mg = ration["MG total"].sum()

    total_ca = ration["Ca total"].sum()

    total_p = ration["P total"].sum()

    total_k = ration["K total"].sum()

    total_na = ration["Na total"].sum()

    total_cout = ration["Coût €"].sum()

    resume = pd.DataFrame({
        "Critère": [
            "MS",
            "UFL",
            "UFV",
            "PDIN",
            "PDIE",
            "MAT",
            "Amidon",
            "Sucres",
            "NDF",
            "ADF",
            "MG",
            "Ca",
            "P",
            "K",
            "Na",
            "Coût"
        ],
        "Valeur": [
            total_ms,
            total_ufl,
            total_ufv,
            total_pdin,
            total_pdie,
            total_mat,
            total_amidon,
            total_sucres,
            total_ndf,
            total_adf,
            total_mg,
            total_ca,
            total_p,
            total_k,
            total_na,
            total_cout
        ]
    })

    st.dataframe(
        resume,
        use_container_width=True,
        hide_index=True
    )
