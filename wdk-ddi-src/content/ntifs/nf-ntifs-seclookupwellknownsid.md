---
UID: NF.ntifs.SecLookupWellKnownSid
title: SecLookupWellKnownSid
author: windows-driver-content
description: SecLookupWellKnownSid accepts a well-known security identifier (SID) type as input and retrieves the local security identifier (SID) for this well known SID.
old-location: ifsk\seclookupwellknownsid.htm
old-project: ifsk
ms.assetid: fbf06a28-d6f8-424c-95e0-ce24653cac64
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SecLookupWellKnownSid
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This SecLookupWellKnownSid function is only available starting with Windows Server 2003.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SecLookupWellKnownSid
req.alt-loc: Ksecdd.lib,Ksecdd.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ksecdd.lib
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
---

# SecLookupWellKnownSid function



## -description
<p><b>SecLookupWellKnownSid</b> accepts a well-known security identifier (SID) type as input and retrieves the local security identifier (SID) for this well known SID.</p>


## -syntax

````
NTSTATUS SecLookupWellKnownSid(
  _In_    WELL_KNOWN_SID_TYPE SidType,
  _Out_   PSID                Sid,
  _In_    ULONG               SidBufferSize,
  _Inout_ PULONG              SidSize
);
````


## -parameters
<dl>

### -param <i>SidType</i> [in]

<dd>
<p>An enumerated type that indicates the type of security identifier (SID) the function returns. This parameter can be one of the following enumerations for WELL_KNOWN_SID_TYPE:</p>
<p></p>
<dl>

### -param <a id="WinNullSid"></a><a id="winnullsid"></a><a id="WINNULLSID"></a>WinNullSid

<dd>
<p>This value indicates a null SID. </p>
</dd>

### -param <a id="WinWorldSid"></a><a id="winworldsid"></a><a id="WINWORLDSID"></a>WinWorldSid

<dd>
<p>This value indicates a SID that matches everyone.</p>
</dd>

### -param <a id="WinLocalSid"></a><a id="winlocalsid"></a><a id="WINLOCALSID"></a>WinLocalSid

<dd>
<p>This value indicates a local SID.</p>
</dd>

### -param <a id="WinCreatorOwnerSid_"></a><a id="wincreatorownersid_"></a><a id="WINCREATOROWNERSID_"></a>WinCreatorOwnerSid 

<dd>
<p>This value indicates a SID that matches the owner or creator of an object. This SID is used in inheritable access-control entries.</p>
</dd>

### -param <a id="WinCreatorGroupSid"></a><a id="wincreatorgroupsid"></a><a id="WINCREATORGROUPSID"></a>WinCreatorGroupSid

<dd>
<p>This value indicates a SID that matches the creator group of an object. This SID is used in inheritable access-control entries.</p>
</dd>

### -param <a id="WinCreatorOwnerServerSid"></a><a id="wincreatorownerserversid"></a><a id="WINCREATOROWNERSERVERSID"></a>WinCreatorOwnerServerSid

<dd>
<p>This value indicates a creator owner server SID. </p>
</dd>

### -param <a id="WinCreatorGroupServerSid"></a><a id="wincreatorgroupserversid"></a><a id="WINCREATORGROUPSERVERSID"></a>WinCreatorGroupServerSid

<dd>
<p>This value indicates a creator group server SID.</p>
</dd>

### -param <a id="WinNtAuthoritySid"></a><a id="winntauthoritysid"></a><a id="WINNTAUTHORITYSID"></a>WinNtAuthoritySid

<dd>
<p>This value indicates a SID for the Windows NT authority.</p>
</dd>

### -param <a id="WinDialupSid"></a><a id="windialupsid"></a><a id="WINDIALUPSID"></a>WinDialupSid

<dd>
<p>This value indicates a SID for a dial-up account.</p>
</dd>

### -param <a id="WinNetworkSid"></a><a id="winnetworksid"></a><a id="WINNETWORKSID"></a>WinNetworkSid

<dd>
<p>This value indicates a SID for a network account. This SID is added to the process of a token when it logs on across a network. The corresponding logon type is LOGON32_LOGON_NETWORK. </p>
</dd>

### -param <a id="WinBatchSid"></a><a id="winbatchsid"></a><a id="WINBATCHSID"></a>WinBatchSid

<dd>
<p>This value indicates a SID for a batch process. This SID is added to the process of a token when it logs on as a batch job. The corresponding logon type is LOGON32_LOGON_BATCH. </p>
</dd>

### -param <a id="WinInteractiveSid"></a><a id="wininteractivesid"></a><a id="WININTERACTIVESID"></a>WinInteractiveSid

<dd>
<p>This value indicates a SID for an interactive account. This SID is added to the process of a token when it logs on interactively. The corresponding logon type is LOGON32_LOGON_INTERACTIVE. </p>
</dd>

### -param <a id="WinServiceSid"></a><a id="winservicesid"></a><a id="WINSERVICESID"></a>WinServiceSid

<dd>
<p>This value indicates a SID for a service. This SID is added to the process of a token when it logs on as a service. The corresponding logon type is LOGON32_LOGON_SERVICE. </p>
</dd>

### -param <a id="WinAnonymousSid"></a><a id="winanonymoussid"></a><a id="WINANONYMOUSSID"></a>WinAnonymousSid

<dd>
<p>This value indicates a SID for the anonymous account. </p>
</dd>

### -param <a id="WinProxySid"></a><a id="winproxysid"></a><a id="WINPROXYSID"></a>WinProxySid

<dd>
<p>This value indicates a proxy SID. </p>
</dd>

### -param <a id="WinEnterpriseControllersSid"></a><a id="winenterprisecontrollerssid"></a><a id="WINENTERPRISECONTROLLERSSID"></a>WinEnterpriseControllersSid

<dd>
<p>This value indicates a SID for an enterprise controller.</p>
</dd>

### -param <a id="WinSelfSid"></a><a id="winselfsid"></a><a id="WINSELFSID"></a>WinSelfSid

<dd>
<p>This value indicates a SID for self.</p>
</dd>

### -param <a id="WinAuthenticatedUserSid"></a><a id="winauthenticatedusersid"></a><a id="WINAUTHENTICATEDUSERSID"></a>WinAuthenticatedUserSid

<dd>
<p>This value indicates a SID that matches any authenticated user.</p>
</dd>

### -param <a id="WinRestrictedCodeSid"></a><a id="winrestrictedcodesid"></a><a id="WINRESTRICTEDCODESID"></a>WinRestrictedCodeSid

<dd>
<p>This value indicates a SID for restricted code.</p>
</dd>

### -param <a id="WinTerminalServerSid"></a><a id="winterminalserversid"></a><a id="WINTERMINALSERVERSID"></a>WinTerminalServerSid

<dd>
<p>This value indicates a SID that matches a terminal server account.</p>
</dd>

### -param <a id="WinRemoteLogonIdSid"></a><a id="winremotelogonidsid"></a><a id="WINREMOTELOGONIDSID"></a>WinRemoteLogonIdSid

<dd>
<p>This value indicates a SID that matches remote logons.</p>
</dd>

### -param <a id="WinLogonIdsSid"></a><a id="winlogonidssid"></a><a id="WINLOGONIDSSID"></a>WinLogonIdsSid

<dd>
<p>This value indicates a SID that matches logon IDs.</p>
</dd>

### -param <a id="WinLocalSystemSid"></a><a id="winlocalsystemsid"></a><a id="WINLOCALSYSTEMSID"></a>WinLocalSystemSid

<dd>
<p>This value indicates a SID that matches the local system.</p>
</dd>

### -param <a id="WinLocalServiceSid"></a><a id="winlocalservicesid"></a><a id="WINLOCALSERVICESID"></a>WinLocalServiceSid

<dd>
<p>This value indicates a SID that matches a local service.</p>
</dd>

### -param <a id="WinNetworkServiceSid"></a><a id="winnetworkservicesid"></a><a id="WINNETWORKSERVICESID"></a>WinNetworkServiceSid

<dd>
<p>This value indicates a SID that matches a network service.</p>
</dd>

### -param <a id="WinBuiltinDomainSid"></a><a id="winbuiltindomainsid"></a><a id="WINBUILTINDOMAINSID"></a>WinBuiltinDomainSid

<dd>
<p>This value indicates a SID that matches the domain account.</p>
</dd>

### -param <a id="WinBuiltinAdministratorsSid"></a><a id="winbuiltinadministratorssid"></a><a id="WINBUILTINADMINISTRATORSSID"></a>WinBuiltinAdministratorsSid

<dd>
<p>This value indicates a SID that matches the administrator account.</p>
</dd>

### -param <a id="WinBuiltinUsersSid"></a><a id="winbuiltinuserssid"></a><a id="WINBUILTINUSERSSID"></a>WinBuiltinUsersSid

<dd>
<p>This value indicates a SID that matches built-in user accounts. </p>
</dd>

### -param <a id="WinBuiltinGuestsSid"></a><a id="winbuiltinguestssid"></a><a id="WINBUILTINGUESTSSID"></a>WinBuiltinGuestsSid

<dd>
<p>This value indicates a SID that matches the guest account.</p>
</dd>

### -param <a id="WinBuiltinPowerUsersSid"></a><a id="winbuiltinpoweruserssid"></a><a id="WINBUILTINPOWERUSERSSID"></a>WinBuiltinPowerUsersSid

<dd>
<p>This value indicates a SID that matches the power users group.</p>
</dd>

### -param <a id="WinBuiltinAccountOperatorsSid"></a><a id="winbuiltinaccountoperatorssid"></a><a id="WINBUILTINACCOUNTOPERATORSSID"></a>WinBuiltinAccountOperatorsSid

<dd>
<p>This value indicates a SID that matches the account operators account.</p>
</dd>

### -param <a id="WinBuiltinSystemOperatorsSid"></a><a id="winbuiltinsystemoperatorssid"></a><a id="WINBUILTINSYSTEMOPERATORSSID"></a>WinBuiltinSystemOperatorsSid

<dd>
<p>This value indicates a SID that matches the system operators group.</p>
</dd>

### -param <a id="WinBuiltinPrintOperatorsSid"></a><a id="winbuiltinprintoperatorssid"></a><a id="WINBUILTINPRINTOPERATORSSID"></a>WinBuiltinPrintOperatorsSid

<dd>
<p>This value indicates a SID that matches the print operators group.</p>
</dd>

### -param <a id="WinBuiltinBackupOperatorsSid"></a><a id="winbuiltinbackupoperatorssid"></a><a id="WINBUILTINBACKUPOPERATORSSID"></a>WinBuiltinBackupOperatorsSid

<dd>
<p>This value indicates a SID that matches the backup operators group.</p>
</dd>

### -param <a id="WinBuiltinReplicatorSid"></a><a id="winbuiltinreplicatorsid"></a><a id="WINBUILTINREPLICATORSID"></a>WinBuiltinReplicatorSid

<dd>
<p>This value indicates a SID that matches the replicator account.</p>
</dd>

### -param <a id="WinBuiltinPreWindows2000CompatibleAccessSid"></a><a id="winbuiltinprewindows2000compatibleaccesssid"></a><a id="WINBUILTINPREWINDOWS2000COMPATIBLEACCESSSID"></a>WinBuiltinPreWindows2000CompatibleAccessSid

<dd>
<p>This value indicates a SID that matches pre-Windows 2000 compatible accounts.</p>
</dd>

### -param <a id="WinBuiltinRemoteDesktopUsersSid"></a><a id="winbuiltinremotedesktopuserssid"></a><a id="WINBUILTINREMOTEDESKTOPUSERSSID"></a>WinBuiltinRemoteDesktopUsersSid

<dd>
<p>This value indicates a SID that matches remote desktop users.</p>
</dd>

### -param <a id="WinBuiltinNetworkConfigurationOperatorsSid"></a><a id="winbuiltinnetworkconfigurationoperatorssid"></a><a id="WINBUILTINNETWORKCONFIGURATIONOPERATORSSID"></a>WinBuiltinNetworkConfigurationOperatorsSid

<dd>
<p>This value indicates a SID that matches the network operators group.</p>
</dd>

### -param <a id="WinAccountAdministratorSid"></a><a id="winaccountadministratorsid"></a><a id="WINACCOUNTADMINISTRATORSID"></a>WinAccountAdministratorSid

<dd>
<p>This value indicates a SID that matches the account administrators group.</p>
</dd>

### -param <a id="WinAccountGuestSid"></a><a id="winaccountguestsid"></a><a id="WINACCOUNTGUESTSID"></a>WinAccountGuestSid

<dd>
<p>This value indicates a SID that matches the account guest group.</p>
</dd>

### -param <a id="WinAccountKrbtgtSid"></a><a id="winaccountkrbtgtsid"></a><a id="WINACCOUNTKRBTGTSID"></a>WinAccountKrbtgtSid

<dd>
<p>This value indicates a SID that matches account Kerberos target group.</p>
</dd>

### -param <a id="WinAccountDomainAdminsSid"></a><a id="winaccountdomainadminssid"></a><a id="WINACCOUNTDOMAINADMINSSID"></a>WinAccountDomainAdminsSid

<dd>
<p>This value indicates a SID that matches the account domain administrator group.</p>
</dd>

### -param <a id="WinAccountDomainUsersSid"></a><a id="winaccountdomainuserssid"></a><a id="WINACCOUNTDOMAINUSERSSID"></a>WinAccountDomainUsersSid

<dd>
<p>This value indicates a SID that matches the account domain users group.</p>
</dd>

### -param <a id="WinAccountDomainGuestsSid"></a><a id="winaccountdomainguestssid"></a><a id="WINACCOUNTDOMAINGUESTSSID"></a>WinAccountDomainGuestsSid

<dd>
<p>This value indicates a SID that matches the account domain guests group.</p>
</dd>

### -param <a id="WinAccountComputersSid"></a><a id="winaccountcomputerssid"></a><a id="WINACCOUNTCOMPUTERSSID"></a>WinAccountComputersSid

<dd>
<p>This value indicates a SID that matches the account computer group.</p>
</dd>

### -param <a id="WinAccountControllersSid"></a><a id="winaccountcontrollerssid"></a><a id="WINACCOUNTCONTROLLERSSID"></a>WinAccountControllersSid

<dd>
<p>This value indicates a SID that matches the account controller group.</p>
</dd>

### -param <a id="WinAccountCertAdminsSid"></a><a id="winaccountcertadminssid"></a><a id="WINACCOUNTCERTADMINSSID"></a>WinAccountCertAdminsSid

<dd>
<p>This value indicates a SID that matches the certificate administrators group. </p>
</dd>

### -param <a id="WinAccountSchemaAdminsSid"></a><a id="winaccountschemaadminssid"></a><a id="WINACCOUNTSCHEMAADMINSSID"></a>WinAccountSchemaAdminsSid

<dd>
<p>This value indicates a SID that matches the schema administrators group.</p>
</dd>

### -param <a id="WinAccountEnterpriseAdminsSid"></a><a id="winaccountenterpriseadminssid"></a><a id="WINACCOUNTENTERPRISEADMINSSID"></a>WinAccountEnterpriseAdminsSid

<dd>
<p>This value indicates a SID that matches the enterprise administrators group.</p>
</dd>

### -param <a id="WinAccountPolicyAdminsSid"></a><a id="winaccountpolicyadminssid"></a><a id="WINACCOUNTPOLICYADMINSSID"></a>WinAccountPolicyAdminsSid

<dd>
<p>This value indicates a SID that matches the policy administrators group.</p>
</dd>

### -param <a id="WinAccountRasAndIasServersSid"></a><a id="winaccountrasandiasserverssid"></a><a id="WINACCOUNTRASANDIASSERVERSSID"></a>WinAccountRasAndIasServersSid

<dd>
<p>This value indicates a SID that matches the RAS and IAS server account.</p>
</dd>

### -param <a id="WinNTLMAuthenticationSid"></a><a id="winntlmauthenticationsid"></a><a id="WINNTLMAUTHENTICATIONSID"></a>WinNTLMAuthenticationSid

<dd>
<p>This value indicates a SID present when the Microsoft NTLM authentication package authenticated the client.</p>
</dd>

### -param <a id="WinDigestAuthenticationSid"></a><a id="windigestauthenticationsid"></a><a id="WINDIGESTAUTHENTICATIONSID"></a>WinDigestAuthenticationSid

<dd>
<p>This value indicates a SID present when the Microsoft Digest authentication package authenticated the client.</p>
</dd>

### -param <a id="WinSChannelAuthenticationSid"></a><a id="winschannelauthenticationsid"></a><a id="WINSCHANNELAUTHENTICATIONSID"></a>WinSChannelAuthenticationSid

<dd>
<p>This value indicates a SID present when the Secure Channel (SSL/TLS) authentication package authenticated the client.</p>
</dd>

### -param <a id="WinThisOrganizationSid"></a><a id="winthisorganizationsid"></a><a id="WINTHISORGANIZATIONSID"></a>WinThisOrganizationSid

<dd>
<p>This value indicates a SID present when the user authenticated from within the forest or across a trust that does not have the selective authentication option enabled. If this SID is present, then WinOtherOrganizationSid cannot be present.</p>
</dd>

### -param <a id="WinOtherOrganizationSid"></a><a id="winotherorganizationsid"></a><a id="WINOTHERORGANIZATIONSID"></a>WinOtherOrganizationSid

<dd>
<p>This value indicates a SID present when the user authenticated across a forest with the selective authentication option enabled. If this SID is present, then WinThisOrganizationSid cannot be present.</p>
</dd>

### -param <a id="WinBuiltinIncomingForestTrustBuildersSid"></a><a id="winbuiltinincomingforesttrustbuilderssid"></a><a id="WINBUILTININCOMINGFORESTTRUSTBUILDERSSID"></a>WinBuiltinIncomingForestTrustBuildersSid

<dd>
<p>This value indicates a SID that allows a user to create incoming forest trusts. It is added to the token of users who are a member of the Incoming Forest Trust Builders built-in group in the root domain of the forest.</p>
</dd>

### -param <a id="WinBuiltinPerfMonitoringUsersSid"></a><a id="winbuiltinperfmonitoringuserssid"></a><a id="WINBUILTINPERFMONITORINGUSERSSID"></a>WinBuiltinPerfMonitoringUsersSid

<dd>
<p>This value indicates a SID that matches the performance monitor user group.</p>
</dd>

### -param <a id="WinBuiltinPerfLoggingUsersSid"></a><a id="winbuiltinperflogginguserssid"></a><a id="WINBUILTINPERFLOGGINGUSERSSID"></a>WinBuiltinPerfLoggingUsersSid

<dd>
<p>This value indicates a SID that matches the performance log user group.</p>
</dd>

### -param <a id="WinBuiltinAuthorizationAccessSid"></a><a id="winbuiltinauthorizationaccesssid"></a><a id="WINBUILTINAUTHORIZATIONACCESSSID"></a>WinBuiltinAuthorizationAccessSid

<dd>
<p>This value indicates a SID that matches the Windows Authorization Access group.</p>
</dd>

### -param <a id="WinBuiltinTerminalServerLicenseServersSid"></a><a id="winbuiltinterminalserverlicenseserverssid"></a><a id="WINBUILTINTERMINALSERVERLICENSESERVERSSID"></a>WinBuiltinTerminalServerLicenseServersSid

<dd>
<p>This value indicates a SID is present in a server that can issue Terminal Server licenses.</p>
</dd>

### -param <a id="WinBuiltinDCOMUsersSid"></a><a id="winbuiltindcomuserssid"></a><a id="WINBUILTINDCOMUSERSSID"></a>WinBuiltinDCOMUsersSid

<dd>
<p>This value indicates a SID that matches the DCOM users group.</p>
</dd>
</dl>
</dd>

### -param <i>Sid</i> [out]

<dd>
<p>
      A pointer to a buffer that receives the SID structure that corresponds to the <i>SidType</i> parameter. If this parameter is <b>NULL</b>, <i>SidBufferSize</i> must be zero. 
     </p>
</dd>

### -param <i>SidBufferSize</i> [in]

<dd>
<p>A variable that specifies the size of the <i>Sid</i> buffer in bytes.</p>
</dd>

### -param <i>SidSize</i> [in, out]

<dd>
<p>An optional pointer to a variable that specifies the size of the <i>Sid</i> buffer. If the function fails because the buffer is too small or if <i>SidBufferSize</i> is zero, this variable receives the required buffer size. On success, this variable contains the size of the returned <i>Sid</i></p>
</dd>
</dl>

## -returns
<p><b>SecLookupWellKnownSid</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: </p><dl>
<dt><b>SEC_E_INTERNAL_ERROR</b></dt>
</dl><p>An internal error occurred while trying to connect to the Local System Authority (LSA) or the local procedure call (LPC) to the security provider failed. </p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The process ID associated with the currently executing thread does not match the current process ID. </p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer size for the <i>Sid</i>, the <i>SidBufferSize</i> parameter, was too small.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>A <b>NULL</b> pointer was passed for <i>Sid</i> parameter or a well-known SID could not be found for the <i>SidType</i> specified. </p><dl>
<dt><b>STATUS_PROCESS_IS_TERMINATING</b></dt>
</dl><p>This process has terminated so it is not possible to establish a local procedure call (LPC) connection.</p>

<p> </p>

## -remarks
<p><b>SecLookupWellKnownSid</b> attempts to find a well known SID using a <i>SidType</i> parameter. In addition to looking up well-known SIDs on the local machine, <b>SecLookupWellKnownSid</b> can look up well-known SIDs on the local domain. <b>SecLookupWellKnownSid</b>first checks a list of well-known local SIDs. If the <i>SidType</i> does not correspond to a local well-known SID, the function checks for well-known SIDs on the primary domain. </p>

<p>If the function cannot find the well known SID for the <i>SidType</i> specified, <b>SecLookupWellKnownSid</b> fails. This can occur if a network time-out prevents the function from finding the SID on the primary domain. It also occurs for a <i>SidType</i> that has no corresponding well-known SID.</p>

<p><b>SecLookupWellKnownSid</b> is equivalent to the Win32   <b>CreateWellKnownSid</b> function. For user-mode applications, the WELL_KNOWN_SID_TYPE enumeration is defined in <i>winbase.h</i>.</p>

<p><b>SecLookupWellKnownSid</b> is exported by the ksecdd driver, which implements this function by using user-mode helper services. Accordingly, the use of this function within file systems must obey the usual rules for communication with user-mode services. <b>SecLookupWellKnownSid</b> cannot be used during paging file I/O. </p>

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
<p>This SecLookupWellKnownSid function is only available starting with Windows Server 2003.</p>
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
<dt>Ksecdd.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-seclookupaccountname.md">SecLookupAccountName</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-seclookupaccountsid.md">SecLookupAccountSid</a>
</dt>
<dt>
<a href="ifsk.sid">SID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SecLookupWellKnownSid function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
