---
UID: NF.ntifs.SeSetSecurityDescriptorInfo
title: SeSetSecurityDescriptorInfo
author: windows-driver-content
description: The SeSetSecurityDescriptorInfo routine sets an object's security descriptor.
old-location: ifsk\sesetsecuritydescriptorinfo.htm
old-project: ifsk
ms.assetid: d6f02142-1cd8-4f09-b106-d963bf080495
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SeSetSecurityDescriptorInfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SeSetSecurityDescriptorInfo
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# SeSetSecurityDescriptorInfo function



## -description
<p>The <b>SeSetSecurityDescriptorInfo</b> routine sets an object's security descriptor.</p>


## -syntax

````
NTSTATUS SeSetSecurityDescriptorInfo(
  _In_opt_ PVOID                 Object,
  _In_     PSECURITY_INFORMATION SecurityInformation,
  _In_     PSECURITY_DESCRIPTOR  SecurityDescriptor,
  _Inout_  PSECURITY_DESCRIPTOR  *ObjectsSecurityDescriptor,
  _In_     POOL_TYPE             PoolType,
  _In_     PGENERIC_MAPPING      GenericMapping
);
````


## -parameters
<dl>

### -param <i>Object</i> [in, optional]

<dd>
<p>Pointer to the object whose security descriptor is to be set. This is used to update security quota information.</p>
</dd>

### -param <i>SecurityInformation</i> [in]

<dd>
<p>Pointer to a bitmask specifying which security information is to be applied to the object. Can be a combination of one or more of the following values. </p>
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
<p>Indicates the discretionary access control list (DACL) of the object is being set. Requires WRITE_DAC access. </p>
</td>
</tr>
<tr>
<td>
<p>GROUP_SECURITY_INFORMATION</p>
</td>
<td>
<p>Indicates the primary group identifier of the object is being set. Requires WRITE_OWNER access. </p>
</td>
</tr>
<tr>
<td>
<p>OWNER_SECURITY_INFORMATION</p>
</td>
<td>
<p>Indicates the owner identifier of the object is being set. Requires WRITE_OWNER access. </p>
</td>
</tr>
<tr>
<td>
<p>SACL_SECURITY_INFORMATION</p>
</td>
<td>
<p>Indicates the system ACL (SACL) of the object is being set. Requires ACCESS_SYSTEM_SECURITY access. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>SecurityDescriptor</i> [in]

<dd>
<p>The input security descriptor to be applied to the object. The caller of this routine is expected to probe and capture the passed security descriptor before calling <b>SeSetSecurityDescriptorInfo</b>, and to release it afterward.</p>
</dd>

### -param <i>ObjectsSecurityDescriptor</i> [in, out]

<dd>
<p>Pointer to a pointer to the object's security descriptor. The security descriptor must be in self-relative format. The caller is responsible for freeing this structure when it is no longer needed.</p>
</dd>

### -param <i>PoolType</i> [in]

<dd>
<p>Specifies the pool type to use when allocating a new security descriptor, which can be one of the following: </p>
<ul>
<li><b>NonPagedPool</b></li>
<li><b>PagedPool</b></li>
<li><b>NonPagedPoolCacheAligned</b></li>
<li><b>PagedPoolCacheAligned</b></li>
</ul>
<p>Usually, a caller specifies <b>PagedPool</b>, or else <b>NonPagedPool</b> if the buffer will be accessed at IRQL &gt;= DISPATCH_LEVEL or in an arbitrary thread context. </p>
<div class="alert"><b>Note</b>    The <b>NonPagedPoolMustSucceed</b> and <b>NonPagedPoolCacheAlignedMustS</b> pool types are obsolete and should no longer be used. </div>
<div> </div>
</dd>

### -param <i>GenericMapping</i> [in]

<dd>
<p>Pointer to a GENERIC_MAPPING structure that specifies the mapping of generic to specific and standard access types for the object being accessed. This mapping structure is expected to be safe to access (that is, captured if necessary) prior to be passed to this routine.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The object's security descriptor was successfully modified.</p><dl>
<dt><b>STATUS_BAD_DESCRIPTOR_FORMAT</b></dt>
</dl><p>The provided object's security descriptor was not in self-relative format.</p><dl>
<dt><b>STATUS_NO_SECURITY_ON_OBJECT</b></dt>
</dl><p>The object does not have a security descriptor.</p>

<p> </p>

## -remarks
<p><b>SeSetSecurityDescriptorInfo</b> modifies an object's existing security descriptor. If the object does not have a security descriptor, the call to <b>SeSetSecurityDescriptorInfo</b> will fail.</p>

<p>To specify whether the object supports automatic inheritance of access control entries (ACE), use <b>SeSetSecurityDescriptorInfoEx</b>.</p>

<p>A security descriptor can be in absolute or self-relative form. In self-relative form, all members of the structure are located contiguously in memory. In absolute form, the structure only contains pointers to the members.</p>

<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK.</p>

<p><b>SeSetSecurityDescriptorInfo</b> modifies an object's existing security descriptor. If the object does not have a security descriptor, the call to <b>SeSetSecurityDescriptorInfo</b> will fail.</p>

<p>To specify whether the object supports automatic inheritance of access control entries (ACE), use <b>SeSetSecurityDescriptorInfoEx</b>.</p>

<p>A security descriptor can be in absolute or self-relative form. In self-relative form, all members of the structure are located contiguously in memory. In absolute form, the structure only contains pointers to the members.</p>

<p>For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK.</p>

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
<p>PASSIVE_LEVEL</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546526">GENERIC_MAPPING</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556635">SECURITY_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556692">SeQuerySecurityDescriptorInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556707">SeSetAccessStateGenericMapping</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556712">SeSetSecurityDescriptorInfoEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SeSetSecurityDescriptorInfo routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
