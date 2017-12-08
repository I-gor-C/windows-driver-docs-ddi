---
UID: NF.ntifs.RtlSetGroupSecurityDescriptor
title: RtlSetGroupSecurityDescriptor function
author: windows-driver-content
description: The RtlSetGroupSecurityDescriptor routine sets the primary group information of an absolute-format security descriptor. It replaces any primary group information that is already present in the security descriptor.
old-location: ifsk\rtlsetgroupsecuritydescriptor.htm
old-project: ifsk
ms.assetid: f0473975-7ab6-46ba-bdb7-eb227e6bc258
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlSetGroupSecurityDescriptor
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
req.alt-api: RtlSetGroupSecurityDescriptor
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
---

# RtlSetGroupSecurityDescriptor function



## -description
The <b>RtlSetGroupSecurityDescriptor</b> routine sets the primary group information of an absolute-format security descriptor. It replaces any primary group information that is already present in the security descriptor. 


## -syntax

````
NTSTATUS RtlSetGroupSecurityDescriptor(
  _Inout_  PSECURITY_DESCRIPTOR SecurityDescriptor,
  _In_opt_ PSID                 Group,
  _In_opt_ BOOLEAN              GroupDefaulted
);
````


## -parameters

### -param SecurityDescriptor [in, out]

Pointer to the <a href="ifsk.security_descriptor">SECURITY_DESCRIPTOR</a> structure whose primary group is to be set. <b>RtlSetGroupSecurityDescriptor</b> replaces any existing primary group with the new primary group. 

### -param Group [in, optional]

Pointer to a security identifier (<a href="ifsk.sid">SID</a>) structure for the security descriptor's new primary owner. This pointer, not the SID structure itself, is copied into the security descriptor. If <i>Group</i> is <b>NULL</b>, <b>RtlSetGroupSecurityDescriptor</b> clears the security descriptor's primary group information. This marks the security descriptor as having no primary group. 

### -param GroupDefaulted [in, optional]

Set this Boolean variable to <b>TRUE</b> if the primary group information is derived from a default mechanism. If this parameter is <b>TRUE</b>, <b>RtlSetGroupSecurityDescriptor</b> sets the SE_GROUP_DEFAULTED flag in the security descriptor's SECURITY_DESCRIPTOR_CONTROL field. If this parameter is <b>FALSE</b>, <b>RtlSetGroupSecurityDescriptor</b> clears the SE_GROUP_DEFAULTED flag. 

## -returns
<b>RtlSetGroupSecurityDescriptor</b> returns STATUS_SUCCESS if the primary group was successfully set or reset. Otherwise, it returns an appropriate NTSTATUS value such as one of the following:
<dl>
<dt><b>STATUS_INVALID_SECURITY_DESCR</b></dt>
</dl>The given security descriptor is not a valid absolute security descriptor. STATUS_INVALID_SECURITY_DESCR is an error code. 
<dl>
<dt><b>STATUS_UNKNOWN_REVISION</b></dt>
</dl>The given security descriptor's revision is not recognized by this routine. STATUS_UNKNOWN_REVISION is an error code. 

 

## -remarks
To retrieve the primary group information for a security descriptor, use <a href="ifsk.rtlgetgroupsecuritydescriptor">RtlGetGroupSecurityDescriptor</a>. 

To set the owner information for a security descriptor, use <a href="ifsk.rtlsetownersecuritydescriptor">RtlSetOwnerSecurityDescriptor</a>. 

For more information about security and access control, see the Microsoft Windows SDK documentation. 

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
This routine is available on Microsoft Windows Server 2003 SP1 and later. 
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
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
IRQL
</th>
<td width="70%">
&lt;= APC_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.rtlgetgroupsecuritydescriptor">RtlGetGroupSecurityDescriptor</a>
</dt>
<dt>
<a href="ifsk.rtlsetownersecuritydescriptor">RtlSetOwnerSecurityDescriptor</a>
</dt>
<dt>
<a href="ifsk.security_descriptor">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="ifsk.security_descriptor_control">SECURITY_DESCRIPTOR_CONTROL</a>
</dt>
<dt>
<a href="ifsk.sid">SID</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlSetGroupSecurityDescriptor routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
