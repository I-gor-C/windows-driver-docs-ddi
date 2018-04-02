---
UID: NN:printerextension.IPrinterExtensionEventArgs
title: IPrinterExtensionEventArgs
author: windows-driver-content
description: Represents the context for the desktop printer extension activation.
old-location: print\iprinterextensioneventargs.htm
old-project: print
ms.assetid: 77850B5A-4E24-4057-B87F-D964620ABF94
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrinterExtensionEventArgs, IPrinterExtensionEventArgs interface [Print Devices], IPrinterExtensionEventArgs interface [Print Devices], described, print.iprinterextensioneventargs, printerextension/IPrinterExtensionEventArgs
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: printerextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	Printerextension.h
api_name:
-	IPrinterExtensionEventArgs
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrinterExtensionEventArgs interface

Represents the context for the desktop printer extension activation.

## Methods

<p>The <b>IPrinterExtensionEventArgs</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrinterExtensionEventArgs::get_BidiNotification](nf-printerextension-iprinterextensioneventargs-get_bidinotification.md) | Gets the text of the bidirectional communication (Bidi) notification, if applicable. |
| [IPrinterExtensionEventArgs::get_DetailedReasonId](nf-printerextension-iprinterextensioneventargs-get_detailedreasonid.md) | Gets a more detailed activation reason than what can be retrieved from ReasonId. |
| [IPrinterExtensionEventArgs::get_ReasonId](nf-printerextension-iprinterextensioneventargs-get_reasonid.md) | Gets the reason why the printer extension was activated. |
| [IPrinterExtensionEventArgs::get_Request](nf-printerextension-iprinterextensioneventargs-get_request.md) | Gets the IPrinterExtensionRequest object for the current event. |
| [IPrinterExtensionEventArgs::get_SourceApplication](nf-printerextension-iprinterextensioneventargs-get_sourceapplication.md) | Gets the name of the application that invoked the printer extension. |
| [IPrinterExtensionEventArgs::get_WindowModal](nf-printerextension-iprinterextensioneventargs-get_windowmodal.md) | Gets the run mode parameter that determines whether or not the printer extension should be run as modal. |
| [IPrinterExtensionEventArgs::get_WindowParent](nf-printerextension-iprinterextensioneventargs-get_windowparent.md) | Gets the handle of the parent window. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh406649">IPrinterExtensionContext</a>



<a href="https://msdn.microsoft.com/4E20303A-BEB3-4928-BA5A-356D978FA2BE">V4 Printer Driver Property Bags</a>