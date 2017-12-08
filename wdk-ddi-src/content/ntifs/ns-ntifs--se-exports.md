---
UID: NS.ntifs._SE_EXPORTS
title: SE_EXPORTS
author: windows-driver-content
description: The SeExports structure is a large external static SE_EXPORTS structure that defines a number of well-known security constants for privilege values and security identifiers.
old-location: ifsk\seexports.htm
old-project: ifsk
ms.assetid: e6c398b4-f38f-4819-96f9-cefc3a728dbc
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: SE_EXPORTS, SE_EXPORTS, *PSE_EXPORTS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SE_EXPORTS
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
req.irql: 
req.iface: 
---

# SE_EXPORTS structure



## -description
<p>The <b>SeExports</b> structure is a large external static SE_EXPORTS structure that defines a number of well-known security constants for privilege values and security identifiers.</p>


## -syntax

````
typedef struct _SE_EXPORTS {
  LUID SeCreateTokenPrivilege;
  LUID SeAssignPrimaryTokenPrivilege;
  LUID SeLockMemoryPrivilege;
  LUID SeIncreaseQuotaPrivilege;
  LUID SeUnsolicitedInputPrivilege;
  LUID SeTcbPrivilege;
  LUID SeSecurityPrivilege;
  LUID SeTakeOwnershipPrivilege;
  LUID SeLoadDriverPrivilege;
  LUID SeCreatePagefilePrivilege;
  LUID SeIncreaseBasePriorityPrivilege;
  LUID SeSystemProfilePrivilege;
  LUID SeSystemtimePrivilege;
  LUID SeProfileSingleProcessPrivilege;
  LUID SeCreatePermanentPrivilege;
  LUID SeBackupPrivilege;
  LUID SeRestorePrivilege;
  LUID SeShutdownPrivilege;
  LUID SeDebugPrivilege;
  LUID SeAuditPrivilege;
  LUID SeSystemEnvironmentPrivilege;
  LUID SeChangeNotifyPrivilege;
  LUID SeRemoteShutdownPrivilege;
  PSID SeNullSid;
  PSID SeWorldSid;
  PSID SeLocalSid;
  PSID SeCreatorOwnerSid;
  PSID SeCreatorGroupSid;
  PSID SeNtAuthoritySid;
  PSID SeDialupSid;
  PSID SeNetworkSid;
  PSID SeBatchSid;
  PSID SeInteractiveSid;
  PSID SeLocalSystemSid;
  PSID SeAliasAdminsSid;
  PSID SeAliasUsersSid;
  PSID SeAliasGuestsSid;
  PSID SeAliasPowerUsersSid;
  PSID SeAliasAccountOpsSid;
  PSID SeAliasSystemOpsSid;
  PSID SeAliasPrintOpsSid;
  PSID SeAliasBackupOpsSid;
  PSID SeAuthenticatedUsersSid;
  PSID SeRestrictedSid;
  PSID SeAnonymousLogonSid;
  LUID SeUndockPrivilege;
  LUID SeSyncAgentPrivilege;
  LUID SeEnableDelegationPrivilege;
  PSID SeLocalServiceSid;
  PSID SeNetworkServiceSid;
  LUID SeManageVolumePrivilege;
  LUID SeImpersonatePrivilege;
  LUID SeCreateGlobalPrivilege;
  LUID SeTrustedCredManAccessPrivilege;
  LUID SeRelabelPrivilege;
  LUID SeIncreaseWorkingSetPrivilege;
  LUID SeTimeZonePrivilege;
  LUID SeCreateSymbolicLinkPrivilege;
  PSID SeIUserSid;
  PSID SeUntrustedMandatorySid;
  PSID SeLowMandatorySid;
  PSID SeMediumMandatorySid;
  PSID SeHighMandatorySid;
  PSID SeSystemMandatorySid;
  PSID SeOwnerRightsSid;
  PSID SeAllAppPackagesSid;
} SE_EXPORTS, *PSE_EXPORTS;
````


## -struct-fields
<dl>

### -field SeCreateTokenPrivilege

<dd>
<p>The privilege that is required to create a primary access token.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Create a token object".</p>
</dd>

### -field SeAssignPrimaryTokenPrivilege

<dd>
<p>The privilege that is required to assign the primary token of a process. The privilege allows a parent process to replace the access token that is associated with a child process.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Replace a process-level token".</p>
</dd>

### -field SeLockMemoryPrivilege

<dd>
<p>The privilege that is required to lock physical pages in memory. This privilege allows a process to keep data in physical memory, which prevents the system from paging the data to virtual memory on a disk.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Required to lock physical pages in memory".</p>
</dd>

### -field SeIncreaseQuotaPrivilege

<dd>
<p>The privilege that is required to increase the quota assigned to a process. The privilege allows a process that has access to a second process to increase the processor quota assigned to the second process. This privilege is useful for system tuning, but it can be abused.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Adjust memory quotas for a process".</p>
</dd>

### -field SeUnsolicitedInputPrivilege

<dd>
<p>The privilege that is required to read unsolicited input from a terminal device. This privilege is obsolete and unused. It has no effect on the system.</p>
</dd>

### -field SeTcbPrivilege

<dd>
<p>The privilege that identifies its holder as part of the trusted computer base. Typically, only low-level authentication services require this privilege. Some trusted protected subsystems are granted this privilege.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Act as part of the operating system".</p>
</dd>

### -field SeSecurityPrivilege

<dd>
<p>The privilege that is required to perform a number of security-related functions, such as controlling and viewing audit messages. This privilege identifies its holder as a security operator. This privilege allows a user to specify object access auditing options for individual resources, including files, Active Directory objects, and Registry keys. A user who has this privilege can also view and clear the security log from Event Viewer.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Manage auditing and security log".</p>
</dd>

### -field SeTakeOwnershipPrivilege

<dd>
<p>The privilege that is required to take ownership of an object without being granted discretionary access. This privilege allows the user to take ownership of any securable object in the system, including Active Directory objects, files and folders, printers, registry keys, processes, and threads. This privilege allows the owner value to be set only to those values that the holder might legitimately assign as the owner of an object. </p>
<p>User-mode applications represent this privilege as the following user-right string: "Take ownership of files or other objects".</p>
</dd>

### -field SeLoadDriverPrivilege

<dd>
<p>The privilege that is required to load or unload a device driver. This privilege allows a user to install and remove drivers for Plug and Play devices. This privilege is not required if a signed driver for the new hardware already exists in the <i>Driver.cab</i> file on the computer.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Load and unload device drivers".</p>
</dd>

### -field SeCreatePagefilePrivilege

<dd>
<p>The privilege that is required to create and change the size of a paging file.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Create a pagefile".</p>
</dd>

### -field SeIncreaseBasePriorityPrivilege

<dd>
<p>The privilege that is required to increase the base priority of a process. This privilege allows a user to increase the base priority class of a process. Increasing relative priority within a priority class is not a privileged operation and does not need this privilege.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Increase scheduling priority".</p>
</dd>

### -field SeSystemProfilePrivilege

<dd>
<p>The privilege that is required to gather profiling information for the entire system. The privilege allows a user to sample the performance of system processes.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Profile system performance".</p>
</dd>

### -field SeSystemtimePrivilege

<dd>
<p>The privilege that is required to modify the system time. This privilege allows the user to adjust the time on the computer's internal clock. This privilege is not required to change the time zone or other display characteristics of the system time.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Change the system time".</p>
</dd>

### -field SeProfileSingleProcessPrivilege

<dd>
<p>The privilege that is required to gather profiling information for a single process. The privilege allows a user to sample the performance of an application process.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Profile single process".</p>
</dd>

### -field SeCreatePermanentPrivilege

<dd>
<p>The privilege that is required to create a permanent object. This privilege allows a process to create a directory object in the object manager. This privilege is useful to kernel-mode components that extend the object namespace. Components that are running in kernel mode have this privilege inherently.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Create permanent shared objects".</p>
</dd>

### -field SeBackupPrivilege

<dd>
<p>The privilege that is required to perform backup operations. This privilege allows the user to circumvent file and directory permissions to back up the system. This privilege causes the system to grant all read access control to any file, regardless of the access control list (ACL) specified for the file. Any access request other than read is still evaluated with the ACL. This privilege is required by the user-mode <a href="base.regsavekey">RegSaveKey</a> and <a href="base.regsavekeyex">RegSaveKeyEx</a> routines. The following access rights are granted if this privilege is held:</p>
<ul>
<li>
<p>READ_CONTROL </p>
</li>
<li>
<p>ACCESS_SYSTEM_SECURITY </p>
</li>
<li>
<p>FILE_GENERIC_READ </p>
</li>
<li>
<p>FILE_TRAVERSE</p>
</li>
</ul>
<p>User-mode applications represent this privilege as the following user-right string: "Back up files and directories".</p>
</dd>

### -field SeRestorePrivilege

<dd>
<p>The privilege that is required to perform restore operations. This privilege allows a user to circumvent file and directory permissions when restoring backed-up files and directories and to set any valid security principal as the owner of an object. This privilege causes the system to grant all write access control to any file, regardless of the ACL specified for the file. Any access request other than write is still evaluated with the ACL. Additionally, this privilege enables you to set any valid user or group SID as the owner of a file. This privilege is required by the user-mode <a href="base.regloadkey">RegLoadKey</a> and <a href="base.regunloadkey">RegUnLoadKey</a> routines that add or remove a hive from the registry. The following access rights are granted if this privilege is held:</p>
<ul>
<li>
<p>WRITE_DAC </p>
</li>
<li>
<p>WRITE_OWNER </p>
</li>
<li>
<p>ACCESS_SYSTEM_SECURITY </p>
</li>
<li>
<p>FILE_GENERIC_WRITE </p>
</li>
<li>
<p>FILE_ADD_FILE </p>
</li>
<li>
<p>FILE_ADD_SUBDIRECTORY </p>
</li>
<li>
<p>DELETE</p>
</li>
</ul>
<p>User-mode applications represent this privilege as the following user-right string: "Restore files and directories".</p>
</dd>

### -field SeShutdownPrivilege

<dd>
<p>The privilege that is required to shut down a local system.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Shut down the system".</p>
</dd>

### -field SeDebugPrivilege

<dd>
<p>The privilege that is required to debug and adjust the memory of a process owned by another account. This privilege allows the user to attach a debugger to any process. This privilege provides access to sensitive and critical operating system components.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Debug programs".</p>
</dd>

### -field SeAuditPrivilege

<dd>
<p>The privilege that is required to generate audit-log entries in the security log. The security log can be used to trace unauthorized system access. This privilege should be given to secure servers.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Generate security audits". </p>
</dd>

### -field SeSystemEnvironmentPrivilege

<dd>
<p>The privilege required to modify the nonvolatile RAM of systems that use this type of memory to store configuration information. </p>
<p>User-mode applications represent this privilege as the following user-right string: "Modify firmware environment values".</p>
</dd>

### -field SeChangeNotifyPrivilege

<dd>
<p>The privilege that is required to receive notifications of changes to files or directories. This privilege allows the user to pass through folders to which the user otherwise has no access while navigating an object path in the NTFS file system or in the registry. This privilege does not allow the user to list the contents of a folder; it allows the user only to traverse its directories. This privilege causes the system to skip all traversal access checks. It is enabled by default for all users.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Bypass traverse checking".</p>
</dd>

### -field SeRemoteShutdownPrivilege

<dd>
<p>The privilege that is required to shut down a system by using a network request. This privilege allows a user to shut down a computer from a remote location on the network.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Force shutdown from a remote system".</p>
</dd>

### -field SeNullSid

<dd>
<p>The null SID. </p>
</dd>

### -field SeWorldSid

<dd>
<p>The SID that matches everyone.</p>
</dd>

### -field SeLocalSid

<dd>
<p>The local SID.</p>
</dd>

### -field SeCreatorOwnerSid

<dd>
<p>The SID that matches the owner or creator of an object. This SID is used in inheritable access control entries (ACEs).</p>
</dd>

### -field SeCreatorGroupSid

<dd>
<p>The SID that matches the creator group of an object. This SID is used in inheritable ACEs.</p>
</dd>

### -field SeNtAuthoritySid

<dd>
<p>The SID for the Microsoft Windows NT authority.</p>
</dd>

### -field SeDialupSid

<dd>
<p>The SID for a dial-up account.</p>
</dd>

### -field SeNetworkSid

<dd>
<p>The SID for a network account. This SID is added to the process of a token when it logs on across a network. The corresponding logon type is LOGON32_LOGON_NETWORK. </p>
</dd>

### -field SeBatchSid

<dd>
<p>The SID for a batch process. This SID is added to the process of a token when it logs on as a batch job. The corresponding logon type is LOGON32_LOGON_BATCH. </p>
</dd>

### -field SeInteractiveSid

<dd>
<p>The SID for an interactive account. This SID is added to the process of a token when it logs on interactively. The corresponding logon type is LOGON32_LOGON_INTERACTIVE. </p>
</dd>

### -field SeLocalSystemSid

<dd>
<p>The SID that matches the LocalSystem account, a predefined local account used by the Service Control Manager. This account is not recognized by the security subsystem. It has extensive privileges on the local computer and acts as the computer on the network. Its token includes the Windows NT AUTHORITY\SYSTEM and BUILTIN\Administrators SIDs; these accounts have access to most system objects. The name of the account in all locales is ".\LocalSystem". The name, "LocalSystem" or "ComputerName\LocalSystem" can also be used. This account does not have a password.</p>
<p>A service that runs in the context of the LocalSystem account inherits the security context of the Service Control Manager. The account is not associated with any logged-on user account. </p>
<p>The LocalSystem account has the following privileges:</p>
<ul>
<li>
<p>SE_ASSIGNPRIMARYTOKEN_NAME </p>
</li>
<li>
<p>SE_AUDIT_NAME </p>
</li>
<li>
<p>SE_BACKUP_NAME </p>
</li>
<li>
<p>SE_CHANGE_NOTIFY_NAME </p>
</li>
<li>
<p>SE_CREATE_PAGEFILE_NAME </p>
</li>
<li>
<p>SE_CREATE_PERMANENT_NAME </p>
</li>
<li>
<p>SE_CREATE_TOKEN_NAME </p>
</li>
<li>
<p>SE_DEBUG_NAME </p>
</li>
<li>
<p>SE_INC_BASE_PRIORITY_NAME </p>
</li>
<li>
<p>SE_INCREASE_QUOTA_NAME </p>
</li>
<li>
<p>SE_LOAD_DRIVER_NAME </p>
</li>
<li>
<p>SE_LOCK_MEMORY_NAME </p>
</li>
<li>
<p>SE_PROF_SINGLE_PROCESS_NAME </p>
</li>
<li>
<p>SE_RESTORE_NAME </p>
</li>
<li>
<p>SE_SECURITY_NAME </p>
</li>
<li>
<p>SE_SHUTDOWN_NAME </p>
</li>
<li>
<p>SE_SYSTEM_ENVIRONMENT_NAME </p>
</li>
<li>
<p>SE_SYSTEM_PROFILE_NAME </p>
</li>
<li>
<p>SE_SYSTEMTIME_NAME </p>
</li>
<li>
<p>SE_TAKE_OWNERSHIP_NAME </p>
</li>
<li>
<p>SE_TCB_NAME </p>
</li>
<li>
<p>SE_UNDOCK_NAME </p>
</li>
</ul>
<p>Most services do not need such a high privilege level. If your service does not need these privileges, and it is not an interactive service, consider using the LocalService account or the NetworkService account. </p>
</dd>

### -field SeAliasAdminsSid

<dd>
<p>The SID that matches the administrator account.</p>
</dd>

### -field SeAliasUsersSid

<dd>
<p>The SID that matches built-in user accounts. </p>
</dd>

### -field SeAliasGuestsSid

<dd>
<p>The SID that matches the guest account.</p>
</dd>

### -field SeAliasPowerUsersSid

<dd>
<p>The SID that matches the power users group.</p>
</dd>

### -field SeAliasAccountOpsSid

<dd>
<p>The SID that matches the account operators account.</p>
</dd>

### -field SeAliasSystemOpsSid

<dd>
<p>The SID that matches the system operators group.</p>
</dd>

### -field SeAliasPrintOpsSid

<dd>
<p>The SID that matches the print operators group.</p>
</dd>

### -field SeAliasBackupOpsSid

<dd>
<p>The SID that matches the backup operators group.</p>
</dd>

### -field SeAuthenticatedUsersSid

<dd>
<p>The SID that matches any authenticated user.</p>
</dd>

### -field SeRestrictedSid

<dd>
<p>The SID for restricted code.</p>
</dd>

### -field SeAnonymousLogonSid

<dd>
<p>The SID for the anonymous account. </p>
</dd>

### -field SeUndockPrivilege

<dd>
<p>The privilege that is required to remove a computer from a docking station. This privilege allows the user of a portable computer to undock the computer by clicking <b>Start</b>, and then clicking <b>Eject PC</b>.</p>
</dd>

### -field SeSyncAgentPrivilege

<dd>
<p>The privilege that is required to synchronize directory service data. This privilege allows a process to read all objects and properties in the directory, regardless of the protection that is set on the objects and properties. This privilege is required in order to use Lightweight Directory Access Protocol (LDAP) directory synchronization (Dirsync) services. This privilege is required for a domain controller to use the LDAP directory synchronization services. </p>
</dd>

### -field SeEnableDelegationPrivilege

<dd>
<p>The privilege that is required to enable computer and user accounts to be trusted for delegation.</p>
</dd>

### -field SeLocalServiceSid

<dd>
<p>The SID that matches the LocalService account, a predefined local account. The LocalService account has minimum privileges on the local computer and presents anonymous credentials on the network. The name of the account in all locales is "NT AUTHORITY\LocalService". This account does not have a password. The LocalService account has its own subkey under the HKEY_USERS registry key. Therefore, the HKEY_CURRENT_USER registry key is associated with the LocalService account.</p>
<p>The LocalService account has the following privileges:</p>
<ul>
<li>
<p>SE_AUDIT_NAME </p>
</li>
<li>
<p>SE_CHANGE_NOTIFY_NAME </p>
</li>
<li>
<p>SE_UNDOCK_NAME </p>
</li>
</ul>
<p>Any privileges assigned to users and authenticated users </p>
<p>The LocalService account is available on the Microsoft Windows XP and later operating systems.</p>
</dd>

### -field SeNetworkServiceSid

<dd>
<p>The SID that matches the NetworkService account, a predefined local account. The NetworkService account has minimum privileges on the local computer and acts as the computer on the network. The name of the account in all locales is "NT AUTHORITY\NetworkService". This account does not have a password. </p>
<p>A service that runs in the context of the NetworkService account presents the computer's credentials to remote servers. By default, the remote token contains SIDs for the Everyone and Authenticated Users groups. </p>
<p>The NetworkService account has its own subkey under the HKEY_USERS registry key. Therefore, the HKEY_CURRENT_USER registry key is associated with the NetworkService account.</p>
<p>The NetworkService account has the following privileges:</p>
<ul>
<li>
<p>SE_AUDIT_NAME </p>
</li>
<li>
<p>SE_CHANGE_NOTIFY_NAME </p>
</li>
<li>
<p>SE_UNDOCK_NAME</p>
</li>
</ul>
<p>Any privileges assigned to users and authenticated users </p>
<p>The NetworkService account is available on Windows XP and later.</p>
</dd>

### -field SeManageVolumePrivilege

<dd>
<p>The privilege that is required to allow a non-administrative or remote user to manage volumes or disks. The operating system checks for this privilege in a user's access token when a process running in the user's security context calls the user mode <a href="fs.setfilevaliddata">SetFileValidData</a> routine.</p>
</dd>

### -field SeImpersonatePrivilege

<dd>
<p>The privilege that is required to impersonate a user. This privilege is available on Windows 2000 with Service Pack 4 (SP4) and later.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Impersonate a client after authentication".</p>
</dd>

### -field SeCreateGlobalPrivilege

<dd>
<p>The privilege that is required for a user account to create global objects in a Terminal Services session. Note that users can still create session-specific objects without being assigned this user right. By default, this privilege is assigned to members of the Administrators group, the System account, and services that are started by the Service Control Manager. This privilege is available on Windows 2000 with Service Pack 4  and later.</p>
<p>User-mode applications represent this privilege as the following user-right string: "Create Global Objects".</p>
</dd>

### -field SeTrustedCredManAccessPrivilege

<dd>
<p>The privilege that is required to access Credential Manager as a trusted caller.
</p>
<p>User-mode applications represent this privilege as the following user-right string: "Access Credential Manager as a trusted caller".
</p>
<div class="alert"><b>Note</b>  Available in Windows Vista and later versions of the Windows operating system.</div>
<div> </div>
</dd>

### -field SeRelabelPrivilege

<dd>
<p>The privilege that is required to modify the mandatory integrity level of an object.
</p>
<p>User-mode applications represent this privilege as the following user-right string: "Modify an object label".
</p>
<div class="alert"><b>Note</b>  Available in Windows Vista and later versions of the Windows operating system.</div>
<div> </div>
</dd>

### -field SeIncreaseWorkingSetPrivilege

<dd>
<p>The privilege that is required to allocate more memory for applications that run in the context of users.
</p>
<p>User-mode applications represent this privilege as the following user-right string: "Increase a process working set".
</p>
<div class="alert"><b>Note</b>  Available in Windows Vista and later versions of the Windows operating system.</div>
<div> </div>
</dd>

### -field SeTimeZonePrivilege

<dd>
<p>The privilege that is required to adjust the time zone associated with the computer's internal clock.

</p>
<p>User-mode applications represent this privilege as the following user-right string: "Change the time zone".</p>
<div class="alert"><b>Note</b>  Available in Windows Vista and later versions of the Windows operating system.</div>
<div> </div>
</dd>

### -field SeCreateSymbolicLinkPrivilege

<dd>
<p>The SID that matches the IUSR built-in account and the IIS_IUSRS built-in group.</p>
<div class="alert"><b>Note</b>  Available in Windows Vista and later versions of the Windows operating system.</div>
<div> </div>
</dd>

### -field SeIUserSid

<dd>
<p>The SID for an untrusted integrity level. </p>
<div class="alert"><b>Note</b>  Available in Windows Vista and later versions of the Windows operating system.</div>
<div> </div>
</dd>

### -field SeUntrustedMandatorySid

<dd>
<p>The SID for an untrusted integrity level. </p>
<div class="alert"><b>Note</b>  Available in Windows Vista and later versions of the Windows operating system.</div>
<div> </div>
</dd>

### -field SeLowMandatorySid

<dd>
<p>The SID for a low integrity level. </p>
<div class="alert"><b>Note</b>  Available in Windows Vista and later versions of the Windows operating system.</div>
<div> </div>
</dd>

### -field SeMediumMandatorySid

<dd>
<p>The SID for a medium integrity level. </p>
<div class="alert"><b>Note</b>  Available in Windows Vista and later versions of the Windows operating system.</div>
<div> </div>
</dd>

### -field SeHighMandatorySid

<dd>
<p>The SID for a high integrity level. </p>
<div class="alert"><b>Note</b>  Available in Windows Vista and later versions of the Windows operating system.</div>
<div> </div>
</dd>

### -field SeSystemMandatorySid

<dd>
<p>The SID for a system integrity level. </p>
<div class="alert"><b>Note</b>  Available in Windows Vista and later versions of the Windows operating system.</div>
<div> </div>
</dd>

### -field SeOwnerRightsSid

<dd>
<p>The SID for a group that represents the current owner of the object. </p>
<div class="alert"><b>Note</b>  Available in Windows Vista and later versions of the Windows operating system.</div>
<div> </div>
</dd>

### -field SeAllAppPackagesSid

<dd>
<p>The SID for a group that represents all application packages. </p>
<div class="alert"><b>Note</b>  Available in Windows 8 and later versions of the Windows operating system.</div>
<div> </div>
</dd>
</dl>

## -remarks
<p><b>SeExports</b> is a large external static SE_EXPORTS structure exported by <i>Ntoskrnl.exe</i>.</p>

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
<a href="ifsk.luid">LUID</a>
</dt>
<dt>
<a href="ifsk.sid">SID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SeExports structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
