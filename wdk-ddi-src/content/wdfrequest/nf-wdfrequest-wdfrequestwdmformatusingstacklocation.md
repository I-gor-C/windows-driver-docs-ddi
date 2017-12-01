---
UID: NF.wdfrequest.WdfRequestWdmFormatUsingStackLocation
title: WdfRequestWdmFormatUsingStackLocation
author: windows-driver-content
description: The WdfRequestWdmFormatUsingStackLocation method formats an I/O request by copying the contents of a specified WDM I/O stack location structure to the next stack location in the request.
old-location: wdf\wdfrequestwdmformatusingstacklocation.htm
old-project: wdf
ms.assetid: 9ee3d748-f9aa-43d6-b472-7b55d2034fc7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfRequestWdmFormatUsingStackLocation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfRequestWdmFormatUsingStackLocation
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, InvalidReqAccess, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2, RequestFormattedValid
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfRequestWdmFormatUsingStackLocation function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfRequestWdmFormatUsingStackLocation</b> method formats an I/O request by copying the contents of a specified WDM <a href="https://msdn.microsoft.com/62c8ee00-c7cb-4aa1-90ab-b8bedbd818ee">I/O stack location</a> structure to the next stack location in the request.</p>


## -syntax

````
VOID WdfRequestWdmFormatUsingStackLocation(
  _In_ WDFREQUEST         Request,
  _In_ PIO_STACK_LOCATION Stack
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>A handle to a framework request object.</p>
</dd>

### -param <i>Stack</i> [in]

<dd>
<p>A pointer to an <a href="..\wdm\ns-wdm--io-stack-location.md">IO_STACK_LOCATION</a> structure that contains driver-supplied information. </p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>The <b>WdfRequestWdmFormatUsingStackLocation</b> method copies the information that is supplied by the <i>Stack</i> parameter into the next IRP stack location in the request. </p>

<p><b>WdfRequestWdmFormatUsingStackLocation</b> formats the request independent of whether the I/O target object of the request is local or remote.</p>

<p>If you want to set a completion routine for the request, your driver must call <a href="..\wdfrequest\nf-wdfrequest-wdfrequestsetcompletionroutine.md">WdfRequestSetCompletionRoutine</a> after calling <b>WdfRequestWdmFormatUsingStackLocation</b>.</p>

<p>For more information about <b>WdfRequestWdmFormatUsingStackLocation</b>, see <a href="wdf.forwarding_i_o_requests">Forwarding I/O Requests</a>.</p>

<p>The following code example supplies an <a href="..\wdm\ns-wdm--io-stack-location.md">IO_STACK_LOCATION</a> structure for an I/O request, sets a <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-completion-routine.md">CompletionRoutine</a> callback function, and then sends the request to an I/O target.</p>

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
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_invalidreqaccess">InvalidReqAccess</a>, <a href="devtest.kmdf_invalidreqaccesslocal">InvalidReqAccessLocal</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_requestformattedvalid">RequestFormattedValid</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfrequest\nf-wdfrequest-wdfrequestsetcompletionroutine.md">WdfRequestSetCompletionRoutine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestWdmFormatUsingStackLocation method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
