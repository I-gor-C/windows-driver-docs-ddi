---
UID: NF.wdfdevice.WdfDeviceConfigureRequestDispatching
title: WdfDeviceConfigureRequestDispatching
author: windows-driver-content
description: The WdfDeviceConfigureRequestDispatching method causes the framework to queue a specified type of I/O requests to a specified I/O queue.
old-location: wdf\wdfdeviceconfigurerequestdispatching.htm
old-project: wdf
ms.assetid: aba4cccd-267d-48cc-a6ff-be19802adfdc
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfDeviceConfigureRequestDispatching
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfDeviceConfigureRequestDispatching
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceConfigureRequestDispatching function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfDeviceConfigureRequestDispatching</b> method causes the framework to queue a specified type of I/O requests to a specified I/O queue.</p>


## -syntax

````
NTSTATUS WdfDeviceConfigureRequestDispatching(
  _In_ WDFDEVICE        Device,
  _In_ WDFQUEUE         Queue,
  _In_ WDF_REQUEST_TYPE RequestType
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>Supplies a handle to a framework device object.</p>
</dd>

### -param <i>Queue</i> [in]

<dd>
<p>Supplies a handle to a framework queue object.</p>
</dd>

### -param <i>RequestType</i> [in]

<dd>
<p>Supplies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552503">WDF_REQUEST_TYPE</a>-typed enumerator that identifies the type of request to be queued. The only valid enumerators are: </p>
<dl>
<dd>
<p><b>WdfRequestTypeCreate</b></p>
</dd>
<dd>
<p><b>WdfRequestTypeRead</b></p>
</dd>
<dd>
<p><b>WdfRequestTypeWrite</b></p>
</dd>
<dd>
<p><b>WdfRequestTypeDeviceControl</b></p>
</dd>
<dd>
<p><b>WdfRequestTypeDeviceControlInternal</b></p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An input parameter is invalid.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The amount of available memory is too low.
</p><dl>
<dt><b>STATUS_WDF_BUSY</b></dt>
</dl><p>The driver has already assigned a queue to the specified request type.</p>

<p> </p>

<p>The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>Each call to <b>WdfDeviceConfigureRequestDispatching</b> specifies one request type. If you want a single I/O queue to receive multiple types of requests (for example, read and write requests), your driver can call <b>WdfDeviceConfigureRequestDispatching</b> multiple times for a single I/O queue.</p>

<p>For more information about <b>WdfDeviceConfigureRequestDispatching</b>, see <a href="wdf.creating_i_o_queues">Creating I/O Queues</a> and <a href="wdf.managing_i_o_queues">Managing I/O Queues</a>.</p>

<p>The following code example initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552359">WDF_IO_QUEUE_CONFIG</a> structure, creates an I/O queue, and then configures the queue so that it receives write requests.</p>

<p>Each call to <b>WdfDeviceConfigureRequestDispatching</b> specifies one request type. If you want a single I/O queue to receive multiple types of requests (for example, read and write requests), your driver can call <b>WdfDeviceConfigureRequestDispatching</b> multiple times for a single I/O queue.</p>

<p>For more information about <b>WdfDeviceConfigureRequestDispatching</b>, see <a href="wdf.creating_i_o_queues">Creating I/O Queues</a> and <a href="wdf.managing_i_o_queues">Managing I/O Queues</a>.</p>

<p>The following code example initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552359">WDF_IO_QUEUE_CONFIG</a> structure, creates an I/O queue, and then configures the queue so that it receives write requests.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
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
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552360">WDF_IO_QUEUE_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547401">WdfIoQueueCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceConfigureRequestDispatching method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
