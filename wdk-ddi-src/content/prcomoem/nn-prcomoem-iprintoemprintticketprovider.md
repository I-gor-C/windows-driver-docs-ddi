---
UID: NN:prcomoem.IPrintOemPrintTicketProvider
title: IPrintOemPrintTicketProvider
author: windows-driver-content
description: This section describes the methods that are defined for the IPrintOemPrintTicketProvider COM interface.
old-location: print\iprintoemprintticketprovider_interface.htm
old-project: print
ms.assetid: a32b5ec9-b4f2-4f33-879d-252806bd34ed
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintOemPrintTicketProvider, IPrintOemPrintTicketProvider interface [Print Devices], IPrintOemPrintTicketProvider interface [Print Devices], described, prcomoem/IPrintOemPrintTicketProvider, print.iprintoemprintticketprovider_interface, print_ticket-package_73ff5919-5d89-4fe1-b10f-03f2b14b716f.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: prcomoem.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	prcomoem.h
api_name:
-	IPrintOemPrintTicketProvider
product: Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintOemPrintTicketProvider interface

This section describes the methods that are defined for the <b>IPrintOemPrintTicketProvider</b> COM interface.

## Methods

<p>The <b>IPrintOemPrintTicketProvider</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintOemPrintTicketProvider::BindPrinter](nf-prcomoem-iprintoemprintticketprovider-bindprinter.md) | The IPrintOemPrintTicketProvider::BindPrinter method enables the core driver to associate a set of private namespace uniform resource identifiers (URIs) with a device. |
| [IPrintOemPrintTicketProvider::CompletePrintCapabilities](nf-prcomoem-iprintoemprintticketprovider-completeprintcapabilities.md) | The IPrintOemPrintTicketProvider::CompletePrintCapabilities method fills in the remaining entries of the specified print capabilities document. |
| [IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket](nf-prcomoem-iprintoemprintticketprovider-convertdevmodetoprintticket.md) | The IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket method converts a DEVMODEW structure into a print ticket. |
| [IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode](nf-prcomoem-iprintoemprintticketprovider-convertprinttickettodevmode.md) | The IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode method converts a print ticket to a DEVMODEW structure. |
| [IPrintOemPrintTicketProvider::ExpandIntentOptions](nf-prcomoem-iprintoemprintticketprovider-expandintentoptions.md) | The IPrintOemPrintTicketProvider::ExpandIntentOptions method enables the plug-in to expand printer options (such as photo printing) into individual feature settings in the print ticket. |
| [IPrintOemPrintTicketProvider::GetSupportedVersions](nf-prcomoem-iprintoemprintticketprovider-getsupportedversions.md) | The IPrintOemPrintTicketProvider::GetSupportedVersions method retrieves major versions of the print schemas that are supported by the plug-in provider. |
| [IPrintOemPrintTicketProvider::PublishPrintTicketHelperInterface](nf-prcomoem-iprintoemprintticketprovider-publishprinttickethelperinterface.md) | The IPrintOemPrintTicketProvider::PublishPrintTicketHelperInterface method publishes the print ticket helper interface for either Unidrv or Pscript5 user interface (UI) plug-ins. |
| [IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace](nf-prcomoem-iprintoemprintticketprovider-querydevicedefaultnamespace.md) | The IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace method queries the device for its default namespace uniform resource identifier (URI). |
| [IPrintOemPrintTicketProvider::ValidatePrintTicket](nf-prcomoem-iprintoemprintticketprovider-validateprintticket.md) | The IPrintOemPrintTicketProvider::ValidatePrintTicket method validates a print ticket. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |