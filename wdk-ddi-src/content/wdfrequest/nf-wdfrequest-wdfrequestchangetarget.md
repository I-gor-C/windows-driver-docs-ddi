---
UID: NF.wdfrequest.WdfRequestChangeTarget
title: WdfRequestChangeTarget function
author: windows-driver-content
description: The WdfRequestChangeTarget method verifies that a specified I/O request can be sent to a specified I/O target.
old-location: wdf\wdfrequestchangetarget.htm
old-project: wdf
ms.assetid: 562e92b4-fe68-4301-af40-f535cc408b9d
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfRequestChangeTarget
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
req.alt-api: WdfRequestChangeTarget
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

# WdfRequestChangeTarget function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfRequestChangeTarget</b> method verifies that a specified I/O request can be sent to a specified I/O target.



## -syntax

````
NTSTATUS WdfRequestChangeTarget(
  _In_ WDFREQUEST  Request,
  _In_ WDFIOTARGET IoTarget
);
````


## -parameters

### -param Request [in]

A handle to a framework request object.


### -param IoTarget [in]

A handle to a framework I/O target object. 


## -returns
<b>WdfRequestChangeTarget</b>  returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An input parameter is invalid.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>There are insufficient system resources to complete the operation.
<dl>
<dt><b>STATUS_REQUEST_NOT_ACCEPTED</b></dt>
</dl>The request's array of I/O stack locations is not large enough to allow the driver to send the request to the I/O target.

 

This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
Your driver should call the <b>WdfRequestChangeTarget</b> method before it calls <a href="wdf.wdfrequestsend">WdfRequestSend</a>, if the driver sends a single I/O request to multiple I/O targets. <b>WdfRequestChangeTarget</b> verifies that the request can be sent to the specified I/O target. 

Most drivers send each request to only one device and thus to only one I/O target. A driver either <a href="wdf.receiving_i_o_requests">receives the request</a> or it creates a new request by calling <a href="wdf.wdfrequestcreate">WdfRequestCreate</a>.

If the driver is sending the request to one device, it calls <a href="wdf.wdfdevicegetiotarget">WdfDeviceGetIoTarget</a> to determine the device's I/O target and then calls <a href="wdf.wdfrequestsend">WdfRequestSend</a> to send the request to the target.

If the driver is sending the request to multiple devices, it calls <a href="wdf.wdfdevicegetiotarget">WdfDeviceGetIoTarget</a> for each device to determine the device's I/O target. Before calling <a href="wdf.wdfrequestsend">WdfRequestSend</a>, the driver must call <b>WdfRequestChangeTarget</b> to ensure that each I/O target is accessible.

For more information about <b>WdfRequestChangeTarget</b>, see <a href="wdf.forwarding_i_o_requests">Forwarding I/O Requests</a>.

The following code example verifies that an I/O request can be sent to a specified device's local I/O target.


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
<a href="wdf.wdfdevicegetiotarget">WdfDeviceGetIoTarget</a>
</dt>
<dt>
<a href="wdf.wdfrequestcreate">WdfRequestCreate</a>
</dt>
<dt>
<a href="wdf.wdfrequestsend">WdfRequestSend</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestChangeTarget method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

