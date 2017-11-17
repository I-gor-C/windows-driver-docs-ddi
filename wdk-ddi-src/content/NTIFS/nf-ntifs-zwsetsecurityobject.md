---
UID: NF.ntifs.ZwSetSecurityObject
title: ZwSetSecurityObject
author: windows-driver-content
description: The ZwSetSecurityObject routine sets an object's security state.
old-location: kernel\zwsetsecurityobject.htm
ms.assetid: fbf6291e-9602-45d7-a620-702491a1d7de
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwSetSecurityObject,NtSetSecurityObject
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
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: ZwSetSecurityObject
req.iface: 
---

# ZwSetSecurityObject function



## -description
<p>The <b>ZwSetSecurityObject</b> routine sets an object's security state.</p>


## -syntax

````
NTSTATUS ZwSetSecurityObject(
  _In_ HANDLE               Handle,
  _In_ SECURITY_INFORMATION SecurityInformation,
  _In_ PSECURITY_DESCRIPTOR SecurityDescriptor
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>Handle for the object whose security state is to be set. This handle must have the access specified in the Meaning column of the table shown in the description of the <i>SecurityInformation</i> parameter.</p>
</dd>

### -param <i>SecurityInformation</i> [in]

<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556635">SECURITY_INFORMATION</a> value specifying the information to be set. Can be a combination of one or more of the following. </p>
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
<p>Indicates the discretionary access control list (DACL) of the object is to be set. Requires WRITE_DAC access.</p>
</td>
</tr>
<tr>
<td>
<p>GROUP_SECURITY_INFORMATION</p>
</td>
<td>
<p>Indicates the primary group identifier of the object is to be set. Requires WRITE_OWNER access.</p>
</td>
</tr>
<tr>
<td>
<p>OWNER_SECURITY_INFORMATION</p>
</td>
<td>
<p>Indicates the owner identifier of the object is to be set. Requires WRITE_OWNER access.</p>
</td>
</tr>
<tr>
<td>
<p>SACL_SECURITY_INFORMATION</p>
</td>
<td>
<p>Indicates the system ACL (SACL) of the object is to be set. Requires ACCESS_SYSTEM_SECURITY access.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>SecurityDescriptor</i> [in]

<dd>
<p>Pointer to the security descriptor to be set for the object.</p>
</dd>
</dl>

## -returns
<p><b>ZwSetSecurityObject</b> returns STATUS_SUCCESS or an appropriate error status. Possible error status codes include the following:</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p><i>Handle</i> does not have the required access rights.</p><dl>
<dt><b>STATUS_ACCESS_VIOLATION</b></dt>
</dl><p><i>SecurityDescriptor</i> is a <b>NULL</b> pointer.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The object's security descriptor could not be captured.</p><dl>
<dt><b>STATUS_INVALID_ACL</b></dt>
</dl><p>The object's security descriptor contains an invalid ACL.</p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p><i>Handle</i> is not a valid handle.</p><dl>
<dt><b>STATUS_INVALID_SECURITY_DESCR</b></dt>
</dl><p><i>SecurityDescriptor</i> does not point to a valid security descriptor.</p><dl>
<dt><b>STATUS_INVALID_SID</b></dt>
</dl><p>The object's security descriptor contains an invalid <b>SID</b>.</p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p><i>Handle</i> is not a handle of the expected type.</p><dl>
<dt><b>STATUS_UNKNOWN_REVISION</b></dt>
</dl><p>The revision level of the object's security descriptor is unknown or is not supported.</p>

<p> </p>

## -remarks
<p>A security descriptor can be in absolute or self-relative form. In self-relative form, all members of the structure are located contiguously in memory. In absolute form, the structure only contains pointers to the members. For more information, see "Absolute and Self-Relative Security Descriptors" in the Security section of the Windows SDK documentation.</p>

<p>For more information about security and access control, see the documentation on these topics in the Windows SDK.</p>

<p>Minifilters should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff544538">FltSetSecurityObject</a> instead of <b>ZwSetSecurityObject</b>. </p>

<p>Callers of <b>ZwSetSecurityObject</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p>A security descriptor can be in absolute or self-relative form. In self-relative form, all members of the structure are located contiguously in memory. In absolute form, the structure only contains pointers to the members. For more information, see "Absolute and Self-Relative Security Descriptors" in the Security section of the Windows SDK documentation.</p>

<p>For more information about security and access control, see the documentation on these topics in the Windows SDK.</p>

<p>Minifilters should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff544538">FltSetSecurityObject</a> instead of <b>ZwSetSecurityObject</b>. </p>

<p>Callers of <b>ZwSetSecurityObject</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

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
<p>Available starting with Windows XP.</p>
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
<p>PASSIVE_LEVEL (see Remarks section)</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544538">FltSetSecurityObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556635">SECURITY_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567066">ZwQuerySecurityObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwSetSecurityObject routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
