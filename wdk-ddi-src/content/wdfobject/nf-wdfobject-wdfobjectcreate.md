---
UID: NF.wdfobject.WdfObjectCreate
title: WdfObjectCreate
author: windows-driver-content
description: The WdfObjectCreate method creates a general framework object.
old-location: wdf\wdfobjectcreate.htm
old-project: wdf
ms.assetid: fd56c529-c7ad-4fc4-8fcc-950a1e8e21e5
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfObjectCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfobject.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfObjectCreate
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
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

# WdfObjectCreate function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfObjectCreate</b> method creates a general framework object.</p>


## -syntax

````
NTSTATUS WdfObjectCreate(
  _In_opt_ PWDF_OBJECT_ATTRIBUTES Attributes,
  _Out_    WDFOBJECT              *Object
);
````


## -parameters
<dl>

### -param <i>Attributes</i> [in, optional]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure that contains driver-supplied attributes for the new object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>Object</i> [out]

<dd>
<p>A pointer to a location that receives a handle to the new framework object.</p>
</dd>
</dl>

## -returns
<p><b>WdfObjectCreate</b> returns STATUS_SUCCESS if the operation succeeds. For a list of additional return values, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.</p>

<p>This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>By default, the new general framework object's parent is the framework driver object that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547175">WdfDriverCreate</a> method created. You can use the <b>ParentObject</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure to specify a different parent. The framework deletes the general object when it deletes the parent object. If your driver does not change the default parent, the driver should delete the general object when it has finished using the object; otherwise, the object will remain until the I/O manager unloads your driver. </p>

<p>For more information about the <b>WdfObjectCreate</b> method, see <a href="wdf.using_general_framework_objects">Using General Framework Objects</a>.</p>

<p>The following code example initializes an WDF_OBJECT_ATTRIBUTES structure and creates a general framework object.</p>

<p>By default, the new general framework object's parent is the framework driver object that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547175">WdfDriverCreate</a> method created. You can use the <b>ParentObject</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure to specify a different parent. The framework deletes the general object when it deletes the parent object. If your driver does not change the default parent, the driver should delete the general object when it has finished using the object; otherwise, the object will remain until the I/O manager unloads your driver. </p>

<p>For more information about the <b>WdfObjectCreate</b> method, see <a href="wdf.using_general_framework_objects">Using General Framework Objects</a>.</p>

<p>The following code example initializes an WDF_OBJECT_ATTRIBUTES structure and creates a general framework object.</p>

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
<dt>Wdfobject.h (include Wdf.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547175">WdfDriverCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548734">WdfObjectDelete</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfObjectCreate method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
