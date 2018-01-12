---
UID: NA:wia_lh
---

# Wia_Lh.h header

## -description

This header is used by Imaging devices. For more information, see
- [Imaging devices](../_image/index.md)

Wia_Lh.h contain these programming interfaces:


## Interfaces

| Title   | Description   |
| ---- |:---- |
| [IWiaImageFilter interface](nn-wia_lh-iwiaimagefilter.md) | The IWiaImageFilter interface is an extension interface implemented by image processing filter developers and called by Microsoft Windows Image Acquisition (WIA). |

## Methods

| Title   | Description   |
| ---- |:---- |
| [IWiaErrorHandler::GetStatusDescription method](nf-wia_lh-iwiaerrorhandler-getstatusdescription.md) | The system UI calls the GetStatusDescription method to provide the user with extra information about an error, if the user requests this information. This method is implemented by a driver's UI extension. |
| [IWiaErrorHandler::ReportStatus method](nf-wia_lh-iwiaerrorhandler-reportstatus.md) | The ReportStatus method displays information about an error or status during a transfer. In some cases this method allows the user to recover from an error. |
| [IWiaImageFilter::FilterPreviewImage method](nf-wia_lh-iwiaimagefilter-filterpreviewimage.md) | The IWiaImageFilter |
| [IWiaImageFilter::InitializeFilter method](nf-wia_lh-iwiaimagefilter-initializefilter.md) | The IWiaImageFilter |
| [IWiaLog::InitializeLog method](nf-wia_lh-iwialog-initializelog.md) | Note that the IWiaLog interface is obsolete for Microsoft Windows XP and later, and is no longer supported. Instead, use the Diagnostic Log Macros.The IWiaLog |
| [IWiaLog::Log method](nf-wia_lh-iwialog-log.md) | The IWiaLog interface is obsolete for Windows XP and later, and is no longer supported. Use the Diagnostic Log Macros instead.The IWiaLog |
| [IWiaLog::hResult method](nf-wia_lh-iwialog-hresult.md) | Note that the IWiaLog interface is obsolete for Microsoft Windows XP and later, and is no longer supported. |
| [IWiaSegmentationFilter::DetectRegions method](nf-wia_lh-iwiasegmentationfilter-detectregions.md) | The IWiaSegmentationFilter |
| [IWiaTransferCallback::GetNextStream method](nf-wia_lh-iwiatransfercallback-getnextstream.md) | The IWiaTransferCallback |
| [IWiaTransferCallback::TransferCallback method](nf-wia_lh-iwiatransfercallback-transfercallback.md) | The IWiaTransferCallback |
