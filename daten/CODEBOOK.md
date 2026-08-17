# Codebook: Kodiertabellen Korpus 1 und Korpus 2

Erklärt Spalten und Wertebereiche der beiden öffentlich einsehbaren
Kodiertabellen. Für die inhaltlichen Kodierregeln (Definitionen der
Kategorien, Abgrenzungskriterien, Beispiele) siehe Anhang A (Beers sechs
Data-Imaginary-Dimensionen) und Anhang B (Faulconbridges vier
Boundary-Work-Modi) der Arbeit.

## `daten/korpus1/Eymann_Kodiertabelle_Korpus1.csv`

Kodierte Segmente aus den Startseiten von 27 Schweizer Legal-Tech-Anbietern,
klassifiziert nach Beers sechs Data-Imaginary-Dimensionen (H1).

| Spalte | Typ | Beschreibung |
|---|---|---|
| `anbieter` | Text | Name des Legal-Tech-Anbieters (27 eindeutige Werte). |
| `sprache` | Kategorie | Sprache des Segments: `de`, `en`, `fr`. |
| `id` | Zahl | Segment-ID, referenziert in der Arbeit als "K1, Segment N". |
| `zitat` | Text | Das kodierte Satz-Segment im Original­wortlaut. |
| `dimension` | Kategorie | Zugeordnete Beer-Dimension: `schnell`, `zugänglich`, `enthüllend`, `panoramisch`, `prophetisch`, `smart`, oder `neutral` (kein erkennbarer Dimensionsbezug, z. B. FAQ, Rechtsklauseln — fliesst nicht in die H1-Auszählung ein). |
| `zweitkategorie_grenzfall` | Kategorie, optional | Nur befüllt, wenn ein explizites sprachliches Signal eine plausible zweite Dimension stützt (s. Kapitel 4.2). Enthält den Namen dieser Zweitkategorie. |
| `begruendung` | Text | Kurze Begründung der Kategorienzuordnung. |

## `daten/korpus2/Eymann_Kodiertabelle_Korpus2.csv`

Kodierte Textstellen aus 23 Texten des schweizerischen Rechts-
professionsdiskurses, klassifiziert nach Faulconbridges vier
Boundary-Work-Modi (H2), plus zwei vertiefende Klassifikationsdurchgänge
(Nachvollziehbarkeit, Zielscheibe von Defending).

| Spalte | Typ | Beschreibung |
|---|---|---|
| `id` | Zahl | Zeilen-ID, referenziert in der Arbeit als "K2, Zeile N". |
| `titel_datei` | Text | Dateiname des Quelltexts. |
| `quelle` | Kategorie | Publikationsorgan (z. B. `Anwaltsrevue`, `NZZ`, `AJP`, `plädoyer`; 12 eindeutige Werte). |
| `jahr` | Zahl | Erscheinungsjahr (2021–2026). |
| `pre_post` | Kategorie | `pre`/`post` relativ zum ChatGPT-Launch (November 2022). Deskriptive Zusatzinformation, kein formal getesteter Faktor. |
| `zitat` | Text | Die kodierte Textstelle im Originalwortlaut. |
| `modus` | Kategorie | Zugeordneter Boundary-Work-Modus: `Defending`, `Creating`, `Negotiating`, `Coalescing`, oder `neutral` (kein Boundary Work). Zusätzlich zwei Prozessmarker ohne inhaltlichen Kodierwert: `Methodenfrage` (dokumentierte methodische Unsicherheit) und `Korrektur` (Korrekturvermerk zu einem früheren Bearbeitungsstand) — beide fliessen nicht in die H2-Auszählung (37 moduskodierte Stellen) ein. |
| `zweitkategorie_grenzfall` | Kategorie, optional | Analog zu Korpus 1: befüllt bei plausibler zweiter Modus-Zuordnung, Format `Modus1/Modus2`. |
| `begruendung` | Text | Kurze Begründung der Modus-Zuordnung. |
| `nachvollziehbarkeit_rolle` | Kategorie, optional | Nur befüllt für Defending-Stellen, die sich auf menschliche Kontrolle/Verantwortung/Prüfung berufen (s. Kapitel 6.5). Werte: `kein_bezug` (kein Kontrollargument), `thematisiert` (explizit als Anforderung benannt), `praemisse` (als unbegründete Voraussetzung behandelt), `problematisiert` (die behauptete Kontrolle selbst wird infrage gestellt). |
| `beer_dimension_ziel` | Kategorie, optional | Nur befüllt für die 31 Defending-Stellen (s. Kapitel 6.4.3). Gegen welche Beer-Dimension sich die Abwehr richtet: `schnell`, `panoramisch`, `prophetisch`, `enthüllend`, `smart`, oder `andere` (kein erkennbarer Dimensionsbezug, z. B. Empathie- oder Konkurrenzargumente). |
| `beer_dimension_ziel_begruendung` | Text, optional | Begründung der Zielscheiben-Zuordnung in der Spalte davor. |

## Hinweise

- Alle Kodierung ist Einzelkodierung ohne unabhängige Zweitkodierung (s.
  Kapitel 6.6.4).
- Leere Zellen (`NaN` beim Einlesen mit pandas) bedeuten "nicht zutreffend
  bzw. nicht erhoben", nicht "Wert unbekannt".
- Rechtschreibung in `zitat`- und `begruendung`-Feldern kann von der
  Originalquelle abweichende Umlaut-Schreibweisen enthalten (ae/oe/ue statt
  ä/ö/ü), Artefakt der ursprünglichen Erhebung.
