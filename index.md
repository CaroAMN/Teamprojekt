# Woche 3 

**Aufgabe 1** 
Hat so weit alles funktioniert, es fehlen allerdings Dateien im erstellten build Ordner. Es wurden nämlich nur .py Dateien mitgenommen, und ich gehe davon aus, dass man doch alle am Ende benötigt für ein funktionierendes package. Konnte allerdings selbst mit unterschiedlichesten Herangehensweisen der Anpassung der __init__.py nicht erreichen, dass auch andere Dateitypen mitgenommen wurden. 

**Aufgabe 2**
Hristian hat die Aufgabe bekommen nach geeignete tools im Internet zu suchen. Das Team hat sich für autopep8 entschieden, weil es den Code auf PEP8 Standard formatiert und es für Atom und VS Code verfügbar ist. Mit Autopep8 wurden die meisten "Violations" auf der Pipeline behoben. Die häufigsten "Violations" waren "missing Whitespaces" und "line too long". Die "line too long" Violations wurden mit black behoben. Black verfügt über den Befehl black -l length. Der Integer der für "lenght" angegeben wird bestimmt wie Lange die Zeilen im Code sein dürfen. Somit wurde die Zeilen länge auf 79 gebracht um das flake8 test zu erfüllen. An einige Stellen im Code gab es länger Kommentar-Blöcke die lediglich den Code erklärt haben. Diese Blöcke die Funktionalität des Codes nicht verändern und um eine gute Lesbarkeit der Kommentare zu erlauben haben wir die Blöcke mit den befehl #noqa: markiert damit flake8 sie beim Testen ignoriert. Bei der Aufgabe hat sich später eine kleine Schwierigkeit ergeben. Als das Team die Aufgabe 4 bearbeitet hat gab es bei Hristian einen Fehler und er könnte die IDViewer.py Datei nicht ausühren. Hristian hat herausgefunden, dass autopep8 einen bug hat der die Import reihenfolge manchmal verändert. Dieses Bug wurde mit dem Kommentar  # NOQA: E402 behoben.
![alt text](Screenshots/cisuccess.png)

**Aufgabe 3**
PR gegen das upstream pyopenms-extra repository
![alt text](Screenshots/PR_auf_pyopenms-extra.jpeg)


**Aufgabe 4**
Fehler bei Alex über die Console: ModuleNotFoundError: No module named 'ControllerWidget'

Wenn ich(Alex) über VS Code gehe, dann läuft es, aber wenn ich ein das XML file öffnen will, dann crashed das Programm ohne wirkliche Fehlermeldung. Nach dem Ausbessern des Codes (Aufgabe 2) und erneutem probieren funktioniert es noch immer nicht, gibt aber jetzt diese Fehlermeldung aus: 
![alt text](Screenshots/Fehlermeldung_Aufgabe04_Alex.png)

Beispiel Tabelle Hristian:
![alt text](Screenshots/extratable.png)

Hristians Lösung war, nach den Vorschlag von Caro, in der Datei ControllerWidget.py eine Methode creatingTables() zu schreiben. Die Methode benutzt QTableWidget um eine Tabelle zu erstellen. Mit .setRowsCount() und .setColumnCount() wurde die Anzahl and Spalten und Zeilen gesetz. Danach wurde die Tabelle zum Layout hinzugefügt und die Methode unter der Loadfile funktion geschrieben. Damit die Tabelle erst bei der Ladung von witere Daten zu zeigen. Da die Tabelle noch keine Sinvolle Daten haben soll wurde nichts mehr beim Laden verändert.
