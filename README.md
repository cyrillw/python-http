# Dokumentation

## Git repository klonen

Das Git repository mit folgendem Befehl klonen:

```
git clone https://github.com/cyrillw/python-http.git
```

## Anleitung zur Nutzung des Programms

Standardmässig benutzen alle Kommandos die URL **https://httpbin.org**. Über den Parameter `--url` kann eine andere URL
angegeben werden.

Einige Kommandos besitzen zusätzliche Parameter. Eine Übersicht aller verfügbaren Parameter kann mit folgendem Befehl
angezeigt werden:

```
python myproject.py --help
```

### Verfügbare Kommandos

Die verfügbaren Kommandos sind:

- html-tag
- get
- post
- list-cookies
- screenshot

Die Kommandos können alle über das `myproject.py` script im Verzeichnis `python-http` ausgeführt werden. Die Details
dazu sind in den folgenden Kapiteln zu finden.

### Command Html-Tag

Mit diesem Kommando kann der Inhalt eines bestimmten HTML-Tags aus einer Webseite ausgelesen werden (Tag Scraping).

**Beispiel**

```
python myproject.py body
```

Das Script ruft die Standard-URL https://httpbin.org auf und gibt den Inhalt des `<body>` Tags zurück.

Es kann auch eine andere URL & ein anderes Tag angegeben werden:

```
python myproject.py title --url https://example.com
```

### Command get

Das get Kommando ruft eine Webseite mit einem HTTP GET Request auf und gibt den Inhalt der Seite zurück.

Zusätzlich können Query Parameter mit `--param` übergeben werden.

**Beispiel**

```
python myproject.py get --param name=John --param role=Student
```

Dies erzeugt intern eine URL ähnlich wie `https://bin.org?name=John&role=Student` und ruft diese dann auf.

Beispiel mit eigener URL:

```
python myproject.py get --url https://httpbin.org/get --param user=test
```

### Command post

Das post Kommando führt eine Form Submission über Selenium aus.
Dabei werden Formularfelder mit --data gefüllt und das Formular abgeschickt.

Hinweis: Diese Funktion funktioniert nur auf Seiten, die ein HTML <form> enthalten.

**Beispiel**

```
python myproject.py post --url https://httpbin.org/forms/post --data custname=John --data custemail=test@example.com
```

Das Script füllt die entsprechenden Formularfelder und sendet das Formular ab.

### Command list-cookies

Dieses Kommando zeigt alle Cookies an, die für eine Seite gesetzt wurden.

Für Tests kann die spezielle httpbin URL verwendet werden, welche direkt ein Cookie setzt.

**Beispiel**

```
python myproject.py list-cookies --url https://httpbin.org/cookies/set?demo=python-http
```

Diese URL setzt automatisch ein Cookie mit dem Namen demo.

### Command screenshot

Dieses Kommando erstellt einen Screenshot einer Webseite.

Standardmässig wird der Screenshot in der Datei screenshot.png gespeichert.

**Beispiel**

```
python myproject.py screenshot --url https://example.com
```

Der Screenshot wird im Projektverzeichnis gespeichert.

Ein eigener Dateiname kann ebenfalls angegeben werden:

```
python myproject.py screenshot --url https://example.com --screenshot example.png
```

### Beispiel für `--output` param
Der Parameter --output kann mit allen Kommandos verwendet werden, um die Ausgabe in eine Datei zu schreiben.

**Beispiel**

```
python myproject.py body --output result.txt
```

Die Antwort der Webseite wird dann in result.txt gespeichert.

## Zusatzfeatures

Neben den Minimalanforderungen wurden folgende zusätzliche Funktionen implementiert:

- **Errorhandling**
  - Fehlermeldung bei ungültigen URLs
  - Meldung wenn bei `post` kein `<form>` Element gefunden wird
  - Warnung wenn einzelne Formularfelder nicht existieren
  - Vermeidung von Python Stacktraces für den Benutzer
- **Output Speicherung**
  - mit dem Parameter `--output` kann die Antwort eines Kommandos in eine Datei gespeichert werden
  - Funktioniert für alle Kommandos (`html-tag`, `get`, `post`, `list-cookies`, `screenshot`)
- **Screenshot Funktion**
  - Mit dem `screenshot` Kommando kann ein Screenshot einer Webseite erstellt werden
  - Optionaler Parameter `--screenshot` zum Festlegen des Dateinamens
