---
UID : NN:printerextension.IPrinterQueueEvent
title : IPrinterQueueEvent
author : windows-driver-content
description : Provides the event delegate for printer queue events.
old-location : print\iprinterqueueevent_interface.htm
old-project : print
ms.assetid : AA4B2578-61C9-47C3-A114-4B873B475124
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : print.iprinterqueueevent_interface, IPrinterQueueEvent interface [Print Devices], IPrinterQueueEvent interface [Print Devices], described, IPrinterQueueEvent, printerextension/IPrinterQueueEvent
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : printerextension.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : printerextension.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : PrintSchemaSelectionType
req.product : Windows 10 or later.
---

# IPrinterQueueEvent interface

Provides the event delegate for printer queue events.

## Methods

<p>The <b>IPrinterQueueEvent</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [printerextension.IPrinterQueueEvent.OnBidiResponseReceived](nf-printerextension-iprinterqueueevent-onbidiresponsereceived.md) | Called when a bidi response is received. |

## Remarks

An event sink that implements <b>IPrinterQueueEvent</b> and the event source, <a href="..\printerextension\nn-printerextension-iprinterqueue.md">IPrinterQueue</a> are connected via the <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/ms694318(v=vs.85).aspx">IConnectionPoint</a> mechanism. You must retrieve a pointer to the <b>IConnectionPoint</b> interface by invoking <b>QueryInterface</b> on the <b>IPrinterQueue</b> object.
<div class="alert"><b>Note</b>  It is mandatory to implement <b>IDispatch::Invoke</b> on the event sink that implements <b>IPrinterQueueEvent</b>, since that is the mechanism via which events are raised. It is sufficient to provide stub implementations of the other methods on the <b>IDispatch</b> interface.
</div><div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | printerextension.h |
| **DLL** |  |

## See Also

<a href="..\printerextension\nn-printerextension-iprinterqueue.md">IPrinterQueue</a>

<a href="http://msdn.microsoft.com/en-us/library/windows/desktop/ms694318(v=vs.85).aspx">IConnectionPoint</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterQueueEvent interface%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>