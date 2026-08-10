"""
Erzeugt drei Abbildungen zum Korpus-Ueberblick als PNG (ohne Diagrammtitel,
da die Beschriftung als Bildunterschrift im Dokument steht). Abbildung 1/2
zeigen zusaetzlich die Kodierdichte je Anbieter/Quelle als Balkenbeschriftung.

Abbildung 1: Satz-Segmente pro Anbieter, Korpus 1, mit Kodierdichte
  (kodierte Stellen / Rohsegmente, in %)
  Quelle: daten/korpus1/Eymann_Korpus1_clean.csv,
          daten/korpus1/Eymann_Kodiertabelle_Korpus1.csv
Abbildung 2: Texte pro Quelle, Korpus 2, mit Anzahl kodierter Stellen
  Quelle: daten/korpus2/Eymann_Kodiertabelle_Korpus2_ENTWURF.csv
Abbildung 3: Texte pro Erscheinungsjahr, Korpus 2, mit Anzahl kodierter Stellen
  Quelle: daten/korpus2/Eymann_Kodiertabelle_Korpus2_ENTWURF.csv

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

MODI_KORPUS2 = {"Defending", "Creating", "Negotiating", "Coalescing"}


def abbildung1_segmente_pro_anbieter():
    with open(ROOT / "daten" / "korpus1" / "Eymann_Korpus1_clean.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    raw_counts = Counter(row["anbieter"] for row in rows)

    with open(ROOT / "daten" / "korpus1" / "Eymann_Kodiertabelle_Korpus1.csv", encoding="utf-8") as f:
        coded_rows = list(csv.DictReader(f))
    coded_counts = Counter(row["anbieter"] for row in coded_rows)

    ranked = raw_counts.most_common()
    labels = [k for k, _ in ranked][::-1]
    values = [v for _, v in ranked][::-1]
    dichte_labels = [f"{v} ({coded_counts.get(k, 0)} kod.)" for k, v in zip(labels, values)]

    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(labels, values, color="#4c72b0")
    ax.set_xlabel("Anzahl Satz-Segmente (Klammer: kodierte Stellen)")
    ax.bar_label(bars, labels=dichte_labels, padding=3)
    ax.set_xlim(0, max(values) * 1.2)
    fig.tight_layout()
    fig.savefig(OUT / "Eymann_Korpus1_segmente_pro_anbieter.png", dpi=150)
    plt.close(fig)


def abbildung2_texte_pro_quelle():
    csv_path = ROOT / "daten" / "korpus2" / "Eymann_Kodiertabelle_Korpus2_ENTWURF.csv"
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
    values = [v for _, v in ranked][::-1]
    dichte_labels = [f"{v} ({coded_pro_quelle.get(k, 0)} kod.)" for k, v in zip(labels, values)]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(labels, values, color="#4c72b0")
    ax.set_xlabel("Anzahl Texte (Klammer: kodierte Stellen)")
    ax.set_xticks(range(0, 13))
    ax.bar_label(bars, labels=dichte_labels, padding=3)
    ax.set_xlim(0, 14.5)
    fig.tight_layout()
    fig.savefig(OUT / "Eymann_Korpus2_texte_pro_quelle.png", dpi=150)
    plt.close(fig)


def abbildung3_texte_pro_jahr():
    csv_path = ROOT / "daten" / "korpus2" / "Eymann_Kodiertabelle_Korpus2_ENTWURF.csv"
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
    values = [texte_pro_jahr[j] for j in jahre]
    dichte_labels = [f"{v} ({coded_pro_jahr.get(j, 0)} kod.)" for j, v in zip(jahre, values)]

    fig, ax = plt.subplots(figsize=(9, 6))
    bars = ax.bar(jahre, values, color="#4c72b0")
    ax.set_xlabel("Erscheinungsjahr")
    ax.set_ylabel("Anzahl Texte (Klammer: kodierte Stellen)")
    ax.set_yticks(range(0, 15))
    ax.bar_label(bars, labels=dichte_labels, padding=3)
    fig.tight_layout()
    fig.savefig(OUT / "Eymann_Korpus2_texte_pro_jahr.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    abbildung1_segmente_pro_anbieter()
    abbildung2_texte_pro_quelle()
    abbildung3_texte_pro_jahr()
    print("Abbildungen erzeugt.")
