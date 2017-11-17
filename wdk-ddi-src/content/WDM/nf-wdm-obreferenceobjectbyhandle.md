---
UID: NF.wdm.ObReferenceObjectByHandle
title: ObReferenceObjectByHandle
author: windows-driver-content
description: The ObReferenceObjectByHandle routine provides access validation on the object handle, and, if access can be granted, returns the corresponding pointer to the object's body.
old-location: kernel\obreferenceobjectbyhandle.htm
ms.assetid: 6397d96e-f3b1-4e2f-91ce-b123c9e8de81
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ObReferenceObjectByHandle
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlObPassive, TargetRelationNeedsRef, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
ms.keywords: ObReferenceObjectByHandle
req.iface: 
req.product: Windows 10 or later.
---

# ObReferenceObjectByHandle function



## -description
<p>The <b>ObReferenceObjectByHandle</b> routine provides access validation on the object handle, and, if access can be granted, returns the corresponding pointer to the object's body.</p>


## -syntax

````
NTSTATUS ObReferenceObjectByHandle(
  _In_      HANDLE                     Handle,
  _In_      ACCESS_MASK                DesiredAccess,
  _In_opt_  POBJECT_TYPE               ObjectType,
  _In_      KPROCESSOR_MODE            AccessMode,
  _Out_     PVOID                      *Object,
  _Out_opt_ POBJECT_HANDLE_INFORMATION HandleInformation
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>Specifies an open handle for an object.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>Specifies the requested types of access to the object. The interpretation of this field is dependent on the object type. Do not use any generic access rights. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>.</p>
</dd>

### -param <i>ObjectType</i> [in, optional]

<dd>
<p>Pointer to the object type. <i>ObjectType</i> can be <b>*ExEventObjectType</b>, <b>*ExSemaphoreObjectType</b>, <b>*IoFileObjectType</b>, <b>*PsProcessType</b>, <b>*PsThreadType</b>, <b>*SeTokenObjectType</b>, <b>*TmEnlistmentObjectType</b>, <b>*TmResourceManagerObjectType</b>, <b>*TmTransactionManagerObjectType</b>, or <b>*TmTransactionObjectType</b>.</p>
<div class="alert"><b>Note</b>  The <b>SeTokenObjectType</b> object type is supported starting with Windows XP.</div>
<div> </div>
<p>If <i>ObjectType</i> is not <b>NULL</b>, the operating system verifies that the supplied object type matches the object type of the object that <i>Handle</i> specifies.</p>
</dd>

### -param <i>AccessMode</i> [in]

<dd>
<p>Specifies the access mode to use for the access check. It must be either <b>UserMode</b> or <b>KernelMode</b>. Drivers should always specify <b>UserMode</b> for handles they receive from user address space.</p>
</dd>

### -param <i>Object</i> [out]

<dd>
<p>Pointer to a variable that receives a pointer to the object's body. The following table contains the pointer types.</p>
<table>
<tr>
<th><i>ObjectType</i> parameter</th>
<th><i>Object </i>pointer type</th>
</tr>
<tr>
<td>
<p><b>*ExEventObjectType</b></p>
</td>
<td>
<p>PKEVENT</p>
</td>
</tr>
<tr>
<td>
<p><b>*ExSemaphoreObjectType</b></p>
</td>
<td>
<p>PKSEMAPHORE</p>
</td>
</tr>
<tr>
<td>
<p><b>*IoFileObjectType</b></p>
</td>
<td>
<p>PFILE_OBJECT</p>
</td>
</tr>
<tr>
<td>
<p><b>*PsProcessType</b></p>
</td>
<td>
<p>PEPROCESS or PKPROCESS</p>
</td>
</tr>
<tr>
<td>
<p><b>*PsThreadType</b></p>
</td>
<td>
<p>PETHREAD or PKTHREAD</p>
</td>
</tr>
<tr>
<td>
<p><b>*SeTokenObjectType</b></p>
</td>
<td>
<p>PACCESS_TOKEN</p>
</td>
</tr>
<tr>
<td>
<p><b>*TmEnlistmentObjectType</b></p>
</td>
<td>
<p>PKENLISTMENT</p>
</td>
</tr>
<tr>
<td>
<p><b>*TmResourceManagerObjectType</b></p>
</td>
<td>
<p>PKRESOURCEMANAGER</p>
</td>
</tr>
<tr>
<td>
<p><b>*TmTransactionManagerObjectType</b></p>
</td>
<td>
<p>PKTM</p>
</td>
</tr>
<tr>
<td>
<p><b>*TmTransactionObjectType</b></p>
</td>
<td>
<p>PKTRANSACTION</p>
</td>
</tr>
</table>
<p> </p>
<p>The structures that the pointer types reference are opaque, and drivers cannot access the structure members. Because the structures are opaque, PEPROCESS is equivalent to PKPROCESS, and PETHREAD is equivalent to PKTHREAD.</p>
<div class="alert"><b>Note</b>  The <b>SeTokenObjectType</b> object type is supported starting with Windows XP.</div>
<div> </div>
</dd>

### -param <i>HandleInformation</i> [out, optional]

<dd>
<p>Drivers set this to <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>ObReferenceObjectByHandle</b> returns STATUS_SUCCESS if the call is successful. Possible return values include the following error codes:</p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p>The <i>ObjectType</i> parameter specifies the wrong object type for the object that is identified by the <i>Handle</i> parameter.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The caller cannot be granted the requested access rights to the object.</p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>The <i>Handle</i> parameter is not a valid object handle.</p>

<p> </p>

## -remarks
<p>A pointer to the object body is retrieved from the object table entry and returned to the caller by means of the <i>Object</i> parameter.</p>

<p>If <i>AccessMode</i> is <b>UserMode</b>, the requested access is compared to the granted access for the object. If <i>AccessMode</i> is <b>KernelMode</b>, the handle should originate in the kernel address space.</p>

<p>Starting with Windows 7, if <i>AccessMode</i> is <b>KernelMode</b> and handle is received from user address space, <a href="https://msdn.microsoft.com/library/windows/hardware/ff557262">Driver Verifier</a> issues bugcheck C4, subcode F6.</p>

<p>If the call succeeds, a pointer to the object body is returned to the caller and the pointer reference count is incremented. Incrementing this count prevents the object from being deleted while the pointer is being referenced. The caller must decrement the reference count with <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a> as soon as it is done with the object.</p>

<p>A pointer to the object body is retrieved from the object table entry and returned to the caller by means of the <i>Object</i> parameter.</p>

<p>If <i>AccessMode</i> is <b>UserMode</b>, the requested access is compared to the granted access for the object. If <i>AccessMode</i> is <b>KernelMode</b>, the handle should originate in the kernel address space.</p>

<p>Starting with Windows 7, if <i>AccessMode</i> is <b>KernelMode</b> and handle is received from user address space, <a href="https://msdn.microsoft.com/library/windows/hardware/ff557262">Driver Verifier</a> issues bugcheck C4, subcode F6.</p>

<p>If the call succeeds, a pointer to the object body is returned to the caller and the pointer reference count is incremented. Incrementing this count prevents the object from being deleted while the pointer is being referenced. The caller must decrement the reference count with <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a> as soon as it is done with the object.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547873">IrqlObPassive</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552918">TargetRelationNeedsRef</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558678">ObReferenceObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558686">ObReferenceObjectByPointer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ObReferenceObjectByHandle routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
