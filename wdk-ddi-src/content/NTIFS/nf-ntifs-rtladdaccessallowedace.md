---
UID: NF.ntifs.RtlAddAccessAllowedAce
title: RtlAddAccessAllowedAce
author: windows-driver-content
description: The RtlAddAccessAllowedAce routine adds an access-allowed access control entry (ACE) to an access control list (ACL). The access is granted to the specified security identifier (SID).
old-location: ifsk\rtladdaccessallowedace.htm
ms.assetid: 39a50efc-b27a-4c73-b436-c6495256d9c6
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
req.alt-api: RtlAddAccessAllowedAce
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
req.irql: < DISPATCH_LEVEL
ms.keywords: RtlAddAccessAllowedAce
req.iface: 
---

# RtlAddAccessAllowedAce function



## -description
<p>The <b>RtlAddAccessAllowedAce</b> routine adds an access-allowed access control entry (ACE) to an access control list (ACL). The access is granted to the specified security identifier (SID). </p>


## -syntax

````
NTSTATUS RtlAddAccessAllowedAce(
  _Inout_ PACL        Acl,
  _In_    ULONG       AceRevision,
  _In_    ACCESS_MASK AccessMask,
  _In_    PSID        Sid
);
````


## -parameters
<dl>

### -param <i>Acl</i> [in, out]

<dd>
<p>Pointer to a caller-allocated buffer containing the ACL to be modified. <b>RtlAddAccessAllowedAce</b> adds an access-allowed ACE to the end of this ACL. The ACE is in the form of an ACCESS_ALLOWED_ACE structure.</p>
</dd>

### -param <i>AceRevision</i> [in]

<dd>
<p>ACL revision level of the ACE to be added. Windows version requirments are the following:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -param ACL_REVISION

</dl>
</td>
<td width="60%">
<p>The revision level valid on all Windows versions.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -param ACL_REVISION_DS

</dl>
</td>
<td width="60%">
<p>The revision level valid starting with Windows 2000.</p>
<div class="alert"><b>Note</b>  <i>AceRevision</i> must be ACL_REVISION_DS if the ACL in <i>Acl</i> contains an object-specific ACE.</div>
<div> </div>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>AccessMask</i> [in]

<dd>
<p>Bitmask of one or more <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> flags specifying the access rights to be granted to the specified SID. For more information, see the description of the <i>DesiredAccess</i> parameter of <b>ZwCreateFile</b>. </p>
</dd>

### -param <i>Sid</i> [in]

<dd>
<p>Pointer to the SID structure representing a user, group, or logon account that is being granted access. </p>
</dd>
</dl>

## -returns
<p><b>RtlAddAccessAllowedAce</b> can return one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The ACE was successfully added.</p><dl>
<dt><b>STATUS_ALLOTTED_SPACE_EXCEEDED</b></dt>
</dl><p>A new ACE does not fit into the ACL. A larger ACL buffer is required. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff552151">RtlCreateAcl</a> for information about calculating the size of an ACL. </p><dl>
<dt><b>STATUS_INVALID_ACL</b></dt>
</dl><p>The specified ACL is not properly formed.</p><dl>
<dt><b>STATUS_INVALID_SID</b></dt>
</dl><p>The specified SID structure is not structurally valid.</p><dl>
<dt><b>STATUS_REVISION_MISMATCH</b></dt>
</dl><p>The specified revision is not known or is not compatible with that of the ACL. </p>

<p> </p>

## -remarks
<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0.</p>

<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0.</p>

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
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538796">ACCESS_ALLOWED_ACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538844">ACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538866">ACL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552151">RtlCreateAcl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561827">RtlCreateSecurityDescriptor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552165">RtlCreateSecurityDescriptorRelative</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563676">SeAssignSecurity</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlAddAccessAllowedAce routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
