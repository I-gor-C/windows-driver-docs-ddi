---
UID: NF.ntifs.NtQuerySecurityObject
title: NtQuerySecurityObject
author: windows-driver-content
description: The ZwQuerySecurityObject routine retrieves a copy of an object's security descriptor.
old-location: kernel\zwquerysecurityobject.htm
old-project: kernel
ms.assetid: bc3c494d-890c-4699-a272-62cbcc234cdd
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NtQuerySecurityObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwQuerySecurityObject,NtQuerySecurityObject
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NtQuerySecurityObject function



## -description
<p>The <b>ZwQuerySecurityObject</b> routine retrieves a copy of an object's security descriptor. </p>


## -syntax

````
NTSTATUS ZwQuerySecurityObject(
  _In_  HANDLE               Handle,
  _In_  SECURITY_INFORMATION SecurityInformation,
  _Out_ PSECURITY_DESCRIPTOR SecurityDescriptor,
  _In_  ULONG                Length,
  _Out_ PULONG               LengthNeeded
);
````


## -parameters
<dl>

### -param Handle [in]

<dd>
<p>Handle for the object whose security descriptor is to be queried. This handle must have the access specified in the Meaning column of the table shown in the description of the <i>SecurityInformation</i> parameter. </p>
</dd>

### -param SecurityInformation [in]

<dd>
<p>Pointer to a <a href="ifsk.security_information">SECURITY_INFORMATION</a> value specifying the information to be queried.</p>
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

### -param SecurityDescriptor [out]

<dd>
<p>Caller-allocated buffer that <b>ZwQuerySecurityObject</b> fills with a copy of the specified security descriptor. The <a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a> structure is returned in self-relative format. </p>
</dd>

### -param Length [in]

<dd>
<p>Size, in bytes, of the buffer pointed to by <i>SecurityDescriptor</i>. </p>
</dd>

### -param LengthNeeded [out]

<dd>
<p>Pointer to a caller-allocated variable that receives the number of bytes required to store the copied security descriptor. </p>
</dd>
</dl>

## -returns
<p><b>ZwQuerySecurityObject</b> returns STATUS_SUCCESS or an appropriate error status. Possible error status codes include the following:</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p><i>Handle</i> did not have the required access. </p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer is too small for the security descriptor. None of the security information was copied to the buffer. </p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p><i>Handle</i> was not a valid handle. </p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p><i>Handle</i> was not a handle of the expected type. </p>

<p> </p>

## -remarks
<p>A security descriptor can be in absolute or self-relative form. In self-relative form, all members of the structure are located contiguously in memory. In absolute form, the structure only contains pointers to the members. </p>

<p>The NTFS file system imposes a 64K limit on the size of the security descriptor that is written to disk for a file. (The FAT file system does not support security descriptors for files.) Thus a 64K <i>SecurityDescriptor</i> buffer is guaranteed to be large enough to hold the returned <b>SECURITY_DESCRIPTOR</b> structure. </p>

<p>For more information about security and access control, see the documentation on these topics in the Windows SDK.</p>

<p>Minifilters should call <a href="..\fltkernel\nf-fltkernel-fltquerysecurityobject.md">FltQuerySecurityObject</a> instead of <b>ZwQuerySecurityObject</b>. </p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

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
<p>Available in Windows XP and later versions of Windows.</p>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltquerysecurityobject.md">FltQuerySecurityObject</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="ifsk.security_information">SECURITY_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwsetsecurityobject.md">ZwSetSecurityObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwQuerySecurityObject routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
