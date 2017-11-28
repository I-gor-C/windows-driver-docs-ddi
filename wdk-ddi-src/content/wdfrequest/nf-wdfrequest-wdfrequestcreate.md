---
UID: NF.wdfrequest.WdfRequestCreate
title: WdfRequestCreate
author: windows-driver-content
description: The WdfRequestCreate method creates an empty framework request object.
old-location: wdf\wdfrequestcreate.htm
old-project: wdf
ms.assetid: 94329e5a-9efb-4e88-92a6-457098d1245f
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfRequestCreate
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
req.alt-api: WdfRequestCreate
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2, ReqDelete, RequestForUrbXrb, RequestSendAndForgetNoFormatting2
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
req.iface: 
req.product: Windows 10 or later.
---

# WdfRequestCreate function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfRequestCreate</b> method creates an empty framework request object.</p>


## -syntax

````
NTSTATUS WdfRequestCreate(
  _In_opt_ PWDF_OBJECT_ATTRIBUTES RequestAttributes,
  _In_opt_ WDFIOTARGET            IoTarget,
  _Out_    WDFREQUEST             *Request
);
````


## -parameters
<dl>

### -param <i>RequestAttributes</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure that specifies object attributes for the request object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>IoTarget</i> [in, optional]

<dd>
<p>A handle to a framework I/O target object. This parameter is optional and can be <b>NULL</b>. If non-<b>NULL</b>, <b>WdfRequestCreate</b> verifies that the driver can eventually send the request to the specified I/O target.</p>
</dd>

### -param <i>Request</i> [out]

<dd>
<p>A pointer to a location that receives a handle to a framework request object. </p>
</dd>
</dl>

## -returns
<p><b>WdfRequestCreate</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An input parameter is invalid.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There are insufficient system resources to complete the operation.</p><dl>
<dt><b>STATUS_REQUEST_NOT_ACCEPTED</b></dt>
</dl><p>The request's array of I/O stack locations is not large enough to allow the driver to send the request to the specified I/O target.</p>

<p> </p>

<p>For a list of additional return values, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.

</p>

<p>This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.


</p>

## -remarks
<p>A framework-based driver can call <b>WdfRequestCreate</b> to create a new request that the driver subsequently passes to other framework functions for initialization. For example, a driver for a USB device might call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551136">WdfUsbTargetPipeFormatRequestForRead</a> to format a new read request.</p>

<p>A framework-based driver that communicates with WDM drivers might specify the contents of a request by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549953">WdfRequestCreateFromIrp</a>.</p>

<p>If a driver calls <b>WdfRequestCreate</b> to create a request object, it must not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a> for the request object. Instead, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548734">WdfObjectDelete</a> when it has finished using the request object. For more information, see <a href="wdf.completing_i_o_requests">Completing I/O Requests</a>.</p>

<p>By default, the new request object's parent is the framework driver object that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547175">WdfDriverCreate</a> method created. You can use the <b>ParentObject</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure to specify a different parent. The framework deletes the request object when it deletes the parent object. If your driver does not change the default parent, the driver should delete the request object when it has finished using the object; otherwise, the request object will remain until the I/O manager unloads your driver. </p>

<p>For more information about calling <b>WdfRequestCreate</b>, see <a href="wdf.creating_framework_request_objects">Creating Framework Request Objects</a>.</p>

<p>The following code example creates an I/O target object, initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure, and calls <b>WdfRequestCreate</b>. The new request object's parent is the I/O target object.</p>

<p>A framework-based driver can call <b>WdfRequestCreate</b> to create a new request that the driver subsequently passes to other framework functions for initialization. For example, a driver for a USB device might call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551136">WdfUsbTargetPipeFormatRequestForRead</a> to format a new read request.</p>

<p>A framework-based driver that communicates with WDM drivers might specify the contents of a request by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549953">WdfRequestCreateFromIrp</a>.</p>

<p>If a driver calls <b>WdfRequestCreate</b> to create a request object, it must not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a> for the request object. Instead, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548734">WdfObjectDelete</a> when it has finished using the request object. For more information, see <a href="wdf.completing_i_o_requests">Completing I/O Requests</a>.</p>

<p>By default, the new request object's parent is the framework driver object that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547175">WdfDriverCreate</a> method created. You can use the <b>ParentObject</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure to specify a different parent. The framework deletes the request object when it deletes the parent object. If your driver does not change the default parent, the driver should delete the request object when it has finished using the object; otherwise, the request object will remain until the I/O manager unloads your driver. </p>

<p>For more information about calling <b>WdfRequestCreate</b>, see <a href="wdf.creating_framework_request_objects">Creating Framework Request Objects</a>.</p>

<p>The following code example creates an I/O target object, initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure, and calls <b>WdfRequestCreate</b>. The new request object's parent is the I/O target object.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547267">InvalidReqAccessLocal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551583">ReqDelete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/jj126208">RequestForUrbXrb</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/jj126210">RequestSendAndForgetNoFormatting2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546786">WdfDeviceInitSetRequestAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547175">WdfDriverCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549953">WdfRequestCreateFromIrp</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550026">WdfRequestReuse</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552402">WDF_OBJECT_ATTRIBUTES_INIT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestCreate method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
