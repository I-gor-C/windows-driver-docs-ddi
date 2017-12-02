---
UID: NF.wdfio.WdfIoQueueFindRequest
title: WdfIoQueueFindRequest
author: windows-driver-content
description: The WdfIoQueueFindRequest method locates the next request in an I/O queue, or the next request that matches specified criteria, but does not grant ownership of the request to the driver.
old-location: wdf\wdfioqueuefindrequest.htm
old-project: wdf
ms.assetid: 379fc7ec-577a-48a4-83b0-4be4e8cfe1bf
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfIoQueueFindRequest
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
req.alt-api: WdfIoQueueFindRequest
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2, wdfioqueuefindrequestfailed, wdfioqueueretrievefoundrequest, wdfioqueueretrievenextrequest
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

# WdfIoQueueFindRequest function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfIoQueueFindRequest</b> method locates the next request in an I/O queue, or the next request that matches specified criteria, but does not grant <a href="wdf.request_ownership">ownership</a> of the request to the driver.</p>


## -syntax

````
NTSTATUS WdfIoQueueFindRequest(
  _In_     WDFQUEUE                Queue,
  _In_opt_ WDFREQUEST              FoundRequest,
  _In_opt_ WDFFILEOBJECT           FileObject,
  _Inout_  PWDF_REQUEST_PARAMETERS Parameters,
  _Out_    WDFREQUEST              *OutRequest
);
````


## -parameters
<dl>

### -param Queue [in]

<dd>
<p>A handle to a framework queue object.</p>
</dd>

### -param FoundRequest [in, optional]

<dd>
<p>A request object handle that the driver received from a previous call to <b>WdfIoQueueFindRequest</b>. This parameter is optional and can be <b>NULL</b>.</p>
</dd>

### -param FileObject [in, optional]

<dd>
<p>A handle to a framework file object. This parameter is optional and can be <b>NULL</b>.</p>
</dd>

### -param Parameters [in, out]

<dd>
<p>A pointer to a driver-allocated <a href="..\wdfrequest\ns-wdfrequest--wdf-request-parameters.md">WDF_REQUEST_PARAMETERS</a> structure that receives parameters that are associated with the found request. This parameter is optional and can be <b>NULL</b>.</p>
</dd>

### -param OutRequest [out]

<dd>
<p>A pointer to a location that receives a handle to the found request. If no match is found, the location receives <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>WdfIoQueueFindRequest</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The driver supplies an invalid handle.</p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>The request that is identified by the <i>FoundRequest</i> parameter cannot be found in the I/O queue.</p><dl>
<dt><b>STATUS_NO_MORE_ENTRIES</b></dt>
</dl><p>The framework reached the end of the I/O queue without finding a request that matches the search criteria.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>The <b>WdfIoQueueFindRequest</b> method searches a specified I/O queue and attempts to find an I/O request. </p>

<p>Your driver can call <b>WdfIoQueueFindRequest</b> only if the driver is using the manual <a href="wdf.dispatching_methods_for_i_o_requests">dispatching method</a> for the specified I/O queue.</p>

<p>If <i>FileObject</i> is not <b>NULL</b>, <b>WdfIoQueueFindRequest</b> only examines requests that are associated with the specified file object handle.</p>

<p>If <i>FoundRequest</i> is <b>NULL</b>, this method locates the first request in the I/O queue that matches the <i>FileObject</i> value. If <i>FoundRequest</i> is not <b>NULL</b>, the method begins searching at the request that is identified by <i>FoundRequest</i>. To create an iterative loop, specify <b>NULL</b> for the first call, and then use the returned handle as the <i>FoundRequest</i> parameter for subsequent calls.</p>

<p>If <i>Parameters</i> is not <b>NULL</b>, this method copies the found request's parameters into the driver-supplied structure.</p>

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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_wdfioqueuefindrequestfailed">wdfioqueuefindrequestfailed</a>, <a href="..\wdfio\nf-wdfio-wdfioqueueretrievefoundrequest.md">wdfioqueueretrievefoundrequest</a>, <a href="..\wdfio\nf-wdfio-wdfioqueueretrievenextrequest.md">wdfioqueueretrievenextrequest</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfio\nf-wdfio-wdfioqueueretrievefoundrequest.md">WdfIoQueueRetrieveFoundRequest</a>
</dt>
<dt>
<a href="..\wdfio\nf-wdfio-wdfioqueuestop.md">WdfIoQueueStop</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548739">WdfObjectDereference</a>
</dt>
<dt>
<a href="..\wdfrequest\ns-wdfrequest--wdf-request-parameters.md">WDF_REQUEST_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoQueueFindRequest method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
