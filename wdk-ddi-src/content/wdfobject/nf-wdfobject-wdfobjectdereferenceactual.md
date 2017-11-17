---
UID: NF.wdfobject.WdfObjectDereferenceActual
title: WdfObjectDereferenceActual
author: windows-driver-content
description: The WdfObjectDereferenceActual method decrements the reference count for a specified framework object and assigns a tag value, line number, and file name to the reference.
old-location: wdf\wdfobjectdereferenceactual.htm
ms.assetid: ff96ea2b-a1f9-417c-98e6-fbf9cc9f6827
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfobject.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfObjectDereferenceActual
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate
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
ms.keywords: WdfObjectDereferenceActual
req.iface: 
req.product: Windows 10 or later.
---

# WdfObjectDereferenceActual function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfObjectDereferenceActual</b> method decrements the reference count for a specified framework object and assigns a tag value, line number, and file name to the reference<i>.</i></p>


## -syntax

````
VOID WdfObjectDereferenceActual(
  _In_     WDFOBJECT Handle,
  _In_opt_ PVOID     Tag,
  _In_     LONG      Line,
  _In_opt_ PCCH      File
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>A handle to a framework object.</p>
</dd>

### -param <i>Tag</i> [in, optional]

<dd>
<p>A driver-defined value that identifies an object reference. The tag value must match a tag value that the driver previously supplied to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548760">WdfObjectReferenceActual</a>.</p>
</dd>

### -param <i>Line</i> [in]

<dd>
<p>A numeric value that represents a line number in a driver source file.</p>
</dd>

### -param <i>File</i> [in, optional]

<dd>
<p>A pointer to a null-terminated constant character string that represents the name of a driver source file. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>If the object's reference count becomes zero, the object might be deleted before <b>WdfObjectDereferenceActual</b> returns. </p>

<p>Calling <b>WdfObjectDereferenceActual</b> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548746">WdfObjectDereferenceWithTag</a> instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff548739">WdfObjectDereference</a> provides additional information (tag string, line number, and file name) to Microsoft debuggers. <b>WdfObjectDereferenceActual</b> allows your driver to specify the line number and file name, while <b>WdfObjectDereferenceWithTag</b> uses the driver's current line number and file name.</p>

<p>You can view the tag, line number, and file name values by using the <b>!wdftagtracker</b> debugger extension. The debugger extension displays the tag value as both a pointer and a series of characters. For more information about debugger extensions, see <a href="wdf.debugging_a_kmdf_driver">Debugging a KMDF Driver</a>.</p>

<p>For more information about object reference counts, see <a href="wdf.framework_object_life_cycle">Framework Object Life Cycle</a>.</p>

<p>The following code example decrements an object's reference count and assigns a tag value, line number, and file name to the reference.</p>

<p>If the object's reference count becomes zero, the object might be deleted before <b>WdfObjectDereferenceActual</b> returns. </p>

<p>Calling <b>WdfObjectDereferenceActual</b> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548746">WdfObjectDereferenceWithTag</a> instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff548739">WdfObjectDereference</a> provides additional information (tag string, line number, and file name) to Microsoft debuggers. <b>WdfObjectDereferenceActual</b> allows your driver to specify the line number and file name, while <b>WdfObjectDereferenceWithTag</b> uses the driver's current line number and file name.</p>

<p>You can view the tag, line number, and file name values by using the <b>!wdftagtracker</b> debugger extension. The debugger extension displays the tag value as both a pointer and a series of characters. For more information about debugger extensions, see <a href="wdf.debugging_a_kmdf_driver">Debugging a KMDF Driver</a>.</p>

<p>For more information about object reference counts, see <a href="wdf.framework_object_life_cycle">Framework Object Life Cycle</a>.</p>

<p>The following code example decrements an object's reference count and assigns a tag value, line number, and file name to the reference.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548739">WdfObjectDereference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548760">WdfObjectReferenceActual</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfObjectDereferenceActual method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
