---
UID: NF.wdfrequest.WdfRequestCreateFromIrp
title: WdfRequestCreateFromIrp function
author: windows-driver-content
description: The WdfRequestCreateFromIrp method creates a framework request object from a specified WDM IRP.
old-location: wdf\wdfrequestcreatefromirp.htm
old-project: wdf
ms.assetid: 7fc67320-6943-4e39-8474-28c24265eae2
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfRequestCreateFromIrp
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
req.alt-api: WdfRequestCreateFromIrp
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfRequestCreateFromIrp function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfRequestCreateFromIrp</b> method creates a framework request object from a specified WDM IRP.



## -syntax

````
NTSTATUS WdfRequestCreateFromIrp(
  _In_opt_ PWDF_OBJECT_ATTRIBUTES RequestAttributes,
  _In_     PIRP                   Irp,
  _In_     BOOLEAN                RequestFreesIrp,
  _Out_    WDFREQUEST             *Request
);
````


## -parameters

### -param RequestAttributes [in, optional]

A pointer to a caller-allocated <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure that specifies object attributes for the request object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES. 


### -param Irp [in]

A pointer to an <a href="kernel.irp">IRP</a> structure that contains a WDM I/O request packet.


### -param RequestFreesIrp [in]

A Boolean value that, if <b>TRUE</b>, indicates that the framework removes the IRP when the request handle is destroyed. If <b>FALSE</b>, the driver must call <a href="kernel.iofreeirp">IoFreeIrp</a> to remove the IRP, using the steps that the following Examples section demonstrates.


### -param Request [out]

A pointer to a location that receives a handle to a framework request object. 


## -returns
<b>WdfRequestCreateFromIrp</b>  returns STATUS_SUCCESS if the operation succeeds. For a list of additional return values, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.

This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.





## -remarks
Typically, framework-based drivers call <b>WdfRequestCreateFromIrp</b> only if they receive WDM IRPs in a WDM dispatch routine and then forward the requests to framework I/O targets.

If a driver calls <b>WdfRequestCreateFromIrp</b> to create a request object, it must not call <a href="wdf.wdfrequestcomplete">WdfRequestComplete</a> for the request object. Instead, the driver must call <a href="wdf.wdfobjectdelete">WdfObjectDelete</a> when it has finished using the request object.

In addition, the driver must not call <a href="wdf.wdfrequestretrieveoutputmemory">WdfRequestRetrieveOutputMemory</a>, <a href="wdf.wdfrequestretrieveoutputbuffer">WdfRequestRetrieveOutputBuffer</a>, <a href="wdf.wdfrequestretrieveinputbuffer">WdfRequestRetrieveInputBuffer</a>, or <a href="wdf.wdfrequestretrieveinputmemory">WdfRequestRetrieveInputMemory</a> with the new request object.

By default, the new request object's parent is the framework driver object that the <a href="wdf.wdfdrivercreate">WdfDriverCreate</a> method created. You can use the <b>ParentObject</b> member of the <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure to specify a different parent. The framework deletes the request object when it deletes the parent object. If your driver does not change the default parent, the driver should delete the request object when it has finished using the object; otherwise, the request object will remain until the I/O manager unloads your driver. 

For more information about creating framework request objects, see <a href="wdf.creating_framework_request_objects">Creating Framework Request Objects</a>.

Framework-based drivers must not use the <b>Tail.Overlay.DriverContext</b> member of the <a href="kernel.irp">IRP</a> structure, because the framework uses this member.

<b>Example 1</b>

The following code example creates a framework request object from a specified WDM IRP and then deletes it. This example sets the <i>RequestFreesIrp</i> parameter to <b>TRUE</b>, so the framework removes the IRP when the request handle is destroyed.

<b>Example 2</b>

The following code example also creates a framework request object from a specified WDM IRP and then deletes it. This example sets the <i>RequestFreesIrp</i> parameter to <b>FALSE</b>, so the driver must call <a href="kernel.iofreeirp">IoFreeIrp</a> to remove the IRP. All of the function calls in the example  are required.


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
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.iofreeirp">IoFreeIrp</a>
</dt>
<dt>
<a href="wdf.wdfdeviceinitsetrequestattributes">WdfDeviceInitSetRequestAttributes</a>
</dt>
<dt>
<a href="wdf.wdfdrivercreate">WdfDriverCreate</a>
</dt>
<dt>
<a href="wdf.wdfrequestcreate">WdfRequestCreate</a>
</dt>
<dt>
<a href="wdf.wdfrequestreuse">WdfRequestReuse</a>
</dt>
<dt>
<a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestCreateFromIrp method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

