---
UID: NF.wdfio.WdfIoQueueRetrieveRequestByFileObject
title: WdfIoQueueRetrieveRequestByFileObject
author: windows-driver-content
description: The WdfIoQueueRetrieveRequestByFileObject method retrieves the next available I/O request, from a specified I/O queue, that is associated with a specified file object.
old-location: wdf\wdfioqueueretrieverequestbyfileobject.htm
old-project: wdf
ms.assetid: 6acff4d8-c21f-49c5-a255-5b46aac97c9f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfIoQueueRetrieveRequestByFileObject
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
req.alt-api: WdfIoQueueRetrieveRequestByFileObject
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DoubleCompletion, DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfIoQueueRetrieveRequestByFileObject function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfIoQueueRetrieveRequestByFileObject</b> method retrieves the next available I/O request, from a specified I/O queue, that is associated with a specified file object. </p>


## -syntax

````
NTSTATUS WdfIoQueueRetrieveRequestByFileObject(
  _In_  WDFQUEUE      Queue,
  _In_  WDFFILEOBJECT FileObject,
  _Out_ WDFREQUEST    *OutRequest
);
````


## -parameters
<dl>

### -param <i>Queue</i> [in]

<dd>
<p>A handle to a framework queue object.</p>
</dd>

### -param <i>FileObject</i> [in]

<dd>
<p>A handle to a framework file object.</p>
</dd>

### -param <i>OutRequest</i> [out]

<dd>
<p>A pointer to a location that receives a handle to a framework request object. If <b>WdfIoQueueRetrieveRequestByFileObject</b> does not return STATUS_SUCCESS, it does not set the location's value. </p>
</dd>
</dl>

## -returns
<p><b>WdfIoQueueRetrieveRequestByFileObject</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The driver supplied an invalid handle.</p><dl>
<dt><b>STATUS_NO_MORE_ENTRIES</b></dt>
</dl><p>The framework reached the end of the I/O queue.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_STATE</b></dt>
</dl><p>The specified I/O queue is configured for the parallel dispatching method.</p><dl>
<dt><b>STATUS_WDF_PAUSED</b></dt>
</dl><p>The specified I/O queue is <a href="wdf.using_power_managed_i_o_queues">power-managed</a> and its device is in a low-power state.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>A driver that has configured an I/O queue for manual or sequential dispatching might call <b>WdfIoQueueRetrieveRequestByFileObject</b>. For more information about using <b>WdfIoQueueRetrieveRequestByFileObject</b> with the manual or sequential dispatching methods, see <a href="wdf.dispatching_methods_for_i_o_requests">Dispatching Methods for I/O Requests</a>. </p>

<p>After calling <b>WdfIoQueueRetrieveRequestByFileObject</b> to obtain an I/O request, the driver <a href="wdf.request_ownership">owns</a> the request and must <a href="wdf.accessing_data_buffers_in_kmdf_drivers">process the I/O request</a> in some manner.</p>

<p>For more information about the <b>WdfIoQueueRetrieveRequestByFileObject</b> method, see <a href="wdf.managing_i_o_queues">Managing I/O Queues</a>.</p>

<p>The following code example obtains, from a specified I/O queue, a handle to the next framework request object that is associated with a specified framework file object.</p>

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
<dt>Wdfio.h (include Wdf.h)</dt>
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
<a href="devtest.kmdf_doublecompletion">DoubleCompletion</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfio\nf-wdfio-wdfioqueueretrievefoundrequest.md">WdfIoQueueRetrieveFoundRequest</a>
</dt>
<dt>
<a href="..\wdfio\nf-wdfio-wdfioqueueretrievenextrequest.md">WdfIoQueueRetrieveNextRequest</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoQueueRetrieveRequestByFileObject method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
