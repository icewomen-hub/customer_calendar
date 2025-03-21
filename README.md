# Aufgabenstellung/Ziel

Erstellen eines Kundenkalenders zur selbständigen Terminbuchung für die Kunden.

Erläuterung für Außenstehede:
Es wird eine Testdatenbank von Kunden benötigt.
Es wird eine Entscheidung getroffen, wie die Anwenderoberfläche aussehen soll.
Und auf welcher Basis dem Kunden der Terminkalender zur Verfügung gestellt werden soll. 

vorläufige Ordnerstruktur: s.u.

## Installation 

Externe Libraries:
- pandas
- pandastable
- tkinter
- tkcalendar

### Abhängigkeiten automatisiert auflösen

<code>customer_calendar %</code><kbd>pip install -r requirements.txt</kbd>
<pre>
<code>customer_calendar> Collecting pandastable==0.13.1 (from -r requirements.txt) ...</code>
</pre>

## Dateistruktur

### Verzeichnisse und Beschreibung

<pre><code>
├── customer_calendar
│   ├── data
│   ├── doq
│   ├── src
│   │   ├── core
│   │   ├── gui
    └── tests
</code></pre>

#### data

Bewegungs- und Stammdaten (als csv, xlsx und json)

#### src

Python Quelltext-Dateien

#### src/core

Generische Funktionalitäten

#### src/gui

Gui Elemente

#### tests

Unit Tests

### Dateien
<pre><code>
.
├── customer_calendar
│   ├── README.md
│   ├── README_TOO.md
│   ├── data
│   │   ├── CalendarLog.json
│   │   ├── Kursplan.xlsx
│   │   ├── calendar_log.json
│   │   ├── course_plan.xlsx
│   │   ├── customers_database.json
│   │   ├── kurs.csv
│   │   ├── passwd.csv
│   │   ├── time_slot.csv
│   │   ├── trainer.csv
│   │   └── wochentag.csv
│   ├── doq
│   │   ├── admin_customer_small.png
│   │   ├── cc_doq.ipynb
│   │   └── tech_doc.md
│   ├── main.py
│   ├── requirements.txt
│   ├── src
│   │   ├── core
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── calendar_log.py
│   │   │   ├── customer_calendar.py
│   │   │   ├── customers.py
│   │   │   ├── data_provider.py
│   │   │   └── table_helper.py
│   │   ├── gui
│   │   │   ├── __init__.py
│   │   │   ├── app.py
│   │   │   ├── app_new.py
│   │   │   ├── config.py
│   │   │   ├── login.py
│   │   │   ├── main.py
│   │   │   └── menu_helper.py
│   │   └── main.py
│   ├── tests
│   └── file.txt
</code></pre>

## Metriken

<pre><code>
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
JSON                             5              0              0           2020
Python                          23            312            100            819
Jupyter Notebook                 8              0            914            666
Markdown                         3             43              0            154
CSV                              5              0              0             44
-------------------------------------------------------------------------------
SUM:                            45            357           1014           3643
-------------------------------------------------------------------------------
</code></pre>
