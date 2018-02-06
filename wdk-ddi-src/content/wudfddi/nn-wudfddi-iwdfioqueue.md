---
UID: NN:wudfddi.IWDFIoQueue
title: IWDFIoQueue
author: windows-driver-content
description: The IWDFIoQueue interface exposes an I/O queue object.
old-location: wdf\iwdfioqueue.htm
old-project: wdf
ms.assetid: 9a3ec86a-6a1d-4c65-a65a-7cb85bbd1ab8
ms.author: windowsdriverdev
ms.date: 1/11/2018
ms.keywords: wdf.iwdfioqueue, IWDFIoQueue interface, IWDFIoQueue interface, described, IWDFIoQueue, wudfddi/IWDFIoQueue, UMDFQueueObjectRef_57878b3d-0771-425d-b8ca-3e4713c96fcc.xml, umdf.iwdfioqueue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: wudfddi.h
req.dll: WUDFx.dll
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	WUDFx.dll
apiname:
-	IWDFIoQueue
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFIoQueue interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFIoQueue</b> interface exposes an I/O queue object.

## Methods

<p>The <b>IWDFIoQueue</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IWDFIoQueue.ConfigureRequestDispatching](nf-wudfddi-iwdfioqueue-configurerequestdispatching.md) | The ConfigureRequestDispatching method configures the queuing of I/O requests of the given type. |
| [wudfddi.IWDFIoQueue.Drain](nf-wudfddi-iwdfioqueue-drain.md) | The Drain method directs the queue to reject new incoming I/O requests and allow already-queued requests to be delivered to the driver for processing. |
| [wudfddi.IWDFIoQueue.DrainSynchronously](nf-wudfddi-iwdfioqueue-drainsynchronously.md) | The DrainSynchronously method directs the queue to reject new incoming I/O requests and allows already-queued requests to be delivered to the driver for processing. This method returns after all requests are completed or canceled. |
| [wudfddi.IWDFIoQueue.GetDevice](nf-wudfddi-iwdfioqueue-getdevice.md) | The GetDevice method retrieves the interface to the device that owns the I/O queue. |
| [wudfddi.IWDFIoQueue.GetState](nf-wudfddi-iwdfioqueue-getstate.md) | The GetState method retrieves the state of an I/O queue. |
| [wudfddi.IWDFIoQueue.Purge](nf-wudfddi-iwdfioqueue-purge.md) | The Purge method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. |
| [wudfddi.IWDFIoQueue.PurgeSynchronously](nf-wudfddi-iwdfioqueue-purgesynchronously.md) | The PurgeSynchronously method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. The method returns after all outstanding requests are canceled. |
| [wudfddi.IWDFIoQueue.RetrieveNextRequest](nf-wudfddi-iwdfioqueue-retrievenextrequest.md) | The RetrieveNextRequest method retrieves the next I/O request from an I/O queue. |
| [wudfddi.IWDFIoQueue.RetrieveNextRequestByFileObject](nf-wudfddi-iwdfioqueue-retrievenextrequestbyfileobject.md) | The RetrieveNextRequestByFileObject method retrieves from an I/O queue the next I/O request whose file object matches the specified file object. |
| [wudfddi.IWDFIoQueue.Start](nf-wudfddi-iwdfioqueue-start.md) | The Start method enables an I/O queue to start receiving new I/O requests and delivering them to a driver. |
| [wudfddi.IWDFIoQueue.Stop](nf-wudfddi-iwdfioqueue-stop.md) | The Stop method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests. |
| [wudfddi.IWDFIoQueue.StopSynchronously](nf-wudfddi-iwdfioqueue-stopsynchronously.md) | The StopSynchronously method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests. The method returns after all delivered requests have been canceled or completed. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h |