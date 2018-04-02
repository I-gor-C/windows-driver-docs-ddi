---
UID: NA:prdrvcom
ms.assetid: 6d969209-8a48-364c-a65e-9376eb7fc29c
ms.author: windowsdriverdev
ms.date: 02/27/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# Prdrvcom.h header



This header is used by print, Display. For more information, see
- [print](../_print/index.md)
- [Display](../_display/index.md)

Prdrvcom.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [BindPrinter function](nf-prdrvcom-bindprinter.md) | The IPrintOemPrintTicketProvider |
| [ConvertDevModeToPrintTicket function](nf-prdrvcom-convertdevmodetoprintticket.md) | The IPrintOemPrintTicketProvider |
| [ConvertPrintTicketToDevMode function](nf-prdrvcom-convertprinttickettodevmode.md) | The IPrintTicketProvider |
| [GetPrintCapabilities function](nf-prdrvcom-getprintcapabilities.md) | The IPrintTicketProvider |
| [GetSupportedVersions function](nf-prdrvcom-getsupportedversions.md) | The GetSupportedVersions function queries for the Direct3D interface versions that the driver supports. |
| [QueryDeviceNamespace function](nf-prdrvcom-querydevicenamespace.md) | The IPrintTicketProvider |
| [ValidatePrintTicket function](nf-prdrvcom-validateprintticket.md) | The IPrintOemPrintTicketProvider |

## Enumerations

| Title   | Description   |
| ---- |:----

# prdrvcom.h header



prdrvcom.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [BindPrinter](nf-prdrvcom-bindprinter.md) | The IPrintOemPrintTicketProvider::BindPrinter method enables the core driver to associate a set of private namespace uniform resource identifiers (URIs) with a device. |
| [ConvertDevModeToPrintTicket](nf-prdrvcom-convertdevmodetoprintticket.md) | The IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket method converts a DEVMODEW structure into a print ticket. |
| [ConvertPrintTicketToDevMode](nf-prdrvcom-convertprinttickettodevmode.md) | The IPrintTicketProvider::ConvertPrintTicketToDevMode method converts a print ticket to a DEVMODEW structure. |
| [GetPrintCapabilities](nf-prdrvcom-getprintcapabilities.md) | The IPrintTicketProvider::GetPrintCapabilities method queries the provider for a complete print capabilities document that describes the printer's features and parameters. |
| [GetSupportedVersions](nf-prdrvcom-getsupportedversions.md) | The IPrintTicketProvider::GetSupportedVersions method retrieves major version numbers of the print schemas that are supported by the plug-in provider. |
| [QueryDeviceNamespace](nf-prdrvcom-querydevicenamespace.md) | The IPrintTicketProvider::QueryDeviceNamespace method queries the device for its default namespace uniform resource identifier (URI). |
| [ValidatePrintTicket](nf-prdrvcom-validateprintticket.md) | The IPrintOemPrintTicketProvider::ValidatePrintTicket method validates a print ticket. |




## Enumerations
| Title | Description |
| ---- |:---- |
| [tagSHIMOPTS](ne-prdrvcom-tagshimopts.md) | "." |