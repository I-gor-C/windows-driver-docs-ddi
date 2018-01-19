---
UID: TP:print
ms.assetid: fc0e0b85-603b-35c9-9d94-fc5cb18ea7c1
ms.author: windowsdriverdev
ms.date: 01/19/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# Print


Overview of the Print technology.

To develop Print, you need these headers:

 * [bidispl.h](..\bidispl\index.md)
 * [compstui.h](..\compstui\index.md)
 * [d4drvif.h](..\d4drvif\index.md)
 * [d4iface.h](..\d4iface\index.md)
 * [filterpipeline.h](..\filterpipeline\index.md)
 * [icm.h](..\icm\index.md)
 * [mxdc.h](..\mxdc\index.md)
 * [prcomoem.h](..\prcomoem\index.md)
 * [prdrvcom.h](..\prdrvcom\index.md)
 * [printerextension.h](..\printerextension\index.md)
 * [printoem.h](..\printoem\index.md)
 * [prnasntp.h](..\prnasntp\index.md)
 * [prntfont.h](..\prntfont\index.md)
 * [tcpxcv.h](..\tcpxcv\index.md)
 * [winddiui.h](..\winddiui\index.md)
 * [winppi.h](..\winppi\index.md)
 * [winsplp.h](..\winsplp\index.md)
 * [winspool.h](..\winspool\index.md)
 * [xpsrassvc.h](..\xpsrassvc\index.md)



## Functions

| Title   | Description   |
| ---- |:---- |
| [AddPortUI function](..\winsplp\nf-winsplp-addportui.md) | A port monitor UI DLL's AddPortUI function adds a printer port, then obtains port configuration information from the user and sends it to the port monitor server DLL. |
| [AddPrintDeviceObject function](..\winsplp\nf-winsplp-addprintdeviceobject.md) | The AddPrintDeviceObject print provider function creates a device object for a print provider queue. |
| [AppendPrinterNotifyInfoData function](..\winsplp\nf-winsplp-appendprinternotifyinfodata.md) | The print spooler's AppendPrinterNotifyInfoData function adds the contents of a specified PRINTER_NOTIFY_INFO_DATA structure to a specified PRINTER_NOTIFY_INFO structure. |
| [CallRouterFindFirstPrinterChangeNotification function](..\winsplp\nf-winsplp-callrouterfindfirstprinterchangenotification.md) | . |
| [ClosePort function](..\winsplp\nf-winsplp-closeport.md) | A language or port monitor's ClosePort function closes a printer port. |
| [ClosePrintProcessor function](..\winsplp\nf-winsplp-closeprintprocessor.md) | A print processor's ClosePrintProcessor function completes the printing of a print job and makes the associated handle invalid. |
| [ConfigurePortUI function](..\winsplp\nf-winsplp-configureportui.md) | A port monitor UI DLL's ConfigurePortUI function obtains port configuration information from the user and sends it to the port monitor server DLL. |
| [ControlPrintProcessor function](..\winsplp\nf-winsplp-controlprintprocessor.md) | A print processor's ControlPrintProcessor function allows the spooler to control a print job. |
| [CreatePrinterIC function](..\winsplp\nf-winsplp-createprinteric.md) | . |
| [DeleteJobNamedProperty function](..\winspool\nf-winspool-deletejobnamedproperty.md) | Deletes the named property for the specified print job on the specified printer. |
| [DeletePortUI function](..\winsplp\nf-winsplp-deleteportui.md) | A port monitor UI DLL's DeletePortUI function deletes a printer port. |
| [DeletePrinterIC function](..\winsplp\nf-winsplp-deleteprinteric.md) | . |
| [DevQueryPrint function](..\winsplp\nf-winsplp-devqueryprint.md) | . |
| [DevQueryPrintEx function](..\winddiui\nf-winddiui-devqueryprintex.md) | A printer interface DLL's DevQueryPrintEx function determines if a specified print job is compatible with the printer's current configuration and can therefore be printed. |
| [DrvConvertDevMode function](..\winddiui\nf-winddiui-drvconvertdevmode.md) | A printer interface DLL's DrvConvertDevMode function converts a printer's DEVMODEW structure from one version to another. |
| [DrvDeviceCapabilities function](..\winddiui\nf-winddiui-drvdevicecapabilities.md) | A printer interface DLL's DrvDeviceCapabilities function returns requested information about a printer's capabilities. |
| [DrvDevicePropertySheets function](..\winddiui\nf-winddiui-drvdevicepropertysheets.md) | A printer interface DLL's DrvDevicePropertySheets function is responsible for creating property sheet pages that describe a printer's properties. |
| [DrvDocumentEvent function](..\winddiui\nf-winddiui-drvdocumentevent.md) | A printer interface DLL's DrvDocumentEvent function can handle certain events associated with printing a document. |
| [DrvDocumentPropertySheets function](..\winddiui\nf-winddiui-drvdocumentpropertysheets.md) | A printer interface DLL's DrvDocumentPropertySheets function is responsible for creating property sheet pages that describe a print document's properties. |
| [DrvDriverEvent function](..\winddiui\nf-winddiui-drvdriverevent.md) | The print spooler calls a printer interface DLL's DrvDriverEvent function when the spooler processes driver-specific events that might require action by the printer driver. |
| [DrvPopulateFilterServices function](..\filterpipeline\nf-filterpipeline-drvpopulatefilterservices.md) | The DrvPopulateFilterServices function is called by the XPSDrv filter pipeline manager to allow the service provider to instantiate filter service objects in the filter pipeline property bag specified by the pPropertyBag parameter. |
| [DrvPrinterEvent function](..\winddiui\nf-winddiui-drvprinterevent.md) | A printer interface DLL's DrvPrinterEvent function is called by the print spooler when processing printer-specific events that might require action by the printer driver. |
| [DrvQueryColorProfile function](..\winddiui\nf-winddiui-drvquerycolorprofile.md) | The DrvQueryColorProfile function allows a printer interface DLL to specify an ICC profile to use for color management. |
| [DrvQueryJobAttributes function](..\winddiui\nf-winddiui-drvqueryjobattributes.md) | The DrvQueryJobAttributes function allows a printer interface DLL to specify support for such capabilities as printing multiple document pages on a physical page (&#0034;N-up&#0034; printing), printing multiple copies of each page, collating pages, and printing pages in reverse order. |
| [DrvSplAbort function](..\winddiui\nf-winddiui-drvsplabort.md) | . |
| [DrvSplClose function](..\winddiui\nf-winddiui-drvsplclose.md) | . |
| [DrvSplDeviceCaps function](..\winddiui\nf-winddiui-drvspldevicecaps.md) | A printer interface DLL's DrvSplDeviceCaps function queries a printer for its capabilities. |
| [DrvSplEndDoc function](..\winddiui\nf-winddiui-drvsplenddoc.md) | . |
| [DrvSplEndPage function](..\winddiui\nf-winddiui-drvsplendpage.md) | . |
| [DrvSplStartDoc function](..\winddiui\nf-winddiui-drvsplstartdoc.md) | . |
| [DrvSplStartPage function](..\winddiui\nf-winddiui-drvsplstartpage.md) | . |
| [DrvSplWritePrinter function](..\winddiui\nf-winddiui-drvsplwriteprinter.md) | . |
| [DrvUpgradePrinter function](..\winddiui\nf-winddiui-drvupgradeprinter.md) | A printer interface DLL's DrvUpgradePrinter function is used for updating a printer's registry settings when a new version of the driver is added to a system. |
| [EnumJobNamedProperties function](..\winspool\nf-winspool-enumjobnamedproperties.md) | . |
| [ExtDeviceMode function](..\winspool\nf-winspool-extdevicemode.md) | The ExtDeviceMode function is provided only for compatibility with 16-bit applications. |
| [FindFirstPrinterChangeNotification function](..\winspool\nf-winspool-findfirstprinterchangenotification.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [FreePrintNamedPropertyArray function](..\winspool\nf-winspool-freeprintnamedpropertyarray.md) | . |
| [FreePrintPropertyValue function](..\winspool\nf-winspool-freeprintpropertyvalue.md) | Frees the value that is retrieved using GetJobNamedPropertyValue function. |
| [GdiDeleteSpoolFileHandle function](..\winppi\nf-winppi-gdideletespoolfilehandle.md) | The GdiDeleteSpoolFileHandle function releases a spool file handle. |
| [GdiEndDocEMF function](..\winppi\nf-winppi-gdienddocemf.md) | The GdiEndDocEMF function ends EMF playback operations for an EMF-formatted print job. |
| [GdiEndPageEMF function](..\winppi\nf-winppi-gdiendpageemf.md) | The GdiEndPageEMF function ends EMF playback operations for a physical page of an EMF-formatted print job. |
| [GdiGetDC function](..\winppi\nf-winppi-gdigetdc.md) | The GdiGetDC function returns a handle to a printer's device context. |
| [GdiGetDevmodeForPage function](..\winppi\nf-winppi-gdigetdevmodeforpage.md) | The GdiGetDevmodeForPage function returns DEVMODEW structures for the specified and previous pages of a print job. |
| [GdiGetPageCount function](..\winppi\nf-winppi-gdigetpagecount.md) | The GdiGetPageCount function returns the number of pages in a print job. |
| [GdiGetPageHandle function](..\winppi\nf-winppi-gdigetpagehandle.md) | The GdiGetPageHandle function returns a handle to the specified page within a print job. |
| [GdiGetSpoolFileHandle function](..\winppi\nf-winppi-gdigetspoolfilehandle.md) | The GdiGetSpoolFileHandle function returns a handle to a print job's EMF file. |
| [GdiPlayPageEMF function](..\winppi\nf-winppi-gdiplaypageemf.md) | The GdiPlayPageEMF function plays the EMF records within a specified rectangle for one document page of a spooled print job. |
| [GdiResetDCEMF function](..\winppi\nf-winppi-gdiresetdcemf.md) | The GdiResetDCEMF function resets a printer's device context during playback of a spooled EMF print job. |
| [GdiStartDocEMF function](..\winppi\nf-winppi-gdistartdocemf.md) | The GdiStartDocEMF function performs initialization operations for an EMF-formatted print job. |
| [GdiStartPageEMF function](..\winppi\nf-winppi-gdistartpageemf.md) | The GdiStartPageEMF function performs initialization operations for a physical page of an EMF-formatted print job. |
| [GenerateCopyFilePaths function](..\winsplp\nf-winsplp-generatecopyfilepaths.md) | A Point and Print DLL's GenerateCopyFilePaths function is used for modifying the source and destination paths used by print spoolers when they copy print queue-associated files to a print client. |
| [GetCPSUIUserData function](..\compstui\nf-compstui-getcpsuiuserdata.md) | CPSUI's GetCPSUIUserData function retrieves data that was previously stored using the SetCPSUIUserData function. |
| [GetJobAttributes function](..\winsplp\nf-winsplp-getjobattributes.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [GetJobAttributesEx function](..\winsplp\nf-winsplp-getjobattributesex.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [GetJobNamedPropertyValue function](..\winspool\nf-winspool-getjobnamedpropertyvalue.md) | Retrieves the value of the named property for the specified print job on the specified printer. |
| [GetPrintOutputInfo function](..\winspool\nf-winspool-getprintoutputinfo.md) | . |
| [GetPrintProcessorCapabilities function](..\winsplp\nf-winsplp-getprintprocessorcapabilities.md) | A print processor's GetPrintProcessorCapabilities function returns capabilities associated with a specified input data type. |
| [ImpersonatePrinterClient function](..\winsplp\nf-winsplp-impersonateprinterclient.md) | ImpersonatePrinterClient resumes impersonation of the client, completing the operation begun by RevertToPrinterSelf. |
| [InitializeMonitor function](..\winsplp\nf-winsplp-initializemonitor.md) | . |
| [InitializeMonitorEx function](..\winsplp\nf-winsplp-initializemonitorex.md) | . |
| [InitializePrintMonitor function](..\winsplp\nf-winsplp-initializeprintmonitor.md) | The InitializePrintMonitor function is obsolete and is supported only for compatibility purposes. |
| [InitializePrintMonitor2 function](..\winsplp\nf-winsplp-initializeprintmonitor2.md) | A print monitor's InitializePrintMonitor2 function initializes a print monitor for use with clustered print servers. |
| [InitializePrintMonitorUI function](..\winsplp\nf-winsplp-initializeprintmonitorui.md) | A port monitor UI DLL's InitializePrintMonitorUI function supplies the print spooler with addresses of DLL functions. |
| [InitializePrintProvidor function](..\winsplp\nf-winsplp-initializeprintprovidor.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [LogJobInfoForBranchOffice function](..\winsplp\nf-winsplp-logjobinfoforbranchoffice.md) | Allows Branch Office clients to send job events to the host print server. |
| [MxdcGetPDEVAdjustment function](..\mxdc\nf-mxdc-mxdcgetpdevadjustment.md) | The MxdcGetPDEVAdjustment function is exported by a printer interface DLL and supplies printer configuration data for the Microsoft XPS Document Converter (MXDC). |
| [OEMAlphaBlend function](..\printoem\nf-printoem-oemalphablend.md) | OEMAlphaBlend function |
| [OEMBitBlt function](..\printoem\nf-printoem-oembitblt.md) | The OEMBitBlt function provides general bit-block transfer capabilities between device-managed surfaces, between GDI-managed standard-format bitmaps, or between a device-managed surface and a GDI-managed standard-format bitmap. |
| [OEMCommand function](..\printoem\nf-printoem-oemcommand.md) | OEMCommand function |
| [OEMCommandCallback function](..\printoem\nf-printoem-oemcommandcallback.md) | OEMCommandCallback function |
| [OEMCommonUIProp function](..\printoem\nf-printoem-oemcommonuiprop.md) | OEMCommonUIProp function |
| [OEMCompression function](..\printoem\nf-printoem-oemcompression.md) | OEMCompression function |
| [OEMCopyBits function](..\printoem\nf-printoem-oemcopybits.md) | The OEMCopyBits function performs translations between device-managed raster surfaces and GDI standard-format bitmaps. |
| [OEMDevMode function](..\printoem\nf-printoem-oemdevmode.md) | OEMDevMode function |
| [OEMDevQueryPrintEx function](..\printoem\nf-printoem-oemdevqueryprintex.md) | OEMDevQueryPrintEx function |
| [OEMDeviceCapabilities function](..\printoem\nf-printoem-oemdevicecapabilities.md) | OEMDeviceCapabilities function |
| [OEMDevicePropertySheets function](..\printoem\nf-printoem-oemdevicepropertysheets.md) | OEMDevicePropertySheets function |
| [OEMDisableDriver function](..\printoem\nf-printoem-oemdisabledriver.md) | OEMDisableDriver function |
| [OEMDisablePDEV function](..\printoem\nf-printoem-oemdisablepdev.md) | OEMDisablePDEV function |
| [OEMDitherColor function](..\printoem\nf-printoem-oemdithercolor.md) | The OEMDitherColor function requests the device to create a brush dithered against a device palette. |
| [OEMDocumentPropertySheets function](..\printoem\nf-printoem-oemdocumentpropertysheets.md) | OEMDocumentPropertySheets function |
| [OEMDownloadCharGlyph function](..\printoem\nf-printoem-oemdownloadcharglyph.md) | OEMDownloadCharGlyph function |
| [OEMDownloadFontHeader function](..\printoem\nf-printoem-oemdownloadfontheader.md) | OEMDownloadFontHeader function |
| [OEMDriverDMS function](..\printoem\nf-printoem-oemdriverdms.md) | OEMDriverDMS function |
| [OEMEnableDriver function](..\printoem\nf-printoem-oemenabledriver.md) | OEMEnableDriver function |
| [OEMEnablePDEV function](..\printoem\nf-printoem-oemenablepdev.md) | OEMEnablePDEV function |
| [OEMEndDoc function](..\printoem\nf-printoem-oemenddoc.md) | The OEMEndDoc function is called by the GDI when it has finished sending a document to the driver for rendering. |
| [OEMEscape function](..\printoem\nf-printoem-oemescape.md) | The OEMEscape function retrieves information from a device that is not available in a device-independent device driver interface; the particular query depends on the value of the iEsc parameter. |
| [OEMFillPath function](..\printoem\nf-printoem-oemfillpath.md) | The OEMFillPath function handles the filling of closed paths. |
| [OEMFilterGraphics function](..\printoem\nf-printoem-oemfiltergraphics.md) | OEMFilterGraphics function |
| [OEMFontInstallerDlgProc function](..\printoem\nf-printoem-oemfontinstallerdlgproc.md) | OEMFontInstallerDlgProc function |
| [OEMFontManagement function](..\printoem\nf-printoem-oemfontmanagement.md) | The OEMFontManagement function is an optional entry point provided for PostScript devices. |
| [OEMGetGlyphMode function](..\printoem\nf-printoem-oemgetglyphmode.md) | The OEMGetGlyphMode function informs the GDI how to cache glyph information. |
| [OEMGetInfo function](..\printoem\nf-printoem-oemgetinfo.md) | OEMGetInfo function |
| [OEMGradientFill function](..\printoem\nf-printoem-oemgradientfill.md) | The OEMGradientFill function shades the specified primitives. |
| [OEMHalftonePattern function](..\printoem\nf-printoem-oemhalftonepattern.md) | OEMHalftonePattern function |
| [OEMIcmCreateColorTransform function](..\printoem\nf-printoem-oemicmcreatecolortransform.md) | The OEMIcmCreateColorTransform function creates an ICM color transform. |
| [OEMIcmDeleteColorTransform function](..\printoem\nf-printoem-oemicmdeletecolortransform.md) | The OEMIcmDeleteColorTransform function deletes the specified color transform. |
| [OEMImageProcessing function](..\printoem\nf-printoem-oemimageprocessing.md) | OEMImageProcessing function |
| [OEMLineTo function](..\printoem\nf-printoem-oemlineto.md) | The OEMLineTo function draws a single, solid, integer-only cosmetic line. |
| [OEMNextBand function](..\printoem\nf-printoem-oemnextband.md) | The OEMNextBand function is called by GDI when it has finished drawing a band for a physical page, so that the driver can send the band to the printer. |
| [OEMOutputCharStr function](..\printoem\nf-printoem-oemoutputcharstr.md) | OEMOutputCharStr function |
| [OEMPDriverEvent function](..\printoem\nf-printoem-oempdriverevent.md) | OEMPDriverEvent function |
| [OEMPaint function](..\printoem\nf-printoem-oempaint.md) | The OEMPaint function is obsolete, and is no longer called by GDI in Windows 2000 and later. See DrvPaint. |
| [OEMPlgBlt function](..\printoem\nf-printoem-oemplgblt.md) | The OEMPlgBlt function provides rotate bit-block transfer capabilities between combinations of device-managed and GDI-managed surfaces. |
| [OEMPrinterEvent function](..\printoem\nf-printoem-oemprinterevent.md) | OEMPrinterEvent function |
| [OEMQueryAdvanceWidths function](..\printoem\nf-printoem-oemqueryadvancewidths.md) | The OEMQueryAdvanceWidths function returns character advance widths for a specified set of glyphs. |
| [OEMQueryColorProfile function](..\printoem\nf-printoem-oemquerycolorprofile.md) | OEMQueryColorProfile function |
| [OEMQueryDeviceSupport function](..\printoem\nf-printoem-oemquerydevicesupport.md) | The OEMQueryDeviceSupport function returns requested device-specific information. |
| [OEMQueryFont function](..\printoem\nf-printoem-oemqueryfont.md) | The OEMQueryFont function is used by GDI to get the IFIMETRICS structure for a given font. |
| [OEMQueryFontData function](..\printoem\nf-printoem-oemqueryfontdata.md) | The OEMQueryFontData function retrieves information about a realized font. |
| [OEMQueryFontTree function](..\printoem\nf-printoem-oemqueryfonttree.md) | The OEMQueryFontTree function provides GDI with a pointer to a structure that defines one of the following |
| [OEMRealizeBrush function](..\printoem\nf-printoem-oemrealizebrush.md) | The OEMRealizeBrush function requests that the driver realize a specified brush for a specified surface. |
| [OEMResetPDEV function](..\printoem\nf-printoem-oemresetpdev.md) | OEMResetPDEV function |
| [OEMSendFontCmd function](..\printoem\nf-printoem-oemsendfontcmd.md) | OEMSendFontCmd function |
| [OEMSendPage function](..\printoem\nf-printoem-oemsendpage.md) | The OEMSendPage function is called by GDI when it has finished drawing a physical page, so that the driver can send the page to the printer. |
| [OEMStartBanding function](..\printoem\nf-printoem-oemstartbanding.md) | The OEMStartBanding function is called by GDI when it is ready to start sending bands of a physical page to the driver for rendering. |
| [OEMStartDoc function](..\printoem\nf-printoem-oemstartdoc.md) | The OEMStartDoc function is called by GDI when it is ready to start sending a document to the driver for rendering. |
| [OEMStartPage function](..\printoem\nf-printoem-oemstartpage.md) | The OEMStartPage function is called by GDI when it is ready to start sending the contents of a physical page to the driver for rendering. |
| [OEMStretchBlt function](..\printoem\nf-printoem-oemstretchblt.md) | The OEMStretchBlt function provides stretching bit-block transfer capabilities between any combination of device-managed and GDI-managed surfaces. |
| [OEMStretchBltROP function](..\printoem\nf-printoem-oemstretchbltrop.md) | The OEMStretchBltROP function performs a stretching bit-block transfer using a raster operation (ROP). |
| [OEMStrokeAndFillPath function](..\printoem\nf-printoem-oemstrokeandfillpath.md) | The OEMStrokeAndFillPath function concurrently strokes and fills a path. |
| [OEMStrokePath function](..\printoem\nf-printoem-oemstrokepath.md) | The OEMStrokePath function strokes a path. |
| [OEMTTDownloadMethod function](..\printoem\nf-printoem-oemttdownloadmethod.md) | OEMTTDownloadMethod function |
| [OEMTTYGetInfo function](..\printoem\nf-printoem-oemttygetinfo.md) | OEMTTYGetInfo function |
| [OEMTextOut function](..\printoem\nf-printoem-oemtextout.md) | The OEMTextOut function calls for the driver to render a set of glyphs at specified positions. |
| [OEMTextOutAsBitmap function](..\printoem\nf-printoem-oemtextoutasbitmap.md) | OEMTextOutAsBitmap function |
| [OEMTransparentBlt function](..\printoem\nf-printoem-oemtransparentblt.md) | The OEMTransparentBlt function provides bit-block transfer capabilities with transparency. |
| [OEMUpdateExternalFonts function](..\printoem\nf-printoem-oemupdateexternalfonts.md) | OEMUpdateExternalFonts function |
| [OEMUpgradePrinter function](..\printoem\nf-printoem-oemupgradeprinter.md) | OEMUpgradePrinter function |
| [OEMUpgradeRegistry function](..\printoem\nf-printoem-oemupgraderegistry.md) | OEMUpgradeRegistry function |
| [OpenPort function](..\winsplp\nf-winsplp-openport.md) | A port monitor's OpenPort function opens a printer port. |
| [OpenPrintProcessor function](..\winsplp\nf-winsplp-openprintprocessor.md) | A print processor's OpenPrintProcessor function prepares the print processor for printing a job and returns a handle. |
| [PartialReplyPrinterChangeNotification function](..\winsplp\nf-winsplp-partialreplyprinterchangenotification.md) | The print spooler's PartialReplyPrinterChangeNotification function allows a print provider to update the spooler's database of printer changes associated with a notification handle. |
| [PlayGdiScriptOnPrinterIC function](..\winsplp\nf-winsplp-playgdiscriptonprinteric.md) | . |
| [PrintDocumentOnPrintProcessor function](..\winsplp\nf-winsplp-printdocumentonprintprocessor.md) | A print processor's PrintDocumentOnPrintProcessor function converts a print job from a spooled format into raw data that can be sent to a print monitor. |
| [PrinterMessageBoxA function](..\winspool\nf-winspool-printermessageboxa.md) | . |
| [PrinterMessageBoxW function](..\winspool\nf-winspool-printermessageboxw.md) | . |
| [ProvidorFindClosePrinterChangeNotification function](..\winsplp\nf-winsplp-providorfindcloseprinterchangenotification.md) | . |
| [ProvidorFindFirstPrinterChangeNotification function](..\winsplp\nf-winsplp-providorfindfirstprinterchangenotification.md) | . |
| [ReadPort function](..\winsplp\nf-winsplp-readport.md) | A port monitor's ReadPort function reads data from a printer port. |
| [RemovePrintDeviceObject function](..\winsplp\nf-winsplp-removeprintdeviceobject.md) | The RemovePrintDeviceObject function removes a device object from a print provider queue. |
| [ReplyPrinterChangeNotification function](..\winsplp\nf-winsplp-replyprinterchangenotification.md) | The print spooler's ReplyPrinterChangeNotification function allows a print provider to update the spooler's database of print queue events associated with a notification handle, and to notify the client that print queue events have occurred. |
| [ReplyPrinterChangeNotificationEx function](..\winsplp\nf-winsplp-replyprinterchangenotificationex.md) | . |
| [RevertToPrinterSelf function](..\winsplp\nf-winsplp-reverttoprinterself.md) | When RevertToPrinterSelf is called on an impersonating thread, it returns the token for the thread that is being impersonated. |
| [RouterAllocBidiMem function](..\winsplp\nf-winsplp-routerallocbidimem.md) | RouterAllocBidiMem allocates a block of memory of a specified size. This function is used by the port monitor to allocate memory for strings and binary objects. |
| [RouterAllocBidiResponseContainer function](..\winsplp\nf-winsplp-routerallocbidiresponsecontainer.md) | RouterAllocBidiResponseContainer allocates a BIDI_RESPONSE_CONTAINER structure containing a list of bidi responses. The bidi response list is an array of BIDI_RESPONSE_DATA structures. |
| [RouterAllocPrinterNotifyInfo function](..\winsplp\nf-winsplp-routerallocprinternotifyinfo.md) | The print spooler's RouterAllocPrinterNotifyInfo function allocates a PRINTER_NOTIFY_INFO structure and an array of PRINTER_NOTIFY_INFO_DATA structures. |
| [RouterCreatePrintAsyncNotificationChannel function](..\prnasntp\nf-prnasntp-routercreateprintasyncnotificationchannel.md) | The RouterCreatePrintAsyncNotificationChannel function creates an asynchronous notification channel that is associated with a printer or print server. |
| [RouterFreeBidiMem function](..\winsplp\nf-winsplp-routerfreebidimem.md) | RouterFreeBidiMem frees a block of memory that was previously allocated by RouterAllocBidiMem. |
| [RouterFreeBidiResponseContainer function](..\winsplp\nf-winsplp-routerfreebidiresponsecontainer.md) | RouterFreeBidiResponseContainer frees a BIDI_RESPONSE_CONTAINER structure previously allocated by RouterAllocBidiResponseContainer. |
| [RouterFreePrinterNotifyInfo function](..\winsplp\nf-winsplp-routerfreeprinternotifyinfo.md) | The print spooler's RouterFreePrinterNotifyInfo function deallocates a specified PRINTER_NOTIFY_INFO structure and its associated PRINTER_NOTIFY_INFO_DATA structure array. |
| [RouterGetPrintClassObject function](..\prnasntp\nf-prnasntp-routergetprintclassobject.md) | The RouterGetPrintClassObject function enumerates the list of print providers, searching for the print provider with the specified name and interface ID. |
| [RouterRegisterForPrintAsyncNotifications function](..\prnasntp\nf-prnasntp-routerregisterforprintasyncnotifications.md) | The RouterRegisterForPrintAsyncNotifications function registers for asynchronous notifications associated with a printer or print server. |
| [RouterUnregisterForPrintAsyncNotifications function](..\prnasntp\nf-prnasntp-routerunregisterforprintasyncnotifications.md) | The RouterUnregisterForPrintAsyncNotifications function unregisters for receiving asynchronous notifications associated with a printer or print server. |
| [SetCPSUIUserData function](..\compstui\nf-compstui-setcpsuiuserdata.md) | CPSUI's SetCPSUIUserData function allows CPSUI applications (including printer interface DLLs) to associate nondisplayed data with a property sheet dialog box. |
| [SetJobNamedProperty function](..\winspool\nf-winspool-setjobnamedproperty.md) | . |
| [SplDeleteSpoolerPortEnd function](..\winsplp\nf-winsplp-spldeletespoolerportend.md) | . |
| [SplDeleteSpoolerPortStart function](..\winsplp\nf-winsplp-spldeletespoolerportstart.md) | . |
| [SplIsSessionZero function](..\winsplp\nf-winsplp-splissessionzero.md) | The SplIsSessionZero function determines whether a certain print job (print handle plus job ID) was issued in session zero. |
| [SplPromptUIInUsersSession function](..\winsplp\nf-winsplp-splpromptuiinuserssession.md) | The SplPromptUIInUsersSession function displays a standard message box in the session indicated by the printer handle and job ID. |
| [SpoolerCopyFileEvent function](..\winsplp\nf-winsplp-spoolercopyfileevent.md) | A Point and Print DLL's SpoolerCopyFileEvent function receives notifications of events associated with copying print queue-associated files to a print client, when the client connects to a print server. |
| [SpoolerFindClosePrinterChangeNotification function](..\winsplp\nf-winsplp-spoolerfindcloseprinterchangenotification.md) | . |
| [SpoolerFindFirstPrinterChangeNotification function](..\winsplp\nf-winsplp-spoolerfindfirstprinterchangenotification.md) | . |
| [SpoolerFindNextPrinterChangeNotification function](..\winsplp\nf-winsplp-spoolerfindnextprinterchangenotification.md) | . |
| [SpoolerFreePrinterNotifyInfo function](..\winsplp\nf-winsplp-spoolerfreeprinternotifyinfo.md) | . |
| [SpoolerRefreshPrinterChangeNotification function](..\winsplp\nf-winsplp-spoolerrefreshprinterchangenotification.md) | . |
| [UpdatePrintDeviceObject function](..\winsplp\nf-winsplp-updateprintdeviceobject.md) | The UpdatePrintDeviceObject function updates the properties of a device object that is in the print provider queue. |
| [WaitForPrinterChange function](..\winspool\nf-winspool-waitforprinterchange.md) | . |
| [WcsAssociateColorProfileWithDevice function](..\icm\nf-icm-wcsassociatecolorprofilewithdevice.md) | The WcsAssociateColorProfileWithDevice function associates a specified WCS color profile with a specified device. |
| [WcsCheckColors function](..\icm\nf-icm-wcscheckcolors.md) | The WcsCheckColors function determines whether the colors in an array lie within the output gamut of a specified WCS color transform. |
| [WcsCreateIccProfile function](..\icm\nf-icm-wcscreateiccprofile.md) | The WcsCreateIccProfile function converts a WCS profile into an ICC profile. |
| [WcsDisassociateColorProfileFromDevice function](..\icm\nf-icm-wcsdisassociatecolorprofilefromdevice.md) | The WcsDisassociateColorProfileFromDevice function disassociates a specified WCS color profile from a specified device. |
| [WcsEnumColorProfiles function](..\icm\nf-icm-wcsenumcolorprofiles.md) | The WcsEnumColorProfiles function enumerates all color profiles that satisfy the enumeration criteria in the specified profile management scope. |
| [WcsEnumColorProfilesSize function](..\icm\nf-icm-wcsenumcolorprofilessize.md) | The WcsEnumColorProfilesSize function returns the size, in bytes, of the buffer required by the WcsEnumColorProfiles function to enumerate color profiles. |
| [WcsGetDefaultColorProfile function](..\icm\nf-icm-wcsgetdefaultcolorprofile.md) | The WcsGetDefaultColorProfile function retrieves the default color profile for a device, or the device-independent default if the device is not specified. |
| [WcsGetDefaultColorProfileSize function](..\icm\nf-icm-wcsgetdefaultcolorprofilesize.md) | The WcsGetDefaultColorProfileSize function returns the size, in bytes, of the default color profile name for a device, including the NULL terminator. |
| [WcsGetUsePerUserProfiles function](..\icm\nf-icm-wcsgetuseperuserprofiles.md) | The WcsGetUsePerUserProfiles function determines whether the user has chosen to use a per-user profile association list for the specified device. |
| [WcsSetDefaultColorProfile function](..\icm\nf-icm-wcssetdefaultcolorprofile.md) | The WcsSetDefaultColorProfile function sets the default color profile name of the specified profile type in the specified profile management scope. |
| [WcsSetUsePerUserProfiles function](..\icm\nf-icm-wcssetuseperuserprofiles.md) | The WcsSetUsePerUserProfiles function allows the user to specify whether or not to use a per-user profile association list for the specified device. |
| [WcsTranslateColors function](..\icm\nf-icm-wcstranslatecolors.md) | The WcsTranslateColors function translates an array of colors from the source color space to the destination color space as defined by a color transform. |
| [WritePort function](..\winsplp\nf-winsplp-writeport.md) | A port monitor's WritePort function writes data to a printer port. |
| [XcvClosePort function](..\winsplp\nf-winsplp-xcvcloseport.md) | A port monitor server DLL's XcvClosePort function closes a printer port that was opened by XcvOpenPort. |
| [XcvDataPort function](..\winsplp\nf-winsplp-xcvdataport.md) | A port monitor server DLL's XcvDataPort function receives information from, and returns information to, the port monitor's UI DLL. |
| [XcvOpenPort function](..\winsplp\nf-winsplp-xcvopenport.md) | A port monitor server DLL's XcvOpenPort function opens a port for configuration operations. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [OEMCUIPCALLBACK callback function](..\printoem\nc-printoem-oemcuipcallback.md) | The OEMCUIPCALLBACK function type is used for defining callback functions that are specified by a user interface plug-in's IPrintOemUI |
| [PFNCOMPROPSHEET callback function](..\compstui\nc-compstui-pfncompropsheet.md) | The ComPropSheet function is supplied by CPSUI and can be called by CPSUI applications (including printer interface DLLs) to build property sheet pages. |
| [PFNGETINFO callback function](..\printoem\nc-printoem-pfngetinfo.md) | The UNIFONTOBJ_GetInfo callback function is provided by the Unidrv driver so that rendering plug-ins can obtain font or glyph information. |
| [PFNPROPSHEETUI callback function](..\compstui\nc-compstui-pfnpropsheetui.md) | The PFNPROPSHEETUI function type is used by CPSUI applications (including printer interface DLLs) for defining page creation callbacks, which specify property sheet pages for creation. |
| [ROUTER_NOTIFY_CALLBACK callback function](..\winsplp\nc-winsplp-router_notify_callback.md) | . |
| [_CPSUICALLBACK callback function](..\compstui\nc-compstui-_cpsuicallback.md) | The _CPSUICALLBACK function type is used by CPSUI applications (including printer interface DLLs) for defining a callback function intended for use as a CPSUI message handler. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [BranchOfficeJobData structure](..\winsplp\ns-winsplp-branchofficejobdata.md) | This structure contains the type of event to log (eEventType), the job ID, and the data required by the event. |
| [BranchOfficeJobDataContainer structure](..\winsplp\ns-winsplp-branchofficejobdatacontainer.md) | This structure defines a container for one or more BranchOfficeJobData structures to sent to a server. |
| [BranchOfficeJobDataError structure](..\winsplp\ns-winsplp-branchofficejobdataerror.md) | This structure contains the necessary data for logging a branch office job failure event on a remote server. This is based on standard job-related data available to the spooler. |
| [BranchOfficeJobDataPipelineFailed structure](..\winsplp\ns-winsplp-branchofficejobdatapipelinefailed.md) | Contains the necessary data for logging a branch office job Pipeline Rendering Failed event on a remote server. This is based on standard job-related data available to the spooler. |
| [BranchOfficeJobDataPrinted structure](..\winsplp\ns-winsplp-branchofficejobdataprinted.md) | Contains the necessary data for logging a branch office job completed event on a remote server. This is based on standard job-related data available to the spooler. |
| [BranchOfficeJobDataRendered structure](..\winsplp\ns-winsplp-branchofficejobdatarendered.md) | Contains the necessary data for logging a branch office job Pipeline Rendering Event on a remote server. This is based on job-related data available to the spooler. |
| [BranchOfficeLogOfflineFileFull structure](..\winsplp\ns-winsplp-branchofficelogofflinefilefull.md) | Contains the necessary data for logging that the offline log archive on the current client overflowed at some point. |
| [IPPARAMS structure](..\printoem\ns-printoem-ipparams.md) | The IPPARAMS structure is used as an input parameter to a rendering plug-in's IPrintOemUni |
| [MESSAGEBOX_PARAMS structure](..\winsplp\ns-winsplp-messagebox_params.md) | The MESSAGEBOX_PARAMS structure is used by the SplPromptUIInUsersSession function to hold information about the appearance and behavior of a message box. |
| [OEMMEMORYUSAGE structure](..\printoem\ns-printoem-oemmemoryusage.md) | The OEMMEMORYUSAGE structure is used as an input parameter to a rendering plug-in's IPrintOemUni |
| [PrintNamedProperty structure](..\winspool\ns-winspool-printnamedproperty.md) | . |
| [PrintPropertiesCollection structure](..\winspool\ns-winspool-printpropertiescollection.md) | . |
| [PrintPropertyValue structure](..\winspool\ns-winspool-printpropertyvalue.md) | . |
| [SHOWUIPARAMS structure](..\winsplp\ns-winsplp-showuiparams.md) | The SplPromptUIInUsersSession function uses the SHOWUIPARAMS structure to hold information about the appearance and behavior of a message box. |
| [_ATTRIBUTE_INFO_1 structure](..\winddiui\ns-winddiui-_attribute_info_1.md) | The ATTRIBUTE_INFO_1 structure is used as a parameter for a printer interface DLL's DrvQueryJobAttributes function. All member values are function-supplied. |
| [_ATTRIBUTE_INFO_2 structure](..\winddiui\ns-winddiui-_attribute_info_2.md) | The ATTRIBUTE_INFO_2 structure is used as a parameter for a printer interface DLL's DrvQueryJobAttributes function. All member values are function-supplied. |
| [_ATTRIBUTE_INFO_3 structure](..\winddiui\ns-winddiui-_attribute_info_3.md) | The ATTRIBUTE_INFO_3 structure is used as a parameter for a printer interface DLL's DrvQueryJobAttributes function. All member values are function-supplied. |
| [_ATTRIBUTE_INFO_4 structure](..\winddiui\ns-winddiui-_attribute_info_4.md) | The ATTRIBUTE_INFO_4 structure is used as a parameter for a printer interface DLL's DrvQueryJobAttributes function. |
| [_BIDI_DATA structure](..\winspool\ns-winspool-_bidi_data.md) | The BIDI_DATA structure is used to store the values of a bidi schema. |
| [_BIDI_REQUEST_CONTAINER structure](..\winspool\ns-winspool-_bidi_request_container.md) | The BIDI_REQUEST_CONTAINER structure is a container for a list of bidi requests. |
| [_BIDI_REQUEST_DATA structure](..\winspool\ns-winspool-_bidi_request_data.md) | The BIDI_REQUEST_DATA structure holds a single bidi request. |
| [_BIDI_RESPONSE_CONTAINER structure](..\winspool\ns-winspool-_bidi_response_container.md) | The BIDI_RESPONSE_CONTAINER structure is a container for a list of bidi responses. |
| [_BIDI_RESPONSE_DATA structure](..\winspool\ns-winspool-_bidi_response_data.md) | The BIDI_RESPONSE_DATA structure holds a single bidi response. |
| [_BINARY_CONTAINER structure](..\winspool\ns-winspool-_binary_container.md) | The BINARY_CONTAINER structure is a container for binary data. |
| [_COMPROPSHEETUI structure](..\compstui\ns-compstui-_compropsheetui.md) | The COMPROPSHEETUI structure is used as an input parameter to CPSUI's ComPropSheet function, if the function code is CPSFUNC_ADD_PCOMPROPSHEETUI. All structure members must be supplied by the caller of ComPropSheet. |
| [_CONFIG_INFO_DATA_1 structure](..\tcpxcv\ns-tcpxcv-_config_info_data_1.md) | The XcvData function uses a CONFIG_INFO_DATA_1 structure when it obtains configuration data for a particular port. |
| [_CPSUICBPARAM structure](..\compstui\ns-compstui-_cpsuicbparam.md) | The CPSUICBPARAM structure is used as the input parameter to _CPSUICALLBACK-typed callback functions. |
| [_CPSUIDATABLOCK structure](..\compstui\ns-compstui-_cpsuidatablock.md) | The CPSUIDATABLOCK structure is used as a parameter for the ComPropSheet function, if the function code is CPSFUNC_SET_DATABLOCK or CPSFUNC_QUERY_DATABLOCK. |
| [_CUSTOMSIZEPARAM structure](..\printoem\ns-printoem-_customsizeparam.md) | The CUSTOMSIZEPARAM structure holds information pertaining to a single custom page size parameter for a printer. |
| [_DATA_HEADER structure](..\prntfont\ns-prntfont-_data_header.md) | The DATA_HEADER structure is used to specify a data section within a Unidrv font format file (.uff file). |
| [_DELETE_PORT_DATA_1 structure](..\tcpxcv\ns-tcpxcv-_delete_port_data_1.md) | The XcvData function uses a DELETE_PORT_DATA_1 structure when it deletes a port. |
| [_DEVICEPROPERTYHEADER structure](..\winddiui\ns-winddiui-_devicepropertyheader.md) | The DEVICEPROPERTYHEADER structure is used as an input parameter to a printer interface DLL's DrvDevicePropertySheets function. |
| [_DEVOBJ structure](..\printoem\ns-printoem-_devobj.md) | The DEVOBJ structure is used as an input argument to several of a rendering plug-in's COM interface methods. |
| [_DEVQUERYPRINT_INFO structure](..\winddiui\ns-winddiui-_devqueryprint_info.md) | The DEVQUERYPRINT_INFO structure is used as an input parameter to a printer interface DLL's DevQueryPrintEx function. |
| [_DLGPAGE structure](..\compstui\ns-compstui-_dlgpage.md) | The DLGPAGE structure is used for specifying a property sheet page to CPSUI's ComPropSheet function. The structure's address is included in a COMPROPSHEETUI structure, and all member values are supplied by the ComPropSheet caller. |
| [_DOCEVENT_CREATEDCPRE structure](..\winddiui\ns-winddiui-_docevent_createdcpre.md) | The DOCEVENT_CREATEDCPRE structure contains a set of values used in certain calls to DrvDocumentEvent and IPrintOemUI2 |
| [_DOCEVENT_ESCAPE structure](..\winddiui\ns-winddiui-_docevent_escape.md) | The DOCEVENT_ESCAPE structure is a container for values used as parameters for the ExtEscape function. |
| [_DOCEVENT_FILTER structure](..\winddiui\ns-winddiui-_docevent_filter.md) | The DOCEVENT_FILTER structure contains a list of document events to which the printer driver will respond. See DrvDocumentEvent for a complete list of the document events. |
| [_DOCUMENTPROPERTYHEADER structure](..\winddiui\ns-winddiui-_documentpropertyheader.md) | The DOCUMENTPROPERTYHEADER structure is used as an input parameter to a printer interface DLL's DrvDocumentPropertySheets function. |
| [_DOT4_ACTIVITY structure](..\d4iface\ns-d4iface-_dot4_activity.md) | . |
| [_DOT4_DC_CREATE_DATA structure](..\d4drvif\ns-d4drvif-_dot4_dc_create_data.md) | Defines the DOT4_DC_CREATE_DATA construct. |
| [_DOT4_DC_DESTROY_DATA structure](..\d4drvif\ns-d4drvif-_dot4_dc_destroy_data.md) | This topic describes the DOT4_DC_DESTROY_DATA structure. |
| [_DOT4_DC_OPEN_DATA structure](..\d4drvif\ns-d4drvif-_dot4_dc_open_data.md) | This topic describes the DOT4_DC_OPEN_DATA structure. |
| [_DOT4_DRIVER_CMD structure](..\d4drvif\ns-d4drvif-_dot4_driver_cmd.md) | This topic describes the DOT4_DRIVER_CMD structure. |
| [_DRIVER_INFO_8A structure](..\winspool\ns-winspool-_driver_info_8a.md) | The DRIVER_INFO_8 structure contains printer driver information. |
| [_DRIVER_INFO_8W structure](..\winspool\ns-winspool-_driver_info_8w.md) | The DRIVER_INFO_8 structure contains printer driver information. |
| [_DRIVER_UPGRADE_INFO_1 structure](..\winddiui\ns-winddiui-_driver_upgrade_info_1.md) | The DRIVER_UPGRADE_INFO_1 structure is used as an input to a printer interface DLL's DrvUpgradePrinter function. |
| [_DRIVER_UPGRADE_INFO_2 structure](..\winddiui\ns-winddiui-_driver_upgrade_info_2.md) | The DRIVER_UPGRADE_INFO_2 structure is used as an input to a printer interface DLL's DrvUpgradePrinter function. |
| [_DRVPROCS structure](..\printoem\ns-printoem-_drvprocs.md) | The DRVPROCS structure is obsolete and is not used with the COM interfaces for Microsoft printer drivers. |
| [_EXTCHKBOX structure](..\compstui\ns-compstui-_extchkbox.md) | The EXTCHKBOX structure is used by CPSUI applications (including printer interface DLLs) for specifying an extended check box, which can be added to a property sheet page option. |
| [_EXTPUSH structure](..\compstui\ns-compstui-_extpush.md) | The EXTPUSH structure is used by CPSUI applications (including printer interface DLLs) for specifying an extended push button, which can be added to a property sheet page option. When the button is pushed, a new dialog can be displayed. |
| [_EXTTEXTMETRIC structure](..\prntfont\ns-prntfont-_exttextmetric.md) | The EXTTEXTMETRIC structure is used to specify font-specific information within Unidrv font metrics files (.ufm files). |
| [_FINVOCATION structure](..\printoem\ns-printoem-_finvocation.md) | The FINVOCATION structure is used as input to the IPrintOemUni |
| [_GETINFO_FONTOBJ structure](..\printoem\ns-printoem-_getinfo_fontobj.md) | The GETINFO_FONTOBJ structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [_GETINFO_GLYPHBITMAP structure](..\printoem\ns-printoem-_getinfo_glyphbitmap.md) | The GETINFO_GLYPHBITMAP structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [_GETINFO_GLYPHSTRING structure](..\printoem\ns-printoem-_getinfo_glyphstring.md) | The GETINFO_GLYPHSTRING structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [_GETINFO_GLYPHWIDTH structure](..\printoem\ns-printoem-_getinfo_glyphwidth.md) | The GETINFO_GLYPHWIDTH structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [_GETINFO_MEMORY structure](..\printoem\ns-printoem-_getinfo_memory.md) | The GETINFO_MEMORY structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [_GETINFO_STDVAR structure](..\printoem\ns-printoem-_getinfo_stdvar.md) | The GETINFO_STDVAR structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [_GLYPHRUN structure](..\prntfont\ns-prntfont-_glyphrun.md) | The GLYPHRUN structure is one of the structures used to define the contents of glyph translation table files (.gtt files). |
| [_INSERTPSUIPAGE_INFO structure](..\compstui\ns-compstui-_insertpsuipage_info.md) | The INSERTPSUIPAGE_INFO structure is used as an input parameter to CPSUI's ComPropSheet function, if the function code is CPSFUNC_INSERT_PSUIPAGE. All member values must be supplied by the ComPropSheet caller. |
| [_INVOC structure](..\prntfont\ns-prntfont-_invoc.md) | The INVOC structure is used for describing printer command strings in Unidrv font metrics files (.ufm files) and glyph translation table files (.gtt files). |
| [_KERNDATA structure](..\prntfont\ns-prntfont-_kerndata.md) | The KERNDATA structure is used for describing printer kerning pairs. |
| [_MAPTABLE structure](..\prntfont\ns-prntfont-_maptable.md) | The MAPTABLE structure is one of the structures used to define the contents of glyph translation table files (.gtt files). |
| [_MONITOR structure](..\winsplp\ns-winsplp-_monitor.md) | The MONITOR structure is obsolete and is supported only for compatibility reasons. |
| [_MONITOR2 structure](..\winsplp\ns-winsplp-_monitor2.md) | The MONITOR2 structure contains pointers to the functions defined by print monitors. |
| [_MONITOREX structure](..\winsplp\ns-winsplp-_monitorex.md) | The MONITOREX structure is obsolete and supported for compatibility purposes only. |
| [_MONITORINIT structure](..\winsplp\ns-winsplp-_monitorinit.md) | The MONITORINIT structure is used as an input parameter to a print monitor's InitializePrintMonitor2 function. |
| [_MONITORREG structure](..\winsplp\ns-winsplp-_monitorreg.md) | The MONITORREG structure supplies print monitors with the address of registry functions to use instead of Win32 registry API functions. |
| [_MONITORUI structure](..\winsplp\ns-winsplp-_monitorui.md) | The MONITORUI structure contains pointers to the functions within a port monitor UI DLL that the print spooler calls. |
| [_NOTIFICATION_CONFIG_1 structure](..\winsplp\ns-winsplp-_notification_config_1.md) | . |
| [_OEMCUIPPARAM structure](..\printoem\ns-printoem-_oemcuipparam.md) | The OEMCUIPPARAM structure is used as an input parameter to a user interface plug-in's IPrintOemUI |
| [_OEMDMPARAM structure](..\printoem\ns-printoem-_oemdmparam.md) | The OEMDMPARAM structure is used as an input parameter to the IPrintOemUI |
| [_OEMFONTINSTPARAM structure](..\prntfont\ns-prntfont-_oemfontinstparam.md) | The OEMFONTINSTPARAM structure is used as an input parameter to a user interface plug-in's IPrintOemUI |
| [_OEMUIOBJ structure](..\printoem\ns-printoem-_oemuiobj.md) | The OEMUIOBJ structure is used as an input argument to several of the methods exported by user interface plug-ins. |
| [_OEMUIPROCS structure](..\printoem\ns-printoem-_oemuiprocs.md) | The OEMUIPROCS structure is obsolete.The OEMUIPROCS structure contains the address of the DrvGetDriverSetting and DrvUpdateUISetting functions that are exported by Microsoft printer drivers. |
| [_OEMUIPSPARAM structure](..\printoem\ns-printoem-_oemuipsparam.md) | The OEMUIPSPARAM structure is passed to a user interface plug-in's IPrintOemUI |
| [_OEM_DMEXTRAHEADER structure](..\printoem\ns-printoem-_oem_dmextraheader.md) | The OEM_DMEXTRAHEADER structure must be used to define the first members of a set of private DEVMODEW structure members. |
| [_OIEXT structure](..\compstui\ns-compstui-_oiext.md) | The OIEXT structure supplies additional, optional information about a property sheet page option that is described by an OPTITEM structure. |
| [_OPTCOMBO structure](..\compstui\ns-compstui-_optcombo.md) | . |
| [_OPTITEM structure](..\compstui\ns-compstui-_optitem.md) | The OPTITEM structure is used by CPSUI applications (including printer interface DLLs) for describing one property sheet option on a property sheet page, if the page is described by a COMPROPSHEETUI structure. |
| [_OPTPARAM structure](..\compstui\ns-compstui-_optparam.md) | An array of OPTPARAM structures is used by CPSUI applications (including printer interface DLLs) for describing all the parameter values associated with a property sheet option. The array's address is included in an OPTTYPE structure. |
| [_OPTTYPE structure](..\compstui\ns-compstui-_opttype.md) | The OPTTYPE structure is used by CPSUI applications (including printer interface DLLs) for describing the type and other characteristics of a property sheet option, if the option is specified by an OPTITEM structure. |
| [_PDEV_ADJUST_GRAPHICS_RESOLUTION structure](..\printoem\ns-printoem-_pdev_adjust_graphics_resolution.md) | The PDEV_ADJUST_GRAPHICS_RESOLUTION structure specifies a graphics resolution value. |
| [_PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA structure](..\printoem\ns-printoem-_pdev_adjust_imageable_origin_area.md) | The PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA structure specifies the imageable origin area. |
| [_PDEV_ADJUST_PAPER_MARGIN structure](..\printoem\ns-printoem-_pdev_adjust_paper_margin.md) | The PDEV_ADJUST_PAPER_MARGIN structure specifies the imageable printing area. |
| [_PDEV_ADJUST_PHYSICAL_PAPER_SIZE structure](..\printoem\ns-printoem-_pdev_adjust_physical_paper_size.md) | The PDEV_ADJUST_PAPER_PHYSICAL_SIZE structure specifies a paper size value. |
| [_PDEV_HOSTFONT_ENABLED structure](..\printoem\ns-printoem-_pdev_hostfont_enabled.md) | The PDEV_HOSTFONT_ENABLED structure indicates whether the Hostfont feature is enabled. |
| [_PDEV_USE_TRUE_COLOR structure](..\printoem\ns-printoem-_pdev_use_true_color.md) | The PDEV_USE_TRUE_COLOR structure indicates whether the output color space should be color or grayscale. |
| [_PORT_DATA_1 structure](..\tcpxcv\ns-tcpxcv-_port_data_1.md) | The XcvData function uses a PORT_DATA_1 structure when it adds a port or configures an existing port. |
| [_PRINTER_EVENT_ATTRIBUTES_INFO structure](..\winddiui\ns-winddiui-_printer_event_attributes_info.md) | The PRINTER_EVENT_ATTRIBUTES_INFO structure contains the former attributes and the new attributes for a printer. |
| [_PRINTER_NOTIFY_INIT structure](..\winsplp\ns-winsplp-_printer_notify_init.md) | . |
| [_PRINTPROCESSOROPENDATA structure](..\winsplp\ns-winsplp-_printprocessoropendata.md) | The PRINTPROCESSOROPENDATA structure is used as an input parameter to a print processor's OpenPrintProcessor function. |
| [_PRINTPROVIDOR structure](..\winsplp\ns-winsplp-_printprovidor.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [_PRINT_FEATURE_OPTION structure](..\prcomoem\ns-prcomoem-_print_feature_option.md) | The PRINT_FEATURE_OPTION structure contains information about a feature-option pair, where the option is one option of a particular feature. |
| [_PROPSHEETUI_GETICON_INFO structure](..\compstui\ns-compstui-_propsheetui_geticon_info.md) | The PROPSHEETUI_GETICON_INFO structure is used as an input parameter to an application's PFNPROPSHEETUI-typed function, when the function is called with a reason value of PROPSHEETUI_REASON_GET_ICON. |
| [_PROPSHEETUI_INFO structure](..\compstui\ns-compstui-_propsheetui_info.md) | The PROPSHEETUI_INFO structure is used as an input parameter to PFNPROPSHEETUI-typed functions. |
| [_PROPSHEETUI_INFO_HEADER structure](..\compstui\ns-compstui-_propsheetui_info_header.md) | The PROPSHEETUI_INFO_HEADER structure is used as an input parameter to an application's PFNPROPSHEETUI-typed function, when the function is called with a reason value of PROPSHEETUI_REASON_GET_INFO_HEADER. |
| [_PSCRIPT5_PRIVATE_DEVMODE structure](..\printoem\ns-printoem-_pscript5_private_devmode.md) | The PSCRIPT5_PRIVATE_DEVMODE structure enables Pscript5 plug-ins to determine the size of the private portion of Pscript5's DEVMODEW structure. |
| [_PSPINFO structure](..\compstui\ns-compstui-_pspinfo.md) | The PSPINFO structure is used as an input parameter to a property sheet page's dialog box procedure, when the Windows message is WM_INITDIALOG. The dialog box procedure's address is specified in a DLGPAGE structure. |
| [_PUBLISHERINFO structure](..\printoem\ns-printoem-_publisherinfo.md) | The PUBLISHERINFO structure is used as an input parameter to the IPrintOemPS |
| [_SETRESULT_INFO structure](..\compstui\ns-compstui-_setresult_info.md) | The SETRESULT_INFO structure is used as an input parameter to an application's PFNPROPSHEETUI-typed callback function. |
| [_SIMULATE_CAPS_1 structure](..\printoem\ns-printoem-_simulate_caps_1.md) | The SIMULATE_CAPS_1 structure contains information about the types of simulations a spooler supports. |
| [_SPLCLIENT_INFO_1 structure](..\winsplp\ns-winsplp-_splclient_info_1.md) | The SPLCLIENT_INFO_1 structure is used as input to the GenerateCopyFilePaths function that is exported by Point and Print DLLs. |
| [_SPLCLIENT_INFO_2_V1 structure](..\winsplp\ns-winsplp-_splclient_info_2_v1.md) | Contains the handle for the server-side printer that is used to make direct API calls from the client to the server without the overhead of the RPC. |
| [_SPLCLIENT_INFO_2_V2 structure](..\winsplp\ns-winsplp-_splclient_info_2_v2.md) | . |
| [_SPLCLIENT_INFO_2_V3 structure](..\winsplp\ns-winsplp-_splclient_info_2_v3.md) | . |
| [_SPLCLIENT_INFO_3_VISTA structure](..\winsplp\ns-winsplp-_splclient_info_3_vista.md) | Contains a super-set of the information in both a SPLCLIENT_INFO_1 and SPLCLIENT_INFO_2 structure. It also contains additional information needed by the provider. |
| [_TRANSDATA structure](..\prntfont\ns-prntfont-_transdata.md) | The TRANSDATA structure is one of the structures used to define the contents of glyph translation table files (.gtt files). |
| [_UFF_FILEHEADER structure](..\prntfont\ns-prntfont-_uff_fileheader.md) | The UFF_FILEHEADER structure is used to define the contents of Unidrv font format files (.uff files). |
| [_UFF_FONTDIRECTORY structure](..\prntfont\ns-prntfont-_uff_fontdirectory.md) | The UFF_FONTDIRECTORY structure is used to specify the directory of font descriptions contained in a Unidrv font format file (.uff file). |
| [_UNIDRVINFO structure](..\prntfont\ns-prntfont-_unidrvinfo.md) | The UNIDRVINFO structure is used to specify printer-specific information within Unidrv font metrics files (.ufm files). |
| [_UNIDRV_PRIVATE_DEVMODE structure](..\printoem\ns-printoem-_unidrv_private_devmode.md) | The UNIDRV_PRIVATE_DEVMODE structure enables Unidrv plug-ins to determine the size of the private portion of Unidrv's DEVMODEW structure. |
| [_UNIFM_HDR structure](..\prntfont\ns-prntfont-_unifm_hdr.md) | The UNIFM_HDR structure is used to define the contents of Unidrv font metrics files (.ufm files). |
| [_UNIFONTOBJ structure](..\printoem\ns-printoem-_unifontobj.md) | The UNIFONTOBJ structure is used as an input parameter to font functions in rendering plug-ins. |
| [_UNI_CODEPAGEINFO structure](..\prntfont\ns-prntfont-_uni_codepageinfo.md) | The UNI_CODEPAGEINFO structure is one of the structures used to define the contents of glyph translation table files (.gtt files). |
| [_UNI_GLYPHSETDATA structure](..\prntfont\ns-prntfont-_uni_glyphsetdata.md) | The UNI_GLYPHSEDATA structure is one of the structures used to define the contents of glyph translation table files (.gtt files). |
| [_USERDATA structure](..\printoem\ns-printoem-_userdata.md) | The USERDATA structure is used by Unidrv and Pscript to specify additional information about printer features. A USERDATA structure pointer is supplied as the UserData member for each OPTITEM structure. |
| [_WIDTHRUN structure](..\prntfont\ns-prntfont-_widthrun.md) | The WIDTHRUN structure is used to define the contents of Unidrv font metrics files (.ufm files). |
| [_WIDTHTABLE structure](..\prntfont\ns-prntfont-_widthtable.md) | The WIDTHTABLE structure is used to define the contents of Unidrv font metrics files (.ufm files). |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [BIDI_TYPE Enumeration](..\winspool\ne-winspool-bidi_type.md) | The BIDI_TYPE enumeration lists the possible values of data transferred in a bidi operation. |
| [BMFORMAT Enumeration](..\icm\ne-icm-bmformat.md) | The values of the BMFORMAT enumeration are used by WCS functions to indicate the format that particular bitmaps are in. This data type is extended from BMFORMAT that is available in versions of Windows released before Windows Vista. |
| [COLORDATATYPE Enumeration](..\icm\ne-icm-colordatatype.md) | The values of the COLORDATATYPE enumeration are used by WCS functions to indicate the data type of vector content. |
| [COLORPROFILESUBTYPE Enumeration](..\icm\ne-icm-colorprofilesubtype.md) | The COLORPROFILESUBTYPE enumeration is used to specify the subtype of color profile. |
| [COLORPROFILETYPE Enumeration](..\icm\ne-icm-colorprofiletype.md) | The COLORPROFILETYPE enumeration is used to specify the type of color profile. |
| [COLORTYPE Enumeration](..\icm\ne-icm-colortype.md) | The values of the COLORTYPE enumeration are used by WCS functions to indicate the format of vector content. Most values have equivalent structures that are contained in the ICM COLOR structure (described in the Microsoft Windows SDK documentation). |
| [UI_TYPE Enumeration](..\winsplp\ne-winsplp-ui_type.md) | . |
| [WCS_PROFILE_MANAGEMENT_SCOPE Enumeration](..\icm\ne-icm-wcs_profile_management_scope.md) | The WCS_PROFILE_MANAGEMENT_SCOPE enumeration is used to specify the scope of a profile management operation, such as associating a profile with a device. |
| [_EATTRIBUTE_DATATYPE Enumeration](..\printoem\ne-printoem-_eattribute_datatype.md) | The EATTRIBUTE_DATATYPE enumerates the possible data types for a global attribute, feature attribute or option attribute. |
| [_NOTIFICATION_CALLBACK_COMMANDS Enumeration](..\winsplp\ne-winsplp-_notification_callback_commands.md) | . |
| [_NOTIFICATION_CONFIG_FLAGS Enumeration](..\winsplp\ne-winsplp-_notification_config_flags.md) | . |
| [_STDVARIABLEINDEX Enumeration](..\printoem\ne-printoem-_stdvariableindex.md) | . |
| [__MIDL___MIDL_itf_filterpipeline_0000_0000_0001 Enumeration](..\filterpipeline\ne-filterpipeline-__midl___midl_itf_filterpipeline_0000_0000_0001.md) | The ExpsCompressionOptions enumeration describes compression options for an XPS part. |
| [__MIDL___MIDL_itf_filterpipeline_0000_0000_0002 Enumeration](..\filterpipeline\ne-filterpipeline-__midl___midl_itf_filterpipeline_0000_0000_0002.md) | The EXpsFontOptions enumeration describes the font options for an XPS part. |
| [__MIDL___MIDL_itf_filterpipeline_0000_0000_0003 Enumeration](..\filterpipeline\ne-filterpipeline-__midl___midl_itf_filterpipeline_0000_0000_0003.md) | The EXpsJobConsumption enumeration describes job consumption updates. |
| [__MIDL___MIDL_itf_filterpipeline_0000_0000_0004 Enumeration](..\filterpipeline\ne-filterpipeline-__midl___midl_itf_filterpipeline_0000_0000_0004.md) | . |
| [__MIDL___MIDL_itf_xpsrassvc_0000_0001_0001 Enumeration](..\xpsrassvc\ne-xpsrassvc-__midl___midl_itf_xpsrassvc_0000_0001_0001.md) | The XPSRAS_RENDERING_MODE enumeration specifies the rendering mode to be used by an XPS rasterizer. |
| [__MIDL___MIDL_itf_xpsrassvc_0000_0003_0001 Enumeration](..\xpsrassvc\ne-xpsrassvc-__midl___midl_itf_xpsrassvc_0000_0003_0001.md) | XPSRAS_PIXEL_FORMAT allows a caller to select the pixel format used by the IWICBitmap interface that is returned by the IXpsRasterizer |
| [__MIDL___MIDL_itf_xpsrassvc_0000_0004_0001 Enumeration](..\xpsrassvc\ne-xpsrassvc-__midl___midl_itf_xpsrassvc_0000_0004_0001.md) | XPSRAS_BACKGROUND_COLOR specifies the background clear color to be used by an XPS rasterizer |
| [tagOEMPTOPTS Enumeration](..\prcomoem\ne-prcomoem-tagoemptopts.md) | . |
| [tagPrintJobStatus Enumeration](..\printerextension\ne-printerextension-tagprintjobstatus.md) | This enumeration is a one-to-one mapping to the spooler flags suppled in the JOB_INFO_X structures. |
| [tagPrintSchemaConstrainedSetting Enumeration](..\printerextension\ne-printerextension-tagprintschemaconstrainedsetting.md) | The PrintSchemaConstrainedSetting enumeration specifies whether the Option is available based on the current device configuration. The constrained attribute appears only in a PrintCapabilities document. |
| [tagPrintSchemaParameterDataType Enumeration](..\printerextension\ne-printerextension-tagprintschemaparameterdatatype.md) | The PrintSchemaParameterDataType enumeration identifies the allowed data types for the Print Schema parameter. |
| [tagPrintSchemaSelectionType Enumeration](..\printerextension\ne-printerextension-tagprintschemaselectiontype.md) | The PrintSchemaSelectionType enumeration identifies how a Feature’s options should be selected. This property appears only in a PrintCapabilities document. |
| [tagSHIMOPTS Enumeration](..\prdrvcom\ne-prdrvcom-tagshimopts.md) | . |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_DOT4_ADD_ACTIVITY_BROADCAST IOCTL](..\d4drvif\ni-d4drvif-ioctl_dot4_add_activity_broadcast.md) | This topic describes IOCTL_DOT4_ADD_ACTIVITY_BROADCAST. |
| [IOCTL_DOT4_CLOSE_CHANNEL IOCTL](..\d4drvif\ni-d4drvif-ioctl_dot4_close_channel.md) | This topic describes IOCTL_DOT4_CLOSE_CHANNEL. |
| [IOCTL_DOT4_CREATE_SOCKET IOCTL](..\d4drvif\ni-d4drvif-ioctl_dot4_create_socket.md) | This topic describes IOCTL_DOT4_CREATE_SOCKET. |
| [IOCTL_DOT4_DESTROY_SOCKET IOCTL](..\d4drvif\ni-d4drvif-ioctl_dot4_destroy_socket.md) | This topic describes IOCTL_DOT4_DESTROY_SOCKET. |
| [IOCTL_DOT4_LAST IOCTL](..\d4drvif\ni-d4drvif-ioctl_dot4_last.md) | This topic describes IOCTL_DOT4_LAST. |
| [IOCTL_DOT4_OPEN_CHANNEL IOCTL](..\d4drvif\ni-d4drvif-ioctl_dot4_open_channel.md) | This topic describes IOCTL_DOT4_OPEN_CHANNEL. |
| [IOCTL_DOT4_READ IOCTL](..\d4drvif\ni-d4drvif-ioctl_dot4_read.md) | This topic describes IOCTL_DOT4_READ. |
| [IOCTL_DOT4_REMOVE_ACTIVITY_BROADCAST IOCTL](..\d4drvif\ni-d4drvif-ioctl_dot4_remove_activity_broadcast.md) | This topic describes IOCTL_DOT4_REMOVE_ACTIVITY_BROADCAST. |
| [IOCTL_DOT4_USER_BASE IOCTL](..\d4drvif\ni-d4drvif-ioctl_dot4_user_base.md) | This topic describes IOCTL_DOT4_USER_BASE. |
| [IOCTL_DOT4_WAIT_ACTIVITY_BROADCAST IOCTL](..\d4drvif\ni-d4drvif-ioctl_dot4_wait_activity_broadcast.md) | This topic describes IOCTL_DOT4_WAIT_ACTIVITY_BROADCAST. |
| [IOCTL_DOT4_WAIT_FOR_CHANNEL IOCTL](..\d4drvif\ni-d4drvif-ioctl_dot4_wait_for_channel.md) | This topic describes IOCTL_DOT4_WAIT_FOR_CHANNEL. |
| [IOCTL_DOT4_WRITE IOCTL](..\d4drvif\ni-d4drvif-ioctl_dot4_write.md) | This topic describes IOCTL_DOT4_WRITE. |

## Interfaces

| Title   | Description   |
| ---- |:---- |
| [IBidiRequest interface](..\bidispl\nn-bidispl-ibidirequest.md) | The IBidiRequest interface allows an application or other objects to compose a bidi request. |
| [IBidiRequestContainer interface](..\bidispl\nn-bidispl-ibidirequestcontainer.md) | The IBidiRequestContainer interface allows an application or other objects to compose and retrieve a list of bidi requests. |
| [IBidiSpl interface](..\bidispl\nn-bidispl-ibidispl.md) | The IBidiSpl interface allows an application or other objects to send a single bidi request or a list of bidi requests. |
| [IBidiSpl2 interface](..\bidispl\nn-bidispl-ibidispl2.md) | The IBidiSpl2 interface enables an application or other objects to send one or more bidi requests using one of the Bidi Request Schemas and receive information formatted as one of the Bidi Response Schemas. |
| [IFixedDocument interface](..\filterpipeline\nn-filterpipeline-ifixeddocument.md) | The IFixedDocument interface represents a fixed document for an XPS document sequence. |
| [IFixedDocumentSequence interface](..\filterpipeline\nn-filterpipeline-ifixeddocumentsequence.md) | The IFixedDocumentSequence interface represents the fixed document sequence for an XPS document. |
| [IFixedPage interface](..\filterpipeline\nn-filterpipeline-ifixedpage.md) | A filter uses the IFixedPage interface to work with fixed pages in an XPS document. |
| [IInterFilterCommunicator interface](..\filterpipeline\nn-filterpipeline-iinterfiltercommunicator.md) | The IInterFilterCommunicator interface is implemented in an object that resides in the PrintFilterPipelineSvc service and is made available to filters through methods in the IPrintPipelineFilter interface. |
| [IPartBase interface](..\filterpipeline\nn-filterpipeline-ipartbase.md) | The IPartBase interface is a common base for document part interfaces. |
| [IPartColorProfile interface](..\filterpipeline\nn-filterpipeline-ipartcolorprofile.md) | The IPartColorProfile interface is the abstraction for an XPS color profile. |
| [IPartDiscardControl interface](..\filterpipeline\nn-filterpipeline-ipartdiscardcontrol.md) | The filter pipeline supports the discard control. |
| [IPartFont interface](..\filterpipeline\nn-filterpipeline-ipartfont.md) | The IPartFont interface is the abstraction for fonts in a part. |
| [IPartFont2 interface](..\filterpipeline\nn-filterpipeline-ipartfont2.md) | . |
| [IPartImage interface](..\filterpipeline\nn-filterpipeline-ipartimage.md) | The IPartImage interface is the abstraction for images in an XPS document. |
| [IPartPrintTicket interface](..\filterpipeline\nn-filterpipeline-ipartprintticket.md) | The IPartPrintTicket interface is the abstraction for a print ticket in an XPS document. |
| [IPartResourceDictionary interface](..\filterpipeline\nn-filterpipeline-ipartresourcedictionary.md) | The IPartResourceDictionary interface is the abstraction for an XPS resource dictionary. |
| [IPartThumbnail interface](..\filterpipeline\nn-filterpipeline-ipartthumbnail.md) | The IPartThumbnail interface is an abstraction for thumbnails in an XPS document. |
| [IPrintClassObjectFactory interface](..\filterpipeline\nn-filterpipeline-iprintclassobjectfactory.md) | TheIPrintClassObjectFactory interface creates print filter-related interfaces. |
| [IPrintJob interface](..\printerextension\nn-printerextension-iprintjob.md) | Contains properties that represent a print job. |
| [IPrintJobCollection interface](..\printerextension\nn-printerextension-iprintjobcollection.md) | This interfaces provides an enumeration of the jobs in the print queue. |
| [IPrintOemEngine interface](..\prcomoem\nn-prcomoem-iprintoemengine.md) | . |
| [IPrintPipelineFilter interface](..\filterpipeline\nn-filterpipeline-iprintpipelinefilter.md) | The methods in the IPrintPipelineFilter interface are called for initialization and shutdown. A filter must implement these methods. |
| [IPrintPipelineManagerControl interface](..\filterpipeline\nn-filterpipeline-iprintpipelinemanagercontrol.md) | The IPrintPipelineManagerControl interface is passed to each filter in the IPrintPipelineFilter |
| [IPrintPipelineProgressReport interface](..\filterpipeline\nn-filterpipeline-iprintpipelineprogressreport.md) | A rendering filter uses the IPrintPipelineProgressReport interface to send progress status to a spooler. |
| [IPrintPipelinePropertyBag interface](..\filterpipeline\nn-filterpipeline-iprintpipelinepropertybag.md) | The IPrintPipelinePropertyBag interface is implemented by the PrintFilterPipelineSvc service and is made available to filters through methods in the IPrintPipelineFilter interface. IprintPipelinePropertyBag inherits from the IUnknown interface. |
| [IPrintReadStream interface](..\filterpipeline\nn-filterpipeline-iprintreadstream.md) | Filters use the IPrintReadStream interface to read data as a raw stream of bytes. |
| [IPrintReadStreamFactory interface](..\filterpipeline\nn-filterpipeline-iprintreadstreamfactory.md) | The IPrintReadStreamFactory interface creates a stream reader that a filter can use to access the stream. For example, a filter could use this stream to access the per-user print ticket. |
| [IPrintSchemaAsyncOperation interface](..\printerextension\nn-printerextension-iprintschemaasyncoperation.md) | Represents an asynchronous operation context for validation, merge or commit operations. |
| [IPrintSchemaAsyncOperationEvent interface](..\printerextension\nn-printerextension-iprintschemaasyncoperationevent.md) | Exposes a validation, merge, or commit completion event delegate. |
| [IPrintSchemaCapabilities interface](..\printerextension\nn-printerextension-iprintschemacapabilities.md) | Provides the primary method to access PrintCapabilities. |
| [IPrintSchemaCapabilities2 interface](..\printerextension\nn-printerextension-iprintschemacapabilities2.md) | The IPrintSchemaCapabilities2 interface represents an extension to the IPrintSchemaCapabilities object, which provides wrapper methods over a print capabilities document. |
| [IPrintSchemaDisplayableElement interface](..\printerextension\nn-printerextension-iprintschemadisplayableelement.md) | Provides the displayable string for a PrintCapabilites PrintSchema element. |
| [IPrintSchemaElement interface](..\printerextension\nn-printerextension-iprintschemaelement.md) | Provides access to the underlying XML node and &#0034;name&#0034; attribute information for a Print Schema element. |
| [IPrintSchemaFeature interface](..\printerextension\nn-printerextension-iprintschemafeature.md) | Exposes a Print Schema Feature element. |
| [IPrintSchemaNUpOption interface](..\printerextension\nn-printerextension-iprintschemanupoption.md) | Exposes a Print Schema NUp Option element. |
| [IPrintSchemaOption interface](..\printerextension\nn-printerextension-iprintschemaoption.md) | Exposes a Print Schema Option object. |
| [IPrintSchemaOptionCollection interface](..\printerextension\nn-printerextension-iprintschemaoptioncollection.md) | Exposes a collection of IPrintSchemaOption objects. |
| [IPrintSchemaPageImageableSize interface](..\printerextension\nn-printerextension-iprintschemapageimageablesize.md) | Exposes the PageImageableSize property of PrintCapabilities. The properties of this interface map directly to those in the PageImageableSize property of PrintCapabilities. |
| [IPrintSchemaPageMediaSizeOption interface](..\printerextension\nn-printerextension-iprintschemapagemediasizeoption.md) | Exposes a Print Schema PageMediaSize Option element. |
| [IPrintSchemaParameterDefinition interface](..\printerextension\nn-printerextension-iprintschemaparameterdefinition.md) | The IPrintSchemaParameterDefinition interface represents a parameter definition, as defined in the Print Schema Specification. |
| [IPrintSchemaParameterInitializer interface](..\printerextension\nn-printerextension-iprintschemaparameterinitializer.md) | The IPrintSchemaParameterInitializer interface represents a parameter initialization value, as defined in the print schema specification. |
| [IPrintSchemaTicket interface](..\printerextension\nn-printerextension-iprintschematicket.md) | Provides the primary method to access and validate a PrintTicket. |
| [IPrintSchemaTicket2 interface](..\printerextension\nn-printerextension-iprintschematicket2.md) | The IPrintSchemaTicket2 interface is an extension to the IPrintSchemaTicket interface, which provides wrapper methods over a print ticket document. |
| [IPrintWriteStream interface](..\filterpipeline\nn-filterpipeline-iprintwritestream.md) | Filters use the IPrintWriteStream interface to write data as a raw stream of bytes. |
| [IPrintWriteStreamFlush interface](..\filterpipeline\nn-filterpipeline-iprintwritestreamflush.md) | Filters use the IPrintWriteStreamFlush interface to explicitly flush data as a raw stream of bytes from a filter. This interface is retrieved through IPrintWriteStream |
| [IPrinterBidiSetRequestCallback interface](..\printerextension\nn-printerextension-iprinterbidisetrequestcallback.md) | Describes the signature of the callback object that receives the Bidi response. |
| [IPrinterExtensionAsyncOperation interface](..\printerextension\nn-printerextension-iprinterextensionasyncoperation.md) | Provides the context associated with an asynchronous operation. |
| [IPrinterExtensionContext interface](..\printerextension\nn-printerextension-iprinterextensioncontext.md) | Represents the context for the activation of a UWP device app for printers. |
| [IPrinterExtensionContextCollection interface](..\printerextension\nn-printerextension-iprinterextensioncontextcollection.md) | Exposes a collection of IPrinterExtensionContext objects. |
| [IPrinterExtensionEventArgs interface](..\printerextension\nn-printerextension-iprinterextensioneventargs.md) | Represents the context for the desktop printer extension activation. |
| [IPrinterExtensionRequest interface](..\printerextension\nn-printerextension-iprinterextensionrequest.md) | Completes the given extension event with either a cancellation or success. |
| [IPrinterPropertyBag interface](..\printerextension\nn-printerextension-iprinterpropertybag.md) | Provides strongly-typed get and set methods. |
| [IPrinterQueue interface](..\printerextension\nn-printerextension-iprinterqueue.md) | Represents a single printer queue. |
| [IPrinterQueue2 interface](..\printerextension\nn-printerextension-iprinterqueue2.md) | Represents a single printer queue. |
| [IPrinterQueueEvent interface](..\printerextension\nn-printerextension-iprinterqueueevent.md) | Provides the event delegate for printer queue events. |
| [IPrinterQueueView interface](..\printerextension\nn-printerextension-iprinterqueueview.md) | Provides a way to change the range of print jobs being monitored. |
| [IPrinterQueueViewEvent interface](..\printerextension\nn-printerextension-iprinterqueueviewevent.md) | Provides the signature of the event handler. |
| [IPrinterScriptContext interface](..\printerextension\nn-printerextension-iprinterscriptcontext.md) | Passed to all third-party constraints JavaScript functions, and provides access to relevant objects. |
| [IPrinterScriptablePropertyBag interface](..\printerextension\nn-printerextension-iprinterscriptablepropertybag.md) | The IPrinterScriptablePropertyBag interface is the property bag interface passed to script clients. |
| [IPrinterScriptablePropertyBag2 interface](..\printerextension\nn-printerextension-iprinterscriptablepropertybag2.md) | . |
| [IPrinterScriptableStream interface](..\printerextension\nn-printerextension-iprinterscriptablestream.md) | The IPrinterScriptableStream interface builds on IPrinterScriptableSequentialStream and adds IStream-like semantics. |
| [IXpsDocument interface](..\filterpipeline\nn-filterpipeline-ixpsdocument.md) | The IXpsDocument interface represents the root of an XPS document. |
| [IXpsDocumentConsumer interface](..\filterpipeline\nn-filterpipeline-ixpsdocumentconsumer.md) | A filter uses the IXpsDocumentConsumer interface when it generates XPS content for the pipeline to consume. |
| [IXpsDocumentProvider interface](..\filterpipeline\nn-filterpipeline-ixpsdocumentprovider.md) | The IxpsDocumentProvider interface provides interfaces to consume parts of a document. |
| [IXpsPartIterator interface](..\filterpipeline\nn-filterpipeline-ixpspartiterator.md) | The IXpsPartIterator interface is an iterator for XPS parts. |
| [IXpsRasterizationFactory1 interface](..\xpsrassvc\nn-xpsrassvc-ixpsrasterizationfactory1.md) | In Windows 8, the improvement of XPSRas to handle high precision colors has led to the development of a new interface, IXPSRasterizationFactory1. |
| [IXpsRasterizationFactory2 interface](..\xpsrassvc\nn-xpsrassvc-ixpsrasterizationfactory2.md) | In Windows 10, the IXpsRasterizationFactory2 interface represents an object factory for creating components that can convert content from XPS to PWG Raster using the XPS Rasterization Service. PWG Raster supports non-square DPIs. |

## Methods

| Title   | Description   |
| ---- |:---- |
| [AddProperty method](..\filterpipeline\nf-filterpipeline-iprintpipelinepropertybag-addproperty.md) | The AddProperty method adds a property to a property bag. |
| [AddRequest method](..\bidispl\nf-bidispl-ibidirequestcontainer-addrequest.md) | The IBidiRequestContainer |
| [BindDevice method](..\bidispl\nf-bidispl-ibidispl-binddevice.md) | The IBidiSpl |
| [BindDevice method](..\bidispl\nf-bidispl-ibidispl2-binddevice.md) | The IBidiSpl2 |
| [Cancel method](..\printerextension\nf-printerextension-iprinterextensionasyncoperation-cancel.md) | Cancels the asynchronous operation. |
| [Cancel method](..\printerextension\nf-printerextension-iprinterextensionrequest-cancel.md) | Completes the extension event with a cancellation. |
| [Cancel method](..\printerextension\nf-printerextension-iprintschemaasyncoperation-cancel.md) | Cancels the asynchronous PrintSchema operation. |
| [Close method](..\filterpipeline\nf-filterpipeline-iprintwritestream-close.md) | The Close method closes a stream and ends the writing to that stream. This method is mandatory. You must call this method when the filter is done writing. |
| [CloseSender method](..\filterpipeline\nf-filterpipeline-ixpsdocumentconsumer-closesender.md) | The CloseSender method tells the Pipeline Manager that the filter is done sending XPS parts. |
| [Commit method](..\printerextension\nf-printerextension-iprinterscriptablestream-commit.md) | Commits the operation. |
| [CommitAsync method](..\printerextension\nf-printerextension-iprintschematicket-commitasync.md) | Gets an asynchronous PrintTicket commit operation context. |
| [Complete method](..\printerextension\nf-printerextension-iprinterextensionrequest-complete.md) | Completes the extension event. |
| [Completed method](..\printerextension\nf-printerextension-iprinterbidisetrequestcallback-completed.md) | Invoked when the Bidi “Set”” operation is completed. |
| [Completed method](..\printerextension\nf-printerextension-iprintschemaasyncoperationevent-completed.md) | Is called when asynchronous PrintSchema operation that is represented by an IPrintSchemaAsyncOperation context is completed. |
| [CreateRasterizer method](..\xpsrassvc\nf-xpsrassvc-ixpsrasterizationfactory2-createrasterizer.md) | The CreateRasterizer method creates an XPS rasterizer object that can convert content from XPS to PWG Raster using the XPS Rasterization Service. PWG Raster supports non-square DPIs. |
| [Current method](..\filterpipeline\nf-filterpipeline-ixpspartiterator-current.md) | The Current method provides the current URI and part. |
| [DeleteProperty method](..\filterpipeline\nf-filterpipeline-iprintpipelinepropertybag-deleteproperty.md) | The DeleteProperty method deletes a property from a property bag. |
| [DeleteResource method](..\filterpipeline\nf-filterpipeline-ifixedpage-deleteresource.md) | The DeleteResource method deletes a resource that is associated with the page. |
| [DisableDriver method](..\prcomoem\nf-prcomoem-iprintoemengine-disabledriver.md) | . |
| [DisablePDEV method](..\prcomoem\nf-prcomoem-iprintoemengine-disablepdev.md) | . |
| [EnableDriver method](..\prcomoem\nf-prcomoem-iprintoemengine-enabledriver.md) | . |
| [EnablePDEV method](..\prcomoem\nf-prcomoem-iprintoemengine-enablepdev.md) | . |
| [FilterFinished method](..\filterpipeline\nf-filterpipeline-iprintpipelinemanagercontrol-filterfinished.md) | The FilterFinished method reports that a filter is finished processing. |
| [FlushData method](..\filterpipeline\nf-filterpipeline-iprintwritestreamflush-flushdata.md) | The FlushData method flushes buffered data to a data stream while leaving the stream open, allowing the caller to write additional data to the stream. |
| [GetAt method](..\printerextension\nf-printerextension-iprinterextensioncontextcollection-getat.md) | Gets a pointer to an IPrinterExtensionContext object. |
| [GetAt method](..\printerextension\nf-printerextension-iprintjobcollection-getat.md) | Gets a pointer to an IPrintJob object. |
| [GetAt method](..\printerextension\nf-printerextension-iprintschemaoptioncollection-getat.md) | Gets a pointer to an IPrintSchemaOption object. |
| [GetBool method](..\printerextension\nf-printerextension-iprinterpropertybag-getbool.md) | Reads a specified boolean property. |
| [GetBool method](..\printerextension\nf-printerextension-iprinterscriptablepropertybag-getbool.md) | Gets a specified boolean property. |
| [GetBytes method](..\printerextension\nf-printerextension-iprinterpropertybag-getbytes.md) | Reads a byte array property. |
| [GetBytes method](..\printerextension\nf-printerextension-iprinterscriptablepropertybag-getbytes.md) | Gets a byte array property. |
| [GetCapabilities method](..\printerextension\nf-printerextension-iprintschematicket-getcapabilities.md) | Gets an IPrintSchemaCapabilities object that represents the printer capabilities based on the current settings of this IPrintSchemaTicket object. |
| [GetDiscardProperties method](..\filterpipeline\nf-filterpipeline-ipartdiscardcontrol-getdiscardproperties.md) | The GetDiscardProperties method gets the properties of the discard control. |
| [GetEnumCount method](..\bidispl\nf-bidispl-ibidirequest-getenumcount.md) | The IBidiRequest |
| [GetEnumObject method](..\bidispl\nf-bidispl-ibidirequestcontainer-getenumobject.md) | The IBidiRequestContainer |
| [GetFeature method](..\printerextension\nf-printerextension-iprintschemacapabilities-getfeature.md) | Gets a named feature from the PrintCapabilities, by name and full namespace URI. |
| [GetFeature method](..\printerextension\nf-printerextension-iprintschematicket-getfeature.md) | Gets a named feature from the PrintTicket, by name and full namespace URI. |
| [GetFeatureByKeyName method](..\printerextension\nf-printerextension-iprintschemacapabilities-getfeaturebykeyname.md) | Gets a feature from the PrintCapabilities based on a given key name. |
| [GetFeatureByKeyName method](..\printerextension\nf-printerextension-iprintschematicket-getfeaturebykeyname.md) | Gets a feature from the PrintTicket based on the specified key name. |
| [GetFontProperties method](..\filterpipeline\nf-filterpipeline-ipartfont-getfontproperties.md) | The GetFontProperties method gets the font properties. |
| [GetFontRestriction method](..\filterpipeline\nf-filterpipeline-ipartfont2-getfontrestriction.md) | . |
| [GetImageProperties method](..\filterpipeline\nf-filterpipeline-ipartimage-getimageproperties.md) | The GetImageProperties method gets an image property that is based on the content type. |
| [GetInt32 method](..\printerextension\nf-printerextension-iprinterpropertybag-getint32.md) | Reads an integer property. |
| [GetInt32 method](..\printerextension\nf-printerextension-iprinterscriptablepropertybag-getint32.md) | Gets an integer property. |
| [GetNewEmptyPart method](..\filterpipeline\nf-filterpipeline-ixpsdocumentconsumer-getnewemptypart.md) | The GetNewEmptyPart method creates a new XPS part. |
| [GetOption method](..\printerextension\nf-printerextension-iprintschemafeature-getoption.md) | Gets the option with the given name. |
| [GetOptions method](..\printerextension\nf-printerextension-iprintschemacapabilities-getoptions.md) | Gets all the options of a feature. |
| [GetOutputData method](..\bidispl\nf-bidispl-ibidirequest-getoutputdata.md) | The IBidiRequest |
| [GetPagePart method](..\filterpipeline\nf-filterpipeline-ifixedpage-getpagepart.md) | The GetPagePart method gets the images, thumbnails, fonts, and so on in a page by using the URI. |
| [GetParameterDefinition method](..\printerextension\nf-printerextension-iprintschemacapabilities2-getparameterdefinition.md) | The GetParameterDefinition method retrieves the IPrintSchemaParameterDefinition object, and it represents the &lt;psf |
| [GetParameterInitializer method](..\printerextension\nf-printerextension-iprintschematicket2-getparameterinitializer.md) | The GetParameterInitializer method retrieves the IPrintSchemaParameterInitializer object, and it represents the &lt;psf |
| [GetPartCompression method](..\filterpipeline\nf-filterpipeline-ipartbase-getpartcompression.md) | The GetPartCompression method gets the compression of the part. |
| [GetPrintClassObject method](..\filterpipeline\nf-filterpipeline-iprintclassobjectfactory-getprintclassobject.md) | The GetPrintClassObject method creates a print filter-related object for a specified printer by using the IID of the interface object to create. |
| [GetPrintTicket method](..\filterpipeline\nf-filterpipeline-ifixeddocument-getprintticket.md) | The GetPrintTicket method gets the print ticket object for the fixed document. |
| [GetPrintTicket method](..\filterpipeline\nf-filterpipeline-ifixeddocumentsequence-getprintticket.md) | The GetPrintTicket method gets the print ticket object for the fixed document sequence. |
| [GetPrintTicket method](..\filterpipeline\nf-filterpipeline-ifixedpage-getprintticket.md) | The GetPrintTicket method gets the print ticket object for the fixed page. |
| [GetPrinterQueueView method](..\printerextension\nf-printerextension-iprinterqueue2-getprinterqueueview.md) | Retrieves an IPrinterQueueView object, and initializes the object with the range of jobs to be monitored. |
| [GetProperties method](..\printerextension\nf-printerextension-iprinterqueue-getproperties.md) | Gets the properties in the property bag for the queue. |
| [GetProperty method](..\filterpipeline\nf-filterpipeline-iprintpipelinepropertybag-getproperty.md) | The GetProperty method gets a property from a property bag. |
| [GetPropertyValue method](..\printerextension\nf-printerextension-iprintschemaoption-getpropertyvalue.md) | Gets the XML node for the &#0034;value&#0034; child element of a &#0034;Property&#0034; or a &#0034;ScoredProperty&#0034; element with the given name. |
| [GetReadStream method](..\printerextension\nf-printerextension-iprinterpropertybag-getreadstream.md) | Gets a stream in order to read from a stream property. |
| [GetReadStream method](..\printerextension\nf-printerextension-iprinterscriptablepropertybag-getreadstream.md) | Gets a read stream and uses it to read from a property. |
| [GetReadStreamAsXML method](..\printerextension\nf-printerextension-iprinterscriptablepropertybag2-getreadstreamasxml.md) | . |
| [GetRequestCount method](..\bidispl\nf-bidispl-ibidirequestcontainer-getrequestcount.md) | The IBidiRequestContainer |
| [GetResult method](..\bidispl\nf-bidispl-ibidirequest-getresult.md) | The IBidiRequest |
| [GetSelectedOptionInPrintTicket method](..\printerextension\nf-printerextension-iprintschemacapabilities-getselectedoptioninprintticket.md) | Gets the selected option for a feature in IPrintSchemaTicket. |
| [GetStream method](..\filterpipeline\nf-filterpipeline-ipartbase-getstream.md) | The GetStream method gets the stream object that contains the part data. Each part has part-specific data that is associated with it (for example, a font, image, and page markup). |
| [GetStream method](..\filterpipeline\nf-filterpipeline-iprintreadstreamfactory-getstream.md) | The GetStream method gets the stream interface. |
| [GetString method](..\printerextension\nf-printerextension-iprinterpropertybag-getstring.md) | Reads a string property. |
| [GetString method](..\printerextension\nf-printerextension-iprinterscriptablepropertybag-getstring.md) | Gets a string property. |
| [GetThumbnail method](..\filterpipeline\nf-filterpipeline-ixpsdocument-getthumbnail.md) | The GetThumbnail method gets the document thumbnail object. |
| [GetThumbnailProperties method](..\filterpipeline\nf-filterpipeline-ipartthumbnail-getthumbnailproperties.md) | The GetThumbnailProperties method gets the thumbnail properties. |
| [GetUri method](..\filterpipeline\nf-filterpipeline-ifixeddocument-geturi.md) | The GetUri method gets the URI of the fixed document. |
| [GetUri method](..\filterpipeline\nf-filterpipeline-ifixeddocumentsequence-geturi.md) | The GetUri method gets the URI of the fixed document sequence. |
| [GetUri method](..\filterpipeline\nf-filterpipeline-ipartbase-geturi.md) | The GetUri method gets the URI of the part. |
| [GetWriteStream method](..\filterpipeline\nf-filterpipeline-ifixedpage-getwritestream.md) | The GetWriteStream method retrieves the stream object to write page markup to read . You can use this stream to change page markup. |
| [GetWriteStream method](..\printerextension\nf-printerextension-iprinterpropertybag-getwritestream.md) | Gets a stream in order to write a stream property. |
| [GetWriteStream method](..\printerextension\nf-printerextension-iprinterscriptablepropertybag-getwritestream.md) | Gets a stream and uses it to write to a stream property. |
| [GetXpsPart method](..\filterpipeline\nf-filterpipeline-ixpsdocumentprovider-getxpspart.md) | The GetXpsPart method retrieves several objects that make up an XPS document. |
| [GetXpsPartIterator method](..\filterpipeline\nf-filterpipeline-ifixedpage-getxpspartiterator.md) | The GetXpsPartIterator method gets an iterator to enumerate all of the parts that are associated with the page. |
| [InitializeFilter method](..\filterpipeline\nf-filterpipeline-iprintpipelinefilter-initializefilter.md) | The InitializeFilter method initializes a filter. |
| [IsDone method](..\filterpipeline\nf-filterpipeline-ixpspartiterator-isdone.md) | The IsDone method determines whether the iterator has finished the iteration. |
| [MultiSendRecv method](..\bidispl\nf-bidispl-ibidispl-multisendrecv.md) | The IBidiSpl |
| [Next method](..\filterpipeline\nf-filterpipeline-ixpspartiterator-next.md) | The Next method advances the iterator to the next part. |
| [NotifyXmlChanged method](..\printerextension\nf-printerextension-iprintschematicket-notifyxmlchanged.md) | Notifies the print system that the XML DOM object has changed. |
| [OnBidiResponseReceived method](..\printerextension\nf-printerextension-iprinterqueueevent-onbidiresponsereceived.md) | Called when a bidi response is received. |
| [OnChanged method](..\printerextension\nf-printerextension-iprinterqueueviewevent-onchanged.md) | Provides an IPrintJobCollection object that provides a snapshot of a range of print jobs in the queue. |
| [ReadBytes method](..\filterpipeline\nf-filterpipeline-iprintreadstream-readbytes.md) | The ReadBytes method reads a number of bytes into a buffer. |
| [ReportProgress method](..\filterpipeline\nf-filterpipeline-iprintpipelineprogressreport-reportprogress.md) | The ReportProgress method reports the progress of the XPS job consumption to the pipeline manager. |
| [RequestCancel method](..\printerextension\nf-printerextension-iprintjob-requestcancel.md) | Requests the cancellation of a print job. |
| [RequestReader method](..\filterpipeline\nf-filterpipeline-iinterfiltercommunicator-requestreader.md) | The RequestReader method retrieves the reader interface for an IInterFilterCommunicator object. |
| [RequestShutdown method](..\filterpipeline\nf-filterpipeline-iprintpipelinemanagercontrol-requestshutdown.md) | The RequestShutdown method requests that a pipeline be shut down. |
| [RequestWriter method](..\filterpipeline\nf-filterpipeline-iinterfiltercommunicator-requestwriter.md) | The RequestWriter method retrieves the writer interface for an IInterFilterCommunicator object. |
| [Reset method](..\filterpipeline\nf-filterpipeline-ixpspartiterator-reset.md) | The Reset method sets the iterator to the first element. |
| [ResetPDEV method](..\prcomoem\nf-prcomoem-iprintoemengine-resetpdev.md) | . |
| [Seek method](..\filterpipeline\nf-filterpipeline-iprintreadstream-seek.md) | The Seek method changes the seek pointer to a new location in the stream. |
| [Seek method](..\printerextension\nf-printerextension-iprinterscriptablestream-seek.md) | Sets the seek pointer. |
| [SendBidiQuery method](..\printerextension\nf-printerextension-iprinterqueue-sendbidiquery.md) | Performs an asynchronous refresh operation with the specified query, and invokes the IPrinterQueueEvent |
| [SendBidiSetRequestAsync method](..\printerextension\nf-printerextension-iprinterqueue2-sendbidisetrequestasync.md) | Uses an XML string value to send a Bidi Set request as an asynchronous operation. |
| [SendFixedDocument method](..\filterpipeline\nf-filterpipeline-ixpsdocumentconsumer-sendfixeddocument.md) | The SendFixedDocument method sends a fixed document object to the pipeline. |
| [SendFixedDocumentSequence method](..\filterpipeline\nf-filterpipeline-ixpsdocumentconsumer-sendfixeddocumentsequence.md) | The SendFixedDocumentSequence method sends a fixed document sequence to the pipeline. |
| [SendFixedPage method](..\filterpipeline\nf-filterpipeline-ixpsdocumentconsumer-sendfixedpage.md) | The SendFixedPage method sends a fixed page of an XPS document to the pipeline. |
| [SendRecv method](..\bidispl\nf-bidispl-ibidispl-sendrecv.md) | The IBidiSpl |
| [SendRecvXMLStream method](..\bidispl\nf-bidispl-ibidispl2-sendrecvxmlstream.md) | The IBidiSpl2 |
| [SendRecvXMLString method](..\bidispl\nf-bidispl-ibidispl2-sendrecvxmlstring.md) | The IBidiSpl2 |
| [SendXpsDocument method](..\filterpipeline\nf-filterpipeline-ixpsdocumentconsumer-sendxpsdocument.md) | The SendXpsDocument method sends an XPS document to the pipeline. |
| [SendXpsUnknown method](..\filterpipeline\nf-filterpipeline-ixpsdocumentconsumer-sendxpsunknown.md) | The SendXpsUnknown method sends an XPS document part that cannot be identified to the filter pipeline. |
| [SetBool method](..\printerextension\nf-printerextension-iprinterpropertybag-setbool.md) | Writes a specified boolean property value. |
| [SetBool method](..\printerextension\nf-printerextension-iprinterscriptablepropertybag-setbool.md) | Writes a specified boolean property value. |
| [SetBytes method](..\printerextension\nf-printerextension-iprinterpropertybag-setbytes.md) | Writes a byte array property. |
| [SetBytes method](..\printerextension\nf-printerextension-iprinterscriptablepropertybag-setbytes.md) | Writes a byte array property. |
| [SetFontContent method](..\filterpipeline\nf-filterpipeline-ipartfont-setfontcontent.md) | The SetFontContent method sets the content of the font. |
| [SetFontOptions method](..\filterpipeline\nf-filterpipeline-ipartfont-setfontoptions.md) | The SetFontOptions method sets the options for the font. |
| [SetImageContent method](..\filterpipeline\nf-filterpipeline-ipartimage-setimagecontent.md) | The SetImageContent method sets an image property that is based on the content type. |
| [SetInputData method](..\bidispl\nf-bidispl-ibidirequest-setinputdata.md) | The IBidiRequest |
| [SetInt32 method](..\printerextension\nf-printerextension-iprinterpropertybag-setint32.md) | Writes an integer property. |
| [SetInt32 method](..\printerextension\nf-printerextension-iprinterscriptablepropertybag-setint32.md) | Writes an integer property. |
| [SetPagePart method](..\filterpipeline\nf-filterpipeline-ifixedpage-setpagepart.md) | The SetPagePart method associates a new part with the page. |
| [SetPartCompression method](..\filterpipeline\nf-filterpipeline-ipartbase-setpartcompression.md) | The SetPartCompression method sets the compression of the part. |
| [SetPrintTicket method](..\filterpipeline\nf-filterpipeline-ifixeddocument-setprintticket.md) | The SetPrintTicket method inserts a print ticket into the fixed document. |
| [SetPrintTicket method](..\filterpipeline\nf-filterpipeline-ifixeddocumentsequence-setprintticket.md) | The SetPrintTicket method inserts a print ticket into the fixed document sequence. |
| [SetPrintTicket method](..\filterpipeline\nf-filterpipeline-ifixedpage-setprintticket.md) | The SetPrintTicket method associates a print ticket with the page. |
| [SetSchema method](..\bidispl\nf-bidispl-ibidirequest-setschema.md) | The IBidiRequest |
| [SetSize method](..\printerextension\nf-printerextension-iprinterscriptablestream-setsize.md) | Sets the size of the scriptable stream, in bytes. |
| [SetString method](..\printerextension\nf-printerextension-iprinterpropertybag-setstring.md) | Writes a string property. |
| [SetString method](..\printerextension\nf-printerextension-iprinterscriptablepropertybag-setstring.md) | Writes a string property. |
| [SetThumbnail method](..\filterpipeline\nf-filterpipeline-ixpsdocument-setthumbnail.md) | The SetThumbnail method removes the current thumbnail object from the document and inserts a new one. |
| [SetThumbnailContent method](..\filterpipeline\nf-filterpipeline-ipartthumbnail-setthumbnailcontent.md) | The SetThumbnailContent method sets the thumbnail content for the part. |
| [SetViewRange method](..\printerextension\nf-printerextension-iprinterqueueview-setviewrange.md) | Sets the range of print jobs being monitored. |
| [ShutdownOperation method](..\filterpipeline\nf-filterpipeline-iprintpipelinefilter-shutdownoperation.md) | The Pipeline Manager uses the ShutdownOperation method to shut down a filter if the print job is canceled or an error occurs. |
| [Start method](..\printerextension\nf-printerextension-iprintschemaasyncoperation-start.md) | Starts the asynchronous PrintSchema operation. |
| [StartOperation method](..\filterpipeline\nf-filterpipeline-iprintpipelinefilter-startoperation.md) | The StartOperation method starts the operation of a filter. The filter reads, processes, and writes data in this method. |
| [UnbindDevice method](..\bidispl\nf-bidispl-ibidispl-unbinddevice.md) | The IBidiSpl |
| [UnbindDevice method](..\bidispl\nf-bidispl-ibidispl2-unbinddevice.md) | The IBidiSpl2 |
| [ValidateAsync method](..\printerextension\nf-printerextension-iprintschematicket-validateasync.md) | Gets an asynchronous PrintTicket validation operation context. |
| [WriteBytes method](..\filterpipeline\nf-filterpipeline-iprintwritestream-writebytes.md) | The WriteBytes method writes a specified number of bytes to a stream. |
