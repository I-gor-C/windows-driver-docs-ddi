---
UID: NF.ntifs.RtlAddAccessAllowedAceEx
title: RtlAddAccessAllowedAceEx
author: windows-driver-content
description: The RtlAddAccessAllowedAceEx routine adds an access-allowed access control entry (ACE) with inheritance ACE flags to an access control list (ACL). The access is granted to the specified security identifier (SID).
old-location: ifsk\rtladdaccessallowedaceex.htm
ms.assetid: aeef74d8-d4a5-4ce4-b7f8-e2a2d263a678
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available in Microsoft Windows 2000 and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlAddAccessAllowedAceEx
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
req.irql: <= APC_LEVEL
ms.keywords: RtlAddAccessAllowedAceEx
req.iface: 
---

# RtlAddAccessAllowedAceEx function



## -description
<p>The <b>RtlAddAccessAllowedAceEx</b> routine adds an access-allowed access control entry (<a href="https://msdn.microsoft.com/library/windows/hardware/ff538844">ACE</a>) with inheritance ACE flags to an access control list (<a href="https://msdn.microsoft.com/library/windows/hardware/ff538866">ACL</a>). The access is granted to the specified security identifier (<a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a>). </p>


## -syntax

````
NTSTATUS RtlAddAccessAllowedAceEx(
  _Inout_ PACL        Acl,
  _In_    ULONG       AceRevision,
  _In_    ULONG       AceFlags,
  _In_    ACCESS_MASK AccessMask,
  _In_    PSID        Sid
);
````


## -parameters
<dl>

### -param <i>Acl</i> [in, out]

<dd>
<p>A pointer to a caller-allocated buffer that contains the ACL to be modified. <b>RtlAddAccessAllowedAceEx</b> adds an access-allowed ACE to the end of this ACL. The ACE is in the form of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff538796">ACCESS_ALLOWED_ACE</a> structure.</p>
</dd>

### -param <i>AceRevision</i> [in]

<dd>
<p>ACL revision level of the ACE to be added. This value can be ACL_REVISION or ACL_REVISION_DS. It must be ACL_REVISION_DS if the ACL contains an object-specific ACE. </p>
</dd>

### -param <i>AceFlags</i> [in]

<dd>
<p>Bitmask specifying the inherit flags of the ACE to be added. </p>
</dd>

### -param <i>AccessMask</i> [in]

<dd>
<p>A bitmask of one or more <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> flags that specify the access rights to be granted to the specified SID. For more information, see the description of the <i>DesiredAccess</i> parameter of <a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a>. </p>
</dd>

### -param <i>Sid</i> [in]

<dd>
<p>A pointer to the SID structure that represents a user, group, or logon account that is being granted access. </p>
</dd>
</dl>

## -returns
<p><b>RtlAddAccessAllowedAceEx</b> can return one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The ACE was successfully added.</p><dl>
<dt><b>STATUS_ALLOTTED_SPACE_EXCEEDED</b></dt>
</dl><p>A new ACE does not fit into the ACL. A larger ACL buffer is required. For more information about how to calculate the size of an ACL, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552151">RtlCreateAcl</a>. </p><dl>
<dt><b>STATUS_INVALID_ACL</b></dt>
</dl><p>The specified ACL is not correctly formed.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The AceFlags parameter was invalid.</p><dl>
<dt><b>STATUS_INVALID_SID</b></dt>
</dl><p>The specified SID structure is not structurally valid.</p><dl>
<dt><b>STATUS_REVISION_MISMATCH</b></dt>
</dl><p>The specified <i>AceRevision</i> is not known or is not compatible with that of the ACL. </p>

<p> </p>

## -remarks
<p>Unlike <a href="https://msdn.microsoft.com/library/windows/hardware/ff552092">RtlAddAccessAllowedAce</a>, this routine sets the inheritance ACE flags.  </p>

<p>For more information about security and access control, see the documentation about these topics in the Microsoft Windows SDK, such as:</p>

<p><a href="http://go.microsoft.com/fwlink/p/?linkid=140858">Access Control Lists</a></p>

<p><a href="http://go.microsoft.com/fwlink/p/?linkid=140859">Creating or Modifying an ACL</a></p>

<p><a href="http://go.microsoft.com/fwlink/p/?linkid=140860">Getting Information from an ACL</a></p>

<p>Unlike <a href="https://msdn.microsoft.com/library/windows/hardware/ff552092">RtlAddAccessAllowedAce</a>, this routine sets the inheritance ACE flags.  </p>

<p>For more information about security and access control, see the documentation about these topics in the Microsoft Windows SDK, such as:</p>

<p><a href="http://go.microsoft.com/fwlink/p/?linkid=140858">Access Control Lists</a></p>

<p><a href="http://go.microsoft.com/fwlink/p/?linkid=140859">Creating or Modifying an ACL</a></p>

<p><a href="http://go.microsoft.com/fwlink/p/?linkid=140860">Getting Information from an ACL</a></p>

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
<p>This routine is available in Microsoft Windows 2000 and later Windows operating systems. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or FltKernel.h)</dt>
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
<p>&lt;= APC_LEVEL</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlAddAccessAllowedAceEx routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
