"""
Erzeugt Tabelle 2: Verteilung der kodierten Stellen in Korpus 2 auf
Faulconbridges vier Boundary-Work-Modi.

Ausgeschlossen: neutral, Reflexiv/kritisch (induktiv ergaenzte
Zusatzkategorie), Methodenfrage und Korrektur (Dokumentationsnotizen,
keine kodierten Textstellen).

Quelle: daten/korpus2/Eymann_Kodiertabelle_Korpus2.csv
Ausgabe: Markdown-Tabelle auf stdout, PNG unter
         outputs/Eymann_Tabelle2_korpus2_boundarywork.png
"""

import csv
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "daten" / "korpus2" / "Eymann_Kodiertabelle_Korpus2.csv"
PNG_PATH = ROOT / "outputs" / "Eymann_Tabelle2_korpus2_boundarywork.png"

MODI = ["Defending", "Creating", "Coalescing", "Negotiating"]
AUSGESCHLOSSEN = {"neutral", "Reflexiv/kritisch", "Methodenfrage", "Korrektur"}


def render_png(header, rows):
    fig, ax = plt.subplots(figsize=(5, 0.45 * (len(rows) + 1)))
    ax.axis("off")
    table = ax.table(cellText=rows, colLabels=header, cellLoc="center", loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 1.6)
    table.auto_set_column_width(col=list(range(len(header))))
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#999999")
        if row == 0:
            cell.set_facecolor("#dbe4f0")
            cell.set_text_props(weight="bold")
    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=200, bbox_inches="tight")
    plt.close(fig)


def main():
    with open(CSV_PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    counts = Counter(row["modus"].strip() for row in rows)
    ausgeschlossen_n = sum(counts.get(k, 0) for k in AUSGESCHLOSSEN)
    total = sum(counts.get(m, 0) for m in MODI)

    assert total + ausgeschlossen_n == len(rows), "Unbekannte Kategorien in der Kodiertabelle gefunden"

    ranked = sorted(MODI, key=lambda m: counts.get(m, 0), reverse=True)

    print(f"Basis: {len(rows)} Zeilen, davon {ausgeschlossen_n} ohne Modusbezug/Dokumentationsnotizen, {total} moduskodierte Stellen.\n")
    print("| Modus | Anzahl | Anteil |")
    print("|---|---|---|")
    table_rows = []
    for m in ranked:
        n = counts.get(m, 0)
        anteil = 100 * n / total
        print(f"| {m} | {n} | {anteil:.1f} % |")
        table_rows.append([m, str(n), f"{anteil:.1f} %"])

    print(f"\n*Tabelle 2: Verteilung der {total} moduskodierten Stellen, Korpus 2.*")

    render_png(["Modus", "Anzahl", "Anteil"], table_rows)


if __name__ == "__main__":
    main()
