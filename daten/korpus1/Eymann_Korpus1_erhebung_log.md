# Erhebungsprotokoll Korpus 1 — Schweizer Legal-Tech/Legal-AI-Marketingtexte

Erhebungsdatum: 2026-07-20
Methode: Abruf der öffentlichen Startseiten via `mcp__workspace__web_fetch`, vorgängige Prüfung der jeweiligen `robots.txt`. Kein Anbieter musste wegen einer Root-Sperre (`Disallow: /`) übersprungen werden — bei allen 29 Domains, bei denen eine robots.txt gefunden wurde, war der Root-Pfad zugänglich (teils mit spezifischen Einschränkungen für einzelne Unterpfade oder einzelne KI-Trainings-Bots, z. B. swiss-noxtua.ch: `ClaudeBot`/`GPTBot`/`Google-Extended` für Training gesperrt, allgemeiner Zugriff aber erlaubt). Bei mehreren Domains (iuslex.ch, justement.ch, swisslex.ch, legaltech.weblaw.ch) existierte keine robots.txt (leere Antwort) — dies wurde als "nicht gesperrt" gewertet. Gegenlesart (nach externem Review 30.08.2026): Bei denselben Domains, allen voran swisslex.ch, blieb auch der Seitenabruf selbst wiederholt vollständig leer (s. Ergebnistabelle) — ein Muster, das eher für eine aktive WAF-/Bot-Abwehr spricht als für eine tatsächlich fehlende robots.txt. Die Wertung "nicht gesperrt" ist vertretbar (kein expliziter `Disallow` erhalten), schliesst diese Alternative aber nicht aus.

**Rechtliche Grundlage.** Die Zulässigkeit der Erhebung wurde oben rein technisch über robots.txt begründet. Ergänzend einschlägig für eine wissenschaftliche Arbeit: Art. 24d URG erlaubt die Vervielfältigung von Werken zu wissenschaftlichen Forschungszwecken, Art. 25 URG die Wiedergabe der hier publizierten kurzen Zitate. Beide Normen tragen die Erhebung und Publikation der Kodiertabellen unabhängig von der robots.txt-Konformität.

**KI-Trainingssperren und Selbstreflexion.** swiss-noxtua.ch sperrt laut robots.txt `ClaudeBot`/`GPTBot`/`Google-Extended` für Training, erlaubt aber allgemeinen Zugriff — die Erhebung selbst ist damit gedeckt. Bemerkenswert für eine Arbeit, die selbst KI-Werkzeuge einsetzt (Anhang E der Seminararbeit) und über professionelle Normen im Umgang mit KI schreibt: Diese Direktiven drücken eine Präferenz gegen KI-Verarbeitung aus, robots.txt regelt aber nur den Crawler-Zugriff, nicht die nachgelagerte Nutzung erhobener Inhalte.

## Ergebnistabelle

| Anbieter | Status | Wortanzahl (grob) | Anmerkung |
|---|---|---|---|
| DeepJudge | ok | ~450 | Vollständige Marketingprosa extrahiert (Hero, Produktbeschreibung, Testimonials, Kennzahlen) |
| iuslex.ch (IUS) | fehler | ~5 | Reine JS-SPA, liefert nur "Loading..." — bekanntes Problem laut Vorgabe |
| DeepLegal | ok | ~430 | Vollständig inkl. FAQ, Preistabelle, Vergleichstabelle |
| Justement | fehler | 0 | Drei Abrufversuche (root, /de, /de/) liefern komplett leere Antwort, auch keine Meta-Tags — bekanntes Problem laut Vorgabe |
| Legartis | ok | ~430 | Vollständig inkl. FAQ, Testimonials, Workflow-Beschreibung |
| Omnilex | ok | ~300 | Vollständig inkl. Preise, Team-Hintergrund (ETH/EPFL) |
| Herlock.ai | ok (teilweise) | ~150 | Stark dynamisch gerenderte SPA; Fliesstext zu Features/Preisen kaum auslesbar, nur Struktur/Testimonial-Zuordnungen und Team-Bios kamen durch |
| Lawise.ai (Jurilo) | ok | ~380 | Domain leitet auf jurilo.ch weiter (Rebranding); Inhalt vollständig |
| Bryter | ok | ~330 | Vollständig inkl. Produktmodule und Anwendungsfälle |
| Swisslex | fehler | 0 | Wiederholt (3x) komplett leere Antwort ohne jeglichen Inhalt, auch robots.txt leer — Ursache unklar |
| CASUS | ok | ~380 | Domain leitet auf getcasus.com weiter; vollständig inkl. Preise, Gründerzitat |
| Leya | ok | ~350 | Domain leitet vollständig auf legora.com weiter (Marke wurde zu "Legora" umbenannt); Inhalt vollständig |
| balo.ai | ok | ~180 | Vollständig, kurze Seite (Nischenanbieter Anonymisierung) |
| ExNunc Intelligence | fehler | ~15 | Domain ist reine Hosting-Platzhalterseite ("site en construction"); operatives Produkt wird unter separater Domain silex.legal vermarktet (dort erfolgreich erhoben) |
| Laine | ok | ~420 | Vollständig inkl. FAQ, Positionierung gegenüber "General AI"/"Copilot" |
| whisperit | ok | ~380 | Vollständig inkl. Testimonials, Praxisgebiete, Sicherheit |
| Contractus Intelligence | ok | ~420 | Vollständig inkl. ROI-Rechner-Beispiel, Kundenstimmen |
| IPQuants | ok | ~350 | Vollständig inkl. Kundenzitate, Kennzahlen |
| Weblaw/LegalTechHub | ok (eingeschränkt) | ~150 | Seite ist primär eine Filter-/Verzeichnis-UI (Marktplatz), wenig eigenständiger Marketing-Fliesstext vorhanden |
| BetterCallClaude | fehler | ~10 | Reine JS-SPA (Lovable-Plattform), nur Meta-Tags auslesbar, kein Body-Text (2 Versuche) |
| Abacus Law | ok | ~350 | Vollständig inkl. Ökosystem-Produkte, Integrationen |
| DocIQ | ok | ~450 | Vollständig inkl. FAQ-Themen, Firmengeschichte seit 2017 |
| Lexplorer | ok | ~350 | Vollständig inkl. Vergleichstabelle, Kennzahlen |
| Libra | ok | ~330 | Vollständig inkl. Testimonial, Sicherheit |
| Silex | ok | ~380 | Vollständig inkl. zahlreicher Anwaltszitate, Kennzahlen |
| Jurata | ok | ~330 | Vollständig inkl. zwei Nutzerpfade, Enterprise-Angebot |
| Lawcodex | fehler | ~10 | Reine JS-SPA, nur Meta-Tags auslesbar, kein Body-Text (2 Versuche) |
| Elisa/legalis | ok | ~280 | Vollständig inkl. FAQ zu Preisen/Zugang |
| Swiss-Noxtua | ok | ~350 | Vollständig inkl. USPs, Funktionsübersicht |

## Zusammenfassung

**23 von 29 Anbietern erfolgreich erhoben, 6 fehlgeschlagen.**

Fehlgeschlagene Anbieter und Gründe:
1. **iuslex.ch (IUS)** — clientseitige JS-SPA liefert nur "Loading...", kein Fliesstext.
2. **Justement** — Seite liefert bei allen Abrufversuchen (root, /de) komplett leeren Inhalt (kein Body, keine Meta-Tags).
3. **Swisslex** — wiederholt vollständig leere Antwort, auch keine robots.txt; Ursache unklar (evtl. Bot-Erkennung).
4. **ExNunc Intelligence** — Domain ist eine unbenutzte Hosting-Platzhalterseite; das tatsächliche Produkt (Silex) läuft unter der eigenständigen Domain silex.legal, die separat erfolgreich erhoben wurde.
5. **BetterCallClaude** — JS-SPA (Lovable), nur HTML-Metadaten ohne Fliesstext auslesbar.
6. **Lawcodex** — JS-SPA, nur HTML-Metadaten ohne Fliesstext auslesbar.

Keine Sperrung durch robots.txt war für einen der 29 Anbieter der Grund für ein Auslassen; alle Fehlschläge sind technischer Natur (clientseitiges Rendering ohne Server-Side-Rendering bzw. leere/blockierte Antworten). Bei zwei Anbietern (Leya→Legora, CASUS→getcasus.com, Lawise.ai→jurilo.ch) erfolgte eine automatische Weiterleitung auf eine umbenannte bzw. konsolidierte Marke/Domain; der dort abgerufene Inhalt wurde trotzdem für den ursprünglich gelisteten Anbieter verwendet, da es sich um dieselbe Unternehmung/dasselbe Produkt handelt (im Rohtext jeweils vermerkt).

Für die fehlgeschlagenen JS-SPA-Fälle wird empfohlen, den Nachauf mit einem Browser-Rendering-Tool (z. B. Chrome-Extension/Headless-Browser) statt reinem `web_fetch` zu wiederholen, falls diese Anbieter für Korpus 1 zwingend benötigt werden.

## Nachtrag 10.08.2026: Korrektur Sprachauswahl bei drei Anbietern

Bei der Erstellung dieses Protokolls war keine explizite Regel dokumentiert, welche Sprachversion einer mehrsprachigen Website erhoben werden soll. Eine nachträgliche Prüfung ergab, dass bei drei Anbietern (Abacus Law, Jurata, Omnilex) die englische Version erfasst wurde, obwohl die jeweilige Wurzel-URL ohne Sprachpfad standardmässig Deutsch anzeigt (verifiziert durch erneuten Abruf ohne Sprachpfad/mit Sprachumschalter-Prüfung). Bei den übrigen 25 Anbietern wurde stichprobenartig geprüft, ob die erfasste Sprache der Standardsprache der Seite entspricht; Abweichungen wurden nur bei diesen drei gefunden (u. a. Legartis, DocIQ, Silex, Lawise.ai/Jurilo bestätigt als tatsächlich englischsprachig bzw. mit Englisch als Standard). Die drei betroffenen Startseiten wurden am 10.08.2026 in der deutschen Standardversion neu erhoben, neu segmentiert (`Eymann_Korpus1_clean.csv`) und neu kodiert (`Eymann_Kodiertabelle_Korpus1.csv`); die alten englischsprachigen Segmente/Codes für diese drei Anbieter wurden entfernt. Neu verwendete URLs: abacus.ch/law, jurata.ch, omnilex.ai (jeweils ohne Sprachpfad). Regel für künftige Erhebungen: massgebend ist die Sprachversion, die beim Aufruf der Wurzel-URL ohne Sprachpfad angezeigt wird.

## Nachtrag 10.08.2026 (Fortsetzung): Vier Einzelfälle nachgeprüft

**Swisslex/Lawcodex-Verwechslung (behoben).** Bei der Nachprüfung zeigte sich, dass die unter "Swisslex" erfassten 10 Segmente inhaltlich eindeutig Lawcodex zuzuordnen sind (u. a. "Our technology, your brand", "marque blanche"-Positionierung, Steupla Sàrl/Lausanne als Betreiberin), während die unter "Lawcodex" erfassten 41 Segmente inhaltlich eindeutig Swisslex zuzuordnen sind (u. a. "Swisslex 6.0", "Since 1986, Swisslex has been Switzerland's most comprehensive legal database"). Die beiden Anbieterlabels wurden bei einem früheren Bearbeitungsschritt offenbar vertauscht (beide ursprünglich als Fehlschlag protokolliert, Inhalt vermutlich später manuell nachgetragen und dabei verwechselt). Korrigiert am 10.08.2026: `anbieter`- und `quelle_url`-Feld für alle betroffenen Zeilen in `Eymann_Korpus1_clean.csv` und `Eymann_Kodiertabelle_Korpus1.csv` getauscht (Text, Sprache, ID und Kodierung unverändert). Betrifft auch Zitate in Kapitel 5.2.2/5.4.1 (dort korrigiert). Reine Sprache/Dimensionen-Verteilung (Tabelle 1/1b) ist von diesem Fix nicht betroffen, nur die Anbieterzuordnung.

Ob die jetzt korrekt zugeordneten Lawcodex- und Swisslex-Segmente (beide Englisch) der jeweiligen Standardsprache der Website entsprechen, liess sich nicht abschliessend klären: lawcodex.ch ist eine clientseitig gerenderte SPA, die bei erneutem Abruf ohne Sprachpfad Französisch als Standardsprache zeigt (og:locale fr_CH), aber keinen auslesbaren Seitentext liefert, weder auf Französisch noch auf Englisch — ein Vergleich ist mit den verfügbaren Mitteln nicht möglich. swisslex.ch liefert bei jedem Abrufversuch eine leere Antwort (deckt sich mit dem ursprünglichen Fehlschlag im Protokoll). Beide bleiben unkorrigiert, da keine belastbare Evidenz für einen Fehlgriff vorliegt (anders als bei Abacus/Jurata/Omnilex, wo der Sprachumschalter der Seite den Standard eindeutig auf Deutsch zeigte).

**CASUS (kein Bias).** getcasus.com (Weiterleitungsziel von casus.ch) zeigt bei Abruf ohne Sprachpfad "EN" als aktiven Sprachumschalter; die im Korpus erfasste englische Version entspricht damit der Standardsprache der Seite. Keine Korrektur nötig.

**Silex (uneinheitlich, nicht korrigiert).** Bei erneutem Abruf zeigt die Wurzel-URL silex.legal/ Französisch als Standardsprache (Sprachumschalter "fr" aktiv, EN/DE/IT wählbar). Die im Korpus erfassten 13 Segmente sind jedoch praktisch vollständig Englisch, obwohl als Quelle dieselbe Wurzel-URL ohne Sprachpfad vermerkt ist. Anders als bei Abacus/Jurata/Omnilex handelt es sich hier vermutlich nicht um eine falsch gewählte URL, sondern um serverseitige Sprachaushandlung (Accept-Language-Header), die je nach Abrufzeitpunkt oder verwendetem Tool unterschiedlich ausfallen kann: Die Erhebung erhielt offenbar Englisch, die heutige Nachprüfung Französisch, bei identischer URL. Eine Korrektur würde deshalb nur eine von mehreren plausiblen Sprachversionen durch eine andere ersetzen, nicht einen dokumentierten Fehler beheben. Nicht korrigiert; als Limitation in Kapitel 6.6 vermerkt.

## Nachtrag 10.08.2026 (Fortsetzung 2): Manuelle Verifikation durch Bernhard, radikale Neuerhebung

Die automatisierten Sprachprüfungen oben erwiesen sich als teilweise unzuverlässig (serverseitige Sprachaushandlung je nach Accept-Language-Header des abrufenden Tools). Bernhard prüfte daraufhin alle 16 zu diesem Zeitpunkt noch englischsprachig im Korpus vertretenen Anbieter manuell im eigenen Browser (Schweizer/deutsche Spracheinstellung). Ergebnis: 11 der 16 Anbieter zeigen bei ihm direkt eine deutsche Startseite (bettercallclaude, getcasus.com/CASUS, dociq.io, lawcodex.ch, jurilo.ch, legartis.ai, libratech.ai, silex.legal, swisslex.ch, whisperit.ai) — im Widerspruch zur automatisierten Prüfung, die für CASUS "kein Bias" und für Silex "uneinheitlich" ergeben hatte. Bryter wurde bei dieser Gelegenheit als ohne erkennbaren Schweiz-Bezug identifiziert und ausgeschlossen (s. `Eymann_Anbieterliste_Korpus1.md`). Vorgehen: automatisierte Neuerhebung der deutschen Version zuerst versuchen, bei Fehlschlag Bernhards manuelle Angabe verwenden.

Automatisiert erfolgreich neu erhoben, neu segmentiert und neu kodiert (10.08.2026): **CASUS** (getcasus.com/de, inkl. /de/pricing für Preise/Sicherheit — Hauptseite ohne Sprachpfad lieferte beim erneuten Abruf teils nur Meta-Tags), **Lawise.ai/Jurilo** (jurilo.ch/de), **Legartis** (legartis.ai/de), **Libra** (libratech.ai/de), **Silex** (silex.legal/de), **whisperit** (whisperit.ai/de). Die alten englischsprachigen Segmente/Codes dieser sechs Anbieter wurden vollständig entfernt (201 Zeilen in `Eymann_Korpus1_clean.csv`, 12 Zeilen in `Eymann_Kodiertabelle_Korpus1.csv`) und durch 152 neue deutsche Segmente (18 neue Kodierungen) ersetzt, IDs 1005–1156. Die frühere Einschätzung "CASUS: kein Bias" und "Silex: nicht korrigiert" oben ist damit überholt.

**Legartis, Segment 185 (Sonderfall).** Das zentrale, in Kapitel 5.4.3 namengebend zitierte Zitat ("Legal expertise, not generic AI [...] developed by lawyers and thinks like them") hat auf der deutschen Seite eine wörtliche Entsprechung: *"Juristische Expertise, keine generische KI: Legartis wurde von Jurist:innen entwickelt und denkt wie sie."* Nach Rücksprache mit Bernhard 1:1 ersetzt (neue ID 1077, weiterhin kodiert als `smart`); die Argumentation in 5.4.3 bleibt inhaltlich unverändert, da beide Sprachversionen dieselbe Aussage treffen.

**DeepLegal (kein Bias, Label-Fix).** Bernhards manueller Befund ("kommt bei mir direkt auf Deutsch") deckt sich mit dem Korpus: von 110 erfassten Segmenten sind 105 bereits als `de` markiert. Die verbleibenden 5 (`en`) sind reine Preis-Fragmente ohne Sprachgehalt (z. B. "Small CHF 19.00 /mtl."), fälschlich als Englisch gelabelt — am 10.08.2026 auf `de` korrigiert. Keine Neuerhebung nötig.

**Noch offen.** Vier Anbieter liefern weiterhin keinen auslesbaren Seitentext beim automatisierten Abruf (bettercallclaude.ch/de: reine JS-SPA, nur Meta-Tags; dociq.io/de: leere Antwort; lawcodex.ch/de: nur Meta-Tags, Locale zeigt weiterhin Französisch; swisslex.ch/de: leere Antwort). Bernhard liefert hierzu den deutschen Seitentext manuell nach; Neuerhebung folgt als separater Schritt, danach konsolidiertes Update von Kapitel 3/5/6 und Tabelle 1/1b/Abbildung 1 für alle 11 Anbieter gemeinsam.

Neuer Sprachsplit nach dieser Korrekturrunde: 845 Segmente gesamt (unverändert 27 Anbieter), davon 527 Deutsch (62,4 %), 306 Englisch (36,2 %), 12 Französisch (1,4 %) — vorher 894 Segmente mit 56,8 % Englisch/41,6 % Deutsch/1,6 % Französisch.

## Nachtrag 10.08.2026 (Abschluss): Letzte 4 Anbieter via manuellem Konsolen-Snapshot

Die verbleibenden vier Anbieter (BetterCallClaude, DocIQ, Lawcodex, Swisslex) liessen sich mit `mcp__workspace__web_fetch` wiederholt nicht abrufen (reine JS-SPA ohne Server-Rendering bzw. leere Antworten). Bernhard hat die deutschen Startseiten daher wie beim ursprünglichen Korpusaufbau selbst im Browser geöffnet und via Konsole (F12) mit `copy(document.documentElement.outerHTML)` als vollständig gerenderten DOM-Snapshot gesichert (`daten/korpus1/manuell/<anbieter>_de.html`). Die vier HTML-Dateien wurden mit BeautifulSoup ausgelesen, der Haupttext manuell von Navigation/Footer bereinigt, satzweise segmentiert und nach Beers Codierregeln kodiert.

Ersetzt (alte Segmente/Codes vollständig entfernt, neue IDs 1157–1224): **BetterCallClaude** (52 alte EN-Zeilen → 20 neue DE-Zeilen, 3 kodiert), **DocIQ** (85 EN + 4 FR → 18 DE, 3 kodiert), **Lawcodex** (10 EN → 9 DE, 3 kodiert), **Swisslex** (23 DE + 18 EN gemischt → 21 DE einheitlich aus derselben Quelle, 4 kodiert). Bei Swisslex wurde der bereits teilweise deutsche Altbestand trotzdem vollständig ersetzt, um eine einheitliche, konsistente Quelle (derselbe Snapshot) für alle Segmente dieses Anbieters zu haben, statt zwei uneinheitliche Teilerhebungen zu vermischen.

## Nachtrag 30.08.2026: Externes Review der Scraping-Praxis, Code-Korrekturen

Ein externes Review bestätigte die Erhebung insgesamt als vorbildlich (identifizierbarer User-Agent mit Kontaktadresse, robots.txt-Prüfung vor jedem Abruf, konservatives Rate-Limiting, kein UA-Spoofing/Stealth/Proxy-Rotation, respektvoller manueller Fallback statt technischer Umgehung von Bot-Sperren, datensparsame `.gitignore`). Vier kleinere technische Punkte wurden daraufhin in `notebooks/Eymann_Erhebung_Korpus1.ipynb` korrigiert:

1. **`robots_check`-Fehlerpfad (RFC 9309 §2.3.1.4):** Behandelte zuvor jede Exception (auch 5xx/Netzwerk-Timeout) pauschal als "erlaubt". Auf `requests`-basierten Abruf mit expliziter Statuscode-Unterscheidung umgestellt: 404/sonstige 4xx weiterhin als "keine Einschränkung", 401/403 sowie 5xx/technisch nicht erreichbar neu als vorübergehend vollständig gesperrt. Bei den tatsächlich erhobenen 29 Domains ohne Netzwerkfehler ändert das nichts am bereits erhobenen Korpus.
2. **Playwright-User-Agent:** liess zuvor die Kontaktadresse weg (inkonsistent zum `requests`-Pfad); jetzt identisch mit Cell 7.
3. **`Accept-Language`-Header:** fehlte im `requests`-Pfad; Ursache des Silex-Falls (s. Nachtrag 10.08.2026: serverseitige Sprachaushandlung lieferte je nach Tool Französisch oder Englisch). Jetzt `de-CH,de;q=0.9` in `requests`- und Playwright-Pfad, für künftige Nacherhebungen deterministisch.
4. **robots.txt-Caching:** wurde zuvor pro Anbieter und pro Erhebungsschleife neu geholt; jetzt pro Domain gecacht.

Zusätzlich per `page.route` Bilder/Fonts/Medien im Playwright-Pfad geblockt (reduziert Serverlast bei `wait_until="networkidle"`). Keine dieser Korrekturen erfordert eine Neuerhebung der bereits publizierten Kodiertabellen.

**Alle 11 Anbieter aus Aufgabe #34 sind damit abgeschlossen.** Finaler Sprachsplit: 721 Segmente gesamt (weiterhin 27 Anbieter — die Segmentzahl sinkt gegenüber der ursprünglichen Erhebung, da die deutschen Originaltexte durchgehend weniger redundant/aufgebläht sind als die vielfach dopplungsreichen englischen Framer/Webflow-Exporte, und da Nicht-Marketing-Inhalte wie Cookie-Banner konsequent ausgeschlossen wurden): 572 Deutsch (79,3 %), 141 Englisch (19,6 %), 8 Französisch (1,1 %). Kodiertabelle: 68 Zeilen, davon 56 Deutsch (82,4 %), 11 Englisch, 1 Französisch — damit beruht die Dimensionsverteilung für H1 nun ganz überwiegend auf deutschsprachigem Material, was den in Gutachtenpunkt A1 kritisierten Sprachbias strukturell behebt. Nächster Schritt: konsolidiertes Update von Kapitel 3/4/5/6 sowie Tabelle 1/1b und Abbildung 1 (Aufgabe #35).
