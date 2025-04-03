from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_pdf(datei, daten, empfehlungen, förderung):
    c = canvas.Canvas(datei, pagesize=A4)
    width, height = A4
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Sanierungsfahrplan – DEMO")

    c.setFont("Helvetica", 12)
    y = height - 100
    c.drawString(50, y, f"Adresse: {daten['adresse']}")
    c.drawString(50, y - 20, f"Baujahr: {daten['baujahr']}")

    y -= 60
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Empfohlene Maßnahmen:")
    c.setFont("Helvetica", 12)
    for emp in empfehlungen:
        y -= 20
        c.drawString(60, y, f"• {emp['maßnahme']} – {emp['kosten']} EUR – ab {emp['jahr']}")

    if förderung:
        y -= 40
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "Fördermittel:")
        c.setFont("Helvetica", 12)
        for f in förderung:
            y -= 20
            c.drawString(60, y, f"• {f['maßnahme']}: ca. {f['förderung']} EUR")
    c.save()
