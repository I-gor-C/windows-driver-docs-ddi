---
UID: NF.wdfrequest.WdfRequestReuse
title: WdfRequestReuse function
author: windows-driver-content
description: The WdfRequestReuse method reinitializes a framework request object so that it can be reused.
old-location: wdf\wdfrequestreuse.htm
old-project: wdf
ms.assetid: 3d649cc5-6512-432c-9bd9-60e18507a873
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfRequestReuse
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfRequestReuse function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfRequestReuse</b> method reinitializes a framework request object so that it can be reused.



## -syntax

````
NTSTATUS WdfRequestReuse(
  _In_ WDFREQUEST                Request,
  _In_ PWDF_REQUEST_REUSE_PARAMS ReuseParams
);
````


## -parameters

### -param Request [in]

A handle to a framework request object.


### -param ReuseParams [in]

A pointer to a caller-allocated <a href="wdf.wdf_request_reuse_params">WDF_REQUEST_REUSE_PARAMS</a> structure.


## -returns
<b>WdfRequestReuse</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An input parameter is invalid.
<dl>
<dt><b>STATUS_WDF_REQUEST_INVALID_STATE</b></dt>
</dl>The driver supplied an IRP in the <a href="wdf.wdf_request_reuse_params">WDF_REQUEST_REUSE_PARAMS</a> structure, but the specified request object was not obtained from <a href="wdf.wdfrequestcreatefromirp">WdfRequestCreateFromIrp</a>.

 

A bug check occurs if the driver supplies an invalid object handle.


## -remarks
A framework-based driver can reuse framework request objects that it created by previous calls to <a href="wdf.wdfrequestcreate">WdfRequestCreate</a> or <a href="wdf.wdfrequestcreatefromirp">WdfRequestCreateFromIrp</a>. Drivers can also reuse request objects that they have <a href="wdf.receiving_i_o_requests">received from the framework</a>, but they cannot set the <a href="wdf.WDF_REQUEST_REUSE_FLAGS">WDF_REQUEST_REUSE_SET_NEW_IRP</a> flag for those request objects.

A driver can reuse a request object after the original request has been completed. After a driver has called <b>WdfRequestReuse</b>, the request's contents must be reinitialized. The driver can specify some request parameters in the <a href="wdf.wdf_request_reuse_params">WDF_REQUEST_REUSE_PARAMS</a> structure. 

If you want the reused request to have a <a href="..\wdfrequest\nc-wdfrequest-evt_wdf_request_completion_routine.md">CompletionRoutine</a> callback function, the driver must call <a href="wdf.wdfrequestsetcompletionroutine">WdfRequestSetCompletionRoutine</a> after calling <b>WdfRequestReuse</b>.

For more information about <b>WdfRequestReuse</b>, see <a href="wdf.reusing_framework_request_objects">Reusing Framework Request Objects</a>.

The following code example is part of a <a href="..\wdfrequest\nc-wdfrequest-evt_wdf_request_completion_routine.md">CompletionRoutine</a> callback function that calls <b>WdfRequestReuse</b> so that the driver can reuse a driver-allocated request.


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
<dt>Wdfrequest.h (include Wdf.h)</dt>
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
&lt;=DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_invalidreqaccess">InvalidReqAccess</a>, <a href="devtest.kmdf_invalidreqaccesslocal">InvalidReqAccessLocal</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_reqsendfail">ReqSendFail</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfrequestcreate">WdfRequestCreate</a>
</dt>
<dt>
<a href="wdf.wdfrequestcreatefromirp">WdfRequestCreateFromIrp</a>
</dt>
<dt>
<a href="wdf.wdfrequestsetcompletionroutine">WdfRequestSetCompletionRoutine</a>
</dt>
<dt>
<a href="wdf.wdf_request_reuse_params">WDF_REQUEST_REUSE_PARAMS</a>
</dt>
<dt>
<a href="wdf.wdf_request_reuse_params_init">WDF_REQUEST_REUSE_PARAMS_INIT</a>
</dt>
<dt>
<a href="..\wdfrequest\nc-wdfrequest-evt_wdf_request_completion_routine.md">CompletionRoutine</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestReuse method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

