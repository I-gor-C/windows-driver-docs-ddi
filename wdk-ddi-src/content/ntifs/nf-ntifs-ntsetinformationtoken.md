---
UID: NF.ntifs.NtSetInformationToken
title: NtSetInformationToken
author: windows-driver-content
description: The ZwSetInformationToken routine modifies information in a specified token. The calling process must have appropriate access rights to set the information.
old-location: kernel\zwsetinformationtoken.htm
old-project: kernel
ms.assetid: fdb1245c-7804-4cb9-9632-bedb9f7f7b2b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NtSetInformationToken
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwSetInformationToken,NtSetInformationToken
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

# NtSetInformationToken function



## -description
<p>The <b>ZwSetInformationToken</b> routine modifies information in a specified token. The calling process must have appropriate access rights to set the information. </p>


## -syntax

````
NTSTATUS ZwSetInformationToken(
  _In_ HANDLE                  TokenHandle,
  _In_ TOKEN_INFORMATION_CLASS TokenInformationClass,
  _In_ PVOID                   TokenInformation,
  _In_ ULONG                   TokenInformationLength
);
````


## -parameters
<dl>

### -param <i>TokenHandle</i> [in]

<dd>
<p>Handle for an access token in which information is to be modified. </p>
</dd>

### -param <i>TokenInformationClass</i> [in]

<dd>
<p>A value from the <a href="..\ntifs\ne-ntifs--token-information-class.md">TOKEN_INFORMATION_CLASS</a> enumerated type identifying the type of information to be modified. The possible values for this parameter are listed in the <i>TokenInformationClass</i> Value column of the table shown in the description of the <i>TokenInformation</i> parameter. </p>
</dd>

### -param <i>TokenInformation</i> [in]

<dd>
<p>Pointer to a caller-supplied buffer containing the information to be modified in the token. The structure of the information in this buffer depends upon the value of <i>TokenInformationClass</i>, as shown in the following table. All structures must be aligned on a 32-bit boundary. </p>
<table>
<tr>
<th><i>TokenInformationClass</i> value</th>
<th>Effect on <i>TokenInformation</i> buffer</th>
</tr>
<tr>
<td>
<p><b>TokenDefaultDacl</b></p>
</td>
<td>
<p>The buffer contains a <a href="..\ntifs\ns-ntifs--token-default-dacl.md">TOKEN_DEFAULT_DACL</a> structure specifying the default <a href="..\ntifs\ns-ntifs--acl.md">DACL</a> for newly created objects. TOKEN_ADJUST_DEFAULT access is required to set this information. The buffer contents are not validated for structural correctness or consistency. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenGroups</b></p>
</td>
<td>
<p>Not a valid information class. This information is read-only. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenOwner</b></p>
</td>
<td>
<p>The buffer contains a <a href="..\ntifs\ns-ntifs--token-owner.md">TOKEN_OWNER</a> structure specifying the default owner <a href="ifsk.sid">SID</a> for newly created objects. TOKEN_ADJUST_DEFAULT access is required to set this information. The owner values that may be specified are restricted to the user and group IDs with an attribute indicating they can be assigned as the owner of objects. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenPrimaryGroup</b></p>
</td>
<td>
<p>The buffer contains a <a href="..\ntifs\ns-ntifs--token-primary-group.md">TOKEN_PRIMARY_GROUP</a> structure specifying the default primary group <b>SID</b> for newly created objects. TOKEN_ADJUST_DEFAULT access is required to set this information. Must be one of the group IDs already in the token. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenPrivileges</b></p>
</td>
<td>
<p>Not a valid information class. This information is read-only. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenSource</b></p>
</td>
<td>
<p>Not a valid information class. This information is read-only. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenStatistics</b></p>
</td>
<td>
<p>Not a valid information class. This information is read-only. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenUser</b></p>
</td>
<td>
<p>Not a valid information class. This information is read-only. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>TokenInformationLength</i> [in]

<dd>
<p>Size, in bytes, of the structure passed in the <i>TokenInformation</i> buffer. Must be greater than or equal to the minimum value given in the following table. </p>
<table>
<tr>
<th><i>TokenInformationClass</i> value</th>
<th>Minimum <i>TokenInformationLength</i></th>
</tr>
<tr>
<td>
<p><b>TokenDefaultDacl</b></p>
</td>
<td>
<p><b>sizeof</b>(<b>TOKEN_DEFAULT_DACL</b>) </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenOwner</b></p>
</td>
<td>
<p><b>sizeof</b>(<b>TOKEN_OWNER</b>) </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenPrimaryGroup</b></p>
</td>
<td>
<p><b>sizeof</b>(<b>TOKEN_PRIMARY_GROUP</b>) </p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>ZwSetInformationToken</b> returns STATUS_SUCCESS or an appropriate error status. Possible error status codes include the following:</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p><i>TokenHandle</i> did not have the required access.</p><dl>
<dt><b>STATUS_ALLOTTED_SPACE_EXCEEDED</b></dt>
</dl><p>The space allotted for storage of the default discretionary access control and the primary group ID is not large enough to accept the new value of one of these fields.</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The value of <i>TokenInformationLength</i> was less than the required minimum.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The specified default owner's security information could not be captured.</p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p><i>TokenHandle</i> was not a valid handle.</p><dl>
<dt><b>STATUS_INVALID_INFO_CLASS</b></dt>
</dl><p><i>TokenInformationClass</i> was not a valid token information class.</p><dl>
<dt><b>STATUS_INVALID_OWNER</b></dt>
</dl><p>The caller cannot set the specified ID to be an owner (or default owner) of an object.</p><dl>
<dt><b>STATUS_INVALID_PRIMARY_GROUP</b></dt>
</dl><p>The caller cannot set the specified ID to be the primary group of an object.</p><dl>
<dt><b>STATUS_INVALID_SID</b></dt>
</dl><p>The specified default owner's security information was not valid.</p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p><i>TokenHandle</i> was not a token handle.</p>

<p> </p>

## -remarks
<p>For more information about security and access control, see the documentation on these topics in the Windows SDK.</p>

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
<p>Available in Windows 7 and later versions of Windows.</p>
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
<a href="..\ntifs\nf-ntifs-psdereferenceimpersonationtoken.md">PsDereferenceImpersonationToken</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-psdereferenceprimarytoken.md">PsDereferencePrimaryToken</a>
</dt>
<dt>
<a href="..\wudfddi\ne-wudfddi--security-impersonation-level.md">SECURITY_IMPERSONATION_LEVEL</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-sequeryauthenticationidtoken.md">SeQueryAuthenticationIdToken</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-sequerysubjectcontexttoken.md">SeQuerySubjectContextToken</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-setokenisadmin.md">SeTokenIsAdmin</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-setokenisrestricted.md">SeTokenIsRestricted</a>
</dt>
<dt>
<a href="ifsk.sid">SID</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-default-dacl.md">TOKEN_DEFAULT_DACL</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-groups.md">TOKEN_GROUPS</a>
</dt>
<dt>
<a href="..\ntifs\ne-ntifs--token-information-class.md">TOKEN_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-owner.md">TOKEN_OWNER</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-primary-group.md">TOKEN_PRIMARY_GROUP</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-privileges.md">TOKEN_PRIVILEGES</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-source.md">TOKEN_SOURCE</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-statistics.md">TOKEN_STATISTICS</a>
</dt>
<dt>
<a href="..\ntifs\ne-ntifs--token-type.md">TOKEN_TYPE</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-user.md">TOKEN_USER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwqueryinformationtoken.md">ZwQueryInformationToken</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwSetInformationToken routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
