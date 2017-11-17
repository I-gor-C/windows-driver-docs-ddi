---
UID: NF.wdfrequest.WdfRequestReuse
title: WdfRequestReuse
author: windows-driver-content
description: The WdfRequestReuse method reinitializes a framework request object so that it can be reused.
old-location: wdf\wdfrequestreuse.htm
ms.assetid: 3d649cc5-6512-432c-9bd9-60e18507a873
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfRequestReuse
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, InvalidReqAccess, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2, ReqSendFail
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: WdfRequestReuse
req.iface: 
req.product: Windows 10 or later.
---

# WdfRequestReuse function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfRequestReuse</b> method reinitializes a framework request object so that it can be reused.</p>


## -syntax

````
NTSTATUS WdfRequestReuse(
  _In_ WDFREQUEST                Request,
  _In_ PWDF_REQUEST_REUSE_PARAMS ReuseParams
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>A handle to a framework request object.</p>
</dd>

### -param <i>ReuseParams</i> [in]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552480">WDF_REQUEST_REUSE_PARAMS</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>WdfRequestReuse</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An input parameter is invalid.</p><dl>
<dt><b>STATUS_WDF_REQUEST_INVALID_STATE</b></dt>
</dl><p>The driver supplied an IRP in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552480">WDF_REQUEST_REUSE_PARAMS</a> structure, but the specified request object was not obtained from <a href="https://msdn.microsoft.com/library/windows/hardware/ff549953">WdfRequestCreateFromIrp</a>.</p>

<p> </p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>A framework-based driver can reuse framework request objects that it created by previous calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549951">WdfRequestCreate</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549953">WdfRequestCreateFromIrp</a>. Drivers can also reuse request objects that they have <a href="wdf.receiving_i_o_requests">received from the framework</a>, but they cannot set the <a href="wdf.WDF_REQUEST_REUSE_FLAGS">WDF_REQUEST_REUSE_SET_NEW_IRP</a> flag for those request objects.</p>

<p>A driver can reuse a request object after the original request has been completed. After a driver has called <b>WdfRequestReuse</b>, the request's contents must be reinitialized. The driver can specify some request parameters in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552480">WDF_REQUEST_REUSE_PARAMS</a> structure. </p>

<p>If you want the reused request to have a <a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a> callback function, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550030">WdfRequestSetCompletionRoutine</a> after calling <b>WdfRequestReuse</b>.</p>

<p>For more information about <b>WdfRequestReuse</b>, see <a href="wdf.reusing_framework_request_objects">Reusing Framework Request Objects</a>.</p>

<p>The following code example is part of a <a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a> callback function that calls <b>WdfRequestReuse</b> so that the driver can reuse a driver-allocated request.</p>

<p>A framework-based driver can reuse framework request objects that it created by previous calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549951">WdfRequestCreate</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549953">WdfRequestCreateFromIrp</a>. Drivers can also reuse request objects that they have <a href="wdf.receiving_i_o_requests">received from the framework</a>, but they cannot set the <a href="wdf.WDF_REQUEST_REUSE_FLAGS">WDF_REQUEST_REUSE_SET_NEW_IRP</a> flag for those request objects.</p>

<p>A driver can reuse a request object after the original request has been completed. After a driver has called <b>WdfRequestReuse</b>, the request's contents must be reinitialized. The driver can specify some request parameters in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552480">WDF_REQUEST_REUSE_PARAMS</a> structure. </p>

<p>If you want the reused request to have a <a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a> callback function, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550030">WdfRequestSetCompletionRoutine</a> after calling <b>WdfRequestReuse</b>.</p>

<p>For more information about <b>WdfRequestReuse</b>, see <a href="wdf.reusing_framework_request_objects">Reusing Framework Request Objects</a>.</p>

<p>The following code example is part of a <a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a> callback function that calls <b>WdfRequestReuse</b> so that the driver can reuse a driver-allocated request.</p>

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
<dt>Wdfrequest.h (include Wdf.h)</dt>
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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547261">InvalidReqAccess</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547267">InvalidReqAccessLocal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551599">ReqSendFail</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549951">WdfRequestCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549953">WdfRequestCreateFromIrp</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550030">WdfRequestSetCompletionRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552480">WDF_REQUEST_REUSE_PARAMS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552483">WDF_REQUEST_REUSE_PARAMS_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestReuse method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
