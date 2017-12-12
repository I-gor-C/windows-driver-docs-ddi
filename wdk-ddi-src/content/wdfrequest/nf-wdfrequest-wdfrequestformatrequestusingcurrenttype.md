---
UID: NF.wdfrequest.WdfRequestFormatRequestUsingCurrentType
title: WdfRequestFormatRequestUsingCurrentType function
author: windows-driver-content
description: The WdfRequestFormatRequestUsingCurrentType method formats a specified I/O request so that the driver can forward it, unmodified, to the driver's local I/O target.
old-location: wdf\wdfrequestformatrequestusingcurrenttype.htm
old-project: wdf
ms.assetid: 51af6f9e-1e38-4af2-9db8-cfad41e2f435
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfRequestFormatRequestUsingCurrentType
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
req.alt-api: WdfRequestFormatRequestUsingCurrentType
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, InvalidReqAccess, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2, RequestFormattedValid
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

# WdfRequestFormatRequestUsingCurrentType function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfRequestFormatRequestUsingCurrentType</b> method formats a specified I/O request so that the driver can <a href="wdf.forwarding_i_o_requests">forward</a> it, unmodified, to the driver's local I/O target.



## -syntax

````
VOID WdfRequestFormatRequestUsingCurrentType(
  _In_ WDFREQUEST Request
);
````


## -parameters

### -param Request [in]

A handle to a framework request object that the driver received from one of its I/O queues.


## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
When your driver <a href="wdf.receiving_i_o_requests">receives an I/O request</a>, sometimes you will want the driver to forward the request, unmodified, to its local I/O target. To forward such a request, the driver must:

Call <b>WdfRequestFormatRequestUsingCurrentType</b> to format the request object so that the framework can pass the request to the driver's local I/O target.

Call <a href="wdf.wdfrequestsend">WdfRequestSend</a> to send the request to the I/O target.

For more information about <b>WdfRequestFormatRequestUsingCurrentType</b>, see <a href="wdf.forwarding_i_o_requests">Forwarding I/O Requests</a>.

The following code example is an <a href="..\wdfio\nc-wdfio-evt_wdf_io_queue_io_default.md">EvtIoDefault</a> callback function that forwards every I/O request that it receives, without modification, to the device's local I/O target.


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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_invalidreqaccess">InvalidReqAccess</a>, <a href="devtest.kmdf_invalidreqaccesslocal">InvalidReqAccessLocal</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_requestformattedvalid">RequestFormattedValid</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfrequestwdmformatusingstacklocation">WdfRequestWdmFormatUsingStackLocation</a>
</dt>
<dt>
<a href="wdf.wdfrequestsend">WdfRequestSend</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestFormatRequestUsingCurrentType method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

