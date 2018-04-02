---
UID: NN:printerextension.IPrintSchemaTicket2
title: IPrintSchemaTicket2
author: windows-driver-content
description: The IPrintSchemaTicket2 interface is an extension to the IPrintSchemaTicket interface, which provides wrapper methods over a print ticket document.
old-location: print\iprintschematicket2.htm
old-project: print
ms.assetid: 52D9FA01-578B-43C2-A0B1-F3CD0BAAFAE4
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintSchemaTicket2, IPrintSchemaTicket2 interface [Print Devices], IPrintSchemaTicket2 interface [Print Devices], described, print.iprintschematicket2, printerextension/IPrintSchemaTicket2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: printerextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
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
-	IPrintSchemaTicket2
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrintSchemaTicket2 interface

The  <b>IPrintSchemaTicket2</b> interface is an extension to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451398">IPrintSchemaTicket</a> interface, which provides wrapper methods over a print ticket document.

## Methods

<p>The <b>IPrintSchemaTicket2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintSchemaTicket2::GetParameterInitializer](nf-printerextension-iprintschematicket2-getparameterinitializer.md) | The GetParameterInitializer method retrieves the IPrintSchemaParameterInitializer object, and it represents the &lt;psf:ParameterInit&gt; element in the PrintTicket XML. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451398">IPrintSchemaTicket</a>