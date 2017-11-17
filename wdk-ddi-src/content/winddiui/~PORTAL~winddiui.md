# Declarations in the winddiui header
This header Winddiui contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [ATTRIBUTE_INFO_1 structure](ns-winddiui--attribute-info-1.md) | The ATTRIBUTE_INFO_1 structure is used as a parameter for a printer interface DLL's DrvQueryJobAttributes function. All member values are function-supplied. |
| [PRINTER_EVENT_ATTRIBUTES_INFO structure](ns-winddiui--printer-event-attributes-info.md) | The PRINTER_EVENT_ATTRIBUTES_INFO structure contains the former attributes and the new attributes for a printer. |
| [PRINTPROCESSOR_CAPS_1 structure](ns-winddiui--printprocessor-caps-1.md) | TBD |
| [DRIVER_UPGRADE_INFO_2 structure](ns-winddiui--driver-upgrade-info-2.md) | The DRIVER_UPGRADE_INFO_2 structure is used as an input to a printer interface DLL's DrvUpgradePrinter function. |
| [DOCEVENT_FILTER structure](ns-winddiui--docevent-filter.md) | The DOCEVENT_FILTER structure contains a list of document events to which the printer driver will respond. See DrvDocumentEvent for a complete list of the document events. |
| [ATTRIBUTE_INFO_4 structure](ns-winddiui--attribute-info-4.md) | The ATTRIBUTE_INFO_4 structure is used as a parameter for a printer interface DLL's DrvQueryJobAttributes function. |
| [DEVICEPROPERTYHEADER structure](ns-winddiui--devicepropertyheader.md) | The DEVICEPROPERTYHEADER structure is used as an input parameter to a printer interface DLL's DrvDevicePropertySheets function. |
| [ATTRIBUTE_INFO_2 structure](ns-winddiui--attribute-info-2.md) | The ATTRIBUTE_INFO_2 structure is used as a parameter for a printer interface DLL's DrvQueryJobAttributes function. All member values are function-supplied. |
| [ATTRIBUTE_INFO_3 structure](ns-winddiui--attribute-info-3.md) | The ATTRIBUTE_INFO_3 structure is used as a parameter for a printer interface DLL's DrvQueryJobAttributes function. All member values are function-supplied. |
| [DOCEVENT_CREATEDCPRE structure](ns-winddiui--docevent-createdcpre.md) | The DOCEVENT_CREATEDCPRE structure contains a set of values used in certain calls to DrvDocumentEvent and IPrintOemUI2 |
| [DOCEVENT_ESCAPE structure](ns-winddiui--docevent-escape.md) | The DOCEVENT_ESCAPE structure is a container for values used as parameters for the ExtEscape function. |
| [DEVQUERYPRINT_INFO structure](ns-winddiui--devqueryprint-info.md) | The DEVQUERYPRINT_INFO structure is used as an input parameter to a printer interface DLL's DevQueryPrintEx function. |
| [DOCUMENTPROPERTYHEADER structure](ns-winddiui--documentpropertyheader.md) | The DOCUMENTPROPERTYHEADER structure is used as an input parameter to a printer interface DLL's DrvDocumentPropertySheets function. |
| [DRIVER_UPGRADE_INFO_1 structure](ns-winddiui--driver-upgrade-info-1.md) | The DRIVER_UPGRADE_INFO_1 structure is used as an input to a printer interface DLL's DrvUpgradePrinter function. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [DOCUMENTEVENT_EVENT function](nf-winddiui-documentevent-event.md) | TBD |
| [DevQueryPrintEx function](nf-winddiui-devqueryprintex.md) | A printer interface DLL's DevQueryPrintEx function determines if a specified print job is compatible with the printer's current configuration and can therefore be printed. |
| [DrvDevicePropertySheets function](nf-winddiui-drvdevicepropertysheets.md) | A printer interface DLL's DrvDevicePropertySheets function is responsible for creating property sheet pages that describe a printer's properties. |
| [DrvSplStartDoc function](nf-winddiui-drvsplstartdoc.md) | TBD |
| [DrvDocumentEvent function](nf-winddiui-drvdocumentevent.md) | A printer interface DLL's DrvDocumentEvent function can handle certain events associated with printing a document. |
| [DrvConvertDevMode function](nf-winddiui-drvconvertdevmode.md) | A printer interface DLL's DrvConvertDevMode function converts a printer's DEVMODEW structure from one version to another. |
| [DOCUMENTEVENT_FLAGS function](nf-winddiui-documentevent-flags.md) | TBD |
| [DrvDriverEvent function](nf-winddiui-drvdriverevent.md) | The print spooler calls a printer interface DLL's DrvDriverEvent function when the spooler processes driver-specific events that might require action by the printer driver. |
| [DrvSplWritePrinter function](nf-winddiui-drvsplwriteprinter.md) | TBD |
| [DrvPrinterEvent function](nf-winddiui-drvprinterevent.md) | A printer interface DLL's DrvPrinterEvent function is called by the print spooler when processing printer-specific events that might require action by the printer driver. |
| [DrvDeviceCapabilities function](nf-winddiui-drvdevicecapabilities.md) | A printer interface DLL's DrvDeviceCapabilities function returns requested information about a printer's capabilities. |
| [DrvSplDeviceCaps function](nf-winddiui-drvspldevicecaps.md) | A printer interface DLL's DrvSplDeviceCaps function queries a printer for its capabilities. |
| [DrvSplStartPage function](nf-winddiui-drvsplstartpage.md) | TBD |
| [DrvSplEndDoc function](nf-winddiui-drvsplenddoc.md) | TBD |
| [DrvSplEndPage function](nf-winddiui-drvsplendpage.md) | TBD |
| [DrvUpgradePrinter function](nf-winddiui-drvupgradeprinter.md) | A printer interface DLL's DrvUpgradePrinter function is used for updating a printer's registry settings when a new version of the driver is added to a system. |
| [DrvSplAbort function](nf-winddiui-drvsplabort.md) | TBD |
| [DrvSplClose function](nf-winddiui-drvsplclose.md) | TBD |
| [DrvQueryJobAttributes function](nf-winddiui-drvqueryjobattributes.md) | The DrvQueryJobAttributes function allows a printer interface DLL to specify support for such capabilities as printing multiple document pages on a physical page (&#0034;N-up&#0034; printing), printing multiple copies of each page, collating pages, and printing pages in reverse order. |
| [DrvDocumentPropertySheets function](nf-winddiui-drvdocumentpropertysheets.md) | A printer interface DLL's DrvDocumentPropertySheets function is responsible for creating property sheet pages that describe a print document's properties. |
| [DrvQueryColorProfile function](nf-winddiui-drvquerycolorprofile.md) | The DrvQueryColorProfile function allows a printer interface DLL to specify an ICC profile to use for color management. |

This header is used in these topics:

- [print](..content/_print)
