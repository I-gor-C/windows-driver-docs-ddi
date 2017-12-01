---
UID: NF.wdm.ObGetObjectSecurity
title: ObGetObjectSecurity
author: windows-driver-content
description: The ObGetObjectSecurity routine gets the security descriptor for a given object.
old-location: kernel\obgetobjectsecurity.htm
old-project: kernel
ms.assetid: 8ac8d3ff-68ec-4e23-bbf9-0a9b7fa13ce3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ObGetObjectSecurity
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
req.alt-api: ObGetObjectSecurity
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlApcLte, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ObGetObjectSecurity function



## -description
<p>The <b>ObGetObjectSecurity</b> routine gets the security descriptor for a given object. </p>


## -syntax

````
NTSTATUS ObGetObjectSecurity(
  _In_  PVOID                Object,
  _Out_ PSECURITY_DESCRIPTOR *SecurityDescriptor,
  _Out_ PBOOLEAN             MemoryAllocated
);
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd>
<p>Pointer to the object.</p>
</dd>

### -param <i>SecurityDescriptor</i> [out]

<dd>
<p>Pointer to a caller-supplied variable that this routine sets to the address of a buffer containing the <a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a> for the given object. If the given object has no security descriptor, this variable is set to <b>NULL</b> on return from <b>ObGetObjectSecurity</b>.</p>
</dd>

### -param <i>MemoryAllocated</i> [out]

<dd>
<p>Pointer to a caller-supplied variable that this routine sets to <b>TRUE</b> if it allocated a buffer to contain the security descriptor. </p>
</dd>
</dl>

## -returns
<p><b>ObGetObjectSecurity</b> either returns STATUS_SUCCESS or an error status, such as STATUS_INSUFFICIENT_RESOURCES if it could not allocate enough memory to return the requested information. </p>

## -remarks
<p>A successful call to <b>ObGetObjectSecurity</b> either returns a self-relative security descriptor in the buffer at *<i>SecurityDescriptor</i> or it returns <b>NULL</b> at <b>*</b><i>SecurityDescriptor</i> if the given object has no security descriptor. For example, any unnamed object, such as an event object, has no security descriptor.</p>

<p>If <b>ObGetObjectSecurity</b> returns STATUS_SUCCESS, the caller must save the value returned at <i>MemoryAllocated</i>. Such a caller must pass <i>MemoryAllocated</i> in a reciprocal call to <a href="..\wdm\nf-wdm-obreleaseobjectsecurity.md">ObReleaseObjectSecurity</a> eventually, thereby restoring the reference count on the security descriptor to its original value and releasing the buffer, if any, that was allocated by <b>ObGetObjectSecurity</b>. </p>

<p><b>ObGetObjectSecurity</b> should only be called at IRQL Level = PASSIVE_LEVEL with APCs enabled, otherwise deadlocks or crashes may occur.</p>

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
<a href="devtest.wdm_irqlapclte">IrqlApcLte</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-obreferenceobjectbyhandle.md">ObReferenceObjectByHandle</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-obreleaseobjectsecurity.md">ObReleaseObjectSecurity</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ObGetObjectSecurity routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
