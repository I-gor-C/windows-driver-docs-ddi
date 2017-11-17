# Declarations in the wiamicro header
This header Wiamicro contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [MicroEntry function](nf-wiamicro-microentry.md) | The MicroEntry function responds to commands sent by the WIA Flatbed driver. |
| [SetPixelWindow function](nf-wiamicro-setpixelwindow.md) | The SetPixelWindow function sets the image area to be scanned. |
| [Scan function](nf-wiamicro-scan.md) | The Scan function reads data from the device and returns the data to the WIA Flatbed driver. |
| [Trace function](nf-wiamicro-trace.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SCANWINDOW structure](ns-wiamicro--scanwindow.md) | The SCANWINDOW structure is used by the WIA Flatbed driver to tell the microdriver what image area to scan. |
| [SCANINFO structure](ns-wiamicro--scaninfo.md) | The SCANINFO structure is used to store and communicate information about a scan acquisition. |
| [RANGEVALUE structure](ns-wiamicro--rangevalue.md) | The RANGEVALUE structure is used by a microdriver to communicate to the WIA Flatbed driver the legal values for a microdriver function parameter. |
| [VAL structure](ns-wiamicro-val.md) | The VAL structure is used by the microdriver and WIA Flatbed driver to pass information between each other. |

This header is used in these topics:

- [image](..content/_image)
