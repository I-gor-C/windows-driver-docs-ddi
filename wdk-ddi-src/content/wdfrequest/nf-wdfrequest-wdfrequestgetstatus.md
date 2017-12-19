---
UID: NF.wdfrequest.WdfRequestGetStatus
title: WdfRequestGetStatus function
author: windows-driver-content
description: The WdfRequestGetStatus method returns the status of an I/O request.
old-location: wdf\wdfrequestgetstatus.htm
old-project: wdf
ms.assetid: 82f922a1-34c1-475b-b12a-210ae602a4bd
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfRequestGetStatus
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
req.alt-api: WdfRequestGetStatus
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2, RequestGetStatusValid
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

# WdfRequestGetStatus function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfRequestGetStatus</b> method returns the status of an I/O request.



## -syntax

````
NTSTATUS WdfRequestGetStatus(
  _In_ WDFREQUEST Request
);
````


## -parameters

### -param Request [in]

A handle to a framework request object.


## -returns
<b>WdfRequestGetStatus</b>  returns an NTSTATUS value. For more information about what value can be returned, see the following Remarks section.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
The <b>WdfRequestGetStatus</b> method returns one of the following:

If a driver's call to <a href="wdf.wdfrequestsend">WdfRequestSend</a> succeeds, <b>WdfRequestGetStatus</b> returns the status value that is set by the driver that calls <a href="wdf.wdfrequestcomplete">WdfRequestComplete</a> to complete the specified request. The driver typically calls <b>WdfRequestGetStatus</b> from within a <a href="..\wdfrequest\nc-wdfrequest-evt_wdf_request_completion_routine.md">CompletionRoutine</a> callback function.

If a driver's call to <a href="wdf.wdfrequestsend">WdfRequestSend</a> fails, <b>WdfRequestGetStatus</b> returns a status value that the framework has set to describe the failure. The driver can call <b>WdfRequestGetStatus</b> immediately after calling <b>WdfRequestSend</b>.

If the driver sets the <a href="wdf.wdf_request_send_options_flags">WDF_REQUEST_SEND_OPTION_SYNCHRONOUS</a> flag for a request when calling <a href="wdf.wdfrequestsend">WdfRequestSend</a>, the driver can call <b>WdfRequestGetStatus</b> immediately after calling <b>WdfRequestSend</b>, whether the call to <b>WdfRequestSend</b> succeeds or fails.

For more information about request completion, see <a href="wdf.completing_i_o_requests">Completing I/O Requests</a>.

The following code example is from the <a href="wdf.sample_kmdf_drivers">KbFiltr</a> sample driver. This example sends an I/O request to an I/O target. If <a href="wdf.wdfrequestsend">WdfRequestSend</a> fails, the example uses the <b>WdfRequestGetStatus</b> return value as input to <a href="wdf.wdfrequestcomplete">WdfRequestComplete</a>. 


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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_requestgetstatusvalid">RequestGetStatusValid</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfrequestcomplete">WdfRequestComplete</a>
</dt>
<dt>
<a href="wdf.wdfrequestsend">WdfRequestSend</a>
</dt>
<dt>
<a href="..\wdfrequest\nc-wdfrequest-evt_wdf_request_completion_routine.md">CompletionRoutine</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestGetStatus method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

