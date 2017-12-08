---
UID: NF.ntifs.SeQueryInformationToken
title: SeQueryInformationToken function
author: windows-driver-content
description: The SeQueryInformationToken routine retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information.
old-location: ifsk\sequeryinformationtoken.htm
old-project: ifsk
ms.assetid: 97e28b53-8b4c-4f76-b6bb-21dad2233463
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
---

# SeQueryInformationToken function



## -description
The <b>SeQueryInformationToken</b> routine retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information. 


## -syntax

````
NTSTATUS SeQueryInformationToken(
  _In_  PACCESS_TOKEN           Token,
  _In_  TOKEN_INFORMATION_CLASS TokenInformationClass,
  _Out_ PVOID                   *TokenInformation
);
````


## -parameters

### -param Token [in]

A pointer to an access token from which information is to be retrieved. If <i>TokenInformationClass</i> is set to <i>TokenSource</i>, the handle must have TOKEN_QUERY_SOURCE access. For all other <i>TokenInformationClass</i> values, the handle must have TOKEN_QUERY access. 

### -param TokenInformationClass [in]

A value from the <a href="ifsk.token_information_class">TOKEN_INFORMATION_CLASS</a> enumerated type that identifies the type of information to be retrieved. 

### -param TokenInformation [out]

If STATUS_SUCCESS is returned, 
	  <i>TokenInformation</i> receives a pointer to a 
	  location that contains the address of a buffer that holds the requested 
	  information. The format of this information buffer depends upon the 
	  value of <i>TokenInformationClass</i>, as shown in 
	  the following table.  Be aware that the buffer is allocated by 
	  <b>SeQueryInformationToken</b> 
	  from paged pool. This buffer must eventually be freed by the caller by 
	  using either 
	  <a href="kernel.exfreepool">ExFreePool</a> or 
	  <a href="kernel.exfreepoolwithtag">ExFreePoolWithTag</a>.
	  
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<b>TokenDefaultDacl</b>
</td>
<td>
The buffer receives a <a href="ifsk.token_default_dacl">TOKEN_DEFAULT_DACL</a> structure that contains the default DACL for newly created objects. 
</td>
</tr>
<tr>
<td>
<b>TokenGroups</b>
</td>
<td>
The buffer receives a <a href="ifsk.token_groups">TOKEN_GROUPS</a> structure that contains the group accounts associated with the token.
</td>
</tr>
<tr>
<td>
<b>TokenImpersonationLevel</b>
</td>
<td>
The buffer receives a <a href="ifsk.security_impersonation_level">SECURITY_IMPERSONATION_LEVEL</a> value which indicates the impersonation level of the token. If the access token is not an impersonation token, the call to <b>SeQueryInformationToken</b> fails. 
</td>
</tr>
<tr>
<td>
<b>TokenOwner</b>
</td>
<td>
The buffer receives a <a href="ifsk.token_owner">TOKEN_OWNER</a> structure that contains the default owner security identifier (<a href="ifsk.sid">SID</a>) for newly created objects.
</td>
</tr>
<tr>
<td>
<b>TokenPrimaryGroup</b>
</td>
<td>
The buffer receives a <a href="ifsk.token_primary_group">TOKEN_PRIMARY_GROUP</a> structure that contains the default primary group SID for newly created objects. 
</td>
</tr>
<tr>
<td>
<b>TokenPrivileges</b>
</td>
<td>
The buffer receives a <a href="ifsk.token_privileges">TOKEN_PRIVILEGES</a> structure that contains the token's privileges.
</td>
</tr>
<tr>
<td>
<b>TokenSessionId</b>
</td>
<td>
The buffer receives a <b>DWORD</b> value (not a pointer to it) that indicates the Terminal Services session identifier that is associated with the token. If the token is associated with the Terminal Server console session, the session identifier is zero. A nonzero session identifier indicates a Terminal Services client session. In a non-Terminal Services environment, the session identifier is zero.
</td>
</tr>
<tr>
<td>
<b>TokenSource</b>
</td>
<td>
The buffer receives a <a href="ifsk.token_source">TOKEN_SOURCE</a> structure that contains the source of the token. TOKEN_QUERY_SOURCE access is needed to retrieve this information.
</td>
</tr>
<tr>
<td>
<b>TokenStatistics</b>
</td>
<td>
The buffer receives a <a href="ifsk.token_statistics">TOKEN_STATISTICS</a> structure that contains various token statistics.
</td>
</tr>
<tr>
<td>
<b>TokenType</b>
</td>
<td>
The buffer receives a <a href="ifsk.token_type">TOKEN_TYPE</a> value that indicates whether the token is a primary or impersonation token. 
</td>
</tr>
<tr>
<td>
<b>TokenUser</b>
</td>
<td>
The buffer receives a <a href="ifsk.token_user">TOKEN_USER</a> structure that contains the token's user account. 
</td>
</tr>
<tr>
<td>
<b>TokenIntegrityLevel</b>
</td>
<td>
The buffer receives a <b>DWORD</b> value (not a pointer to it) that specifies the token’s integrity level. 
</td>
</tr>
</table>
 

## -returns
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The call to <a href="ifsk.sequeryinformationtoken">SeQueryInformationToken</a> succeeded.
<dl>
<dt><b>STATUS_INVALID_INFO_CLASS</b></dt>
</dl>An invalid value was supplied for <i>TokenInformationClass</i>. 

 

## -remarks
For more information about security and access control, see the documentation about these topics in the Microsoft Windows SDK.

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
This routine is available on Microsoft Windows 2000 and later versions of the operating system. 
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
<a href="ifsk.psdereferenceimpersonationtoken">PsDereferenceImpersonationToken</a>
</dt>
<dt>
<a href="ifsk.psdereferenceprimarytoken">PsDereferencePrimaryToken</a>
</dt>
<dt>
<a href="ifsk.security_impersonation_level">SECURITY_IMPERSONATION_LEVEL</a>
</dt>
<dt>
<a href="ifsk.sequeryauthenticationidtoken">SeQueryAuthenticationIdToken</a>
</dt>
<dt>
<a href="ifsk.sequerysubjectcontexttoken">SeQuerySubjectContextToken</a>
</dt>
<dt>
<a href="ifsk.setokenisadmin">SeTokenIsAdmin</a>
</dt>
<dt>
<a href="ifsk.setokenisrestricted">SeTokenIsRestricted</a>
</dt>
<dt>
<a href="ifsk.sid">SID</a>
</dt>
<dt>
<a href="ifsk.token_default_dacl">TOKEN_DEFAULT_DACL</a>
</dt>
<dt>
<a href="ifsk.token_groups">TOKEN_GROUPS</a>
</dt>
<dt>
<a href="ifsk.token_information_class">TOKEN_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="ifsk.token_owner">TOKEN_OWNER</a>
</dt>
<dt>
<a href="ifsk.token_primary_group">TOKEN_PRIMARY_GROUP</a>
</dt>
<dt>
<a href="ifsk.token_privileges">TOKEN_PRIVILEGES</a>
</dt>
<dt>
<a href="ifsk.token_source">TOKEN_SOURCE</a>
</dt>
<dt>
<a href="ifsk.token_statistics">TOKEN_STATISTICS</a>
</dt>
<dt>
<a href="ifsk.token_type">TOKEN_TYPE</a>
</dt>
<dt>
<a href="ifsk.token_user">TOKEN_USER</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SeQueryInformationToken routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
