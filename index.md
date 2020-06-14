# Woche 6
## Aufgabe 1

Hristian hat einen Label hinzugefügt der anzeigt ob eine Datei geladen wurde. Es wurde ein Bug von Alex gefunden auf Windows. Beim laden der Datei wenn man auf schließen drückt, wird das gesamte Program geschloßen. Auf Ubuntu läuft das Program weiter.

## Aufgabe 2
Hristian hat die Klasse in der Gui Dokumentiert und Kommentiert nach den NumPy/SciPy Standard
![alt text](Screenshots/docclass.png)

## Allgemeines
- Logik wurde auseinandergenommen für die DECOY Sequenzen. Dadurch ist ein Fehler in der Logik selbst aufgetreten, da es Proteine ohne Proteinsequenz gibt, welche den counter für das neue Setzen des Pointers in der Datei nicht berücksichtigt haben, da der Fall eben nicht durch den if-case gelaufen ist. Daher kam es in den Listen zu Verschiebungen und darauf folgend zu falschen Ausgaben.

- GUI wurde in drei Methoden umgeschrieben, entsprechend welche Auswahl getroffen wurde für die Suche. Für sowohl bessere Lesbarkeit des Codes wie auch darauf folgend besseres Debugging. 

![alt text](Screenshots/Fehler_mit_fileTell.png)


![alt text](Screenshots/docmethoden.png)




# Woche 4-5 (über Pfingsten)

Das repo wurde auf dem master branch bereinigt und auf den Stand vom 15. Mai zurückgesetzt, sodass es updates vom master:pyopenms-extra entgegen nehmen kann.

## Die Gruppe hatte die Aufgabe 1 zu erledigen

## Aufgabe 1
Hristian hat das Hauptgerüst des Mainwindows und das Layout erstellt. Danach wurden von ihm searchbars und buttons erstellt. Die Buttons wurden verbunden und implementiert mit die jeweiligen Funktionen aus der logic Datei die Alex erstellt hat. Das Layout wurde mehrmals angepsst, weil die Gruppe in laufe der 2 Wochen das Design immer wieder verbessert hat. Die ursprüngliche Idee war, die gesuchten Proteine in eine Tabelle zu zeigen. Dem entschprechend wurde am Anfang ein QGridLayout benutzt. Nach dem Vorlschalg von den Tutoren wurde das Design verändert und die Tabelle wurde ersetzt durch ein Treeview der von Caro implementiert wurde. Hristian hat das Layout auf eine QVBoxLayout geändert der zusätzlich 3 QHBoxLayouts enthält. Somit wurde eine strukturiertes Aussehen ereicht. Die Tutoren haben ebenso vorgeschlagen eine dynamische Suche zu implementieren. Das bedeutet das man auch Präfixe von Protein Accessions als Eingabe für eine Suche benutzen kann und alle Proteine zeigt die diese Präfixe haben. Nach dem Alex die Funktionen in der Logic angepasst hat wurden sie von Hristian in das UI implementiert und das Treeview wurde mit eine for Schleife erweitert. Somit werden jetzt alle Proteine in dem Fenster angezeigt.  
## Aufgabe 2
Bei diese Aufgabe hat sich die Gruppe entschieden Radiobuttons zu benutzen die jeweils eine Input-Möglichkeit darstellen. Die 3 Möglichkeiten sind ID(Protein accession) Sequenz und Proteinname. Zusätlich wurde ein Chekbox hinzugefügt, die es ermöglicht nach den Decoy Proteine zu suchen. Diese kann an und ausgemacht werden. Die Radiobuttons und die Checkbox wurden von Hristian implementiert. Zusätzlich wurden von Hrisitan Error Messages implmentiert für flasches Eingaben oder für gar keine Eingaben sowie ein Load button und eine load Funktion mit der man die Datei auswählen kann und der Pfad dazu kopiert wird.

## Aufgabe 3
...
Bei diese Aufgabe hat die Gruppe die meisten Schwierigkeiten. Die Idee ist gesuchte Sequenz-Teile in der Ausgabe zu markieren(z.B durch Farbe) und zusätzlich sollte es möglich sein mit der Maus teile aus der Squenz zu markieren und zu Färben. Dabei waren die 2 Hauptprobleme
1. Die markierte Stelle in der Sqeuenz als information im Code zu bekommen
2. Die Strings zu färben, es wurde zum Zeitpunkt dieser Dokumentation keine funktion gefunden , die die Strings färben kann
Das 2 Problem wurde von Caro und Hristian gelöst. Die Ausgabe wird nun nicht mehr über QPlainTextedit gemacht sondern mit QTextEdit. QTextEdit hat die Methode .SetTextColot die QColor als Argument bekommt und die Textfarbe von den nächsten hinzugefügten String ändert. Somit wurde das GUI um ein weiteres Feature erweitert indem die gesuchte Proteinsequenz in der Ausgabe rot markiert wird.











# Woche 3

## Github io page
Die io page läuft nun nicht mehr über den master branch und die README, sonder es wurde ein neuer branch gh-pages erstellt und die Datei index.md wird für die Dokumentation genutz. Da das repository schon einen docs Ordner auf dem master branch besitzt wurde die variante mit dem neuen branch gewählt.

## Aufgabe 1
Hat so weit alles funktioniert, es fehlen allerdings Dateien im erstellten build Ordner. Es wurden nämlich nur .py Dateien mitgenommen, und ich gehe davon aus, dass man doch alle am Ende benötigt für ein funktionierendes package. Konnte allerdings selbst mit unterschiedlichesten Herangehensweisen der Anpassung der __init__.py nicht erreichen, dass auch andere Dateitypen mitgenommen wurden.

## Aufgabe 2
Hristian hat die Aufgabe bekommen nach geeignete tools im Internet zu suchen. Das Team hat sich für autopep8 entschieden, weil es den Code auf PEP8 Standard formatiert und es für Atom und VS Code verfügbar ist. Mit Autopep8 wurden die meisten "Violations" auf der Pipeline behoben. Die häufigsten "Violations" waren "missing Whitespaces" und "line too long". Die "line too long" Violations wurden mit black behoben. Black verfügt über den Befehl black -l length. Der Integer der für "lenght" angegeben wird bestimmt wie Lange die Zeilen im Code sein dürfen. Somit wurde die Zeilen länge auf 79 gebracht um das flake8 test zu erfüllen. An einige Stellen im Code gab es länger Kommentar-Blöcke die lediglich den Code erklärt haben. Diese Blöcke die Funktionalität des Codes nicht verändern und um eine gute Lesbarkeit der Kommentare zu erlauben haben wir die Blöcke mit den befehl #noqa: markiert damit flake8 sie beim Testen ignoriert. Bei der Aufgabe hat sich später eine kleine Schwierigkeit ergeben. Als das Team die Aufgabe 4 bearbeitet hat gab es bei Hristian einen Fehler und er könnte die IDViewer.py Datei nicht ausühren. Hristian hat herausgefunden, dass autopep8 einen bug hat der die Import reihenfolge manchmal verändert. Dieses Bug wurde mit dem Kommentar  # NOQA: E402 behoben.
![alt text](Screenshots/cisuccess.png)

## Aufgabe 3
PR gegen das upstream pyopenms-extra repository
![alt text](Screenshots/PR_auf_pyopenms-extra.jpeg)


## Aufgabe 4
Fehler bei Alex über die Console: ModuleNotFoundError: No module named 'ControllerWidget'

Wenn ich(Alex) über VS Code gehe, dann läuft es, aber wenn ich ein das XML file öffnen will, dann crashed das Programm ohne wirkliche Fehlermeldung. Nach dem Ausbessern des Codes (Aufgabe 2) und erneutem probieren funktioniert es noch immer nicht, gibt aber jetzt diese Fehlermeldung aus:
![alt text](Screenshots/Fehlermeldung_Aufgabe04_Alex.png)

Beispiel Tabelle Hristian:
![alt text](Screenshots/extratable.png)

Hristians Lösung war, nach den Vorschlag von Caro, in der Datei ControllerWidget.py eine Methode creatingTables() zu schreiben. Die Methode benutzt QTableWidget um eine Tabelle zu erstellen. Mit .setRowsCount() und .setColumnCount() wurde die Anzahl and Spalten und Zeilen gesetz. Danach wurde die Tabelle zum Layout hinzugefügt und die Methode unter der Loadfile funktion geschrieben. Damit die Tabelle erst bei der Ladung von witere Daten zu zeigen. Da die Tabelle noch keine Sinvolle Daten haben soll wurde nichts mehr beim Laden verändert.

**Caro**

Bei laden der Daten wurde folgende Fehlermeldung genereiert und es wurden keine Spektren angezeig. Der fehler konnte leider nicht behoben werden.

![alt text](Screenshots/error-IDViewer.png)

![alt text](Screenshots/w3-IDViewer.png)

Des weiteren konnte eine weitere Tabelle hinzugefügt werden. Dafür wurde eine eine Datei TestTabel.py im ordner view erstellt und diese im ControllerWidget importiert und über der vorhanden Tabelle hinzugefügt.

![alt text](Screenshots/IDViewer-Tabelle-Caro.png)
