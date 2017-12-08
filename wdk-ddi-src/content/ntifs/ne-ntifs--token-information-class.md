---
UID: NE.ntifs._TOKEN_INFORMATION_CLASS
title: TOKEN_INFORMATION_CLASS
author: windows-driver-content
description: The TOKEN_INFORMATION_CLASS enumeration type contains values that specify the type of information being assigned to or retrieved from an access token.
old-location: ifsk\token_information_class.htm
old-project: ifsk
ms.assetid: dd2323fa-2c58-462e-905f-3b201ef0c343
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: VOLUME_READ_PLEX_INPUT, VOLUME_READ_PLEX_INPUT, *PVOLUME_READ_PLEX_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TOKEN_INFORMATION_CLASS
req.alt-loc: ntifs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# TOKEN_INFORMATION_CLASS enumeration



## -description
<p>The <b>TOKEN_INFORMATION_CLASS</b> enumeration type contains values that specify the type of information being assigned to or retrieved from an access token. </p>
<p>
<a href="..\ntifs\nf-ntifs-sequeryinformationtoken.md">SeQueryInformationToken</a> and <a href="..\ntifs\nf-ntifs-zwqueryinformationtoken.md">ZwQueryInformationToken</a> use <b>TOKEN_INFORMATION_CLASS</b> values to indicate the type of token information to retrieve. </p>


## -syntax

````
typedef enum _TOKEN_INFORMATION_CLASS { 
  TokenUser                             = 1,
  TokenGroups                           = 2,
  TokenPrivileges                       = 3,
  TokenOwner                            = 4,
  TokenPrimaryGroup                     = 5,
  TokenDefaultDacl                      = 6,
  TokenSource                           = 7,
  TokenType                             = 8,
  TokenImpersonationLevel               = 9,
  TokenStatistics                       = 10,
  TokenRestrictedSids                   = 11,
  TokenSessionId                        = 12,
  TokenGroupsAndPrivileges              = 13,
  TokenSessionReference                 = 14,
  TokenSandBoxInert                     = 15,
  TokenAuditPolicy                      = 16,
  TokenOrigin                           = 17,
  TokenLinkedToken                      = 19,
  TokenElevation                        = 20,
  TokenHasRestrictions                  = 21,
  TokenAccessInformation                = 22,
  TokenVirtualizationAllowed            = 23,
  TokenVirtualizationEnabled            = 24,
  TokenIntegrityLevel                   = 25,
  TokenUIAccess                         = 26,
  TokenMandatoryPolicy                  = 27,
  TokenLogonSid                         = 28,
  TokenIsAppContainer                   = 29,
  TokenCapabilities                     = 30,
  TokenAppContainerSid                  = 31,
  TokenAppContainerNumber               = 32,
  TokenUserClaimAttributes              = 33,
  TokenDeviceClaimAttributes            = 34,
  TokenRestrictedUserClaimAttributes    = 35,
  TokenRestrictedDeviceClaimAttributes  = 36,
  TokenDeviceGroups                     = 37,
  TokenRestrictedDeviceGroups           = 38,
  TokenSecurityAttributes               = 39,
  TokenIsRestricted                     = 40,
  TokenProcessTrustLevel                = 41,
  MaxTokenInfoClass                     = 42
} TOKEN_INFORMATION_CLASS, *PTOKEN_INFORMATION_CLASS;
````


## -enum-fields
<dl>

### -field TokenUser

<dd>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-user.md">TOKEN_USER</a> structure containing the token's user account. </p>
</dd>

### -field TokenGroups

<dd>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-groups.md">TOKEN_GROUPS</a> structure containing the group accounts associated with the token. </p>
</dd>

### -field TokenPrivileges

<dd>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-privileges.md">TOKEN_PRIVILEGES</a> structure containing the token's privileges. </p>
</dd>

### -field TokenOwner

<dd>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-owner.md">TOKEN_OWNER</a> structure containing the default owner SID for newly created objects. </p>
</dd>

### -field TokenPrimaryGroup

<dd>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-primary-group.md">TOKEN_PRIMARY_GROUP</a> structure containing the default primary group SID for newly created objects. </p>
</dd>

### -field TokenDefaultDacl

<dd>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-default-dacl.md">TOKEN_DEFAULT_DACL</a> structure containing the default discretionary ACL (DACL)) for newly created objects. </p>
</dd>

### -field TokenSource

<dd>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-source.md">TOKEN_SOURCE</a> structure containing the source of the token. TOKEN_QUERY_SOURCE access is needed to retrieve this information. </p>
</dd>

### -field TokenType

<dd>
<p>The buffer receives a <a href="..\ntifs\ne-ntifs--token-type.md">TOKEN_TYPE</a> value indicating whether the token is a primary or impersonation token. </p>
</dd>

### -field TokenImpersonationLevel

<dd>
<p>The buffer receives a <a href="..\wudfddi\ne-wudfddi--security-impersonation-level.md">SECURITY_IMPERSONATION_LEVEL</a> value indicating the impersonation level of the token. If the access token is not an impersonation token, the call to <a href="..\ntifs\nf-ntifs-sequeryinformationtoken.md">SeQueryInformationToken</a> or <a href="..\ntifs\nf-ntifs-zwqueryinformationtoken.md">ZwQueryInformationToken</a> fails. </p>
</dd>

### -field TokenStatistics

<dd>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-statistics.md">TOKEN_STATISTICS</a> structure containing various token statistics. </p>
</dd>

### -field TokenRestrictedSids

<dd>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-groups.md">TOKEN_GROUPS</a> structure containing the list of restricting SIDs in a restricted token. This value is valid starting with Windows Vista.</p>
</dd>

### -field TokenSessionId

<dd>
<p>The buffer receives a DWORD value that indicates the Terminal Services session identifier associated with the token. If the token is associated with the Terminal Server console session, the session identifier is zero. A nonzero session identifier indicates a Terminal Services client session. In a non-Terminal Services environment, the session identifier is zero. This value is valid starting with Windows Vista.</p>
</dd>

### -field TokenGroupsAndPrivileges

<dd>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-groups-and-privileges.md">TOKEN_GROUPS_AND_PRIVILEGES</a> structure that contains the user SID, the group accounts, the restricted SIDs, and the authentication ID associated with the token. This value is valid starting with Windows Vista.</p>
</dd>

### -field TokenSessionReference

<dd>
<p>Reserved for system use.</p>
</dd>

### -field TokenSandBoxInert

<dd>
<p>The buffer receives a DWORD value that is nonzero if the token includes the SANDBOX_INERT flag. This value is valid starting with Windows Vista.</p>
</dd>

### -field TokenAuditPolicy

<dd>
<p>Reserved for system use.</p>
</dd>

### -field TokenOrigin

<dd>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-origin.md">TOKEN_ORIGIN</a> value. </p>
<p>If the token resulted from a logon that used explicit credentials, such as passing a name, domain, and password to the user-mode <a href="security.logonuser">LogonUser</a> function, then the <b>TOKEN_ORIGIN</b> structure will contain the ID of the logon session that created it.</p>
<p>If the token resulted from network authentication, such as a call to user-mode <b>AcceptSecurityContext</b> function or a call to user-mode <b>LogonUser</b> function with dwLogonType set to LOGON32_LOGON_NETWORK or LOGON32_LOGON_NETWORK_CLEARTEXT, then this value will be zero.</p>
<p> This value is valid starting with Windows Server 2003.</p>
</dd>

### -field TokenLinkedToken

<dd>
<p>The buffer receives a <a href="security.token_linked_token">TOKEN_LINKED_TOKEN</a> structure that contains a handle to another token that is linked to this token. This value is valid starting with Windows Vista.</p>
</dd>

### -field TokenElevation

<dd>
<p>The buffer receives a <a href="security.token_elevation">TOKEN_ELEVATION</a> structure that specifies whether the token is elevated. This value is valid starting with Windows Vista.</p>
</dd>

### -field TokenHasRestrictions

<dd>
<p>The buffer receives a <b>DWORD</b> value that is nonzero if the token has ever been filtered. This value is valid starting with Windows Vista.</p>
</dd>

### -field TokenAccessInformation

<dd>
<p>The buffer receives a <a href="security.token_access_information">TOKEN_ACCESS_INFORMATION</a> structure that specifies  security information contained in the token. This value is valid starting with Windows Vista.</p>
</dd>

### -field TokenVirtualizationAllowed

<dd>
<p>The buffer receives a <b>DWORD</b> value that is nonzero if  <a href="security.v_gly#_security_virtualization_gly#_security_virtualization_gly"><i>virtualization</i></a> is allowed for the token. This value is valid starting with Windows Vista.</p>
</dd>

### -field TokenVirtualizationEnabled

<dd>
<p>The buffer receives a <b>DWORD</b> value that is nonzero if  <a href="security.v_gly#_security_virtualization_gly#_security_virtualization_gly"><i>virtualization</i></a> is enabled for the token. This value is valid starting with Windows Vista.</p>
</dd>

### -field TokenIntegrityLevel

<dd>
<p>The buffer receives a <a href="security.token_mandatory_label">TOKEN_MANDATORY_LABEL</a> structure that specifies the token's integrity level. This value is valid starting with Windows Vista. For <a href="..\ntifs\nf-ntifs-sequeryinformationtoken.md">SeQueryInformationToken</a> the output is the actual integrity level  (<b>DWORD</b>).</p>
</dd>

### -field TokenUIAccess

<dd>
<p>The buffer receives a <b>DWORD</b> value that is nonzero if  the token has the UIAccess flag set. This value is valid starting with Windows Vista.</p>
</dd>

### -field TokenMandatoryPolicy

<dd>
<p>The buffer receives a <a href="security.token_mandatory_policy">TOKEN_MANDATORY_POLICY</a> structure that specifies the token's mandatory integrity policy. This value is valid starting with Windows Vista.</p>
</dd>

### -field TokenLogonSid

<dd>
<p>The buffer receives a <a href="..\ntifs\ns-ntifs--token-groups.md">TOKEN_GROUPS</a> structure that specifies the token's logon SID. This value is valid starting with Windows Vista.</p>
</dd>

### -field TokenIsAppContainer

<dd>
<p>The buffer receives a <b>DWORD</b> value that is nonzero if  the token has the application container flag set. This value is valid starting with Windows 8.</p>
</dd>

### -field TokenCapabilities

<dd>
<p>The buffer receives a <b>TOKEN_GROUPS</b> structure and an array of <b>SID_AND_ATTRIBUTES</b> structures for each token capability. This value is valid starting with Windows 8.</p>
</dd>

### -field TokenAppContainerSid

<dd>
<p>The buffer receives a <b>TOKEN_APPCONTAINER_INFORMATION</b> structure that contains the AppContainerSid associated with the token. If the token is not associated with an app container, the TokenAppContainer member of the <b>TOKEN_APPCONTAINER_INFORMATION</b> structure points to NULL. This value is valid starting with Windows 8.</p>
</dd>

### -field TokenAppContainerNumber

<dd>
<p>The buffer receives a <b>DWORD</b> value that is the application container number. This value is valid starting with Windows 8.</p>
</dd>

### -field TokenUserClaimAttributes

<dd>
<p>The buffer receives a <a href="security.token_mandatory_policy">CLAIM_SECURITY_ATTRIBUTES_INFORMATION</a> structure that specifies the user's claim attributes. This value is valid starting with Windows 8.</p>
</dd>

### -field TokenDeviceClaimAttributes

<dd>
<p>The buffer receives a <a href="security.token_mandatory_policy">CLAIM_SECURITY_ATTRIBUTES_INFORMATION</a> structure that specifies the device's claim attributes. This value is valid starting with Windows 8.</p>
</dd>

### -field TokenRestrictedUserClaimAttributes

<dd>
<p>Reserved for system use. </p>
</dd>

### -field TokenRestrictedDeviceClaimAttributes

<dd>
<p>Reserved for system use. </p>
</dd>

### -field TokenDeviceGroups

<dd>
<p>The buffer receives a <b>TOKEN_GROUPS</b> structure and an array of <b>SID_AND_ATTRIBUTES</b> structures for each device group. This value is valid starting with Windows 8.</p>
</dd>

### -field TokenRestrictedDeviceGroups

<dd>
<p>Reserved for system use. </p>
</dd>

### -field TokenSecurityAttributes

<dd>
<p>Reserved for system use. </p>
</dd>

### -field TokenIsRestricted

<dd>
<p>Reserved for system use. </p>
</dd>

### -field TokenProcessTrustLevel

<dd>
<p>Reserved for system use. </p>
</dd>

### -field MaxTokenInfoClass

<dd>
<p>The maximum value for this enumeration.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\ns-ntifs--acl.md">ACL</a>
</dt>
<dt>
<a href="..\wudfddi\ne-wudfddi--security-impersonation-level.md">SECURITY_IMPERSONATION_LEVEL</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-sefiltertoken.md">SeFilterToken</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-sequeryinformationtoken.md">SeQueryInformationToken</a>
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
<a href="..\ntifs\ns-ntifs--token-owner.md">TOKEN_OWNER</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-origin.md">TOKEN_ORIGIN</a>
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
<a href="..\ntifs\nf-ntifs-zwqueryinformationtoken.md">ZwQueryInformationToken</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwsetinformationtoken.md">ZwSetInformationToken</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20TOKEN_INFORMATION_CLASS enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
