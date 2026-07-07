# Seminararbeit: KI im Schweizer Recht — Data Imaginaries und Boundary Work im Vergleich

Bernhard Eymann · LUMACSS, Universität Luzern · Abgabe: 31. August 2026

Details zu Forschungsfrage, Theorie und Methodik: siehe `PROJEKTDOSSIER.md`.
Workflow und Arbeitspakete: siehe `Workflow_Arbeitspakete.md`.

## Ordnerstruktur

```
daten/korpus1/      Rohtexte & bereinigtes Korpus Legal-Tech (Web Scraping)
daten/korpus2/      PDFs & bereinigtes Korpus Rechtsdiskurs (Jusletter, Anwaltsrevue, SAV)
notebooks/          Jupyter-Notebooks, ein Notebook pro Arbeitsschritt
outputs/            Grafiken, Tabellen, Analyseergebnisse
exzerpte/           Obsidian-Exzerpte der Theorie-/Seminarliteratur
literatur/          PDFs der Pflicht- und Zusatzlektüre
references.bib      Literaturverzeichnis (BibTeX)
```

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

Dieser Ordner wird über kDrive cloud-synchronisiert. Cloud-Sync-Ordner sind für Git
ungeeignet: Git benötigt atomare Rename-Operationen für Locks/Refs, die vom
Sync-Client blockiert bzw. mit den Cowork-Dateizugriffsregeln verhindert werden
(`git init` hat hier wiederholt eine korrupte `.git/config` erzeugt).

**Empfehlung:** Das Git-Repository lokal ausserhalb des kDrive-Ordners anlegen
(z.B. `~/dev/seminararbeit-ki-recht/`), dort mit `git init` starten, remote auf
GitHub verbinden (`gh repo create` oder manuell) und die Dateien aus diesem Ordner
hinein kopieren bzw. symlinken. `requirements.txt`, `environment.yml` und
`.gitignore` liegen bereits fertig hier im Projektordner und können 1:1
übernommen werden.

Alternativ: Sync für den lokalen Git-Ordner in den kDrive-Ausschlusslisten
deaktivieren, falls das Repo doch im selben Pfad liegen soll.
