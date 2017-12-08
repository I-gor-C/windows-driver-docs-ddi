---
UID: NF.wdm.RtlSetDaclSecurityDescriptor
title: RtlSetDaclSecurityDescriptor function
author: windows-driver-content
description: The RtlSetDaclSecurityDescriptor routine sets the DACL information of an absolute-format security descriptor, or if there is already a DACL present in the security descriptor, it is superseded.
old-location: kernel\rtlsetdaclsecuritydescriptor.htm
old-project: kernel
ms.assetid: d22f4a14-2293-4210-bead-5814484a1471
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RtlSetDaclSecurityDescriptor
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlSetDaclSecurityDescriptor
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
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# RtlSetDaclSecurityDescriptor function



## -description
The <b>RtlSetDaclSecurityDescriptor</b> routine sets the DACL information of an absolute-format security descriptor, or if there is already a DACL present in the security descriptor, it is superseded.


## -syntax

````
NTSTATUS RtlSetDaclSecurityDescriptor(
  _Inout_  PSECURITY_DESCRIPTOR SecurityDescriptor,
  _In_     BOOLEAN              DaclPresent,
  _In_opt_ PACL                 Dacl,
  _In_opt_ BOOLEAN              DaclDefaulted
);
````


## -parameters

### -param SecurityDescriptor [in, out]

A pointer to a <a href="kernel.security_descriptor">SECURITY_DESCRIPTOR</a> structure. This structure is the security descriptor to which the DACL is to be applied.

### -param DaclPresent [in]

Whether to indicate that a DACL is present in the security descriptor. If this parameter is <b>FALSE</b>, <b>RtlSetDaclSecurityDescriptor</b> sets the SE_DACL_PRESENT control flag in the security descriptor to <b>FALSE</b>. In this case, the remaining optional parameters (<i>Dacl</i> and <i>DaclDefaulted</i>) are ignored. If <i>DaclPresent</i> is <b>TRUE</b>, the SE_DACL_PRESENT flag in the security descriptor is set to <b>TRUE</b> and the remaining optional parameters are <u>not</u> ignored. For more information about the SE_DACL_PRESENT flag, see <a href="ifsk.security_descriptor_control">SECURITY_DESCRIPTOR_CONTROL</a>.

### -param Dacl [in, optional]

A pointer to the DACL for the security descriptor. If this parameter is <b>NULL</b>, the DACL pointer in the security descriptor is set to <b>NULL</b>. A <b>NULL</b> DACL pointer unconditionally grants all access to an object and is not the same as an empty DACL. An empty DACL denies all access to an object. If <i>Dacl</i> is non-<b>NULL</b>, the <a href="ifsk.acl">ACL</a> structure supplied by the caller is referenced by, but not copied into, the security descriptor. The caller can allocate the <b>ACL</b> structure from paged system memory, and can call the <a href="ifsk.rtlcreateacl">RtlCreateAcl</a> routine to initialize the structure.

### -param DaclDefaulted [in, optional]

Whether the DACL was supplied by some default mechanism, or was explicitly specified by the caller. If this parameter is <b>TRUE</b>, the DACL was supplied by a default mechanism. If <i>DaclDefaulted</i> is <b>FALSE</b>, the caller explicitly specified the DACL. <b>RtlSetDaclSecurityDescriptor</b> copies the value specified for this parameter to the SE_DACL_DEFAULTED control flag in the security descriptor. For more information about the SE_DACL_DEFAULTED flag, see <a href="ifsk.security_descriptor_control">SECURITY_DESCRIPTOR_CONTROL</a>.

## -returns
<b>RtlSetDaclSecurityDescriptor</b> can return one of the following status values.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The call completed successfully.
<dl>
<dt><b>STATUS_UNKNOWN_REVISION</b></dt>
</dl>The revision of the security descriptor is unknown.
<dl>
<dt><b>STATUS_INVALID_SECURITY_DESCR</b></dt>
</dl>The security descriptor is not an absolute format security descriptor.

 

## -remarks


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
Available starting with Windows 2000.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.acl">ACL</a>
</dt>
<dt>
<a href="ifsk.rtlcreateacl">RtlCreateAcl</a>
</dt>
<dt>
<a href="kernel.rtlcreatesecuritydescriptor">RtlCreateSecurityDescriptor</a>
</dt>
<dt>
<a href="kernel.rtllengthsecuritydescriptor">RtlLengthSecurityDescriptor</a>
</dt>
<dt>
<a href="kernel.rtlvalidsecuritydescriptor">RtlValidSecurityDescriptor</a>
</dt>
<dt>
<a href="kernel.security_descriptor">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="ifsk.security_descriptor_control">SECURITY_DESCRIPTOR_CONTROL</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlSetDaclSecurityDescriptor routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
