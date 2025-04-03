import matplotlib.pyplot as plt
import streamlit as st

def render_diagramm(empfehlungen):
    if not empfehlungen:
        st.info("Keine Maßnahmen vorhanden.")
        return
    labels = [e["maßnahme"] for e in empfehlungen]
    kosten = [e["kosten"] for e in empfehlungen]

    fig, ax = plt.subplots()
    ax.barh(labels, kosten)
    ax.set_xlabel("Kosten (€)")
    ax.set_title("Sanierungskosten")
    st.pyplot(fig)
