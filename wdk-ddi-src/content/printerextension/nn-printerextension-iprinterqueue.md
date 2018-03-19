---
UID: NN:printerextension.IPrinterQueue
title: IPrinterQueue
author: windows-driver-content
description: Represents a single printer queue.
old-location: print\iprinterqueue_interface.htm
old-project: print
ms.assetid: 2DB57234-E783-4C6B-A743-F1E9F7D34D97
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrinterQueue, IPrinterQueue interface [Print Devices], IPrinterQueue interface [Print Devices], described, print.iprinterqueue_interface, printerextension/IPrinterQueue
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
| [IPrinterQueue::get_Handle](nf-printerextension-iprinterqueue-get_handle.md) | Gets the underlying native handle for this print queue. |
| [IPrinterQueue::get_Name](nf-printerextension-iprinterqueue-get_name.md) | Gets the name of the printer for this print queue. |
| [IPrinterQueue::GetProperties](nf-printerextension-iprinterqueue-getproperties.md) | Gets the properties in the property bag for the queue. |
| [IPrinterQueue::SendBidiQuery](nf-printerextension-iprinterqueue-sendbidiquery.md) | Performs an asynchronous refresh operation with the specified query, and invokes the IPrinterQueueEvent::OnBidiResponseReceived method. |

## Remarks
Any event sink that implements <a href="..\printerextension\nn-printerextension-iprinterqueueevent.md">IPrinterQueueEvent</a> is connected to the associated event source, <b>IPrinterQueue</b>, via the <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/ms694318(v=vs.85).aspx">IConnectionPoint</a> mechanism. You must retrieve a pointer to the <b>IConnectionPoint</b> interface by invoking <b>QueryInterface</b> on the <b>IPrinterQueue</b> object.

<div class="alert"><b>Note</b>  It is mandatory to implement <b>IDispatch::Invoke</b> on the event sink that implements <b>IPrinterQueueEvent</b>, since that is the mechanism via which events are raised. It is sufficient to provide stub implementations of the other methods on the <b>IDispatch</b> interface.
</div>
<div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="..\printerextension\nn-printerextension-iprinterqueueevent.md">IPrinterQueueEvent</a>



<a href="http://msdn.microsoft.com/en-us/library/windows/desktop/ms694318(v=vs.85).aspx">IConnectionPoint</a>