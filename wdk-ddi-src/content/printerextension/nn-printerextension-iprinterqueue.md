---
UID: NN:printerextension.IPrinterQueue
title: IPrinterQueue
author: windows-driver-content
description: Represents a single printer queue.
old-location: print\iprinterqueue_interface.htm
old-project: print
ms.assetid: 2DB57234-E783-4C6B-A743-F1E9F7D34D97
ms.author: windowsdriverdev
ms.date: 2/2/2018
ms.keywords: print.iprinterqueue_interface, IPrinterQueue interface [Print Devices], IPrinterQueue interface [Print Devices], described, IPrinterQueue, printerextension/IPrinterQueue
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
-	IPrinterQueue
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrinterQueue interface

Represents a single printer queue.

## Methods

<p>The <b>IPrinterQueue</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [printerextension.IPrinterQueue.GetProperties](nf-printerextension-iprinterqueue-getproperties.md) | Gets the properties in the property bag for the queue. |
| [printerextension.IPrinterQueue.SendBidiQuery](nf-printerextension-iprinterqueue-sendbidiquery.md) | Performs an asynchronous refresh operation with the specified query, and invokes the IPrinterQueueEvent::OnBidiResponseReceived method. |

## Remarks

Any event sink that implements <a href="..\printerextension\nn-printerextension-iprinterqueueevent.md">IPrinterQueueEvent</a> is connected to the associated event source, <b>IPrinterQueue</b>, via the <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/ms694318(v=vs.85).aspx">IConnectionPoint</a> mechanism. You must retrieve a pointer to the <b>IConnectionPoint</b> interface by invoking <b>QueryInterface</b> on the <b>IPrinterQueue</b> object.
<div class="alert"><b>Note</b>  It is mandatory to implement <b>IDispatch::Invoke</b> on the event sink that implements <b>IPrinterQueueEvent</b>, since that is the mechanism via which events are raised. It is sufficient to provide stub implementations of the other methods on the <b>IDispatch</b> interface.
</div><div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="..\printerextension\nn-printerextension-iprinterqueueevent.md">IPrinterQueueEvent</a>

<a href="http://msdn.microsoft.com/en-us/library/windows/desktop/ms694318(v=vs.85).aspx">IConnectionPoint</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterQueue interface%20 RELEASE:%20(2/2/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>