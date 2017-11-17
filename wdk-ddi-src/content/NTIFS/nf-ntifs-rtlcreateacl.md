---
UID: NF.ntifs.RtlCreateAcl
title: RtlCreateAcl
author: windows-driver-content
description: The RtlCreateAcl routine creates and initializes an access control list (ACL).
old-location: ifsk\rtlcreateacl.htm
ms.assetid: d7bf1fa0-81e0-4b44-adcd-d8f629453ac8
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
req.alt-api: RtlCreateAcl
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
ms.keywords: RtlCreateAcl
req.iface: 
---

# RtlCreateAcl function



## -description
<p>The <b>RtlCreateAcl</b> routine creates and initializes an access control list (ACL). </p>


## -syntax

````
NTSTATUS RtlCreateAcl(
  _Out_ PACL  Acl,
  _In_  ULONG AclLength,
  _In_  ULONG AceRevision
);
````


## -parameters
<dl>

### -param <i>Acl</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer to receive the initialized ACL structure. This buffer must be at least <b>sizeof</b>(ACL),</p>
</dd>

### -param <i>AclLength</i> [in]

<dd>
<p>Length, in bytes, of the buffer pointed to by the <i>Acl</i> parameter. This value must be large enough to contain the ACL header and all of the access-control entries (ACE) to be stored in the ACL. See the following Remarks section for information about calculating the size of an ACL. </p>
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
<div class="alert"><b>Note</b>  <i>AceRevision</i> must be ACL_REVISION_DS if the ACL in <i>Acl</i> contains an object-specific ACE.</div>
<div> </div>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>RtlCreateAcl</b> can return one of the following status values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The ACL was successfully created and initialized.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The new ACL does not fit into the buffer at <i>Acl</i>. A larger ACL buffer is required. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The specified revision is not current, or the value of <i>AclLength</i> is too large. </p>

<p> </p>

## -remarks
<p>The ACL that is initialized by <b>RtlCreateAcl</b> contains no access control entries (ACE). This ACL is empty, as opposed to being a nonexistent ACL. If an empty ACL is applied to an object, the ACL implicitly denies all access to that object. To add ACEs to the ACL, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff552092">RtlAddAccessAllowedAce</a>.</p>

<p>To calculate the size of an ACL, add <b>sizeof</b>(ACL) to the size of all the ACEs to be stored in the ACL. To calculate the size of an ACE, add the size of the ACE structure, such as <b>sizeof</b>(ACCESS_ALLOWED_ACE), to the length of the SID associated with the ACE, and then subtract the size of the <b>SidStart</b> member (which is part of both the ACE structure and the SID). Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553085">RtlLengthSid</a> function to get the length of a specified SID.</p>

<p>The following example shows how to calculate the size of an access-allowed ACE:</p>

<p>To calculate the size of an ACL, use the following algorithm, substituting the appropriate ACE structure in the <b>sizeof</b>(ACE) expression:</p>

<p>For more information about security and access control, see the documentation on these topics in thePlatform Software Development Kit (SDK).</p>

<p>The ACL that is initialized by <b>RtlCreateAcl</b> contains no access control entries (ACE). This ACL is empty, as opposed to being a nonexistent ACL. If an empty ACL is applied to an object, the ACL implicitly denies all access to that object. To add ACEs to the ACL, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff552092">RtlAddAccessAllowedAce</a>.</p>

<p>To calculate the size of an ACL, add <b>sizeof</b>(ACL) to the size of all the ACEs to be stored in the ACL. To calculate the size of an ACE, add the size of the ACE structure, such as <b>sizeof</b>(ACCESS_ALLOWED_ACE), to the length of the SID associated with the ACE, and then subtract the size of the <b>SidStart</b> member (which is part of both the ACE structure and the SID). Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553085">RtlLengthSid</a> function to get the length of a specified SID.</p>

<p>The following example shows how to calculate the size of an access-allowed ACE:</p>

<p>To calculate the size of an ACL, use the following algorithm, substituting the appropriate ACE structure in the <b>sizeof</b>(ACE) expression:</p>

<p>For more information about security and access control, see the documentation on these topics in thePlatform Software Development Kit (SDK).</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538844">ACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538866">ACL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552092">RtlAddAccessAllowedAce</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553085">RtlLengthSid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlCreateAcl routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
