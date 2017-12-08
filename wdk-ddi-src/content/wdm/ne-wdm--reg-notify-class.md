---
UID: NE.wdm._REG_NOTIFY_CLASS
title: REG_NOTIFY_CLASS
author: windows-driver-content
description: The REG_NOTIFY_CLASS enumeration type specifies the type of registry operation that the configuration manager is passing to a RegistryCallback routine.
old-location: kernel\reg_notify_class.htm
old-project: kernel
ms.assetid: 2ec47d47-1de3-43af-9a71-7fa366ba2d1a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available for Windows XP and later versions of the Windows operating system, but some enumeration values are available only for specified later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: REG_NOTIFY_CLASS
req.alt-loc: Wdm.h
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
req.product: Windows 10 or later.
---

# REG_NOTIFY_CLASS enumeration



## -description
<p>The <b>REG_NOTIFY_CLASS</b> enumeration type specifies the type of registry operation that the configuration manager is passing to a <a href="kernel.registrycallback">RegistryCallback</a> routine.</p>


## -syntax

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


## -enum-fields
<dl>

### -field RegNtDeleteKey

<dd>
<p>Specifies that a thread is attempting to delete a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field RegNtPreDeleteKey

<dd>
<p>Specifies that a thread is attempting to delete a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtSetValueKey

<dd>
<p>Specifies that a thread is attempting to set a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field RegNtPreSetValueKey

<dd>
<p>Specifies that a thread is attempting to set a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtDeleteValueKey

<dd>
<p>Specifies that a thread is attempting to delete a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field RegNtPreDeleteValueKey

<dd>
<p>Specifies that a thread is attempting to delete a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtSetInformationKey

<dd>
<p>Specifies that a thread is attempting to set the metadata for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field RegNtPreSetInformationKey

<dd>
<p>Specifies that a thread is attempting to set the metadata for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtRenameKey

<dd>
<p>Specifies that a thread is attempting to rename a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field RegNtPreRenameKey

<dd>
<p>Specifies that a thread is attempting to rename a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtEnumerateKey

<dd>
<p>Specifies that a thread is attempting to enumerate a subkey of a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field RegNtPreEnumerateKey

<dd>
<p>Specifies that a thread is attempting to enumerate a subkey of a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtEnumerateValueKey

<dd>
<p>Specifies that a thread is attempting to enumerate a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field RegNtPreEnumerateValueKey

<dd>
<p>Specifies that a thread is attempting to enumerate a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtQueryKey

<dd>
<p>Specifies that a thread is attempting to read the metadata for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field RegNtPreQueryKey

<dd>
<p>Specifies that a thread is attempting to read the metadata for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtQueryValueKey

<dd>
<p>Specifies that a thread is attempting to read a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field RegNtPreQueryValueKey

<dd>
<p>Specifies that a thread is attempting to read a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtQueryMultipleValueKey

<dd>
<p>Specifies that a thread is attempting to query multiple value entries for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on only Windows XP.</p>
</dd>

### -field RegNtPreQueryMultipleValueKey

<dd>
<p>Specifies that a thread is attempting to query multiple value entries for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPreCreateKey

<dd>
<p>Specifies that a thread is attempting to create a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows XP and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostCreateKey

<dd>
<p>Specifies that a thread has successfully created a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows XP and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPreOpenKey

<dd>
<p>Specifies that a thread is attempting to open an existing key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows XP and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostOpenKey

<dd>
<p>Specifies that a thread has successfully opened an existing key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows XP and later versions of the Windows operating system.</p>
</dd>

### -field RegNtKeyHandleClose

<dd>
<p>Specifies that a thread is attempting to close a key handle. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field RegNtPreKeyHandleClose

<dd>
<p>Specifies that a thread is attempting to close a key handle. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system. Drivers can monitor this registry operation but they cannot block or modify it.</p>
</dd>

### -field RegNtPostDeleteKey

<dd>
<p>Specifies that the system has attempted to delete the key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostSetValueKey

<dd>
<p>Specifies that the system has attempted to set a value entry for a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostDeleteValueKey

<dd>
<p>Specifies that the system has attempted to delete a value entry for a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostSetInformationKey

<dd>
<p>Specifies that the system has attempted to set the key's metadata. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostRenameKey

<dd>
<p>Specifies that the system has attempted to rename the key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostEnumerateKey

<dd>
<p>Specifies that the system has attempted to enumerate the subkey of a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostEnumerateValueKey

<dd>
<p>Specifies that the system has attempted to enumerate the value entry of a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostQueryKey

<dd>
<p>Specifies that the system has attempted to query the metadata for a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostQueryValueKey

<dd>
<p>Specifies that the system has attempted to query a value entry for the key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostQueryMultipleValueKey

<dd>
<p>Specifies that the system has attempted to query multiple value entries for the key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostKeyHandleClose

<dd>
<p>Specifies that the system has attempted to close a key handle. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPreCreateKeyEx

<dd>
<p>Specifies that a thread is attempting to create a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostCreateKeyEx

<dd>
<p>Specifies that the system has attempted to create a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPreOpenKeyEx

<dd>
<p>Specifies that a thread is attempting to open an existing key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostOpenKeyEx

<dd>
<p>Specifies that the system has attempted to open an existing key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPreFlushKey

<dd>
<p>Specifies that a thread is attempting to write a key to disk. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostFlushKey

<dd>
<p>Specifies that the system has attempted to write a key to disk. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPreLoadKey

<dd>
<p>Specifies that a thread is attempting to load a registry hive from a file. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostLoadKey

<dd>
<p>Specifies that the system has attempted to load a registry hive from a file. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPreUnLoadKey

<dd>
<p>Specifies that a thread is attempting to unload a registry hive. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostUnLoadKey

<dd>
<p>Specifies that the system has attempted to unload a registry hive. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPreQueryKeySecurity

<dd>
<p>Specifies that a thread is attempting to obtain a registry key's security information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostQueryKeySecurity

<dd>
<p>Specifies that a thread has attempted to obtain a registry key's security information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPreSetKeySecurity

<dd>
<p>Specifies that a thread is attempting to set a registry key's security information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostSetKeySecurity

<dd>
<p>Specifies that a thread has attempted to set a registry key's security information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field RegNtCallbackObjectContextCleanup

<dd>
<p>
      Specifies that the driver has called <a href="..\wdm\nf-wdm-cmunregistercallback.md">CmUnRegisterCallback</a> or the driver's <a href="kernel.registrycallback">RegistryCallback</a> routine has just finished processing a <b>RegNtPreKeyHandleClose</b> class value. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPreRestoreKey

<dd>
<p>Specifies that a thread is attempting to restore a registry key's information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system. </p>
</dd>

### -field RegNtPostRestoreKey

<dd>
<p>Specifies that a thread has attempted to restore a registry key's information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPreSaveKey

<dd>
<p>Specifies that a thread is attempting to save a registry key's information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostSaveKey

<dd>
<p>Specifies that a thread has attempted to save a registry key's information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPreReplaceKey

<dd>
<p>Specifies that a thread is attempting to replace a registry key's information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostReplaceKey

<dd>
<p>Specifies that a thread has attempted to replace a registry key's information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPreQueryKeyName

<dd>
<p>Specifies that a thread is attempting to obtain the full path of a registry key. Use this value on Windows 10 and later versions of the Windows operating system.</p>
</dd>

### -field RegNtPostQueryKeyName

<dd>
<p>Specifies that a thread has attempted to obtain the full path of a registry key. Use this value on Windows 10 and later versions of the Windows operating system.</p>
</dd>

### -field MaxRegNtNotifyClass

<dd>
<p>Specifies the maximum value in this enumeration type.</p>
</dd>
</dl>

## -remarks
<p>When the configuration manager calls a driver's <i>RegistryCallback</i> routine, it passes a <b>REG_NOTIFY_CLASS</b> enumeration value to the routine. The configuration manager also passes a notification-specific structure that contains information about the notification. For a list of these structures, see <a href="kernel.registrycallback">RegistryCallback</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available for Windows XP and later versions of the Windows operating system, but some enumeration values are available only for specified later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-cmunregistercallback.md">CmUnRegisterCallback</a>
</dt>
<dt>
<a href="kernel.registrycallback">RegistryCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20REG_NOTIFY_CLASS Enumeration enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
