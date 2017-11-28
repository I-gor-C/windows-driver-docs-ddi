---
UID: NF.ntifs.RtlDeleteAce
title: RtlDeleteAce
author: windows-driver-content
description: The RtlDeleteAce routine deletes an access control entry (ACE) from a specified access control list (ACL).
old-location: ifsk\rtldeleteace.htm
old-project: ifsk
ms.assetid: 2bf90d1d-887f-4d0c-8d79-e102a14dfe71
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlDeleteAce
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows Server 2003 SP1 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlDeleteAce
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
req.iface: 
---

# RtlDeleteAce function



## -description
<p>The <b>RtlDeleteAce</b> routine deletes an access control entry (ACE) from a specified access control list (ACL).</p>


## -syntax

````
NTSTATUS RtlDeleteAce(
  _Inout_ PACL  Acl,
  _In_    ULONG AceIndex
);
````


## -parameters
<dl>

### -param <i>Acl</i> [in, out]

<dd>
<p>Pointer to the ACL to be modified. <b>RtlDeleteAce</b> deletes the specified ACE from this ACL. </p>
</dd>

### -param <i>AceIndex</i> [in]

<dd>
<p>Specifies the ACE to delete. A value of zero corresponds to the first ACE in the ACL, 1 to the second ACE, and so on.</p>
</dd>
</dl>

## -returns
<p><b>RtlDeleteAce</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One of the parameter values was invalid. Possible reasons include: </p>

<p>The specified ACL is invalid.</p>

<p>The specified index value is out of range. </p>

<p>STATUS_INVALID_PARAMETER is an error code. </p>

<p> </p>

## -remarks
<p>For information about calculating the size of an ACL, see the Remarks section of the reference entry for <a href="https://msdn.microsoft.com/library/windows/hardware/ff552151">RtlCreateAcl</a>. </p>

<p>To add an ACE to an ACL, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff552101">RtlAddAce</a>. </p>

<p>To obtain a pointer to an ACE in an ACL, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff552288">RtlGetAce</a>. </p>

<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK. </p>

<p>For information about calculating the size of an ACL, see the Remarks section of the reference entry for <a href="https://msdn.microsoft.com/library/windows/hardware/ff552151">RtlCreateAcl</a>. </p>

<p>To add an ACE to an ACL, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff552101">RtlAddAce</a>. </p>

<p>To obtain a pointer to an ACE in an ACL, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff552288">RtlGetAce</a>. </p>

<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538844">ACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538866">ACL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552101">RtlAddAce</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552151">RtlCreateAcl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552288">RtlGetAce</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlDeleteAce routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
