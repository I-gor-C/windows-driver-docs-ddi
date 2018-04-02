---
UID: NN:printerextension.IPrinterQueueViewEvent
title: IPrinterQueueViewEvent
author: windows-driver-content
description: Provides the signature of the event handler.
old-location: print\iprinterqueueviewevent.htm
old-project: print
ms.assetid: 23951787-C147-43A6-99D6-71AC037F6A43
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrinterQueueViewEvent, IPrinterQueueViewEvent interface [Print Devices], IPrinterQueueViewEvent interface [Print Devices], described, print.iprinterqueueviewevent, printerextension/IPrinterQueueViewEvent
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
-	IPrinterQueueViewEvent
product:
- Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrinterQueueViewEvent interface

Provides the signature of the event handler.

## Methods

<p>The <b>IPrinterQueueViewEvent</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrinterQueueViewEvent::OnChanged](nf-printerextension-iprinterqueueviewevent-onchanged.md) | Provides an IPrintJobCollection object that provides a snapshot of a range of print jobs in the queue. |

## Remarks
<b>IPrinterQueueViewEvent</b> also helps to make it possible to perform job management from a UWP device app or from a printer extension. For more information, see <a href="https://msdn.microsoft.com/D1236DD2-D4AD-4615-9036-7EC75D6CADCE">Job Management</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/D1236DD2-D4AD-4615-9036-7EC75D6CADCE">Job Management</a>