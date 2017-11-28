# Wiamicro.h header


This header is used by unknown technology.

Wiamicro.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [MicroEntry function](nf-wiamicro-microentry.md) | The MicroEntry function responds to commands sent by the WIA Flatbed driver. |
| [Scan function](nf-wiamicro-scan.md) | The Scan function reads data from the device and returns the data to the WIA Flatbed driver. |
| [SetPixelWindow function](nf-wiamicro-setpixelwindow.md) | The SetPixelWindow function sets the image area to be scanned. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [RANGEVALUE structure](ns-wiamicro--rangevalue.md) | The RANGEVALUE structure is used by a microdriver to communicate to the WIA Flatbed driver the legal values for a microdriver function parameter. |
| [SCANINFO structure](ns-wiamicro--scaninfo.md) | The SCANINFO structure is used to store and communicate information about a scan acquisition. |
| [SCANWINDOW structure](ns-wiamicro--scanwindow.md) | The SCANWINDOW structure is used by the WIA Flatbed driver to tell the microdriver what image area to scan. |
| [VAL structure](ns-wiamicro-val.md) | The VAL structure is used by the microdriver and WIA Flatbed driver to pass information between each other. |
