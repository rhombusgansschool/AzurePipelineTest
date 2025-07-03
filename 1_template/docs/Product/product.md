# Product

### General

In Product können Produktpläne erstellt und bearbeitet werden. Neben einer Übersicht aller Input-Parameter und einer detaillierten Darstellung der Output-Parameter finden Sie hier auch zahlreiche weitere Einstellungsmöglichkeiten für die Bildverarbeitung.

### GUI

![](./img/Product_GUI.png)

### Toolbar

![](./img/Product_Toolbar.jpg)

Aktuell ausgewähltes Produkt und Procedure

![.](./img/Product_Toolbar_CurrentProduct.jpg)

#### Produkt

![.](./img/Product_Toolbar_Produkt.jpg)

Dieser Toolbar-Abschnitt bietet verschiedene Möglichkeiten, Produkt-Profile zu bearbeiten, neu zu erstellen oder anzupassen.
Nach diesen Produkt-Profilen als Vorgabe werden die Bilddaten analysiert und entsprechend verarbeitet.

#### Prüfplan

![](./img/Product_Toolbar_Pruefplan.jpg)

Verwaltet den aktuell im Produkt geladenen <img src="../img/internalDocumentation/Halcon.png" alt="HALCON" style="height:1em; vertical-align:middle; position:relative; top:-2px;"> HALCON-Code.

#### Steuerung

Der Steuerungs-Toolbar-Abschnitt ermöglicht das Wechseln zwischen Live-Betrieb und Ringspeicher-Modus sowie das Ausführen der Bildverarbeitung.  

![.](./img/Product_Toolbar_Steuerung.jpg)

??? note "Steuerung"  

    ||||
    |--------------|--------------|--------------|
    |![.](./img/Product_Toolbar_IconLive.png)| **Live**<br>**Manuell** | Wechselt die aktuelle Ansicht auf `Live` / `Manuell` |
    |![.](./img/Product_Toolbar_IconRingspeicher.png)| **Ringspeicher** | Blendet die Liste der gespeicherten Datensätze ein und ermöglicht die erneute Analyse mit der aktuell geladenen Produkt-Vorlage |
    |![.](./img/Product_Toolbar_IconAusfuehren.png)| **Ausf&uuml;hren** | Startet je nach aktueller Ansicht (Live/Ringspeicher) die Aufnahme eines neuen Datensatzes oder verarbeitet den aktuell im Ringspeicher gewählten Datensatz erneut |
    | ![](./img/Product_Toolbar_IconIdentifier.jpg) | **Identifier** | Benennung des aktuell ausgewerteten Datensatzes |
    | ![](./img/Product_Toolbar_IconAutoInkrement.jpg) | **AutoInkrement** | Automatisches Hochzählen der Datensatznummer |
    | ![](./img/Product_Toolbar_IconHalcon.jpg) | **Halcon** | Zugriff auf die HALCON-Prozesskonfiguration |

#### Parameter

![.](./img/Product_Toolbar_Parameter.jpg)

Der Parameter Toolbar-Abschnitt bietet verschiedene Möglichkeiten, Parameter des aktuellen Produkt-Profile zu bearbeiten.
Funktionen sind je nach zugewiesenem Benutzer-Berechtigungen oder ausgewähltem Objekt ausgegraut und somit gesperrt.

Zur Bearbeitung einer z.B. HRegion wählen Sie diese aus und wählen ![.](./img/Product_Toolbar_IconBearbeiten.png)

![type:video](./img/Product_Parameter_EditRegion.mp4){: clas="no-audio" }

Die Parameter-Suche bietet das reduzieren der Ansicht auf die gewünschten Parameter.

![](./img/Product_Toolbar_ParameterSuche.gif)
