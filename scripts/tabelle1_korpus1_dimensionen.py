"""
Erzeugt Tabelle 1: Verteilung der kodierten Stellen in Korpus 1 auf Beers
sechs Data-Imaginary-Dimensionen. Neutral-Zeilen werden ausgeschlossen.

Quelle: daten/korpus1/Eymann_Kodiertabelle_Korpus1.csv
Ausgabe: Markdown-Tabelle auf stdout, PNG unter
         outputs/Eymann_Tabelle1_korpus1_dimensionen.png
"""

import csv
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "daten" / "korpus1" / "Eymann_Kodiertabelle_Korpus1.csv"
PNG_PATH = ROOT / "outputs" / "Eymann_Tabelle1_korpus1_dimensionen.png"

# Reihenfolge und Anzeigenamen der sechs Beer-Dimensionen
DIMENSIONEN = ["panoramisch", "smart", "schnell", "zugänglich", "enthüllend", "prophetisch"]


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

    counts = Counter(row["dimension"].strip() for row in rows)
    neutral = counts.pop("neutral", 0)
    total = sum(counts[d] for d in DIMENSIONEN)

    assert total + neutral == len(rows), "Unbekannte Kategorien in der Kodiertabelle gefunden"

    # nach Haeufigkeit absteigend sortieren
    ranked = sorted(DIMENSIONEN, key=lambda d: counts.get(d, 0), reverse=True)

    print(f"Basis: {len(rows)} kodierte Stellen, davon {neutral} neutral, {total} dimensionskodiert.\n")
    print("| Dimension | Anzahl | Anteil |")
    print("|---|---|---|")
    table_rows = []
    for d in ranked:
        n = counts.get(d, 0)
        anteil = 100 * n / total
        print(f"| {d.capitalize()} | {n} | {anteil:.1f} % |")
        table_rows.append([d.capitalize(), str(n), f"{anteil:.1f} %"])

    print(f"\n*Tabelle 1: Verteilung der {total} dimensionskodierten Stellen, Korpus 1.*")

    render_png(["Dimension", "Anzahl", "Anteil"], table_rows)


if __name__ == "__main__":
    main()
