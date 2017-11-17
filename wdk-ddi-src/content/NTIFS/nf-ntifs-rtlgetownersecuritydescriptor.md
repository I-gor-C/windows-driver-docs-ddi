---
UID: NF.ntifs.RtlGetOwnerSecurityDescriptor
title: RtlGetOwnerSecurityDescriptor
author: windows-driver-content
description: The RtlGetOwnerSecurityDescriptor routine returns the owner information for a given security descriptor.
old-location: ifsk\rtlgetownersecuritydescriptor.htm
ms.assetid: 64c1b899-5737-474c-92ee-f18f7f2f06f5
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlGetOwnerSecurityDescriptor
req.alt-loc: NtosKrnl.exe,Ntdll.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode); 
Ntdll.dll (user mode)
req.irql: PASSIVE_LEVEL
ms.keywords: RtlGetOwnerSecurityDescriptor
req.iface: 
---

# RtlGetOwnerSecurityDescriptor function



## -description
<p>The <b>RtlGetOwnerSecurityDescriptor</b> routine returns the owner information for a given security descriptor.</p>


## -syntax

````
NTSTATUS RtlGetOwnerSecurityDescriptor(
  _In_  PSECURITY_DESCRIPTOR SecurityDescriptor,
  _Out_ PSID                 *Owner,
  _Out_ PBOOLEAN             OwnerDefaulted
);
````


## -parameters
<dl>

### -param <i>SecurityDescriptor</i> [in]

<dd>
<p>Pointer to the security descriptor.</p>
</dd>

### -param <i>Owner</i> [out]

<dd>
<p>Pointer to an address to receive a pointer to the owner security identifier (<a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a>). If the security descriptor does not currently contain an owner SID, <i>Owner</i> receives <b>NULL</b>.</p>
</dd>

### -param <i>OwnerDefaulted</i> [out]

<dd>
<p>Pointer to a Boolean variable that receives <b>TRUE</b> if the owner information is derived from a default mechanism, rather than by the original provider of the security descriptor explicitly, <b>FALSE</b> otherwise. Valid only if <i>Owner</i> receives a non-<b>NULL</b> value.</p>
</dd>
</dl>

## -returns
<p><b>RtlGetOwnerSecurityDescriptor</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following:</p><dl>
<dt><b>STATUS_UNKNOWN_REVISION</b></dt>
</dl><p>The security descriptor's revision level is not known or is not supported. This is an error code. </p>

<p> </p>

## -remarks
<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK.</p>

<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK.</p>

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
<p>This routine is available on Microsoft Windows 2000 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<dt>NtosKrnl.exe (kernel mode); </dt>
<dt>Ntdll.dll (user mode)</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561827">RtlCreateSecurityDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562025">RtlLengthSecurityDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562781">RtlSetDaclSecurityDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553220">RtlSetOwnerSecurityDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563024">RtlValidSecurityDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlGetOwnerSecurityDescriptor routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
