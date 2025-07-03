# Prüfplan

### General

Verwaltet den aktuell im Produkt geladenen <img src="../img/internalDocumentation/Halcon.png" alt="HALCON" style="height:1em; vertical-align:middle; position:relative; top:-2px;"> HALCON-Code.

||||
|--------------|--------------|--------------|
| ![](./img/Product_Toolbar_IconOeffnen.jpg)        | **Öffnen** | Öffnet den aktuellen Prüfplan extern in HDevelop |
| ![](./img/Product_Toolbar_IconAktualisieren.jpg)  | **Aktualisieren** | Öffnet den aktuellen Prüfplan - neu einlesen und aktualisieren |
| ![](./img/Product_Toolbar_IconVerwalten.jpg)      | **Verwalten**     | Prüfpläne verwalten und organisieren |

### Öffnen - Öffnet den aktuellen Prüfplan extern in HDevelop

![](./img/Product_Toolbar_IconOeffnen.jpg)

Öffnet die aktuelle im Produkt aktive Halcon-Prozedur (`.hdvp`) mithilfe des unter [Settings](../GL.Settings/settings.md#halcon) eingestellten `HDevelop`.

<img src="./img/Product_Pruefplan_Oeffnen.png" alt="Öffnen" style="width:50%;">

### Aktualisieren - Öffnet das `Update`-Fenster

![](./img/Product_Toolbar_IconAktualisieren.jpg)

![](./img/Product_Pruefplan_Update.jpg)

Hier lassen sich die in der `Procedure` festgelegten `Input`- und `Output`-`Parameter` der <img src="../img/internalDocumentation/Halcon.png" alt="HALCON" style="height:1em; vertical-align:middle; position:relative; top:-2px;"> bearbeiten und einstellen. <br> (Die `Parameter` müssen zuerst in der Halcon-`Procedure` angelegt werden, bevor diese im Update-Fenster eingebunden werden können.)

![](./img/Product_Pruefplan_UpdateParameter.jpg)

### Verwalten - Öffnet das `Inspection-Plan`-Fenster

![](./img/Product_Pruefplan_Verwalten.jpg)

Hier kann die aktuelle `Procedure` ausgewählt und aktiviert werden.

Eine Prozess-Beschreibung hierzu finden Sie unter [Halcon-Procedure Initialisieren](product_halcon_initialize.md)