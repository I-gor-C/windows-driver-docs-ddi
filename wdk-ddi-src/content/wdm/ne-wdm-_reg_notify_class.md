---
UID : NE:wdm._REG_NOTIFY_CLASS
title : "_REG_NOTIFY_CLASS"
author : windows-driver-content
description : The REG_NOTIFY_CLASS enumeration type specifies the type of registry operation that the configuration manager is passing to a RegistryCallback routine.
old-location : kernel\reg_notify_class.htm
old-project : kernel
ms.assetid : 2ec47d47-1de3-43af-9a71-7fa366ba2d1a
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RegNtCallbackObjectContextCleanup, REG_NOTIFY_CLASS, RegNtPostSetValueKey, RegNtPreQueryKeySecurity, wdm/RegNtPostRestoreKey, _REG_NOTIFY_CLASS, RegNtPreEnumerateKey, wdm/RegNtPreLoadKey, wdm/RegNtPostCreateKey, RegNtPostQueryKeySecurity, wdm/RegNtPreQueryValueKey, RegNtPreCreateKey, RegNtQueryValueKey, wdm/RegNtDeleteKey, RegNtQueryKey, wdm/RegNtPostKeyHandleClose, RegNtQueryMultipleValueKey, RegNtPostKeyHandleClose, wdm/RegNtPreSaveKey, wdm/RegNtPostDeleteValueKey, RegNtDeleteKey, RegNtPreDeleteValueKey, RegNtPostDeleteValueKey, wdm/RegNtPostLoadKey, RegNtPostQueryKey, RegNtPreQueryKey, wdm/RegNtPostFlushKey, RegNtPostUnLoadKey, wdm/RegNtPostSetKeySecurity, RegNtPreQueryValueKey, wdm/RegNtPreDeleteKey, RegNtPreCreateKeyEx, wdm/RegNtPreQueryMultipleValueKey, wdm/RegNtPreQueryKey, RegNtPreEnumerateValueKey, RegNtPreRenameKey, RegNtPostLoadKey, wdm/RegNtPreEnumerateValueKey, wdm/RegNtPostQueryKeyName, RegNtPostEnumerateKey, RegNtPostSaveKey, RegNtPreReplaceKey, RegNtPreFlushKey, wdm/RegNtPostQueryMultipleValueKey, wdm/RegNtQueryKey, wdm/RegNtPreDeleteValueKey, RegNtPreKeyHandleClose, wdm/RegNtEnumerateKey, wdm/RegNtPostOpenKey, wdm/RegNtPreOpenKeyEx, wdm/RegNtPreKeyHandleClose, wdm/RegNtSetValueKey, REG_NOTIFY_CLASS enumeration [Kernel-Mode Driver Architecture], RegNtPreOpenKey, wdm/RegNtPostReplaceKey, wdm/RegNtPostSetInformationKey, RegNtPreSetInformationKey, wdm/RegNtPostCreateKeyEx, RegNtPreQueryMultipleValueKey, wdm/RegNtPostRenameKey, wdm/RegNtPostDeleteKey, wdm/RegNtPostUnLoadKey, RegNtPostSetInformationKey, RegNtPostOpenKey, RegNtPostSetKeySecurity, RegNtPostFlushKey, RegNtPreLoadKey, RegNtEnumerateValueKey, wdm/RegNtPreReplaceKey, wdm/RegNtPostSaveKey, MaxRegNtNotifyClass, RegNtPostRestoreKey, wdm/RegNtPreRestoreKey, wdm/RegNtPreFlushKey, RegNtSetInformationKey, wdm/RegNtPreUnLoadKey, RegNtPreRestoreKey, RegNtDeleteValueKey, RegNtPreSetKeySecurity, wdm/RegNtPostEnumerateValueKey, wdm/RegNtPostSetValueKey, wdm/RegNtPreSetValueKey, wdm/RegNtQueryValueKey, RegNtPreSetValueKey, wdm/RegNtPreCreateKey, wdm/REG_NOTIFY_CLASS, wdm/RegNtPreCreateKeyEx, wdm/RegNtPreQueryKeySecurity, wdm/RegNtKeyHandleClose, wdm/RegNtPreRenameKey, wdm/RegNtQueryMultipleValueKey, RegNtPostOpenKeyEx, RegNtPostQueryValueKey, RegNtPostCreateKey, RegNtPreOpenKeyEx, RegNtPostEnumerateValueKey, wdm/RegNtPostQueryValueKey, wdm/RegNtPreOpenKey, RegNtRenameKey, wdm/RegNtPreSetKeySecurity, wdm/RegNtPreSetInformationKey, RegNtSetValueKey, wdm/RegNtPreEnumerateKey, RegNtEnumerateKey, RegNtPostCreateKeyEx, RegNtPreDeleteKey, wdm/RegNtPostQueryKey, RegNtPostRenameKey, wdm/RegNtRenameKey, RegNtKeyHandleClose, wdm/RegNtPostQueryKeySecurity, sysenum_b6fa1e3a-74d4-4925-b7c9-60d905c48f50.xml, RegNtPreSaveKey, RegNtPreQueryKeyName, wdm/RegNtPreQueryKeyName, wdm/RegNtEnumerateValueKey, wdm/RegNtPostOpenKeyEx, wdm/RegNtCallbackObjectContextCleanup, RegNtPostDeleteKey, wdm/RegNtPostEnumerateKey, RegNtPostQueryMultipleValueKey, kernel.reg_notify_class, RegNtPostReplaceKey, wdm/MaxRegNtNotifyClass, wdm/RegNtSetInformationKey, wdm/RegNtDeleteValueKey, RegNtPostQueryKeyName, RegNtPreUnLoadKey
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : wdm.h
req.include-header : Wdm.h, Ntddk.h, Ntifs.h
req.target-type : Windows
req.target-min-winverclnt : Available for Windows XP and later versions of the Windows operating system, but some enumeration values are available only for specified later versions of the Windows operating system.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : REG_NOTIFY_CLASS
req.product : Windows 10 or later.
---

# _REG_NOTIFY_CLASS Enumeration
The <b>REG_NOTIFY_CLASS</b> enumeration type specifies the type of registry operation that the configuration manager is passing to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a> routine.

## Syntax
````
enum REG_NOTIFY_CLASS {
  RegNtDeleteKey, 
  RegNtPreDeleteKey                  = RegNtDeleteKey, 
  RegNtSetValueKey, 
  RegNtPreSetValueKey                = RegNtSetValueKey, 
  RegNtDeleteValueKey, 
  RegNtPreDeleteValueKey             = RegNtDeleteValueKey, 
  RegNtSetInformationKey, 
  RegNtPreSetInformationKey          = RegNtSetInformationKey, 
  RegNtRenameKey, 
  RegNtPreRenameKey                  = RegNtRenameKey, 
  RegNtEnumerateKey, 
  RegNtPreEnumerateKey               = RegNtEnumerateKey, 
  RegNtEnumerateValueKey, 
  RegNtPreEnumerateValueKey          = RegNtEnumerateValueKey, 
  RegNtQueryKey, 
  RegNtPreQueryKey                   = RegNtQueryKey, 
  RegNtQueryValueKey, 
  RegNtPreQueryValueKey              = RegNtQueryValueKey, 
  RegNtQueryMultipleValueKey, 
  RegNtPreQueryMultipleValueKey      = RegNtQueryMultipleValueKey, 
  RegNtPreCreateKey, 
  RegNtPostCreateKey, 
  RegNtPreOpenKey, 
  RegNtPostOpenKey, 
  RegNtKeyHandleClose, 
  RegNtPreKeyHandleClose             = RegNtKeyHandleClose, 
  RegNtPostDeleteKey, 
  RegNtPostSetValueKey, 
  RegNtPostDeleteValueKey, 
  RegNtPostSetInformationKey, 
  RegNtPostRenameKey, 
  RegNtPostEnumerateKey, 
  RegNtPostEnumerateValueKey, 
  RegNtPostQueryKey, 
  RegNtPostQueryValueKey, 
  RegNtPostQueryMultipleValueKey, 
  RegNtPostKeyHandleClose, 
  RegNtPreCreateKeyEx, 
  RegNtPostCreateKeyEx, 
  RegNtPreOpenKeyEx, 
  RegNtPostOpenKeyEx, 
  RegNtPreFlushKey, 
  RegNtPostFlushKey, 
  RegNtPreLoadKey, 
  RegNtPostLoadKey, 
  RegNtPreUnLoadKey, 
  RegNtPostUnLoadKey, 
  RegNtPreQueryKeySecurity, 
  RegNtPostQueryKeySecurity, 
  RegNtPreSetKeySecurity, 
  RegNtPostSetKeySecurity, 
  RegNtCallbackObjectContextCleanup, 
  RegNtPreRestoreKey, 
  RegNtPostRestoreKey, 
  RegNtPreSaveKey, 
  RegNtPostSaveKey, 
  RegNtPreReplaceKey, 
  RegNtPostReplaceKey, 
  RegNtPreQueryKeyName, 
  RegNtPostQueryKeyName, 
  MaxRegNtNotifyClass 

};
````

## Constants

<table>

<tr>
<td>MaxRegNtNotifyClass</td>
<td>Specifies the maximum value in this enumeration type.</td>
</tr>

<tr>
<td>RegNtCallbackObjectContextCleanup</td>
<td>Specifies that the driver has called <a href="..\wdm\nf-wdm-cmunregistercallback.md">CmUnRegisterCallback</a> or the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a> routine has just finished processing a <b>RegNtPreKeyHandleClose</b> class value. Use this value on Windows Vista and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtDeleteKey</td>
<td>Specifies that a thread is attempting to delete a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</td>
</tr>

<tr>
<td>RegNtDeleteValueKey</td>
<td>Specifies that a thread is attempting to delete a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</td>
</tr>

<tr>
<td>RegNtEnumerateKey</td>
<td>Specifies that a thread is attempting to enumerate a subkey of a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</td>
</tr>

<tr>
<td>RegNtEnumerateValueKey</td>
<td>Specifies that a thread is attempting to enumerate a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</td>
</tr>

<tr>
<td>RegNtKeyHandleClose</td>
<td>Specifies that a thread is attempting to close a key handle. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</td>
</tr>

<tr>
<td>RegNtPostCreateKey</td>
<td>Specifies that a thread has successfully created a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows XP and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostCreateKeyEx</td>
<td>Specifies that the system has attempted to create a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostDeleteKey</td>
<td>Specifies that the system has attempted to delete the key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostDeleteValueKey</td>
<td>Specifies that the system has attempted to delete a value entry for a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostEnumerateKey</td>
<td>Specifies that the system has attempted to enumerate the subkey of a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostEnumerateValueKey</td>
<td>Specifies that the system has attempted to enumerate the value entry of a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostFlushKey</td>
<td>Specifies that the system has attempted to write a key to disk. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostKeyHandleClose</td>
<td>Specifies that the system has attempted to close a key handle. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostLoadKey</td>
<td>Specifies that the system has attempted to load a registry hive from a file. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostOpenKey</td>
<td>Specifies that a thread has successfully opened an existing key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows XP and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostOpenKeyEx</td>
<td>Specifies that the system has attempted to open an existing key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostQueryKey</td>
<td>Specifies that the system has attempted to query the metadata for a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostQueryKeyName</td>
<td>Specifies that a thread has attempted to obtain the full path of a registry key. Use this value on Windows 10 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostQueryKeySecurity</td>
<td>Specifies that a thread has attempted to obtain a registry key's security information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostQueryMultipleValueKey</td>
<td>Specifies that the system has attempted to query multiple value entries for the key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostQueryValueKey</td>
<td>Specifies that the system has attempted to query a value entry for the key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostRenameKey</td>
<td>Specifies that the system has attempted to rename the key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostReplaceKey</td>
<td>Specifies that a thread has attempted to replace a registry key's information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostRestoreKey</td>
<td>Specifies that a thread has attempted to restore a registry key's information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostSaveKey</td>
<td>Specifies that a thread has attempted to save a registry key's information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostSetInformationKey</td>
<td>Specifies that the system has attempted to set the key's metadata. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostSetKeySecurity</td>
<td>Specifies that a thread has attempted to set a registry key's security information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostSetValueKey</td>
<td>Specifies that the system has attempted to set a value entry for a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPostUnLoadKey</td>
<td>Specifies that the system has attempted to unload a registry hive. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreCreateKey</td>
<td>Specifies that a thread is attempting to create a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows XP and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreCreateKeyEx</td>
<td>Specifies that a thread is attempting to create a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreDeleteKey</td>
<td>Specifies that a thread is attempting to delete a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreDeleteValueKey</td>
<td>Specifies that a thread is attempting to delete a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreEnumerateKey</td>
<td>Specifies that a thread is attempting to enumerate a subkey of a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreEnumerateValueKey</td>
<td>Specifies that a thread is attempting to enumerate a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreFlushKey</td>
<td>Specifies that a thread is attempting to write a key to disk. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreKeyHandleClose</td>
<td>Specifies that a thread is attempting to close a key handle. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system. Drivers can monitor this registry operation but they cannot block or modify it.</td>
</tr>

<tr>
<td>RegNtPreLoadKey</td>
<td>Specifies that a thread is attempting to load a registry hive from a file. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreOpenKey</td>
<td>Specifies that a thread is attempting to open an existing key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows XP and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreOpenKeyEx</td>
<td>Specifies that a thread is attempting to open an existing key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreQueryKey</td>
<td>Specifies that a thread is attempting to read the metadata for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreQueryKeyName</td>
<td>Specifies that a thread is attempting to obtain the full path of a registry key. Use this value on Windows 10 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreQueryKeySecurity</td>
<td>Specifies that a thread is attempting to obtain a registry key's security information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreQueryMultipleValueKey</td>
<td>Specifies that a thread is attempting to query multiple value entries for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreQueryValueKey</td>
<td>Specifies that a thread is attempting to read a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreRenameKey</td>
<td>Specifies that a thread is attempting to rename a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreReplaceKey</td>
<td>Specifies that a thread is attempting to replace a registry key's information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreRestoreKey</td>
<td>Specifies that a thread is attempting to restore a registry key's information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreSaveKey</td>
<td>Specifies that a thread is attempting to save a registry key's information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreSetInformationKey</td>
<td>Specifies that a thread is attempting to set the metadata for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreSetKeySecurity</td>
<td>Specifies that a thread is attempting to set a registry key's security information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreSetValueKey</td>
<td>Specifies that a thread is attempting to set a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtPreUnLoadKey</td>
<td>Specifies that a thread is attempting to unload a registry hive. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</td>
</tr>

<tr>
<td>RegNtQueryKey</td>
<td>Specifies that a thread is attempting to read the metadata for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</td>
</tr>

<tr>
<td>RegNtQueryMultipleValueKey</td>
<td>Specifies that a thread is attempting to query multiple value entries for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on only Windows XP.</td>
</tr>

<tr>
<td>RegNtQueryValueKey</td>
<td>Specifies that a thread is attempting to read a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</td>
</tr>

<tr>
<td>RegNtRenameKey</td>
<td>Specifies that a thread is attempting to rename a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</td>
</tr>

<tr>
<td>RegNtSetInformationKey</td>
<td>Specifies that a thread is attempting to set the metadata for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</td>
</tr>

<tr>
<td>RegNtSetValueKey</td>
<td>Specifies that a thread is attempting to set a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</td>
</tr>
</table>

## Remarks

When the configuration manager calls a driver's <i>RegistryCallback</i> routine, it passes a <b>REG_NOTIFY_CLASS</b> enumeration value to the routine. The configuration manager also passes a notification-specific structure that contains information about the notification. For a list of these structures, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available for Windows XP and later versions of the Windows operating system, but some enumeration values are available only for specified later versions of the Windows operating system. Available for Windows XP and later versions of the Windows operating system, but some enumeration values are available only for specified later versions of the Windows operating system. |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a>

<a href="..\wdm\nf-wdm-cmunregistercallback.md">CmUnRegisterCallback</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20REG_NOTIFY_CLASS enumeration%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>