# Convergence of Evidence QGIS Plugin
QGIS Plugin to compute the Convergence of Evidence.

In the framework of the World Atlas of Desertification, 14 indicators, called Global Change Issues (GCI), are used to compute the Convergence of Evidence (CoE). Each indicator is a spatial layer with global coverage and can take values 0 or 1. An indicator takes a value of 1 if it is considered a potential issue relevant for land degradation. The thresholds to assign the values can be stratified by land cover class. The coincidence of issues is summarised as the sum of issues.

The Convergence of Evidence is a map showing the occurence of specific processes related to land degradation (which are indicated as global Change Issues - GCIs).

Where all the processes are identified as being potentially contributing to land degradation, none on its own is really enough to explain it (only in very specific cases). As we can't model the interaction, we 'simply' try to indicate how many of these processes (GCIs) are simultaneously at play and where this happens. The occurrence of such 'accumulation' at any given location indicates a certain stress on the land resources and suggest that potentially this led, or can lead, to land degradation.
## REQUIREMENTS

To work, the plugin needs to have the R software installed.
