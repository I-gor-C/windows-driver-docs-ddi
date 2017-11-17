---
UID: NE.wdfio._WDF_IO_QUEUE_DISPATCH_TYPE
title: WDF_IO_QUEUE_DISPATCH_TYPE
author: windows-driver-content
description: The WDF_IO_QUEUE_DISPATCH_TYPE enumeration type identifies the request dispatching methods that can be associated with a framework queue object.
old-location: wdf\wdf_io_queue_dispatch_type.htm
ms.assetid: 90f2f490-ee29-4e20-94b2-65a9bba3e831
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfio.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_IO_QUEUE_DISPATCH_TYPE
req.alt-loc: wdfio.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL (see Remarks section)
ms.keywords: WDF_INTERRUPT_INFO, WDF_INTERRUPT_INFO, *PWDF_INTERRUPT_INFO
req.iface: 
req.product: Windows 10 or later.
---

# WDF_IO_QUEUE_DISPATCH_TYPE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_IO_QUEUE_DISPATCH_TYPE</b> enumeration type identifies the request dispatching methods that can be associated with a framework queue object. </p>


## -syntax

````
typedef enum _WDF_IO_QUEUE_DISPATCH_TYPE { 
  WdfIoQueueDispatchInvalid     = 0,
  WdfIoQueueDispatchSequential  = 1,
  WdfIoQueueDispatchParallel    = 2,
  WdfIoQueueDispatchManual      = 3,
  WdfIoQueueDispatchMax         = 4
} WDF_IO_QUEUE_DISPATCH_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WdfIoQueueDispatchInvalid"></a><a id="wdfioqueuedispatchinvalid"></a><a id="WDFIOQUEUEDISPATCHINVALID"></a><b>WdfIoQueueDispatchInvalid</b>

<dd>
<p>Reserved for internal use.</p>
</dd>

### -field <a id="WdfIoQueueDispatchSequential"></a><a id="wdfioqueuedispatchsequential"></a><a id="WDFIOQUEUEDISPATCHSEQUENTIAL"></a><b>WdfIoQueueDispatchSequential</b>

<dd>
<p>The I/O queue's requests are presented to the driver's <a href="wdf.request_handlers">request handlers</a> one at a time. The framework does not deliver the next request until a driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a> to complete the current request.</p>
</dd>

### -field <a id="WdfIoQueueDispatchParallel"></a><a id="wdfioqueuedispatchparallel"></a><a id="WDFIOQUEUEDISPATCHPARALLEL"></a><b>WdfIoQueueDispatchParallel</b>

<dd>
<p>The framework presents requests to the driver's request handlers as soon as the requests are available. </p>
</dd>

### -field <a id="WdfIoQueueDispatchManual"></a><a id="wdfioqueuedispatchmanual"></a><a id="WDFIOQUEUEDISPATCHMANUAL"></a><b>WdfIoQueueDispatchManual</b>

<dd>
<p>The framework places requests into the queue but does not deliver them to the driver. The driver must retrieve requests from the queue by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh975100">WdfIoQueueRetrieveNextRequest</a>.</p>
</dd>

### -field <a id="WdfIoQueueDispatchMax"></a><a id="wdfioqueuedispatchmax"></a><a id="WDFIOQUEUEDISPATCHMAX"></a><b>WdfIoQueueDispatchMax</b>

<dd>
<p>Reserved for internal use only.</p>
</dd>
</dl>

## -remarks
<p>For more information, see <a href="wdf.dispatching_methods_for_i_o_requests">Dispatching Methods for I/O Requests</a>.</p>

<p>For more information, see <a href="wdf.dispatching_methods_for_i_o_requests">Dispatching Methods for I/O Requests</a>.</p>

<p>For more information, see <a href="wdf.dispatching_methods_for_i_o_requests">Dispatching Methods for I/O Requests</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfio.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>