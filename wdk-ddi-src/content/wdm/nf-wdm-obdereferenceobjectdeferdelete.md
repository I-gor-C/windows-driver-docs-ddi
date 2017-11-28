---
UID: NF.wdm.ObDereferenceObjectDeferDelete
title: ObDereferenceObjectDeferDelete
author: windows-driver-content
description: The ObDereferenceObjectDeferDelete routine decrements the reference count for the given object, checks for object retention, and avoids deadlocks.
old-location: kernel\obdereferenceobjectdeferdelete.htm
old-project: kernel
ms.assetid: 6b20db9e-807d-40f5-844f-f9726e3a854f
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ObDereferenceObjectDeferDelete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Fltkernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ObDereferenceObjectDeferDelete
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ObDereferenceObjectDeferDelete function



## -description
<p>The <b>ObDereferenceObjectDeferDelete</b> routine decrements the reference count for the given object, checks for object retention, and avoids deadlocks.</p>


## -syntax

````
VOID ObDereferenceObjectDeferDelete(
  _In_ PVOID Object
);
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd>
<p>A pointer to the body of the object.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>ObDereferenceObjectDeferDelete</b> is similar to <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a> except that, when the reference count of the object reaches zero, the object manager passes the object deletion request to a worker thread. Therefore, the deletion later occurs at IRQL = PASSIVE_LEVEL.</p>

<p>Use <b>ObDereferenceObjectDeferDelete</b> for any object when the immediate deletion by the current thread of the object (by using <b>ObDereferenceObject</b>) might result in a deadlock.</p>

<p>For example, such a deadlock can occur if <b>ObDereferenceObject</b> is used to dereference a <a href="https://msdn.microsoft.com/b558ace9-b416-4572-ac94-58a083c9d33b">Kernel Transaction Manager</a> (KTM) object when a higher level driver on the driver stack is holding a lock.</p>

<p>To avoid such deadlocks, use <b>ObDereferenceObjectDeferDelete</b> instead of <b>ObDereferenceObject</b> to dereference KTM objects.</p>

<p><b>ObDereferenceObjectDeferDelete</b> is similar to <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a> except that, when the reference count of the object reaches zero, the object manager passes the object deletion request to a worker thread. Therefore, the deletion later occurs at IRQL = PASSIVE_LEVEL.</p>

<p>Use <b>ObDereferenceObjectDeferDelete</b> for any object when the immediate deletion by the current thread of the object (by using <b>ObDereferenceObject</b>) might result in a deadlock.</p>

<p>For example, such a deadlock can occur if <b>ObDereferenceObject</b> is used to dereference a <a href="https://msdn.microsoft.com/b558ace9-b416-4572-ac94-58a083c9d33b">Kernel Transaction Manager</a> (KTM) object when a higher level driver on the driver stack is holding a lock.</p>

<p>To avoid such deadlocks, use <b>ObDereferenceObjectDeferDelete</b> instead of <b>ObDereferenceObject</b> to dereference KTM objects.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Fltkernel.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558678">ObReferenceObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ObDereferenceObjectDeferDelete routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
