import streamlit as st
from report.pdf_export import export_pdf
from report.diagramm import render_diagramm
import os

st.set_page_config(page_title="Sanierungsfahrplan Demo", layout="centered")
st.title("🏡 Sanierungsfahrplan – DEMO")

st.markdown("Dies ist eine interaktive Vorschau für einen digitalen Sanierungsfahrplan.")

# Demo-Daten
daten = {
    "adresse": "Musterstraße 12, Beispielstadt",
    "baujahr": 1975,
    "heizung_baujahr": 1995,
    "dämmung": {"dach": False, "kellerdecke": False},
    "erneuerbare_energien": False
}

empfehlungen = [
    {"maßnahme": "Dachdämmung", "kosten": 9500, "jahr": 2025},
    {"maßnahme": "Kellerdeckendämmung", "kosten": 3800, "jahr": 2026},
    {"maßnahme": "Heizung tauschen", "kosten": 14500, "jahr": 2025},
    {"maßnahme": "Photovoltaik installieren", "kosten": 8900, "jahr": 2027}
]

förderung = [
    {"maßnahme": "Dachdämmung", "förderung": 3000},
    {"maßnahme": "Wärmepumpe", "förderung": 5000},
    {"maßnahme": "Photovoltaik", "förderung": 2000}
]

st.subheader("📋 Gebäudeinformationen (Beispiel)")
st.write(f"Adresse: {daten['adresse']}")
st.write(f"Baujahr: {daten['baujahr']}")
st.write(f"Heizung: {daten['heizung_baujahr']}")

st.subheader("🔧 Empfohlene Sanierungsmaßnahmen")
for e in empfehlungen:
    st.markdown(f"- **{e['maßnahme']}** – {e['kosten']} € – ab {e['jahr']}")

st.subheader("💶 Mögliche Fördermittel")
for f in förderung:
    st.markdown(f"- **{f['maßnahme']}**: ca. {f['förderung']} €")

st.subheader("📊 Kostenübersicht")
render_diagramm(empfehlungen)

st.subheader("📄 Fahrplan als PDF")
pfad = "output/demo_fahrplan.pdf"
os.makedirs("output", exist_ok=True)
export_pdf(pfad, daten, empfehlungen, förderung)

with open(pfad, "rb") as f:
    st.download_button("📥 PDF herunterladen", f, file_name="Sanierungsfahrplan_DEMO.pdf")
