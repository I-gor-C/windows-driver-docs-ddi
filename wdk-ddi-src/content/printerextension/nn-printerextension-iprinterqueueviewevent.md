---
UID: NN:printerextension.IPrinterQueueViewEvent
title: IPrinterQueueViewEvent
author: windows-driver-content
description: Provides the signature of the event handler.
old-location: print\iprinterqueueviewevent.htm
old-project: print
ms.assetid: 23951787-C147-43A6-99D6-71AC037F6A43
ms.author: windowsdriverdev
ms.date: 2/2/2018
ms.keywords: print.iprinterqueueviewevent, IPrinterQueueViewEvent interface [Print Devices], IPrinterQueueViewEvent interface [Print Devices], described, IPrinterQueueViewEvent, printerextension/IPrinterQueueViewEvent
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
req.lib: printerextension.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	Printerextension.h
apiname:
-	IPrinterQueueViewEvent
product: Windows
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
| [printerextension.IPrinterQueueViewEvent.OnChanged](nf-printerextension-iprinterqueueviewevent-onchanged.md) | Provides an IPrintJobCollection object that provides a snapshot of a range of print jobs in the queue. |

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



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterQueueViewEvent interface%20 RELEASE:%20(2/2/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>