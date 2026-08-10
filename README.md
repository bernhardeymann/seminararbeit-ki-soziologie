# Seminararbeit: KI im Schweizer Recht — Data Imaginaries und Boundary Work im Vergleich

Bernhard Eymann · LUMACSS, Universität Luzern · Abgabe: 31. August 2026

Dieses Repository enthält die Code- und Datengrundlage für die Resultate in
Kapitel 5 der Seminararbeit. Der Fliesstext selbst ist nicht Teil des Repos.

## Inhalt

- `daten/korpus1/Eymann_Kodiertabelle_Korpus1.csv`,
  `daten/korpus2/Eymann_Kodiertabelle_Korpus2_ENTWURF.csv` — die kodierten
  Segmente (Zitat, Kategorie, Begründung), Basis für Tabelle 1/2 und die
  Hypothesenprüfung (Kapitel 5.2/5.3).
- `scripts/tabelle1_korpus1_dimensionen.py`,
  `scripts/tabelle2_korpus2_boundarywork.py` — erzeugen Tabelle 1 und
  Tabelle 2 aus den Kodiertabellen.
- `scripts/gen_abbildungen_kapitel5.py` — erzeugt Abbildung 1–3
  (Korpus-Überblick, Kapitel 5.1).
- `notebooks/Eymann_Erhebung_Korpus1.ipynb`,
  `notebooks/Eymann_Bereinigung_Korpus1.ipynb` — Erhebung und Aufbereitung
  von Korpus 1 (Kapitel 3/4).

Die Kandidatenidentifikation und Kodierung selbst erfolgte manuell (s.
Kapitel 4) und ist nicht als Code hinterlegt — die Kodiertabellen sind das
Ergebnis dieses Schritts.

## Ausführen

```bash
pip install -r requirements.txt
python scripts/tabelle1_korpus1_dimensionen.py
python scripts/tabelle2_korpus2_boundarywork.py
python scripts/gen_abbildungen_kapitel5.py
```
