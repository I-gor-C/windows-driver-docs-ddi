---
UID: NF.wdm.ObReferenceObjectByPointer
title: ObReferenceObjectByPointer
author: windows-driver-content
description: The ObReferenceObjectByPointer routine increments the pointer reference count for a given object.
old-location: kernel\obreferenceobjectbypointer.htm
old-project: kernel
ms.assetid: c575bd3f-6790-4815-b7c7-8ee16a9cac17
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ObReferenceObjectByPointer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ObReferenceObjectByPointer
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: TargetRelationNeedsRef, HwStorPortProhibitedDDIs
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

# ObReferenceObjectByPointer function



## -description
<p>The <b>ObReferenceObjectByPointer</b> routine increments the pointer reference count for a given object.</p>


## -syntax

````
NTSTATUS ObReferenceObjectByPointer(
  _In_     PVOID           Object,
  _In_     ACCESS_MASK     DesiredAccess,
  _In_opt_ POBJECT_TYPE    ObjectType,
  _In_     KPROCESSOR_MODE AccessMode
);
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd>
<p>Pointer to the object's body.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>Specifies a mask representing the requested access to the object.</p>
</dd>

### -param <i>ObjectType</i> [in, optional]

<dd>
<p>Pointer to the object type. <i>ObjectType</i> can be <b>*ExEventObjectType</b>, <b>*ExSemaphoreObjectType</b>, <b>*IoFileObjectType</b>, <b>*PsProcessType</b>, <b>*PsThreadType</b>, <b>*SeTokenObjectType</b>, <b>*TmEnlistmentObjectType</b>, <b>*TmResourceManagerObjectType</b>, <b>*TmTransactionManagerObjectType</b>, or <b>*TmTransactionObjectType</b>. </p>
<div class="alert"><b>Note</b>    The <b>SeTokenObjectType</b> object type is supported in Windows XP and later versions of Windows.</div>
<div> </div>
<p>This parameter can also be <b>NULL</b> if <i>AccessMode</i> is <b>KernelMode</b>.</p>
</dd>

### -param <i>AccessMode</i> [in]

<dd>
<p>Indicates the access mode to use for the access check. It must be either <b>UserMode</b> or <b>KernelMode</b>. Lower-level drivers should specify <b>KernelMode</b>.</p>
</dd>
</dl>

## -returns
<p><b>ObReferenceObjectByPointer</b> returns an NTSTATUS value. Possible return values include:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl>

## -remarks
<p>Calling this routine prevents the object from being deleted, possibly by another component's call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a>. The caller must decrement the reference count with <b>ObDereferenceObject</b> as soon as it is done with the object.</p>

<p>Calling this routine prevents the object from being deleted, possibly by another component's call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a>. The caller must decrement the reference count with <b>ObDereferenceObject</b> as soon as it is done with the object.</p>

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
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552918">TargetRelationNeedsRef</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
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
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558679">ObReferenceObjectByHandle</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ObReferenceObjectByPointer routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
