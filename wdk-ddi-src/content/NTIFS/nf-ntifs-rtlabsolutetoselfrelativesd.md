---
UID: NF.ntifs.RtlAbsoluteToSelfRelativeSD
title: RtlAbsoluteToSelfRelativeSD
author: windows-driver-content
description: The RtlAbsoluteToSelfRelativeSD routine creates a new security descriptor in self-relative format by using a security descriptor in absolute format as a template.
old-location: ifsk\rtlabsolutetoselfrelativesd.htm
ms.assetid: e6247856-5abf-44ea-afe8-9be3f61271a4
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows Server 2003 SP1 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlAbsoluteToSelfRelativeSD
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
req.irql: <= APC_LEVEL
ms.keywords: RtlAbsoluteToSelfRelativeSD
req.iface: 
---

# RtlAbsoluteToSelfRelativeSD function



## -description
<p>The <b>RtlAbsoluteToSelfRelativeSD</b> routine creates a new security descriptor in self-relative format by using a security descriptor in absolute format as a template. </p>


## -syntax

````
NTSTATUS RtlAbsoluteToSelfRelativeSD(
  _In_    PSECURITY_DESCRIPTOR AbsoluteSecurityDescriptor,
  _Out_   PSECURITY_DESCRIPTOR SelfRelativeSecurityDescriptor,
  _Inout_ PULONG               BufferLength
);
````


## -parameters
<dl>

### -param <i>AbsoluteSecurityDescriptor</i> [in]

<dd>
<p>Pointer to a caller-allocated buffer that contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a> structure in absolute format. <b>RtlAbsoluteToSelfRelativeSD</b> creates a version of this security descriptor in self-relative format without modifying the original. </p>
</dd>

### -param <i>SelfRelativeSecurityDescriptor</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer that receives a security descriptor in self-relative format. </p>
</dd>

### -param <i>BufferLength</i> [in, out]

<dd>
<p>Pointer to a caller-allocated variable that specifies the size, in bytes, of the buffer pointed to by the <i>SelfRelativeSecurityDescriptor</i> parameter. If the buffer is not large enough to hold the security descriptor, <b>RtlAbsoluteToSelfRelativeSD</b> returns STATUS_BUFFER_TOO_SMALL and sets this variable to the minimum required size. </p>
</dd>
</dl>

## -returns
<p><b>RtlAbsoluteToSelfRelativeSD</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following:</p><dl>
<dt><b>STATUS_BAD_DESCRIPTOR_FORMAT</b></dt>
</dl><p>The buffer pointed to by the <i>AbsoluteSecurityDescriptor</i> parameter did not contain a SECURITY_DESCRIPTOR structure in absolute format. STATUS_BAD_DESCRIPTOR_FORMAT is an error code. </p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer pointed to by the <i>SelfRelativeSecurityDescriptor</i> parameter was too small to contain the security descriptor in self-relative format. STATUS_BUFFER_TOO_SMALL is an error code. </p>

<p> </p>

## -remarks
<p>A security descriptor in absolute format contains pointers to the information it contains, rather than containing the information itself. A security descriptor in self-relative format contains the information in a contiguous block of memory. In a self-relative security descriptor, a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a> structure always starts the information, but the security descriptor's other components can follow the SECURITY_DESCRIPTOR structure in any order. Instead of using memory addresses, the components of the security descriptor are identified by offsets from the beginning of the security descriptor. This format is useful when a security descriptor must be stored on a disk or transmitted by means of a communications protocol. </p>

<p>To create a new security descriptor in absolute format by using a security descriptor in self-relative format as a template, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff553214">RtlSelfRelativeToAbsoluteSD</a>. </p>

<p>For more information about security and access control, see the Microsoft Windows SDK documentation. </p>

<p>A security descriptor in absolute format contains pointers to the information it contains, rather than containing the information itself. A security descriptor in self-relative format contains the information in a contiguous block of memory. In a self-relative security descriptor, a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a> structure always starts the information, but the security descriptor's other components can follow the SECURITY_DESCRIPTOR structure in any order. Instead of using memory addresses, the components of the security descriptor are identified by offsets from the beginning of the security descriptor. This format is useful when a security descriptor must be stored on a disk or transmitted by means of a communications protocol. </p>

<p>To create a new security descriptor in absolute format by using a security descriptor in self-relative format as a template, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff553214">RtlSelfRelativeToAbsoluteSD</a>. </p>

<p>For more information about security and access control, see the Microsoft Windows SDK documentation. </p>

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
<p>This routine is available on Microsoft Windows Server 2003 SP1 and later. </p>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538866">ACL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561827">RtlCreateSecurityDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562025">RtlLengthSecurityDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553214">RtlSelfRelativeToAbsoluteSD</a>
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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlAbsoluteToSelfRelativeSD routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
