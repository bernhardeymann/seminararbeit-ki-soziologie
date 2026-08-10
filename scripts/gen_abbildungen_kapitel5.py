"""
Erzeugt drei Abbildungen zum Korpus-Ueberblick als PNG (ohne Diagrammtitel,
da die Beschriftung als Bildunterschrift im Dokument steht).

Abbildung 1: Satz-Segmente pro Anbieter, Korpus 1
  Quelle: daten/korpus1/Eymann_Korpus1_clean.csv
Abbildung 2/3: Texte pro Quelle bzw. Erscheinungsjahr, Korpus 2
  Werte fest hinterlegt (Korpus-2-Metadaten)

Ausgabe: outputs/Eymann_Korpus1_segmente_pro_anbieter.png,
         outputs/Eymann_Korpus2_texte_pro_quelle.png,
         outputs/Eymann_Korpus2_texte_pro_jahr.png
"""

import csv
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "outputs"

plt.rcParams["font.size"] = 11


def abbildung1_segmente_pro_anbieter():
    csv_path = ROOT / "daten" / "korpus1" / "Eymann_Korpus1_clean.csv"
    with open(csv_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    counts = Counter(row["anbieter"] for row in rows)
    ranked = counts.most_common()
    labels = [k for k, _ in ranked][::-1]
    values = [v for _, v in ranked][::-1]

    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(labels, values, color="#4c72b0")
    ax.set_xlabel("Anzahl Satz-Segmente")
    ax.bar_label(bars, padding=3)
    ax.set_xlim(0, max(values) * 1.08)
    fig.tight_layout()
    fig.savefig(OUT / "Eymann_Korpus1_segmente_pro_anbieter.png", dpi=150)
    plt.close(fig)


def abbildung2_texte_pro_quelle():
    daten = [
        ("Anwaltsrevue", 11), ("NZZ", 2), ("AJP", 1), ("ZZZ", 1), ("SJ", 1),
        ("inside-it.ch", 1), ("HAVE", 1), ("Revue de l'avocat", 1),
        ("NZZ am Sonntag", 1), ("ZBJV", 1), ("unternehmensjurist", 1),
        ("plädoyer", 1),
    ]
    labels = [k for k, _ in daten][::-1]
    values = [v for _, v in daten][::-1]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(labels, values, color="#4c72b0")
    ax.set_xlabel("Anzahl Texte")
    ax.set_xticks(range(0, 13))
    ax.bar_label(bars, padding=3)
    ax.set_xlim(0, 12.5)
    fig.tight_layout()
    fig.savefig(OUT / "Eymann_Korpus2_texte_pro_quelle.png", dpi=150)
    plt.close(fig)


def abbildung3_texte_pro_jahr():
    jahre = ["2021", "2023", "2024", "2025", "2026"]
    values = [1, 4, 9, 4, 5]

    fig, ax = plt.subplots(figsize=(9, 6))
    bars = ax.bar(jahre, values, color="#4c72b0")
    ax.set_xlabel("Erscheinungsjahr")
    ax.set_ylabel("Anzahl Texte")
    ax.set_yticks(range(0, 11))
    ax.bar_label(bars, padding=3)
    fig.tight_layout()
    fig.savefig(OUT / "Eymann_Korpus2_texte_pro_jahr.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    abbildung1_segmente_pro_anbieter()
    abbildung2_texte_pro_quelle()
    abbildung3_texte_pro_jahr()
    print("Abbildungen erzeugt.")
