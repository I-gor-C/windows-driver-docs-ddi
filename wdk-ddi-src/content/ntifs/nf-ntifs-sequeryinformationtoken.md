---
UID: NF.ntifs.SeQueryInformationToken
title: SeQueryInformationToken
author: windows-driver-content
description: The SeQueryInformationToken routine retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information.
old-location: ifsk\sequeryinformationtoken.htm
old-project: ifsk
ms.assetid: 97e28b53-8b4c-4f76-b6bb-21dad2233463
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SeQueryInformationToken
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows 2000 and later versions of the operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SeQueryInformationToken
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

# SeQueryInformationToken function



## -description
<p>The <b>SeQueryInformationToken</b> routine retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information. </p>


## -syntax

````
NTSTATUS SeQueryInformationToken(
  _In_  PACCESS_TOKEN           Token,
  _In_  TOKEN_INFORMATION_CLASS TokenInformationClass,
  _Out_ PVOID                   *TokenInformation
);
````


## -parameters
<dl>

### -param <i>Token</i> [in]

<dd>
<p>A pointer to an access token from which information is to be retrieved. If <i>TokenInformationClass</i> is set to <i>TokenSource</i>, the handle must have TOKEN_QUERY_SOURCE access. For all other <i>TokenInformationClass</i> values, the handle must have TOKEN_QUERY access. </p>
</dd>

### -param <i>TokenInformationClass</i> [in]

<dd>
<p>A value from the <a href="..\ntifs\ne-ntifs--token-information-class.md">TOKEN_INFORMATION_CLASS</a> enumerated type that identifies the type of information to be retrieved. </p>
</dd>

### -param <i>TokenInformation</i> [out]

<dd>
<p>If STATUS_SUCCESS is returned, 
	  <i>TokenInformation</i> receives a pointer to a 
	  location that contains the address of a buffer that holds the requested 
	  information. The format of this information buffer depends upon the 
	  value of <i>TokenInformationClass</i>, as shown in 
	  the following table.  Be aware that the buffer is allocated by 
	  <b>SeQueryInformationToken</b> 
	  from paged pool. This buffer must eventually be freed by the caller by 
	  using either 
	  <a href="..\ntddk\nf-ntddk-exfreepool.md">ExFreePool</a> or 
	  <a href="..\wdm\nf-wdm-exfreepoolwithtag.md">ExFreePoolWithTag</a>.
	  </p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p><b>TokenDefaultDacl</b></p>
</td>
<td>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-default-dacl.md">TOKEN_DEFAULT_DACL</a> structure that contains the default DACL for newly created objects. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenGroups</b></p>
</td>
<td>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-groups.md">TOKEN_GROUPS</a> structure that contains the group accounts associated with the token.</p>
</td>
</tr>
<tr>
<td>
<p><b>TokenImpersonationLevel</b></p>
</td>
<td>
<p>The buffer receives a <a href="..\wudfddi\ne-wudfddi--security-impersonation-level.md">SECURITY_IMPERSONATION_LEVEL</a> value which indicates the impersonation level of the token. If the access token is not an impersonation token, the call to <b>SeQueryInformationToken</b> fails. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenOwner</b></p>
</td>
<td>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-owner.md">TOKEN_OWNER</a> structure that contains the default owner security identifier (<a href="ifsk.sid">SID</a>) for newly created objects.</p>
</td>
</tr>
<tr>
<td>
<p><b>TokenPrimaryGroup</b></p>
</td>
<td>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-primary-group.md">TOKEN_PRIMARY_GROUP</a> structure that contains the default primary group SID for newly created objects. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenPrivileges</b></p>
</td>
<td>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-privileges.md">TOKEN_PRIVILEGES</a> structure that contains the token's privileges.</p>
</td>
</tr>
<tr>
<td>
<p><b>TokenSessionId</b></p>
</td>
<td>
<p>The buffer receives a <b>DWORD</b> value (not a pointer to it) that indicates the Terminal Services session identifier that is associated with the token. If the token is associated with the Terminal Server console session, the session identifier is zero. A nonzero session identifier indicates a Terminal Services client session. In a non-Terminal Services environment, the session identifier is zero.</p>
</td>
</tr>
<tr>
<td>
<p><b>TokenSource</b></p>
</td>
<td>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-source.md">TOKEN_SOURCE</a> structure that contains the source of the token. TOKEN_QUERY_SOURCE access is needed to retrieve this information.</p>
</td>
</tr>
<tr>
<td>
<p><b>TokenStatistics</b></p>
</td>
<td>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-statistics.md">TOKEN_STATISTICS</a> structure that contains various token statistics.</p>
</td>
</tr>
<tr>
<td>
<p><b>TokenType</b></p>
</td>
<td>
<p>The buffer receives a <a href="..\ntifs\ne-ntifs--token-type.md">TOKEN_TYPE</a> value that indicates whether the token is a primary or impersonation token. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenUser</b></p>
</td>
<td>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-user.md">TOKEN_USER</a> structure that contains the token's user account. </p>
</td>
</tr>
<tr>
<td>
<p><b>TokenIntegrityLevel</b></p>
</td>
<td>
<p>The buffer receives a <b>DWORD</b> value (not a pointer to it) that specifies the token’s integrity level. </p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The call to <a href="..\ntifs\nf-ntifs-sequeryinformationtoken.md">SeQueryInformationToken</a> succeeded.</p><dl>
<dt><b>STATUS_INVALID_INFO_CLASS</b></dt>
</dl><p>An invalid value was supplied for <i>TokenInformationClass</i>. </p>

<p> </p>

## -remarks
<p>For more information about security and access control, see the documentation about these topics in the Microsoft Windows SDK.</p>

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
<p>This routine is available on Microsoft Windows 2000 and later versions of the operating system. </p>
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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SeQueryInformationToken routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
