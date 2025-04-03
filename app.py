import streamlit as st
from report.pdf_export import export_pdf
from report.diagramm import render_diagramm
import os

st.set_page_config(page_title="Sanierungsfahrplan Demo", layout="centered", page_icon="🏡")
st.image("static/logo.png", width=180)

st.markdown("### Willkommen zur Demo des digitalen Sanierungsfahrplans 🏡")
st.markdown("""
Diese Demo zeigt beispielhaft, wie für ein Gebäude automatisch ein individueller Sanierungsfahrplan erstellt wird.

**Inhalte dieser Vorschau:**
- 📋 Gebäudedaten (Beispiel)
- 🔧 Sanierungsmaßnahmen inkl. Kosten
- 💶 Fördermöglichkeiten
- 📄 Fahrplan als PDF
- 📊 Interaktives Kostendiagramm
- 📍 Kartenansicht (simuliert)
- ▶️ Video-Vorschau

➡️ Die Vollversion erlaubt eigene Eingaben und individuelle Berechnungen.
""")

# Beispiel-Daten
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

st.markdown("### 📋 Gebäudeinformationen (Beispiel)")
st.write(f"Adresse: {daten['adresse']}")
st.write(f"Baujahr: {daten['baujahr']}")
st.write(f"Heizung: {daten['heizung_baujahr']}")

st.markdown("### 🔧 Empfohlene Sanierungsmaßnahmen")
for e in empfehlungen:
    st.markdown(f"- **{e['maßnahme']}** – {e['kosten']} € – ab {e['jahr']}")

st.markdown("### 💶 Mögliche Fördermittel")
for f in förderung:
    st.markdown(f"- **{f['maßnahme']}**: ca. {f['förderung']} €")

st.markdown("### 📍 Standortübersicht (simuliert)")
st.image("static/map_demo.png", caption="Beispielhafter Gebäude-Standort", use_column_width=True)

st.markdown("### 📊 Kostenübersicht")
st.caption("Hier sehen Sie eine grobe Übersicht der Investitionskosten je Maßnahme.")
render_diagramm(empfehlungen)

st.markdown("### 📄 Fahrplan als PDF")
pfad = "output/demo_fahrplan.pdf"
os.makedirs("output", exist_ok=True)
export_pdf(pfad, daten, empfehlungen, förderung)
with open(pfad, "rb") as f:
    st.download_button("📥 Sanierungsfahrplan (PDF) herunterladen", f, file_name="Sanierungsfahrplan_DEMO.pdf")

st.markdown("### ▶️ Kurze Tool-Vorschau (1 Min)")
st.video("https://www.youtube.com/embed/VaPghYtE_Uk")

st.markdown("---")
st.caption("Diese Vorschau zeigt die automatisierte Analyse für ein Beispielgebäude.")
st.markdown("📬 Bei Interesse: [kontakt@deinunternehmen.de](mailto:kontakt@deinunternehmen.de)")
