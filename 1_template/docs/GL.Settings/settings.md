# Settings

Settings bietet verschiedene Einstellungen zur Inbetriebnahme, Anpassung und Optimierung.

Die Settings sind je nach aktueller [Benutzerebene](../GL.Authentication/usermanagement.md#benutzer-ebene) nicht verfügbar.

![](./img/Settings_UserLevel.bmp)

### GUI

![GUI Overview](./img/Settings_GUI.png)

### Application

Die Anwendungseinstellungen bietet diverse Hardware-Einstellungen:

![](./img/Settings_Snippet_Application.png)

???+ note "Application [03] Parameters"

    **ImageFolder**: :material-folder-sync: Ordnerpfad zum einlesen von Bildern (wenn keine Bilder von der Kamera eingelesen werden)

    **Axis**: :material-ip-network: IP-Adresse der Achse

    **Camera**: :material-ip-network: Auswahl und Erkennung der Kamera<br>Über :material-magnify: `Search` lässt sich der Camera-String finden, der wichtige Informationen wie die Seriennummer enthält.

### Authentication  

![Authentication Settings](./img/Settings_Snippet_Authentication.png)  

???+ note "Authentication [03] Parameter"  

    **AutoLogOutActive**: Gibt an, ob der aktuelle User nach einer festgelegten Zeit ausgeloggt werden soll  
    
    **AutoLogOutIntervall**: Die bestimmte Zeit in Minuten, nach der der User ausgeloggt wird :octicons-clock-16:

    **CardReaderPreferred**: Angabe, ob der User-Login über ein Kartenlesegerät erfolgen soll :material-checkbox-marked-outline:  

### Halcon  

![Halcon Settings](./img/Settings_Snippet_Halcon.png)  

???+ note "Halcon [03] Parameter"  

    **HDevelopPath**: Pfad zur HDevelop-Executable  

    **ModuleInformation**: Anzeige und Ausführung von Halcon-Modulen  

    **ProcedurePath**: Gibt den Ordnerpfad an, in dem die Halcon-Prozeduren liegen :material-folder:  


### Inspection

![Inspection Settings](./img/Settings_Snippet_Inspection.png)

???+ note "Buffer [03] Parameters"

    **Buffer Capacity**: Größe des Ringspeichers (Bilderanzahl)  

    **Compression**: Kompressionsstufe für gespeicherte Bilder  

    **Path**: Speicherort des Puffers  

### Logging  

![Logging Settings](./img/Settings_Snippet_Logging.png)  

???+ note "Logging [01] Parameter"

    **GenerateQRCodes**: Erstellt QR-Codes (im Menüpunkt Logging) zum schnellen Teilen von Log-Daten über Email  
    **LogLevel**: Gibt an, welche Programm-Events in den Logs gespeichert werden sollen  
    <img src="./img/Settings_Snippet_QRCodesLogging.png" alt="QR Codes Logging" style="height:10%;">

### WPF  

![WPF Settings](./img/Settings_Snippet_WPF.png)

???+ note "WPF Parameters"

    **Language**: Sprache der Benutzeroberfläche  

    **Theme**: Benutzeroberfläche-Design (Hell/Dunkel)  