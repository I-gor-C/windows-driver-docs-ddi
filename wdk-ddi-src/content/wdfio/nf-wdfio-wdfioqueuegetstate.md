---
UID: NF.wdfio.WdfIoQueueGetState
title: WdfIoQueueGetState function
author: windows-driver-content
description: The WdfIoQueueGetState method returns the status of a specified I/O queue.
old-location: wdf\wdfioqueuegetstate.htm
old-project: wdf
ms.assetid: 83bfddd5-fc4d-4f5c-9904-7564810f5b4c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfIoQueueGetState
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfio.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfIoQueueGetState
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfIoQueueGetState function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]
The <b>WdfIoQueueGetState</b> method returns the status of a specified I/O queue.


## -syntax

````
WDF_IO_QUEUE_STATE WdfIoQueueGetState(
  _In_      WDFQUEUE Queue,
  _Out_opt_ PULONG   QueueRequests,
  _Out_opt_ PULONG   DriverRequests
);
````


## -parameters

### -param Queue [in]

A handle to a framework queue object.

### -param QueueRequests [out, optional]

A pointer to a location that receives the number of I/O requests that are currently in the I/O queue and have not been delivered to the driver. This pointer is optional and can be <b>NULL</b>.

### -param DriverRequests [out, optional]

A pointer to a location that receives the number of I/O requests that have been delivered to the driver but that the driver has not completed or canceled. This pointer is optional and can be <b>NULL</b>.

## -returns
<b>WdfIoQueueGetState</b> returns a <a href="wdf.wdf_io_queue_state">WDF_IO_QUEUE_STATE</a>-typed value, which can contain the bitwise OR of several <b>WDF_IO_QUEUE_STATE</b> enumerators. 

A bug check occurs if the driver supplies an invalid object handle.



## -remarks
After calling <b>WdfIoQueueGetState</b>, your driver can pass the received state value to the following functions, which are defined in <i>Wdfio.h</i>:


<a href="wdf.wdf_io_queue_drained">WDF_IO_QUEUE_DRAINED</a>, which returns <b>TRUE</b> if the queue is drained.


<a href="wdf.wdf_io_queue_idle">WDF_IO_QUEUE_IDLE</a>, which returns <b>TRUE</b> if the queue is idle.


<a href="wdf.wdf_io_queue_purged">WDF_IO_QUEUE_PURGED</a>, which returns <b>TRUE</b> if the queue is purged.


<a href="wdf.wdf_io_queue_ready">WDF_IO_QUEUE_READY</a>, which returns <b>TRUE</b> if the queue is ready.


<a href="wdf.wdf_io_queue_stopped">WDF_IO_QUEUE_STOPPED</a>, which returns <b>TRUE</b> if the queue is stopped.

If your driver uses the framework's <a href="wdf.using_automatic_synchronization">automatic synchronization</a>, the I/O queue's status will not change between the time that the <b>WdfIoQueueGetState</b> method obtains status information from the framework and the time that the method returns. Otherwise the queue's status might change before the <b>WdfIoQueueGetState</b> method returns.

For more information about the <b>WdfIoQueueGetState</b> method, see <a href="wdf.managing_i_o_queues#obtaining_i_o_queue_properties#obtaining_i_o_queue_properties">Obtaining I/O Queue Properties</a>.

The following code example is a routine that returns <b>TRUE</b> if a specified I/O queue is idle.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version
</th>
<td width="70%">
1.0
</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version
</th>
<td width="70%">
2.0
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdfio.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= DISPATCH_LEVEL
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_io_queue_state">WDF_IO_QUEUE_STATE</a>
</dt>
<dt>
<a href="..\wdfio\nc-wdfio-evt_wdf_io_queue_state.md">EvtIoQueueState</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoQueueGetState method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
