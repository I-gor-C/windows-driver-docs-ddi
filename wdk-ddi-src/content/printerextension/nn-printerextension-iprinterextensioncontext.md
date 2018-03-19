---
UID: NN:printerextension.IPrinterExtensionContext
title: IPrinterExtensionContext
author: windows-driver-content
description: Represents the context for the activation of a UWP device app for printers.
old-location: print\iprinterextensioncontext_interface.htm
old-project: print
ms.assetid: DD0B5E6F-8E16-48E1-967B-D188535E1320
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrinterExtensionContext, IPrinterExtensionContext interface [Print Devices], IPrinterExtensionContext interface [Print Devices], described, print.iprinterextensioncontext_interface, printerextension/IPrinterExtensionContext
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
-	IPrinterExtensionContext
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrinterExtensionContext interface

Represents the context for the activation of a UWP device app for printers.

## Methods

<p>The <b>IPrinterExtensionContext</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrinterExtensionContext::get_DriverProperties](nf-printerextension-iprinterextensioncontext-get_driverproperties.md) | Gets the driver property bag. |
| [IPrinterExtensionContext::get_PrinterQueue](nf-printerextension-iprinterextensioncontext-get_printerqueue.md) | Gets the queue for the printer. |
| [IPrinterExtensionContext::get_PrintSchemaTicket](nf-printerextension-iprinterextensioncontext-get_printschematicket.md) | Gets the print ticket that is appropriate for the queue and the activation. |
| [IPrinterExtensionContext::get_UserProperties](nf-printerextension-iprinterextensioncontext-get_userproperties.md) | Gets the user property bag for this app. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/5E3DC6C7-E370-4120-81B7-2093812AD009">IPrinterExtensionContextCollection::GetAt</a>



<a href="https://msdn.microsoft.com/947063C6-563A-4BB7-918E-479941B4583F">IPrinterExtensionEvent::OnPrinterQueuesEnumerated</a>



<a href="https://msdn.microsoft.com/4E20303A-BEB3-4928-BA5A-356D978FA2BE">V4 Printer Driver Property Bags</a>



<a href="..\printerextension\nn-printerextension-iprinterextensioncontextcollection.md">IPrinterExtensionContextCollection</a>



<a href="https://msdn.microsoft.com/F2279727-168D-451B-8EDB-8A4A36ACA08F">IPrinterExtensionContextCollection::Count</a>