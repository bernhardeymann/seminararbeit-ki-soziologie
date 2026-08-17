"""
Erzeugt drei Abbildungen zum Korpus-Ueberblick als PNG (ohne Diagrammtitel,
da die Beschriftung als Bildunterschrift im Dokument steht). Alle drei zeigen
je zwei Balken pro Anbieter/Quelle/Jahr: Rohdaten (Segmente bzw. Texte) und,
in Kontrastfarbe, die Anzahl kodierter Stellen.

Abbildung 1: Satz-Segmente pro Anbieter, Korpus 1, plus kodierte Stellen
  Quelle: daten/korpus1/Eymann_Korpus1_clean.csv,
          daten/korpus1/Eymann_Kodiertabelle_Korpus1.csv
Abbildung 2: Texte pro Quelle, Korpus 2, plus kodierte Stellen
  Quelle: daten/korpus2/Eymann_Kodiertabelle_Korpus2.csv
Abbildung 3: Texte pro Erscheinungsjahr, Korpus 2, plus kodierte Stellen
  Quelle: daten/korpus2/Eymann_Kodiertabelle_Korpus2.csv

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
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "outputs"

plt.rcParams["font.size"] = 11

MODI_KORPUS2 = {"Defending", "Creating", "Negotiating", "Coalescing"}

FARBE_ROH = "#4c72b0"
FARBE_KODIERT = "#dd8452"


def abbildung1_segmente_pro_anbieter():
    with open(ROOT / "daten" / "korpus1" / "Eymann_Korpus1_clean.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    raw_counts = Counter(row["anbieter"] for row in rows)

    with open(ROOT / "daten" / "korpus1" / "Eymann_Kodiertabelle_Korpus1.csv", encoding="utf-8") as f:
        coded_rows = list(csv.DictReader(f))
    coded_counts = Counter(row["anbieter"] for row in coded_rows)

    ranked = raw_counts.most_common()
    labels = [k for k, _ in ranked][::-1]
    raw_values = [v for _, v in ranked][::-1]
    coded_values = [coded_counts.get(k, 0) for k in labels]

    y = np.arange(len(labels))
    h = 0.38

    fig, ax = plt.subplots(figsize=(12, 9))
    bars_roh = ax.barh(y + h / 2, raw_values, height=h, color=FARBE_ROH, label="Rohsegmente")
    bars_kod = ax.barh(y - h / 2, coded_values, height=h, color=FARBE_KODIERT, label="Kodierte Stellen")
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlabel("Anzahl")
    ax.bar_label(bars_roh, padding=3)
    ax.bar_label(bars_kod, padding=3)
    ax.set_xlim(0, max(raw_values) * 1.12)
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig(OUT / "Eymann_Korpus1_segmente_pro_anbieter.png", dpi=150)
    plt.close(fig)


def abbildung2_texte_pro_quelle():
    csv_path = ROOT / "daten" / "korpus2" / "Eymann_Kodiertabelle_Korpus2.csv"
    with open(csv_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    texte_pro_quelle = Counter()
    coded_pro_quelle = Counter()
    seen = set()
    for r in rows:
        if r["titel_datei"] not in seen:
            seen.add(r["titel_datei"])
            texte_pro_quelle[r["quelle"]] += 1
        if r["modus"] in MODI_KORPUS2:
            coded_pro_quelle[r["quelle"]] += 1

    ranked = texte_pro_quelle.most_common()
    labels = [k for k, _ in ranked][::-1]
    text_values = [v for _, v in ranked][::-1]
    coded_values = [coded_pro_quelle.get(k, 0) for k in labels]

    y = np.arange(len(labels))
    h = 0.38

    fig, ax = plt.subplots(figsize=(10, 7))
    bars_txt = ax.barh(y + h / 2, text_values, height=h, color=FARBE_ROH, label="Texte")
    bars_kod = ax.barh(y - h / 2, coded_values, height=h, color=FARBE_KODIERT, label="Kodierte Stellen")
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlabel("Anzahl")
    ax.set_xticks(range(0, 16))
    ax.bar_label(bars_txt, padding=3)
    ax.bar_label(bars_kod, padding=3)
    ax.set_xlim(0, 16)
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig(OUT / "Eymann_Korpus2_texte_pro_quelle.png", dpi=150)
    plt.close(fig)


def abbildung3_texte_pro_jahr():
    csv_path = ROOT / "daten" / "korpus2" / "Eymann_Kodiertabelle_Korpus2.csv"
    with open(csv_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    texte_pro_jahr = Counter()
    coded_pro_jahr = Counter()
    seen = set()
    for r in rows:
        if r["titel_datei"] not in seen:
            seen.add(r["titel_datei"])
            texte_pro_jahr[r["jahr"]] += 1
        if r["modus"] in MODI_KORPUS2:
            coded_pro_jahr[r["jahr"]] += 1

    jahre = sorted(texte_pro_jahr)
    text_values = [texte_pro_jahr[j] for j in jahre]
    coded_values = [coded_pro_jahr.get(j, 0) for j in jahre]

    x = np.arange(len(jahre))
    w = 0.38

    fig, ax = plt.subplots(figsize=(9, 6))
    bars_txt = ax.bar(x - w / 2, text_values, width=w, color=FARBE_ROH, label="Texte")
    bars_kod = ax.bar(x + w / 2, coded_values, width=w, color=FARBE_KODIERT, label="Kodierte Stellen")
    ax.set_xticks(x)
    ax.set_xticklabels(jahre)
    ax.set_xlabel("Erscheinungsjahr")
    ax.set_ylabel("Anzahl")
    ax.set_yticks(range(0, 15))
    ax.bar_label(bars_txt, padding=3)
    ax.bar_label(bars_kod, padding=3)
    ax.legend(loc="upper left")
    fig.tight_layout()
    fig.savefig(OUT / "Eymann_Korpus2_texte_pro_jahr.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    abbildung1_segmente_pro_anbieter()
    abbildung2_texte_pro_quelle()
    abbildung3_texte_pro_jahr()
    print("Abbildungen erzeugt.")
