---
UID: NE.ntifs._TOKEN_INFORMATION_CLASS
title: TOKEN_INFORMATION_CLASS
author: windows-driver-content
description: The TOKEN_INFORMATION_CLASS enumeration type contains values that specify the type of information being assigned to or retrieved from an access token.
old-location: ifsk\token_information_class.htm
ms.assetid: dd2323fa-2c58-462e-905f-3b201ef0c343
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: ifsk
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
ms.keywords: VOLUME_READ_PLEX_INPUT, VOLUME_READ_PLEX_INPUT, *PVOLUME_READ_PLEX_INPUT
req.iface: 
---

# TOKEN_INFORMATION_CLASS enumeration



## -description
<p>The <b>TOKEN_INFORMATION_CLASS</b> enumeration type contains values that specify the type of information being assigned to or retrieved from an access token. </p>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556690">SeQueryInformationToken</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567055">ZwQueryInformationToken</a> use <b>TOKEN_INFORMATION_CLASS</b> values to indicate the type of token information to retrieve. </p>


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

### -field <a id="TokenUser"></a><a id="tokenuser"></a><a id="TOKENUSER"></a><b>TokenUser</b>

<dd>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556855">TOKEN_USER</a> structure containing the token's user account. </p>
</dd>

### -field <a id="TokenGroups"></a><a id="tokengroups"></a><a id="TOKENGROUPS"></a><b>TokenGroups</b>

<dd>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556834">TOKEN_GROUPS</a> structure containing the group accounts associated with the token. </p>
</dd>

### -field <a id="TokenPrivileges"></a><a id="tokenprivileges"></a><a id="TOKENPRIVILEGES"></a><b>TokenPrivileges</b>

<dd>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556846">TOKEN_PRIVILEGES</a> structure containing the token's privileges. </p>
</dd>

### -field <a id="TokenOwner"></a><a id="tokenowner"></a><a id="TOKENOWNER"></a><b>TokenOwner</b>

<dd>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556842">TOKEN_OWNER</a> structure containing the default owner SID for newly created objects. </p>
</dd>

### -field <a id="TokenPrimaryGroup"></a><a id="tokenprimarygroup"></a><a id="TOKENPRIMARYGROUP"></a><b>TokenPrimaryGroup</b>

<dd>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556845">TOKEN_PRIMARY_GROUP</a> structure containing the default primary group SID for newly created objects. </p>
</dd>

### -field <a id="TokenDefaultDacl"></a><a id="tokendefaultdacl"></a><a id="TOKENDEFAULTDACL"></a><b>TokenDefaultDacl</b>

<dd>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556831">TOKEN_DEFAULT_DACL</a> structure containing the default discretionary ACL (DACL)) for newly created objects. </p>
</dd>

### -field <a id="TokenSource"></a><a id="tokensource"></a><a id="TOKENSOURCE"></a><b>TokenSource</b>

<dd>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556848">TOKEN_SOURCE</a> structure containing the source of the token. TOKEN_QUERY_SOURCE access is needed to retrieve this information. </p>
</dd>

### -field <a id="TokenType"></a><a id="tokentype"></a><a id="TOKENTYPE"></a><b>TokenType</b>

<dd>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556851">TOKEN_TYPE</a> value indicating whether the token is a primary or impersonation token. </p>
</dd>

### -field <a id="TokenImpersonationLevel"></a><a id="tokenimpersonationlevel"></a><a id="TOKENIMPERSONATIONLEVEL"></a><b>TokenImpersonationLevel</b>

<dd>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556631">SECURITY_IMPERSONATION_LEVEL</a> value indicating the impersonation level of the token. If the access token is not an impersonation token, the call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556690">SeQueryInformationToken</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567055">ZwQueryInformationToken</a> fails. </p>
</dd>

### -field <a id="TokenStatistics"></a><a id="tokenstatistics"></a><a id="TOKENSTATISTICS"></a><b>TokenStatistics</b>

<dd>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556849">TOKEN_STATISTICS</a> structure containing various token statistics. </p>
</dd>

### -field <a id="TokenRestrictedSids"></a><a id="tokenrestrictedsids"></a><a id="TOKENRESTRICTEDSIDS"></a><b>TokenRestrictedSids</b>

<dd>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556834">TOKEN_GROUPS</a> structure containing the list of restricting SIDs in a restricted token. This value is valid starting with Windows Vista.</p>
</dd>

### -field <a id="TokenSessionId"></a><a id="tokensessionid"></a><a id="TOKENSESSIONID"></a><b>TokenSessionId</b>

<dd>
<p>The buffer receives a DWORD value that indicates the Terminal Services session identifier associated with the token. If the token is associated with the Terminal Server console session, the session identifier is zero. A nonzero session identifier indicates a Terminal Services client session. In a non-Terminal Services environment, the session identifier is zero. This value is valid starting with Windows Vista.</p>
</dd>

### -field <a id="TokenGroupsAndPrivileges"></a><a id="tokengroupsandprivileges"></a><a id="TOKENGROUPSANDPRIVILEGES"></a><b>TokenGroupsAndPrivileges</b>

<dd>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556836">TOKEN_GROUPS_AND_PRIVILEGES</a> structure that contains the user SID, the group accounts, the restricted SIDs, and the authentication ID associated with the token. This value is valid starting with Windows Vista.</p>
</dd>

### -field <a id="TokenSessionReference"></a><a id="tokensessionreference"></a><a id="TOKENSESSIONREFERENCE"></a><b>TokenSessionReference</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="TokenSandBoxInert"></a><a id="tokensandboxinert"></a><a id="TOKENSANDBOXINERT"></a><b>TokenSandBoxInert</b>

<dd>
<p>The buffer receives a DWORD value that is nonzero if the token includes the SANDBOX_INERT flag. This value is valid starting with Windows Vista.</p>
</dd>

### -field <a id="TokenAuditPolicy"></a><a id="tokenauditpolicy"></a><a id="TOKENAUDITPOLICY"></a><b>TokenAuditPolicy</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="TokenOrigin"></a><a id="tokenorigin"></a><a id="TOKENORIGIN"></a><b>TokenOrigin</b>

<dd>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556839">TOKEN_ORIGIN</a> value. </p>
<p>If the token resulted from a logon that used explicit credentials, such as passing a name, domain, and password to the user-mode <a href="security.logonuser">LogonUser</a> function, then the <b>TOKEN_ORIGIN</b> structure will contain the ID of the logon session that created it.</p>
<p>If the token resulted from network authentication, such as a call to user-mode <b>AcceptSecurityContext</b> function or a call to user-mode <b>LogonUser</b> function with dwLogonType set to LOGON32_LOGON_NETWORK or LOGON32_LOGON_NETWORK_CLEARTEXT, then this value will be zero.</p>
<p> This value is valid starting with Windows Server 2003.</p>
</dd>

### -field <a id="TokenLinkedToken"></a><a id="tokenlinkedtoken"></a><a id="TOKENLINKEDTOKEN"></a><b>TokenLinkedToken</b>

<dd>
<p>The buffer receives a <a href="security.token_linked_token">TOKEN_LINKED_TOKEN</a> structure that contains a handle to another token that is linked to this token. This value is valid starting with Windows Vista.</p>
</dd>

### -field <a id="TokenElevation"></a><a id="tokenelevation"></a><a id="TOKENELEVATION"></a><b>TokenElevation</b>

<dd>
<p>The buffer receives a <a href="security.token_elevation">TOKEN_ELEVATION</a> structure that specifies whether the token is elevated. This value is valid starting with Windows Vista.</p>
</dd>

### -field <a id="TokenHasRestrictions"></a><a id="tokenhasrestrictions"></a><a id="TOKENHASRESTRICTIONS"></a><b>TokenHasRestrictions</b>

<dd>
<p>The buffer receives a <b>DWORD</b> value that is nonzero if the token has ever been filtered. This value is valid starting with Windows Vista.</p>
</dd>

### -field <a id="TokenAccessInformation"></a><a id="tokenaccessinformation"></a><a id="TOKENACCESSINFORMATION"></a><b>TokenAccessInformation</b>

<dd>
<p>The buffer receives a <a href="security.token_access_information">TOKEN_ACCESS_INFORMATION</a> structure that specifies  security information contained in the token. This value is valid starting with Windows Vista.</p>
</dd>

### -field <a id="TokenVirtualizationAllowed"></a><a id="tokenvirtualizationallowed"></a><a id="TOKENVIRTUALIZATIONALLOWED"></a><b>TokenVirtualizationAllowed</b>

<dd>
<p>The buffer receives a <b>DWORD</b> value that is nonzero if  <a href="security.v_gly#_security_virtualization_gly#_security_virtualization_gly"><i>virtualization</i></a> is allowed for the token. This value is valid starting with Windows Vista.</p>
</dd>

### -field <a id="TokenVirtualizationEnabled"></a><a id="tokenvirtualizationenabled"></a><a id="TOKENVIRTUALIZATIONENABLED"></a><b>TokenVirtualizationEnabled</b>

<dd>
<p>The buffer receives a <b>DWORD</b> value that is nonzero if  <a href="security.v_gly#_security_virtualization_gly#_security_virtualization_gly"><i>virtualization</i></a> is enabled for the token. This value is valid starting with Windows Vista.</p>
</dd>

### -field <a id="TokenIntegrityLevel"></a><a id="tokenintegritylevel"></a><a id="TOKENINTEGRITYLEVEL"></a><b>TokenIntegrityLevel</b>

<dd>
<p>The buffer receives a <a href="security.token_mandatory_label">TOKEN_MANDATORY_LABEL</a> structure that specifies the token's integrity level. This value is valid starting with Windows Vista. For <a href="https://msdn.microsoft.com/library/windows/hardware/ff556690">SeQueryInformationToken</a> the output is the actual integrity level  (<b>DWORD</b>).</p>
</dd>

### -field <a id="TokenUIAccess"></a><a id="tokenuiaccess"></a><a id="TOKENUIACCESS"></a><b>TokenUIAccess</b>

<dd>
<p>The buffer receives a <b>DWORD</b> value that is nonzero if  the token has the UIAccess flag set. This value is valid starting with Windows Vista.</p>
</dd>

### -field <a id="TokenMandatoryPolicy"></a><a id="tokenmandatorypolicy"></a><a id="TOKENMANDATORYPOLICY"></a><b>TokenMandatoryPolicy</b>

<dd>
<p>The buffer receives a <a href="security.token_mandatory_policy">TOKEN_MANDATORY_POLICY</a> structure that specifies the token's mandatory integrity policy. This value is valid starting with Windows Vista.</p>
</dd>

### -field <a id="TokenLogonSid"></a><a id="tokenlogonsid"></a><a id="TOKENLOGONSID"></a><b>TokenLogonSid</b>

<dd>
<p>The buffer receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556834">TOKEN_GROUPS</a> structure that specifies the token's logon SID. This value is valid starting with Windows Vista.</p>
</dd>

### -field <a id="TokenIsAppContainer"></a><a id="tokenisappcontainer"></a><a id="TOKENISAPPCONTAINER"></a><b>TokenIsAppContainer</b>

<dd>
<p>The buffer receives a <b>DWORD</b> value that is nonzero if  the token has the application container flag set. This value is valid starting with Windows 8.</p>
</dd>

### -field <a id="TokenCapabilities"></a><a id="tokencapabilities"></a><a id="TOKENCAPABILITIES"></a><b>TokenCapabilities</b>

<dd>
<p>The buffer receives a <b>TOKEN_GROUPS</b> structure and an array of <b>SID_AND_ATTRIBUTES</b> structures for each token capability. This value is valid starting with Windows 8.</p>
</dd>

### -field <a id="TokenAppContainerSid"></a><a id="tokenappcontainersid"></a><a id="TOKENAPPCONTAINERSID"></a><b>TokenAppContainerSid</b>

<dd>
<p>The buffer receives a <b>TOKEN_APPCONTAINER_INFORMATION</b> structure that contains the AppContainerSid associated with the token. If the token is not associated with an app container, the TokenAppContainer member of the <b>TOKEN_APPCONTAINER_INFORMATION</b> structure points to NULL. This value is valid starting with Windows 8.</p>
</dd>

### -field <a id="TokenAppContainerNumber"></a><a id="tokenappcontainernumber"></a><a id="TOKENAPPCONTAINERNUMBER"></a><b>TokenAppContainerNumber</b>

<dd>
<p>The buffer receives a <b>DWORD</b> value that is the application container number. This value is valid starting with Windows 8.</p>
</dd>

### -field <a id="TokenUserClaimAttributes"></a><a id="tokenuserclaimattributes"></a><a id="TOKENUSERCLAIMATTRIBUTES"></a><b>TokenUserClaimAttributes</b>

<dd>
<p>The buffer receives a <a href="security.token_mandatory_policy">CLAIM_SECURITY_ATTRIBUTES_INFORMATION</a> structure that specifies the user's claim attributes. This value is valid starting with Windows 8.</p>
</dd>

### -field <a id="TokenDeviceClaimAttributes"></a><a id="tokendeviceclaimattributes"></a><a id="TOKENDEVICECLAIMATTRIBUTES"></a><b>TokenDeviceClaimAttributes</b>

<dd>
<p>The buffer receives a <a href="security.token_mandatory_policy">CLAIM_SECURITY_ATTRIBUTES_INFORMATION</a> structure that specifies the device's claim attributes. This value is valid starting with Windows 8.</p>
</dd>

### -field <a id="TokenRestrictedUserClaimAttributes"></a><a id="tokenrestricteduserclaimattributes"></a><a id="TOKENRESTRICTEDUSERCLAIMATTRIBUTES"></a><b>TokenRestrictedUserClaimAttributes</b>

<dd>
<p>Reserved for system use. </p>
</dd>

### -field <a id="TokenRestrictedDeviceClaimAttributes"></a><a id="tokenrestricteddeviceclaimattributes"></a><a id="TOKENRESTRICTEDDEVICECLAIMATTRIBUTES"></a><b>TokenRestrictedDeviceClaimAttributes</b>

<dd>
<p>Reserved for system use. </p>
</dd>

### -field <a id="TokenDeviceGroups"></a><a id="tokendevicegroups"></a><a id="TOKENDEVICEGROUPS"></a><b>TokenDeviceGroups</b>

<dd>
<p>The buffer receives a <b>TOKEN_GROUPS</b> structure and an array of <b>SID_AND_ATTRIBUTES</b> structures for each device group. This value is valid starting with Windows 8.</p>
</dd>

### -field <a id="TokenRestrictedDeviceGroups"></a><a id="tokenrestricteddevicegroups"></a><a id="TOKENRESTRICTEDDEVICEGROUPS"></a><b>TokenRestrictedDeviceGroups</b>

<dd>
<p>Reserved for system use. </p>
</dd>

### -field <a id="TokenSecurityAttributes"></a><a id="tokensecurityattributes"></a><a id="TOKENSECURITYATTRIBUTES"></a><b>TokenSecurityAttributes</b>

<dd>
<p>Reserved for system use. </p>
</dd>

### -field <a id="TokenIsRestricted"></a><a id="tokenisrestricted"></a><a id="TOKENISRESTRICTED"></a><b>TokenIsRestricted</b>

<dd>
<p>Reserved for system use. </p>
</dd>

### -field <a id="TokenProcessTrustLevel"></a><a id="tokenprocesstrustlevel"></a><a id="TOKENPROCESSTRUSTLEVEL"></a><b>TokenProcessTrustLevel</b>

<dd>
<p>Reserved for system use. </p>
</dd>

### -field <a id="MaxTokenInfoClass"></a><a id="maxtokeninfoclass"></a><a id="MAXTOKENINFOCLASS"></a><b>MaxTokenInfoClass</b>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538866">ACL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556631">SECURITY_IMPERSONATION_LEVEL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556654">SeFilterToken</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556690">SeQueryInformationToken</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556724">SeTokenIsRestricted</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556831">TOKEN_DEFAULT_DACL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556834">TOKEN_GROUPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556842">TOKEN_OWNER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556839">TOKEN_ORIGIN</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567055">ZwQueryInformationToken</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567102">ZwSetInformationToken</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20TOKEN_INFORMATION_CLASS enumeration%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
