# Seminararbeit: KI im Schweizer Recht — Data Imaginaries und Boundary Work im Vergleich

Bernhard Eymann · LUMACSS, Universität Luzern · Abgabe: 31. August 2026

Dieses Repository dokumentiert Code und Daten-Pipeline der Seminararbeit
(Web Scraping, Datenaufbereitung, Kodierung, Abbildungen/Tabellen). Der
Fliesstext der Arbeit selbst ist nicht Teil dieses Repos (s. "Versionierung"
unten).

## Ordnerstruktur

```
daten/korpus1/      Rohtexte & bereinigtes Korpus Legal-Tech (Web Scraping)
daten/korpus2/      PDFs & bereinigtes Korpus Rechtsdiskurs (Jusletter, Anwaltsrevue, SAV)
notebooks/          Jupyter-Notebooks, ein Notebook pro Arbeitsschritt
scripts/            Python-Skripte für Abbildungen und Tabellen (Kapitel 5)
outputs/            Grafiken, Tabellen, Analyseergebnisse
exzerpte/           Obsidian-Exzerpte der Theorie-/Seminarliteratur
literatur/          PDFs der Pflicht- und Zusatzlektüre
references.bib      Literaturverzeichnis (BibTeX)
```

Nicht alles hier liegt auch im öffentlichen GitHub-Repo — siehe Abschnitt
"Versionierung" unten und `.gitignore`.

## Namenskonvention

- Notebooks: `Eymann_[Schritt].ipynb` (z.B. `Eymann_Erhebung_Korpus1.ipynb`)
- Datendateien: `Eymann_[Datei].csv`
- Code-Kommentare: Deutsch

## Python-Umgebung einrichten

**Mit conda:**
```bash
conda env create -f environment.yml
conda activate seminararbeit-ki-recht
```

**Mit venv:**
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Versionierung (GitHub)

Repo: https://github.com/bernhardeymann/seminararbeit-ki-soziologie (öffentlich)

Das Git-Repository liegt direkt in diesem (kDrive-synchronisierten) Projektordner.
`git init`/`commit`/`push` funktionieren hier über ein lokales Terminal einwandfrei
— nur ein direkter `git init`-Versuch aus der Cowork-Sandbox heraus schlug wegen
deren Dateizugriffsregeln fehl (korrupte `.git/config`). Falls kDrive-Sync
während eines Commits aktiv eingreift (seltene "bad config"-Fehler), Sync für den
Ordner kurz pausieren, Befehl wiederholen, danach wieder aktivieren.

**Was NICHT im Repo landet** (siehe `.gitignore`):
- `daten/` (mit einer Ausnahme, s.u.) — Drittquellen-Volltexte (CSV/PDF/HTML),
  teils urheberrechtlich geschützt (Jusletter/Anwaltsrevue via
  Bibliothekszugang, gescraptes Legal-Tech-Marketingmaterial), sowie interne
  Arbeitsnotizen (Anbieterliste, Workflow, Erhebungslog, Codierregeln in
  Arbeitsfassung)
- `literatur/*.pdf` — Volltexte der Pflichtlektüre
- `exzerpte/` — enthält wörtliche Zitate aus copyright-geschütztem Material
- `Eymann_Proposal*`, `PROJEKTDOSSIER.md`, `Workflow_Arbeitspakete.md` — private
  Entwürfe, Kontaktdaten, interne Planung
- `Eymann_Kapitel_*`, `Eymann_Anhang_*`, `Eymann_Gliederung*` u.a. — der
  Fliesstext der Seminararbeit selbst, inkl. kompilierter Exporte in `outputs/`
- venv/conda-Umgebungen, Caches, Zugangsdaten

Im Repo landen: `notebooks/`, `scripts/`, `references.bib`,
`requirements.txt`, `environment.yml`, `README.md`, `.gitignore`, sowie als
bewusste Ausnahme aus `daten/` die beiden finalen Kodiertabellen
(`Eymann_Kodiertabelle_Korpus1_ENTWURF.csv`,
`Eymann_Kodiertabelle_Korpus2_ENTWURF.csv`) — sie enthalten kurze, einzelne
Zitatstellen mit Quellenangabe (keine ganzen Texte) und bilden die
Nachvollziehbarkeitsgrundlage für Tabelle 1/2 in Kapitel 5. Alles zusammen
ist, was für Reproduzierbarkeit und Code-Nachvollziehbarkeit nötig ist, ohne
geschützte Volltexte, private Notizen oder den Arbeitstext selbst offenzulegen.
