---
UID: NF.ntifs.ZwQueryInformationToken
title: ZwQueryInformationToken
author: windows-driver-content
description: The ZwQueryInformationToken routine retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information.
old-location: kernel\zwqueryinformationtoken.htm
old-project: kernel
ms.assetid: 554b541b-943a-413e-9803-7dba17d0c6ce
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ZwQueryInformationToken
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
req.alt-api: ZwQueryInformationToken,NtQueryInformationToken
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

# ZwQueryInformationToken function



## -description
<p>The <b>ZwQueryInformationToken</b> routine retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information. </p>


## -syntax

````
NTSTATUS ZwQueryInformationToken(
  _In_  HANDLE                  TokenHandle,
  _In_  TOKEN_INFORMATION_CLASS TokenInformationClass,
  _Out_ PVOID                   TokenInformation,
  _In_  ULONG                   TokenInformationLength,
  _Out_ PULONG                  ReturnLength
);
````


## -parameters
<dl>

### -param <i>TokenHandle</i> [in]

<dd>
<p>Handle for an access token from which information is to be retrieved. If <i>TokenInformationClass</i> is set to <b>TokenSource</b>, the handle must have TOKEN_QUERY_SOURCE access. For all other <i>TokenInformationClass</i> values, the handle must have TOKEN_QUERY access. For more information about access rights for access-token objects, see the Security section of the Windows SDK documentation.</p>
</dd>

### -param <i>TokenInformationClass</i> [in]

<dd>
<p>A value from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556838">TOKEN_INFORMATION_CLASS</a> enumerated type identifying the type of information to be retrieved. The possible values for this parameter are listed in the <i>TokenInformationClass</i> Value column of the table shown in the description of the <i>TokenInformation</i> parameter.</p>
</dd>

### -param <i>TokenInformation</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer that receives the requested information about the token. The structure put into this buffer depends upon the value of <i>TokenInformationClass</i>, as shown in the following table. All structures must be aligned on a 32-bit boundary.</p>
<table>
<tr>
<th><i>TokenInformationClass</i> Value</th>
<th>Effect on <i>TokenInformation</i> Buffer</th>
</tr>
<tr>
<td>
<p><b>TokenDefaultDacl</b></p>
</td>
<td>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556831">TOKEN_DEFAULT_DACL</a> structure containing the default <a href="..\ntifs\ns-ntifs--acl.md">DACL</a> for newly created objects. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenGroups</b></p>
</td>
<td>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556834">TOKEN_GROUPS</a> structure containing the group accounts associated with the token.</p>
</td>
</tr>
<tr>
<td>
<p><b>TokenImpersonationLevel</b></p>
</td>
<td>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556631">SECURITY_IMPERSONATION_LEVEL</a> value indicating the impersonation level of the token. If the access token is not an impersonation token, the call to <b>ZwQueryInformationToken</b> fails. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenOwner</b></p>
</td>
<td>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556842">TOKEN_OWNER</a> structure containing the default owner <a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a> for newly created objects.</p>
</td>
</tr>
<tr>
<td>
<p><b>TokenPrimaryGroup</b></p>
</td>
<td>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556845">TOKEN_PRIMARY_GROUP</a> structure containing the default primary group SID for newly created objects. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenPrivileges</b></p>
</td>
<td>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556846">TOKEN_PRIVILEGES</a> structure containing the token's privileges.</p>
</td>
</tr>
<tr>
<td>
<p><b>TokenSessionId</b></p>
</td>
<td>
<p>The buffer receives a 32-bit value specifying the Terminal Services session identifier associated with the token. If the token is associated with the Terminal Server console session, the session identifier is zero. A nonzero session identifier indicates a Terminal Services client session. In a non-Terminal Services environment, the session identifier is zero.</p>
</td>
</tr>
<tr>
<td>
<p><b>TokenSource</b></p>
</td>
<td>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556848">TOKEN_SOURCE</a> structure containing the source of the token. TOKEN_QUERY_SOURCE access is needed to retrieve this information.</p>
</td>
</tr>
<tr>
<td>
<p><b>TokenStatistics</b></p>
</td>
<td>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556849">TOKEN_STATISTICS</a> structure containing various token statistics.</p>
</td>
</tr>
<tr>
<td>
<p><b>TokenType</b></p>
</td>
<td>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556851">TOKEN_TYPE</a> value indicating whether the token is a primary or impersonation token. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenUser</b></p>
</td>
<td>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556855">TOKEN_USER</a> structure containing the token's user account. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>TokenInformationLength</i> [in]

<dd>
<p>Length, in bytes, of the caller-allocated <i>TokenInformation</i> buffer. </p>
</dd>

### -param <i>ReturnLength</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives the actual length, in bytes, of the information returned in the <i>TokenInformation</i> buffer. If either of the following conditions is true, no data is returned in the <i>TokenInformation</i> buffer: </p>
<ul>
<li>
<p>The size of the requested token information structure is greater than <i>TokenInformationLength</i>. In this case, <i>ReturnLength</i> receives the actual number of bytes needed to store the requested information. </p>
</li>
<li>
<p>The value of <i>TokenInformationClass</i> is <b>TokenDefaultDacl</b>, and there is no default DACL established for the token. In this case, <i>ReturnLength</i> receives zero. </p>
</li>
</ul>
</dd>
</dl>

## -returns
<p><b>ZwQueryInformationToken</b> returns STATUS_SUCCESS or an appropriate error status. Possible error status codes include the following:</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p><i>TokenHandle</i> did not have the required access.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The size of the requested token information structure is greater than <i>TokenInformationLength</i>. The number of bytes required is returned in <i>ReturnLength</i>. </p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p><i>TokenHandle</i> was not a valid handle. </p><dl>
<dt><b>STATUS_INVALID_INFO_CLASS</b></dt>
</dl><p><i>TokenInformationClass</i> was not a valid token information class. </p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p><i>TokenHandle</i> was not a token handle. </p>

<p> </p>

## -remarks
<p>The <b>ZwQueryInformationToken</b> routine can be used by a file system or file system filter driver to determine the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a> of the caller that initiated the request during <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a> processing. If <b>TokenUser</b> is specified for the <i>TokenInformationClass</i> parameter passed to <b>ZwQueryInformationToken</b>, a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556855">TOKEN_USER</a> structure is returned in the buffer pointed to by the <i>TokenInformation</i> parameter. This returned buffer contains an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556742">SID_AND_ATTRIBUTES</a> structure with the user <b>SID</b>.</p>

<p>For more information about security and access control, see the documentation on these topics in the Windows SDK. </p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p>The <b>ZwQueryInformationToken</b> routine can be used by a file system or file system filter driver to determine the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a> of the caller that initiated the request during <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a> processing. If <b>TokenUser</b> is specified for the <i>TokenInformationClass</i> parameter passed to <b>ZwQueryInformationToken</b>, a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556855">TOKEN_USER</a> structure is returned in the buffer pointed to by the <i>TokenInformation</i> parameter. This returned buffer contains an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556742">SID_AND_ATTRIBUTES</a> structure with the user <b>SID</b>.</p>

<p>For more information about security and access control, see the documentation on these topics in the Windows SDK. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538866">ACL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556631">SECURITY_IMPERSONATION_LEVEL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556690">SeQueryInformationToken</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556742">SID_AND_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556831">TOKEN_DEFAULT_DACL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556834">TOKEN_GROUPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556838">TOKEN_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556842">TOKEN_OWNER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556845">TOKEN_PRIMARY_GROUP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556846">TOKEN_PRIVILEGES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556848">TOKEN_SOURCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556849">TOKEN_STATISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556851">TOKEN_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556855">TOKEN_USER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567102">ZwSetInformationToken</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwQueryInformationToken routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
