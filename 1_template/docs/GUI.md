# Benutzer-Oberfläche (GUI)

GUI nach Programmstart:

![](./img/GUI/GUI_GUI.png){ width=75% }


### Men&uuml; Band

Das Seitenmen&uuml; auf der linken Seite ist ausklappbar.

![](./img/internalDocumentation/Ribbonband_animation.gif)

 Es zeigt je nach [Benutzerebene](./GL.Authentication/usermanagement.md#benutzer-ebene) eventuell mehr oder weniger Optionen.

<style>
.dynamic-text {
    font-size: 1.3em;  /* sets font size - 1.0em = "normal"  */
}
.hidden-header {
    font-size: 0; /* Makes text disappear */
}
</style>

| <span class="hidden-header">Men&uuml;band</span> | <span class="hidden-header">Dokumentationsseiten</span> |
|---------|---------------------------|
| ![Menu](./img/GUI/GUI_Ribbonband.png) | <br><br><br><br><span class="dynamic-text">[Live](./Live/live.md)<br> Aktuell verarbeiteter Datensatz <br> [Buffer](./GL.Buffer/buffer.md)<br> Datens&auml;tze im Ringspeicher <br> [Product](./GL.Buffer/buffer.md)<br> Produkt-Einstellungen <br> [Setting](./Product/product.md)<br> Programm-Einstellungen <br> [Logging](./GL.Settings/settings.md)<br> Einsicht in interne Programabl&auml;ufe <br> [User management](./GL.Authentication/usermanagement.md) <br> Benutzer-Management</span> |

## View-Overlay

Als ausklappbares Hover-Over-Menü - In der linken oberen Ecke finden sich die Einstellungen zur Bild-Ansicht und deren Overlays

![](./img/GUI/GUI_ViewOverlay_2.gif)

Hier lassen sich verschiedene Overlays einblenden und Ansichtsoptionen verändern.

Allgemeinere Funktionen:

- Histogramm: Statistische Darstellung des aktuellen Datensatzes  
<img src="./img/GUI/GUI_ViewOverlay_Histogram.png" alt="Histogramm" style="width:50%;">
- 3D-Anzeige: Der Wechsel auf die 3D-Ansicht die sich vorallem für Datensätze mit Höheninformationen eignet.
- Darstellung: Verschiedene Optionen wie die Anzeige als "Temperature"-Gradient

## Status-Leiste

Die Status-Leiste unten rechts ist in jedem Programm-Teil sichtbar und zeigt den aktuellen Status der jew. Kommunikation.

Beispiel:
![](./img/GUI/GUI_Statusleiste.png)

Aktueller Status: SPS-Kommunikation
Aktueller Status: Kamera

Durch einen Doppelklick :material-cursor-default-click: auf einen Status wird das jeweilige Gerät entweder **Connected** oder **Disconnected**:  
- **Connected**: ![](./img/GUI/GUI_Status_Connected.bmp)  
- **Disconnected**: ![](./img/GUI/GUI_Status_Disconnected.bmp)