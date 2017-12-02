---
UID: NF.ntifs.RtlGetGroupSecurityDescriptor
title: RtlGetGroupSecurityDescriptor
author: windows-driver-content
description: The RtlGetGroupSecurityDescriptor routine returns the primary group information for a given security descriptor.
old-location: ifsk\rtlgetgroupsecuritydescriptor.htm
old-project: ifsk
ms.assetid: a2fbb125-42cf-4c33-83bb-3fc875712be3
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlGetGroupSecurityDescriptor
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
req.alt-api: RtlGetGroupSecurityDescriptor
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

# RtlGetGroupSecurityDescriptor function



## -description
<p>The <b>RtlGetGroupSecurityDescriptor</b> routine returns the primary group information for a given security descriptor.</p>


## -syntax

````
NTSTATUS RtlGetGroupSecurityDescriptor(
  _In_  PSECURITY_DESCRIPTOR SecurityDescriptor,
  _Out_ PSID                 *Group,
  _Out_ PBOOLEAN             GroupDefaulted
);
````


## -parameters
<dl>

### -param SecurityDescriptor [in]

<dd>
<p>Pointer to the security descriptor whose primary group information is to be returned.</p>
</dd>

### -param Group [out]

<dd>
<p>Pointer to a variable that receives a pointer to the security identifier (<a href="ifsk.sid">SID</a>) for the primary group. If the security descriptor does not contain a primary group, <i>*Group</i> receives <b>NULL</b>.</p>
</dd>

### -param GroupDefaulted [out]

<dd>
<p>Pointer to a Boolean variable that receives the value of the SE_GROUP_DEFAULTED flag in the security descriptor's SECURITY_DESCRIPTOR_CONTROL structure. This value is valid only if <i>*Group</i> receives a non-<b>NULL</b> value.</p>
</dd>
</dl>

## -returns
<p><b>RtlGetGroupSecurityDescriptor</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following:</p><dl>
<dt><b>STATUS_UNKNOWN_REVISION</b></dt>
</dl><p>The security descriptor's revision level is not known or is not supported. This is an error code. </p>

<p> </p>

## -remarks
<p>If the security descriptor pointed to by <i>SecurityDescriptor</i> contains a primary group, <b>RtlGetGroupSecurityDescriptor</b> sets the pointer pointed to by <i>Group</i> to the address of the security descriptor's group SID and sets the variable pointed to by <i>GroupDefaulted</i> to a valid value. </p>

<p>If the security descriptor pointed to by <i>SecurityDescriptor</i> does not contain a primary group, <b>RtlGetGroupSecurityDescriptor</b> sets the pointer pointed to by <i>Group</i> to <b>NULL</b> and ignores the remaining output parameter, <i>GroupDefaulted</i>. </p>

<p>To set the primary group information for a security descriptor, use <a href="..\ntifs\nf-ntifs-rtlsetgroupsecuritydescriptor.md">RtlSetGroupSecurityDescriptor</a>. </p>

<p>To retrieve the owner information for a security descriptor, use <a href="..\ntifs\nf-ntifs-rtlgetownersecuritydescriptor.md">RtlGetOwnerSecurityDescriptor</a>. </p>

<p>For more information about security and access control, see the Microsoft Windows SDK documentation.</p>

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
<a href="..\ntifs\nf-ntifs-rtlgetownersecuritydescriptor.md">RtlGetOwnerSecurityDescriptor</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtlsetgroupsecuritydescriptor.md">RtlSetGroupSecurityDescriptor</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="ifsk.sid">SID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlGetGroupSecurityDescriptor routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
