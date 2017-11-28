---
UID: NF.fltkernel.FltObjectReference
title: FltObjectReference
author: windows-driver-content
description: The FltObjectReference routine adds a rundown reference to an opaque filter, instance, or volume pointer.
old-location: ifsk\fltobjectreference.htm
old-project: ifsk
ms.assetid: ad6317bf-92fc-4e77-9993-37b7aa123a3d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltObjectReference
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltObjectReference
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# FltObjectReference function



## -description
<p>The <b>FltObjectReference</b> routine adds a rundown reference to an opaque filter, instance, or volume pointer. </p>


## -syntax

````
NTSTATUS FltObjectReference(
  _Inout_ PVOID FltObject
);
````


## -parameters
<dl>

### -param <i>FltObject</i> [in, out]

<dd>
<p>Opaque filter pointer (PFLT_FILTER), instance pointer (PFLT_INSTANCE), or volume pointer (PFLT_VOLUME). </p>
</dd>
</dl>

## -returns
<p><b>FltObjectReference</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following: </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The minifilter driver, instance, or volume is being torn down. This is an error code. </p>

<p> </p>

## -remarks
<p>Adding a rundown reference to an opaque filter, instance, or volume object pointer prevents the object from being freed. </p>

<p>To remove a rundown reference from an opaque filter, instance, or volume pointer, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543378">FltObjectDereference</a>. </p>

<p>Adding a rundown reference to an opaque filter, instance, or volume object pointer prevents the object from being freed. </p>

<p>To remove a rundown reference from an opaque filter, instance, or volume pointer, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543378">FltObjectDereference</a>. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543378">FltObjectDereference</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltObjectReference routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
