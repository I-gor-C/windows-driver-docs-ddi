---
UID: NF.ntifs.SeSetSecurityDescriptorInfo
title: SeSetSecurityDescriptorInfo function
author: windows-driver-content
description: The SeSetSecurityDescriptorInfo routine sets an object's security descriptor.
old-location: ifsk\sesetsecuritydescriptorinfo.htm
old-project: ifsk
ms.assetid: d6f02142-1cd8-4f09-b106-d963bf080495
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
---

# SeSetSecurityDescriptorInfo function



## -description
The <b>SeSetSecurityDescriptorInfo</b> routine sets an object's security descriptor.


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

### -param Object [in, optional]

Pointer to the object whose security descriptor is to be set. This is used to update security quota information.

### -param SecurityInformation [in]

Pointer to a bitmask specifying which security information is to be applied to the object. Can be a combination of one or more of the following values. 
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
DACL_SECURITY_INFORMATION
</td>
<td>
Indicates the discretionary access control list (DACL) of the object is being set. Requires WRITE_DAC access. 
</td>
</tr>
<tr>
<td>
GROUP_SECURITY_INFORMATION
</td>
<td>
Indicates the primary group identifier of the object is being set. Requires WRITE_OWNER access. 
</td>
</tr>
<tr>
<td>
OWNER_SECURITY_INFORMATION
</td>
<td>
Indicates the owner identifier of the object is being set. Requires WRITE_OWNER access. 
</td>
</tr>
<tr>
<td>
SACL_SECURITY_INFORMATION
</td>
<td>
Indicates the system ACL (SACL) of the object is being set. Requires ACCESS_SYSTEM_SECURITY access. 
</td>
</tr>
</table>
 

### -param SecurityDescriptor [in]

The input security descriptor to be applied to the object. The caller of this routine is expected to probe and capture the passed security descriptor before calling <b>SeSetSecurityDescriptorInfo</b>, and to release it afterward.

### -param ObjectsSecurityDescriptor [in, out]

Pointer to a pointer to the object's security descriptor. The security descriptor must be in self-relative format. The caller is responsible for freeing this structure when it is no longer needed.

### -param PoolType [in]

Specifies the pool type to use when allocating a new security descriptor, which can be one of the following: 
<ul>
<li><b>NonPagedPool</b></li>
<li><b>PagedPool</b></li>
<li><b>NonPagedPoolCacheAligned</b></li>
<li><b>PagedPoolCacheAligned</b></li>
</ul>
Usually, a caller specifies <b>PagedPool</b>, or else <b>NonPagedPool</b> if the buffer will be accessed at IRQL &gt;= DISPATCH_LEVEL or in an arbitrary thread context. 
<div class="alert"><b>Note</b>    The <b>NonPagedPoolMustSucceed</b> and <b>NonPagedPoolCacheAlignedMustS</b> pool types are obsolete and should no longer be used. </div>
<div> </div>

### -param GenericMapping [in]

Pointer to a GENERIC_MAPPING structure that specifies the mapping of generic to specific and standard access types for the object being accessed. This mapping structure is expected to be safe to access (that is, captured if necessary) prior to be passed to this routine.

## -returns
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The object's security descriptor was successfully modified.
<dl>
<dt><b>STATUS_BAD_DESCRIPTOR_FORMAT</b></dt>
</dl>The provided object's security descriptor was not in self-relative format.
<dl>
<dt><b>STATUS_NO_SECURITY_ON_OBJECT</b></dt>
</dl>The object does not have a security descriptor.

 

## -remarks
<b>SeSetSecurityDescriptorInfo</b> modifies an object's existing security descriptor. If the object does not have a security descriptor, the call to <b>SeSetSecurityDescriptorInfo</b> will fail.

To specify whether the object supports automatic inheritance of access control entries (ACE), use <b>SeSetSecurityDescriptorInfoEx</b>.

A security descriptor can be in absolute or self-relative form. In self-relative form, all members of the structure are located contiguously in memory. In absolute form, the structure only contains pointers to the members.

For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK.

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
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.ace">ACE</a>
</dt>
<dt>
<a href="ifsk.acl">ACL</a>
</dt>
<dt>
<a href="kernel.generic_mapping">GENERIC_MAPPING</a>
</dt>
<dt>
<a href="kernel.rtlcreatesecuritydescriptor">RtlCreateSecurityDescriptor</a>
</dt>
<dt>
<a href="ifsk.rtlcreatesecuritydescriptorrelative">RtlCreateSecurityDescriptorRelative</a>
</dt>
<dt>
<a href="kernel.rtllengthsecuritydescriptor">RtlLengthSecurityDescriptor</a>
</dt>
<dt>
<a href="kernel.rtlsetdaclsecuritydescriptor">RtlSetDaclSecurityDescriptor</a>
</dt>
<dt>
<a href="ifsk.rtlsetownersecuritydescriptor">RtlSetOwnerSecurityDescriptor</a>
</dt>
<dt>
<a href="kernel.rtlvalidsecuritydescriptor">RtlValidSecurityDescriptor</a>
</dt>
<dt>
<a href="ifsk.security_descriptor">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="ifsk.security_information">SECURITY_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.sequerysecuritydescriptorinfo">SeQuerySecurityDescriptorInfo</a>
</dt>
<dt>
<a href="ifsk.sesetaccessstategenericmapping">SeSetAccessStateGenericMapping</a>
</dt>
<dt>
<a href="ifsk.sesetsecuritydescriptorinfoex">SeSetSecurityDescriptorInfoEx</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SeSetSecurityDescriptorInfo routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
