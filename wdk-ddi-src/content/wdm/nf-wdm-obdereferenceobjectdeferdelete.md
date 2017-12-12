---
UID: NF.wdm.ObDereferenceObjectDeferDelete
title: ObDereferenceObjectDeferDelete function
author: windows-driver-content
description: The ObDereferenceObjectDeferDelete routine decrements the reference count for the given object, checks for object retention, and avoids deadlocks.
old-location: kernel\obdereferenceobjectdeferdelete.htm
old-project: kernel
ms.assetid: 6b20db9e-807d-40f5-844f-f9726e3a854f
ms.author: windowsdriverdev
ms.date: 12/7/2017
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
req.product: Windows 10 or later.
---

# ObDereferenceObjectDeferDelete function



## -description
The <b>ObDereferenceObjectDeferDelete</b> routine decrements the reference count for the given object, checks for object retention, and avoids deadlocks.



## -syntax

````
VOID ObDereferenceObjectDeferDelete(
  _In_ PVOID Object
);
````


## -parameters

### -param Object [in]

A pointer to the body of the object.


## -returns
None


## -remarks
<b>ObDereferenceObjectDeferDelete</b> is similar to <a href="kernel.obdereferenceobject">ObDereferenceObject</a> except that, when the reference count of the object reaches zero, the object manager passes the object deletion request to a worker thread. Therefore, the deletion later occurs at IRQL = PASSIVE_LEVEL.

Use <b>ObDereferenceObjectDeferDelete</b> for any object when the immediate deletion by the current thread of the object (by using <b>ObDereferenceObject</b>) might result in a deadlock.

For example, such a deadlock can occur if <b>ObDereferenceObject</b> is used to dereference a <a href="https://msdn.microsoft.com/b558ace9-b416-4572-ac94-58a083c9d33b">Kernel Transaction Manager</a> (KTM) object when a higher level driver on the driver stack is holding a lock.

To avoid such deadlocks, use <b>ObDereferenceObjectDeferDelete</b> instead of <b>ObDereferenceObject</b> to dereference KTM objects.


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
Version

</th>
<td width="70%">
Available in Windows Vista and later versions of Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Fltkernel.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.obdereferenceobject">ObDereferenceObject</a>
</dt>
<dt>
<a href="kernel.obreferenceobject">ObReferenceObject</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ObDereferenceObjectDeferDelete routine%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

