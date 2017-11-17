---
UID: NF.ntifs.SeQuerySecurityDescriptorInfo
title: SeQuerySecurityDescriptorInfo
author: windows-driver-content
description: The SeQuerySecurityDescriptorInfo routine retrieves a copy of an object's security descriptor.
old-location: ifsk\sequerysecuritydescriptorinfo.htm
ms.assetid: 4803e816-c59a-42b2-adc1-7a197ae16d42
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SeQuerySecurityDescriptorInfo
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
req.irql: PASSIVE_LEVEL
ms.keywords: SeQuerySecurityDescriptorInfo
req.iface: 
---

# SeQuerySecurityDescriptorInfo function



## -description
<p>The <b>SeQuerySecurityDescriptorInfo</b> routine retrieves a copy of an object's security descriptor.</p>


## -syntax

````
NTSTATUS SeQuerySecurityDescriptorInfo(
  _In_    PSECURITY_INFORMATION SecurityInformation,
  _Out_   PSECURITY_DESCRIPTOR  SecurityDescriptor,
  _Inout_ PULONG                Length,
  _Inout_ PSECURITY_DESCRIPTOR  *ObjectsSecurityDescriptor
);
````


## -parameters
<dl>

### -param <i>SecurityInformation</i> [in]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556635">SECURITY_INFORMATION</a> value specifying which security information is being queried. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DACL_SECURITY_INFORMATION</p>
</td>
<td>
<p>Indicates the discretionary access control list (DACL) of the object is being queried. Requires READ_CONTROL access. </p>
</td>
</tr>
<tr>
<td>
<p>GROUP_SECURITY_INFORMATION</p>
</td>
<td>
<p>Indicates the primary group identifier of the object is being queried. Requires READ_CONTROL access. </p>
</td>
</tr>
<tr>
<td>
<p>OWNER_SECURITY_INFORMATION</p>
</td>
<td>
<p>Indicates the owner identifier of the object is being queried. Requires READ_CONTROL access. </p>
</td>
</tr>
<tr>
<td>
<p>SACL_SECURITY_INFORMATION</p>
</td>
<td>
<p>Indicates the system ACL (SACL) of the object is being queried. Requires ACCESS_SYSTEM_SECURITY access. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>SecurityDescriptor</i> [out]

<dd>
<p>Caller-allocated user buffer that <b>SeQuerySecurityDescriptorInfo</b> fills with a copy of the specified security descriptor in self-relative format. </p>
</dd>

### -param <i>Length</i> [in, out]

<dd>
<p>Pointer to a variable that specifies the size, in bytes, of the buffer pointed to by <i>SecurityDescriptor</i>. Upon return, <b>SeQuerySecurityDescriptorInfo</b> sets this variable to the number of bytes required to store the requested information.</p>
</dd>

### -param <i>ObjectsSecurityDescriptor</i> [in, out]

<dd>
<p>Pointer to a pointer to an object's security descriptor. The security descriptor must be in self-relative format.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The call to <b>SeQuerySecurityDescriptorInfo</b> succeeded.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer is too small for the security descriptor. None of the security information was copied to the buffer.</p>

<p> </p>

## -remarks
<p>A security descriptor can be in absolute or self-relative format. A security descriptor in absolute format contains pointers to the information it contains, rather than containing the information itself. A security descriptor in self-relative format contains the information in a contiguous block of memory. In a self-relative security descriptor, a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a> structure always starts the information, but the security descriptor's other components can follow the SECURITY_DESCRIPTOR structure in any order. Instead of using memory addresses, the components of the security descriptor are identified by offsets from the beginning of the security descriptor. This format is useful when a security descriptor must be stored on a disk or transmitted by means of a communications protocol. </p>

<p>Because the security descriptor is returned in self-relative format, the caller of <b>SeQuerySecurityDescriptorInfo</b> should cast the value returned in the <i>SecurityDescriptor</i> parameter to type PISECURITY_DESCRIPTOR_RELATIVE. </p>

<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK.</p>

<p>A security descriptor can be in absolute or self-relative format. A security descriptor in absolute format contains pointers to the information it contains, rather than containing the information itself. A security descriptor in self-relative format contains the information in a contiguous block of memory. In a self-relative security descriptor, a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a> structure always starts the information, but the security descriptor's other components can follow the SECURITY_DESCRIPTOR structure in any order. Instead of using memory addresses, the components of the security descriptor are identified by offsets from the beginning of the security descriptor. This format is useful when a security descriptor must be stored on a disk or transmitted by means of a communications protocol. </p>

<p>Because the security descriptor is returned in self-relative format, the caller of <b>SeQuerySecurityDescriptorInfo</b> should cast the value returned in the <i>SecurityDescriptor</i> parameter to type PISECURITY_DESCRIPTOR_RELATIVE. </p>

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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538866">ACL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552089">RtlAbsoluteToSelfRelativeSD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561827">RtlCreateSecurityDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552165">RtlCreateSecurityDescriptorRelative</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552976">RtlGetOwnerSecurityDescriptor</a>
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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SeQuerySecurityDescriptorInfo routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
