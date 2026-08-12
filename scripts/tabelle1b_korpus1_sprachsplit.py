"""
Erzeugt Tabelle 1b: Verteilung der kodierten Stellen in Korpus 1 auf Beers
sechs Data-Imaginary-Dimensionen, aufgeschluesselt nach Sprache (Deutsch/
Englisch). Franzoesisch (n=1) wird aus Platzgruenden nur als Fussnote
gefuehrt, nicht als eigene Spalte. Neutral-Zeilen werden ausgeschlossen.

Quelle: daten/korpus1/Eymann_Kodiertabelle_Korpus1.csv
Ausgabe: Markdown-Tabelle auf stdout, PNG unter
         outputs/Eymann_Tabelle1b_korpus1_sprachsplit.png
"""

import csv
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "daten" / "korpus1" / "Eymann_Kodiertabelle_Korpus1.csv"
PNG_PATH = ROOT / "outputs" / "Eymann_Tabelle1b_korpus1_sprachsplit.png"

DIMENSIONEN = ["panoramisch", "smart", "schnell", "zugänglich", "enthüllend", "prophetisch"]


def render_png(header, rows):
    fig, ax = plt.subplots(figsize=(6.5, 0.45 * (len(rows) + 1)))
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

    dims = [r for r in rows if r["dimension"].strip() != "neutral"]
    de = Counter(r["dimension"].strip() for r in dims if r["sprache"].strip() == "de")
    en = Counter(r["dimension"].strip() for r in dims if r["sprache"].strip() == "en")
    fr = Counter(r["dimension"].strip() for r in dims if r["sprache"].strip() == "fr")

    n_de, n_en, n_fr = sum(de.values()), sum(en.values()), sum(fr.values())
    assert n_de + n_en + n_fr == len(dims)

    # Reihenfolge nach Gesamthaeufigkeit (wie Tabelle 1), damit beide Tabellen
    # vergleichbar bleiben
    total = Counter(r["dimension"].strip() for r in dims)
    ranked = sorted(DIMENSIONEN, key=lambda d: total.get(d, 0), reverse=True)

    print(f"Basis: {len(dims)} dimensionskodierte Stellen (deutsch n={n_de}, englisch n={n_en}, franzoesisch n={n_fr}).\n")
    print("| Dimension | gesamt (n=%d) | deutsch (n=%d) | englisch (n=%d) |" % (len(dims), n_de, n_en))
    print("|---|---|---|---|")
    table_rows = []
    for d in ranked:
        g, dd, ee = total.get(d, 0), de.get(d, 0), en.get(d, 0)
        print(f"| {d.capitalize()} | {g} | {dd} | {ee} |")
        table_rows.append([d.capitalize(), str(g), str(dd), str(ee)])

    print(f"\n*Tabelle 1b: Verteilung der {n_de} (deutsch) bzw. {n_en} (englisch) dimensionskodierten "
          f"Stellen, Korpus 1. Franzoesisch (n={n_fr}) nicht separat ausgewiesen.*")

    render_png(["Dimension", "gesamt", "deutsch", "englisch"], table_rows)


if __name__ == "__main__":
    main()
