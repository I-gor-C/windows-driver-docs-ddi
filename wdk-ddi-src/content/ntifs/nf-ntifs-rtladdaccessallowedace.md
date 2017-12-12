---
UID: NF.ntifs.RtlAddAccessAllowedAce
title: RtlAddAccessAllowedAce function
author: windows-driver-content
description: The RtlAddAccessAllowedAce routine adds an access-allowed access control entry (ACE) to an access control list (ACL). The access is granted to the specified security identifier (SID).
old-location: ifsk\rtladdaccessallowedace.htm
old-project: ifsk
ms.assetid: 39a50efc-b27a-4c73-b436-c6495256d9c6
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlAddAccessAllowedAce
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
req.alt-api: RtlAddAccessAllowedAce
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
req.irql: < DISPATCH_LEVEL
---

# RtlAddAccessAllowedAce function



## -description
The <b>RtlAddAccessAllowedAce</b> routine adds an access-allowed access control entry (ACE) to an access control list (ACL). The access is granted to the specified security identifier (SID). 



## -syntax

````
NTSTATUS RtlAddAccessAllowedAce(
  _Inout_ PACL        Acl,
  _In_    ULONG       AceRevision,
  _In_    ACCESS_MASK AccessMask,
  _In_    PSID        Sid
);
````


## -parameters

### -param Acl [in, out]

Pointer to a caller-allocated buffer containing the ACL to be modified. <b>RtlAddAccessAllowedAce</b> adds an access-allowed ACE to the end of this ACL. The ACE is in the form of an ACCESS_ALLOWED_ACE structure.


### -param AceRevision [in]

ACL revision level of the ACE to be added. Windows version requirments are the following:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">

### -param ACL_REVISION

</td>
<td width="60%">
The revision level valid on all Windows versions.

</td>
</tr>
<tr>
<td width="40%">

### -param ACL_REVISION_DS

</td>
<td width="60%">
The revision level valid starting with Windows 2000.

<div class="alert"><b>Note</b>  <i>AceRevision</i> must be ACL_REVISION_DS if the ACL in <i>Acl</i> contains an object-specific ACE.</div>
<div> </div>
</td>
</tr>
</table>
 


### -param AccessMask [in]

Bitmask of one or more <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> flags specifying the access rights to be granted to the specified SID. For more information, see the description of the <i>DesiredAccess</i> parameter of <b>ZwCreateFile</b>. 


### -param Sid [in]

Pointer to the SID structure representing a user, group, or logon account that is being granted access. 


## -returns
<b>RtlAddAccessAllowedAce</b> can return one of the following values:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The ACE was successfully added.
<dl>
<dt><b>STATUS_ALLOTTED_SPACE_EXCEEDED</b></dt>
</dl>A new ACE does not fit into the ACL. A larger ACL buffer is required. See <a href="ifsk.rtlcreateacl">RtlCreateAcl</a> for information about calculating the size of an ACL. 
<dl>
<dt><b>STATUS_INVALID_ACL</b></dt>
</dl>The specified ACL is not properly formed.
<dl>
<dt><b>STATUS_INVALID_SID</b></dt>
</dl>The specified SID structure is not structurally valid.
<dl>
<dt><b>STATUS_REVISION_MISMATCH</b></dt>
</dl>The specified revision is not known or is not compatible with that of the ACL. 

 


## -remarks
For more information about security and access control, see the documentation on these topics in the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0.


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
&lt; DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.access_allowed_ace">ACCESS_ALLOWED_ACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="ifsk.ace">ACE</a>
</dt>
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
<a href="kernel.seassignsecurity">SeAssignSecurity</a>
</dt>
<dt>
<a href="ifsk.sid">SID</a>
</dt>
<dt>
<a href="kernel.zwcreatefile">ZwCreateFile</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlAddAccessAllowedAce routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

