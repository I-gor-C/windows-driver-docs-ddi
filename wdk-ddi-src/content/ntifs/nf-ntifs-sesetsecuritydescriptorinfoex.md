---
UID: NF.ntifs.SeSetSecurityDescriptorInfoEx
title: SeSetSecurityDescriptorInfoEx
author: windows-driver-content
description: The SeSetSecurityDescriptorInfoEx routine modifies an object's security descriptor and specifies whether the object supports automatic inheritance of access control entries (ACE).
old-location: ifsk\sesetsecuritydescriptorinfoex.htm
old-project: ifsk
ms.assetid: 90526705-069d-432f-87b1-1efc247aee05
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: SeSetSecurityDescriptorInfoEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SeSetSecurityDescriptorInfoEx
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

# SeSetSecurityDescriptorInfoEx function



## -description
<p>The <b>SeSetSecurityDescriptorInfoEx</b> routine modifies an object's security descriptor and specifies whether the object supports automatic inheritance of access control entries (ACE).</p>


## -syntax

````
NTSTATUS SeSetSecurityDescriptorInfoEx(
  _In_opt_ PVOID                 Object,
  _In_     PSECURITY_INFORMATION SecurityInformation,
  _In_     PSECURITY_DESCRIPTOR  SecurityDescriptor,
  _Inout_  PSECURITY_DESCRIPTOR  *ObjectsSecurityDescriptor,
  _In_     ULONG                 AutoInheritFlags,
  _In_     POOL_TYPE             PoolType,
  _In_     PGENERIC_MAPPING      GenericMapping
);
````


## -parameters
<dl>

### -param Object [in, optional]

<dd>
<p>Pointer to the object whose security descriptor is to be modified. This is used to update security quota information.</p>
</dd>

### -param SecurityInformation [in]

<dd>
<p>Pointer to a value specifying which security information is to be set. Can be a combination of one or more of the following. </p>
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

### -param SecurityDescriptor [in]

<dd>
<p>The input security descriptor to be applied to the object. The caller of this routine is expected to probe and capture the passed security descriptor before calling, and to release it after calling.</p>
</dd>

### -param ObjectsSecurityDescriptor [in, out]

<dd>
<p>Pointer to a pointer to the object's security descriptor. The security descriptor must be in self-relative format. This structure must be deallocated by the caller.</p>
</dd>

### -param AutoInheritFlags [in]

<dd>
<p>Bitmask that controls automatic inheritance of ACEs. Set to the logical OR of one or more of the following bit flags: </p>
<table>
<tr>
<th>Security Information Flags</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>SEF_DACL_AUTO_INHERIT</p>
</td>
<td>
<p>If this flag is set, the DACL is treated as an auto-inherit DACL and is processed as described in the following Remarks section. This bit is ignored if DACL_SECURITY_INFORMATION is not set in the <i>SecurityInformation</i> parameter.</p>
</td>
</tr>
<tr>
<td>
<p>SEF_SACL_AUTO_INHERIT</p>
</td>
<td>
<p>If this flag is set, the SACL is treated as an auto-inherit SACL and is processed as described in the following Remarks section. This bit is ignored if SACL_SECURITY_INFORMATION is not set in the <i>SecurityInformation</i> parameter.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param PoolType [in]

<dd>
<p>Specifies the pool type to use when allocating a new security descriptor, which can be one of the following: </p>
<ul>
<li><b>NonPagedPool</b></li>
<li><b>PagedPool</b></li>
<li><b>NonPagedPoolCacheAligned</b></li>
<li><b>PagedPoolCacheAligned</b></li>
</ul>
<p>Usually, a caller specifies <b>PagedPool</b>, or else <b>NonPagedPool</b> if the buffer will be accessed at IRQL &gt;= DISPATCH_LEVEL or in an arbitrary thread context. </p>
<p><b>Note</b>: The <b>NonPagedPoolMustSucceed</b> and <b>NonPagedPoolCacheAlignedMustS</b> pool types are obsolete and should no longer be used. </p>
</dd>

### -param GenericMapping [in]

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
<p>If the <i>AutoInheritFlags</i> parameter is zero, the effect of calling <b>SeSetSecurityDescriptorInfoEx</b> is the same as that of calling <b>SeSetSecurityDescriptorInfo</b>.</p>

<p>If <i>AutoInheritFlags</i> specifies the SEF_DACL_AUTO_INHERIT bit, <b>SeSetSecurityDescriptorInfoEx</b> applies the following rules to the DACL to create the new security descriptor from the current descriptor:</p>

<p>If the SE_DACL_PROTECTED flag is not set in the control bits of the either the current security descriptor or the input <i>SecurityDescriptor</i>, <b>SeSetSecurityDescriptorInfoEx</b> constructs the output security descriptor from the inherited ACEs of the current security descriptor and noninherited ACEs of <i>SecurityDescriptor</i>. That is, it is impossible to change an inherited ACE by changing the ACL on an object. This behavior preserves the inherited ACEs as they were inherited from the parent container. </p>

<p>If SE_DACL_PROTECTED is set in the input <i>SecurityDescriptor</i>, the current security descriptor is ignored. The output security descriptor is built as a copy of the input <i>SecurityDescriptor</i> with any INHERITED_ACE bits turned off. </p>

<p>Ideally an ACL editor should turn off the INHERITED_ACE bits indicating to its caller that the ACEs inherited from the object's parent are now being explicitly set on the object. </p>

<p>If SE_DACL_PROTECTED is set in the current security descriptor and not in the <i>SecurityDescriptor</i>, the current security descriptor is ignored. The output security descriptor is built as a copy of the <i>SecurityDescriptor</i>. It is the caller's responsibility to ensure that the correct ACEs have the INHERITED_ACE bit turned on. </p>

<p>If <i>AutoInheritFlags</i> specifies the SEF_SACL_AUTO_INHERIT bit, <b>SeSetSecurityDescriptorInfoEx</b> applies similar rules to the new SACL.</p>

<p>For more information about access control and ACE inheritance, see the Security section of the Microsoft Windows SDK documentation.</p>

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
<p>This routine is available on Microsoft Windows 2000 and later. </p>
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
<a href="ifsk.ace">ACE</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--acl.md">ACL</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--generic-mapping.md">GENERIC_MAPPING</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtlcreatesecuritydescriptor.md">RtlCreateSecurityDescriptor</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtlcreatesecuritydescriptorrelative.md">RtlCreateSecurityDescriptorRelative</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtllengthsecuritydescriptor.md">RtlLengthSecurityDescriptor</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtlsetdaclsecuritydescriptor.md">RtlSetDaclSecurityDescriptor</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtlsetownersecuritydescriptor.md">RtlSetOwnerSecurityDescriptor</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtlvalidsecuritydescriptor.md">RtlValidSecurityDescriptor</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="ifsk.security_information">SECURITY_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-sequerysecuritydescriptorinfo.md">SeQuerySecurityDescriptorInfo</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-sesetsecuritydescriptorinfo.md">SeSetSecurityDescriptorInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SeSetSecurityDescriptorInfoEx routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
