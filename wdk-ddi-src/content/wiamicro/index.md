---
UID : NA:wiamicro
ms.assetid : 6e3ffcb6-f08e-3947-9774-2adf8c435369
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# wiamicro.h header



wiamicro.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [MicroEntry](nf-wiamicro-microentry.md) | The MicroEntry function responds to commands sent by the WIA Flatbed driver. |
| [Scan](nf-wiamicro-scan.md) | The Scan function reads data from the device and returns the data to the WIA Flatbed driver. |
| [SetPixelWindow](nf-wiamicro-setpixelwindow.md) | The SetPixelWindow function sets the image area to be scanned. |



## Structures
| Title | Description |
| ---- |:---- |
| [_RANGEVALUE](ns-wiamicro-_rangevalue.md) | The RANGEVALUE structure is used by a microdriver to communicate to the WIA Flatbed driver the legal values for a microdriver function parameter. |
| [_SCANINFO](ns-wiamicro-_scaninfo.md) | The SCANINFO structure is used to store and communicate information about a scan acquisition. |
| [_SCANWINDOW](ns-wiamicro-_scanwindow.md) | The SCANWINDOW structure is used by the WIA Flatbed driver to tell the microdriver what image area to scan. |
| [VAL](ns-wiamicro-val.md) | The VAL structure is used by the microdriver and WIA Flatbed driver to pass information between each other. |