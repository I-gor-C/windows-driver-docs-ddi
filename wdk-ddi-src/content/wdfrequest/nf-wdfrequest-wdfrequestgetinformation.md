---
UID: NF.wdfrequest.WdfRequestGetInformation
title: WdfRequestGetInformation function
author: windows-driver-content
description: The WdfRequestGetInformation method returns completion status information for a specified I/O request.
old-location: wdf\wdfrequestgetinformation.htm
old-project: wdf
ms.assetid: fd5f29f7-e9c6-48c4-8704-5db37b8c6337
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfRequestGetInformation
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
req.alt-api: WdfRequestGetInformation
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, InvalidReqAccess, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2
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

# WdfRequestGetInformation function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]
The <b>WdfRequestGetInformation</b> method returns completion status information for a specified I/O request.


## -syntax

````
ULONG_PTR WdfRequestGetInformation(
  _In_ WDFREQUEST Request
);
````


## -parameters

### -param Request [in]

A handle to a framework request object.

## -returns
<b>WdfRequestGetInformation</b> returns the information that a lower-level driver set by calling <a href="wdf.wdfrequestsetinformation">WdfRequestSetInformation</a> or <a href="wdf.wdfrequestcompletewithinformation">WdfRequestCompleteWithInformation</a>.

A bug check occurs if the driver supplies an invalid object handle.



## -remarks
A driver can call <a href="wdf.wdfrequestsetinformation">WdfRequestSetInformation</a> or <a href="wdf.wdfrequestcompletewithinformation">WdfRequestCompleteWithInformation</a> to set completion status information for an I/O request. Your driver can call <b>WdfRequestGetInformation</b> after a lower-level driver completes a request, to obtain completion status information that the lower-level driver set. 

If your driver calls <b>WdfRequestGetInformation</b> after it calls <a href="wdf.wdfrequestcomplete">WdfRequestComplete</a> to complete the request, <b>WdfRequestGetInformation</b> returns <b>NULL</b>.

For more information about <b>WdfRequestGetInformation</b>, see <a href="wdf.completing_i_o_requests">Completing I/O Requests</a>.

The following code example sends an I/O request to an I/O target and then obtains status information that the I/O target provided.

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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_invalidreqaccess">InvalidReqAccess</a>, <a href="devtest.kmdf_invalidreqaccesslocal">InvalidReqAccessLocal</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfrequestcompletewithinformation">WdfRequestCompleteWithInformation</a>
</dt>
<dt>
<a href="wdf.wdfrequestsetinformation">WdfRequestSetInformation</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestGetInformation method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
