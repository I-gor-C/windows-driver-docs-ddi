---
UID: NF.ntifs.RtlAddAce
title: RtlAddAce
author: windows-driver-content
description: The RtlAddAce routine adds one or more access control entries (ACEs) to a specified access control list (ACL).
old-location: ifsk\rtladdace.htm
old-project: ifsk
ms.assetid: 291b1fa9-5f42-49b6-b6de-20054a832bb2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlAddAce
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available starting with Windows Server 2003 with SP1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlAddAce
req.alt-loc: NtosKrnl.exe,Ntdll.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode); Ntdll.dll (user mode)
req.irql: <= APC_LEVEL
req.iface: 
---

# RtlAddAce function



## -description
<p>The <b>RtlAddAce</b> routine adds one or more access control entries (ACEs) to a specified access control list (ACL).</p>


## -syntax

````
NTSTATUS RtlAddAce(
  _Inout_ PACL  Acl,
  _In_    ULONG AceRevision,
  _In_    ULONG StartingAceIndex,
  _In_    PVOID AceList,
  _In_    ULONG AceListLength
);
````


## -parameters
<dl>

### -param Acl [in, out]

<dd>
<p>Pointer to the ACL to be modified. <b>RtlAddAce</b> adds the specified ACEs to this ACL. </p>
</dd>

### -param AceRevision [in]

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

### -param StartingAceIndex [in]

<dd>
<p>Specifies the position in the ACL's list of ACEs at which to add new ACEs. A value of zero inserts the ACEs at the beginning of the list. A value of MAXULONG appends the ACEs to the end of the list.</p>
</dd>

### -param AceList [in]

<dd>
<p>Pointer to a buffer containing a list of one or more ACEs to be added to the specified ACL. The ACEs in the list must be stored contiguously.</p>
</dd>

### -param AceListLength [in]

<dd>
<p>Size, in bytes, of the input buffer pointed to by the <i>AceList</i> parameter. </p>
</dd>
</dl>

## -returns
<p><b>RtlAddAce</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following:</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The new ACEs do not fit into the ACL. A larger ACL buffer is required. STATUS_BUFFER_TOO_SMALL is an error code. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One of the parameter values was invalid. Possible reasons include: </p>

<p>The specified ACL is invalid.</p>

<p>The specified revision is unknown, is not compatible with revisions in the ACE list, or is not compatible with the revision of the ACL. </p>

<p>STATUS_INVALID_PARAMETER is an error code. </p>

<p> </p>

## -remarks
<p>For information about calculating the size of an ACL, see the Remarks section of the reference entry for <a href="..\ntifs\nf-ntifs-rtlcreateacl.md">RtlCreateAcl</a>. </p>

<p>To obtain a pointer to an ACE in an ACL, use <a href="..\ntifs\nf-ntifs-rtlgetace.md">RtlGetAce</a>. </p>

<p>To delete an ACE from an ACL, use <a href="..\ntifs\nf-ntifs-rtldeleteace.md">RtlDeleteAce</a>. </p>

<p>To add an access-allowed ACE to an ACL, use <a href="..\ntifs\nf-ntifs-rtladdaccessallowedace.md">RtlAddAccessAllowedAce</a>. </p>

<p>For more information about security and access control, see the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0 documentation.</p>

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
<p>This routine is available starting with Windows Server 2003 with SP1. </p>
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
<a href="ifsk.ace">ACE</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--acl.md">ACL</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtladdaccessallowedace.md">RtlAddAccessAllowedAce</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtlcreateacl.md">RtlCreateAcl</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtldeleteace.md">RtlDeleteAce</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtlgetace.md">RtlGetAce</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlAddAce routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
