---
UID: NA:wia_lh
ms.assetid: 99eafa9d-3584-3ffa-9589-0fb46987965a
ms.author: windowsdriverdev
ms.date: 03/13/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# Wia_Lh.h header



This header is used by Imaging devices. For more information, see
- [Imaging devices](../_image/index.md)

Wia_Lh.h contain these programming interfaces:


## Interfaces

| Title   | Description   |
| ---- |:---- |
| [IWiaErrorHandler interface](nn-wia_lh-iwiaerrorhandler.md) | The IWiaErrorHandler interface provides the GetStatusDescription and ReportStatus methods, which enable minidrivers to give users information about status or errors during a data transfer and possibly give an opportunity to recover from errors. |
| [IWiaImageFilter interface](nn-wia_lh-iwiaimagefilter.md) | The IWiaImageFilter interface is an extension interface implemented by image processing filter developers and called by Microsoft Windows Image Acquisition (WIA). |
| [IWiaLog interface](nn-wia_lh-iwialog.md) | The IWiaLog interface provides methods to enable minidrivers to log trace, error, and warning messages to the diagnostic log file Wiaservc.log. |
| [IWiaSegmentationFilter interface](nn-wia_lh-iwiasegmentationfilter.md) | The IWiaSegmentationFilter interface provides the DetectRegions method, which enables minidrivers to detect image subregions on a flatbed scanner's platen. This interface is available in Windows Vista and later. |
| [IWiaTransferCallback interface](nn-wia_lh-iwiatransfercallback.md) | The IWiaTransferCallback interface is implemented by image processing filter developers and called by Microsoft Windows Image Acquisition (WIA). |

## Methods

| Title   | Description   |
| ---- |:----

# wia_lh.h header



wia_lh.h contains the following programming interfaces:



## Interfaces
| Title | Description |
| ---- |:---- |
| [IWiaErrorHandler](nn-wia_lh-iwiaerrorhandler.md) | The IWiaErrorHandler interface provides the GetStatusDescription and ReportStatus methods, which enable minidrivers to give users information about status or errors during a data transfer and possibly give an opportunity to recover from errors. |
| [IWiaImageFilter](nn-wia_lh-iwiaimagefilter.md) | The IWiaImageFilter interface is an extension interface implemented by image processing filter developers and called by Microsoft Windows Image Acquisition (WIA). |
| [IWiaLog](nn-wia_lh-iwialog.md) | The IWiaLog interface provides methods to enable minidrivers to log trace, error, and warning messages to the diagnostic log file Wiaservc.log. |
| [IWiaSegmentationFilter](nn-wia_lh-iwiasegmentationfilter.md) | The IWiaSegmentationFilter interface provides the DetectRegions method, which enables minidrivers to detect image subregions on a flatbed scanner's platen. This interface is available in Windows Vista and later. |
| [IWiaTransferCallback](nn-wia_lh-iwiatransfercallback.md) | The IWiaTransferCallback interface is implemented by image processing filter developers and called by Microsoft Windows Image Acquisition (WIA). |