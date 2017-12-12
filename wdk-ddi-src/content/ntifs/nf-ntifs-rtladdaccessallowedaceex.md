---
UID: NF.ntifs.RtlAddAccessAllowedAceEx
title: RtlAddAccessAllowedAceEx function
author: windows-driver-content
description: The RtlAddAccessAllowedAceEx routine adds an access-allowed access control entry (ACE) with inheritance ACE flags to an access control list (ACL). The access is granted to the specified security identifier (SID).
old-location: ifsk\rtladdaccessallowedaceex.htm
old-project: ifsk
ms.assetid: aeef74d8-d4a5-4ce4-b7f8-e2a2d263a678
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlAddAccessAllowedAceEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available in Microsoft Windows 2000 and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlAddAccessAllowedAceEx
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
---

# RtlAddAccessAllowedAceEx function



## -description
The <b>RtlAddAccessAllowedAceEx</b> routine adds an access-allowed access control entry (<a href="ifsk.ace">ACE</a>) with inheritance ACE flags to an access control list (<a href="ifsk.acl">ACL</a>). The access is granted to the specified security identifier (<a href="ifsk.sid">SID</a>). 



## -syntax

````
NTSTATUS RtlAddAccessAllowedAceEx(
  _Inout_ PACL        Acl,
  _In_    ULONG       AceRevision,
  _In_    ULONG       AceFlags,
  _In_    ACCESS_MASK AccessMask,
  _In_    PSID        Sid
);
````


## -parameters

### -param Acl [in, out]

A pointer to a caller-allocated buffer that contains the ACL to be modified. <b>RtlAddAccessAllowedAceEx</b> adds an access-allowed ACE to the end of this ACL. The ACE is in the form of an <a href="ifsk.access_allowed_ace">ACCESS_ALLOWED_ACE</a> structure.


### -param AceRevision [in]

ACL revision level of the ACE to be added. This value can be ACL_REVISION or ACL_REVISION_DS. It must be ACL_REVISION_DS if the ACL contains an object-specific ACE. 


### -param AceFlags [in]

Bitmask specifying the inherit flags of the ACE to be added. 


### -param AccessMask [in]

A bitmask of one or more <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> flags that specify the access rights to be granted to the specified SID. For more information, see the description of the <i>DesiredAccess</i> parameter of <a href="kernel.zwcreatefile">ZwCreateFile</a>. 


### -param Sid [in]

A pointer to the SID structure that represents a user, group, or logon account that is being granted access. 


## -returns
<b>RtlAddAccessAllowedAceEx</b> can return one of the following values:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The ACE was successfully added.
<dl>
<dt><b>STATUS_ALLOTTED_SPACE_EXCEEDED</b></dt>
</dl>A new ACE does not fit into the ACL. A larger ACL buffer is required. For more information about how to calculate the size of an ACL, see <a href="ifsk.rtlcreateacl">RtlCreateAcl</a>. 
<dl>
<dt><b>STATUS_INVALID_ACL</b></dt>
</dl>The specified ACL is not correctly formed.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>The AceFlags parameter was invalid.
<dl>
<dt><b>STATUS_INVALID_SID</b></dt>
</dl>The specified SID structure is not structurally valid.
<dl>
<dt><b>STATUS_REVISION_MISMATCH</b></dt>
</dl>The specified <i>AceRevision</i> is not known or is not compatible with that of the ACL. 

 


## -remarks
Unlike <a href="ifsk.rtladdaccessallowedace">RtlAddAccessAllowedAce</a>, this routine sets the inheritance ACE flags.  

For more information about security and access control, see the documentation about these topics in the Microsoft Windows SDK, such as:

<a href="http://go.microsoft.com/fwlink/p/?linkid=140858">Access Control Lists</a>

<a href="http://go.microsoft.com/fwlink/p/?linkid=140859">Creating or Modifying an ACL</a>

<a href="http://go.microsoft.com/fwlink/p/?linkid=140860">Getting Information from an ACL</a>


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
This routine is available in Microsoft Windows 2000 and later Windows operating systems. 

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or FltKernel.h)</dt>
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
&lt;= APC_LEVEL

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
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlAddAccessAllowedAceEx routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

