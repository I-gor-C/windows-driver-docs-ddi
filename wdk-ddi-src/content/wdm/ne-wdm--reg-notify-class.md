---
UID: NE.wdm._REG_NOTIFY_CLASS
title: REG_NOTIFY_CLASS
author: windows-driver-content
description: The REG_NOTIFY_CLASS enumeration type specifies the type of registry operation that the configuration manager is passing to a RegistryCallback routine.
old-location: kernel\reg_notify_class.htm
old-project: kernel
ms.assetid: 2ec47d47-1de3-43af-9a71-7fa366ba2d1a
ms.author: windowsdriverdev
ms.date: 11/20/2017
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
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# REG_NOTIFY_CLASS enumeration



## -description
<p>The <b>REG_NOTIFY_CLASS</b> enumeration type specifies the type of registry operation that the configuration manager is passing to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a> routine.</p>


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

### -field <a id="RegNtDeleteKey"></a><a id="regntdeletekey"></a><a id="REGNTDELETEKEY"></a><b>RegNtDeleteKey</b>

<dd>
<p>Specifies that a thread is attempting to delete a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field <a id="RegNtPreDeleteKey"></a><a id="regntpredeletekey"></a><a id="REGNTPREDELETEKEY"></a><b>RegNtPreDeleteKey</b>

<dd>
<p>Specifies that a thread is attempting to delete a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtSetValueKey"></a><a id="regntsetvaluekey"></a><a id="REGNTSETVALUEKEY"></a><b>RegNtSetValueKey</b>

<dd>
<p>Specifies that a thread is attempting to set a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field <a id="RegNtPreSetValueKey"></a><a id="regntpresetvaluekey"></a><a id="REGNTPRESETVALUEKEY"></a><b>RegNtPreSetValueKey</b>

<dd>
<p>Specifies that a thread is attempting to set a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtDeleteValueKey"></a><a id="regntdeletevaluekey"></a><a id="REGNTDELETEVALUEKEY"></a><b>RegNtDeleteValueKey</b>

<dd>
<p>Specifies that a thread is attempting to delete a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field <a id="RegNtPreDeleteValueKey"></a><a id="regntpredeletevaluekey"></a><a id="REGNTPREDELETEVALUEKEY"></a><b>RegNtPreDeleteValueKey</b>

<dd>
<p>Specifies that a thread is attempting to delete a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtSetInformationKey"></a><a id="regntsetinformationkey"></a><a id="REGNTSETINFORMATIONKEY"></a><b>RegNtSetInformationKey</b>

<dd>
<p>Specifies that a thread is attempting to set the metadata for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field <a id="RegNtPreSetInformationKey"></a><a id="regntpresetinformationkey"></a><a id="REGNTPRESETINFORMATIONKEY"></a><b>RegNtPreSetInformationKey</b>

<dd>
<p>Specifies that a thread is attempting to set the metadata for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtRenameKey"></a><a id="regntrenamekey"></a><a id="REGNTRENAMEKEY"></a><b>RegNtRenameKey</b>

<dd>
<p>Specifies that a thread is attempting to rename a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field <a id="RegNtPreRenameKey"></a><a id="regntprerenamekey"></a><a id="REGNTPRERENAMEKEY"></a><b>RegNtPreRenameKey</b>

<dd>
<p>Specifies that a thread is attempting to rename a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtEnumerateKey"></a><a id="regntenumeratekey"></a><a id="REGNTENUMERATEKEY"></a><b>RegNtEnumerateKey</b>

<dd>
<p>Specifies that a thread is attempting to enumerate a subkey of a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field <a id="RegNtPreEnumerateKey"></a><a id="regntpreenumeratekey"></a><a id="REGNTPREENUMERATEKEY"></a><b>RegNtPreEnumerateKey</b>

<dd>
<p>Specifies that a thread is attempting to enumerate a subkey of a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtEnumerateValueKey"></a><a id="regntenumeratevaluekey"></a><a id="REGNTENUMERATEVALUEKEY"></a><b>RegNtEnumerateValueKey</b>

<dd>
<p>Specifies that a thread is attempting to enumerate a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field <a id="RegNtPreEnumerateValueKey"></a><a id="regntpreenumeratevaluekey"></a><a id="REGNTPREENUMERATEVALUEKEY"></a><b>RegNtPreEnumerateValueKey</b>

<dd>
<p>Specifies that a thread is attempting to enumerate a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtQueryKey"></a><a id="regntquerykey"></a><a id="REGNTQUERYKEY"></a><b>RegNtQueryKey</b>

<dd>
<p>Specifies that a thread is attempting to read the metadata for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field <a id="RegNtPreQueryKey"></a><a id="regntprequerykey"></a><a id="REGNTPREQUERYKEY"></a><b>RegNtPreQueryKey</b>

<dd>
<p>Specifies that a thread is attempting to read the metadata for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtQueryValueKey"></a><a id="regntqueryvaluekey"></a><a id="REGNTQUERYVALUEKEY"></a><b>RegNtQueryValueKey</b>

<dd>
<p>Specifies that a thread is attempting to read a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field <a id="RegNtPreQueryValueKey"></a><a id="regntprequeryvaluekey"></a><a id="REGNTPREQUERYVALUEKEY"></a><b>RegNtPreQueryValueKey</b>

<dd>
<p>Specifies that a thread is attempting to read a value entry for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtQueryMultipleValueKey"></a><a id="regntquerymultiplevaluekey"></a><a id="REGNTQUERYMULTIPLEVALUEKEY"></a><b>RegNtQueryMultipleValueKey</b>

<dd>
<p>Specifies that a thread is attempting to query multiple value entries for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on only Windows XP.</p>
</dd>

### -field <a id="RegNtPreQueryMultipleValueKey"></a><a id="regntprequerymultiplevaluekey"></a><a id="REGNTPREQUERYMULTIPLEVALUEKEY"></a><b>RegNtPreQueryMultipleValueKey</b>

<dd>
<p>Specifies that a thread is attempting to query multiple value entries for a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPreCreateKey"></a><a id="regntprecreatekey"></a><a id="REGNTPRECREATEKEY"></a><b>RegNtPreCreateKey</b>

<dd>
<p>Specifies that a thread is attempting to create a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows XP and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostCreateKey"></a><a id="regntpostcreatekey"></a><a id="REGNTPOSTCREATEKEY"></a><b>RegNtPostCreateKey</b>

<dd>
<p>Specifies that a thread has successfully created a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows XP and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPreOpenKey"></a><a id="regntpreopenkey"></a><a id="REGNTPREOPENKEY"></a><b>RegNtPreOpenKey</b>

<dd>
<p>Specifies that a thread is attempting to open an existing key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows XP and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostOpenKey"></a><a id="regntpostopenkey"></a><a id="REGNTPOSTOPENKEY"></a><b>RegNtPostOpenKey</b>

<dd>
<p>Specifies that a thread has successfully opened an existing key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows XP and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtKeyHandleClose"></a><a id="regntkeyhandleclose"></a><a id="REGNTKEYHANDLECLOSE"></a><b>RegNtKeyHandleClose</b>

<dd>
<p>Specifies that a thread is attempting to close a key handle. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value only on Windows XP.</p>
</dd>

### -field <a id="RegNtPreKeyHandleClose"></a><a id="regntprekeyhandleclose"></a><a id="REGNTPREKEYHANDLECLOSE"></a><b>RegNtPreKeyHandleClose</b>

<dd>
<p>Specifies that a thread is attempting to close a key handle. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system. Drivers can monitor this registry operation but they cannot block or modify it.</p>
</dd>

### -field <a id="RegNtPostDeleteKey"></a><a id="regntpostdeletekey"></a><a id="REGNTPOSTDELETEKEY"></a><b>RegNtPostDeleteKey</b>

<dd>
<p>Specifies that the system has attempted to delete the key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostSetValueKey"></a><a id="regntpostsetvaluekey"></a><a id="REGNTPOSTSETVALUEKEY"></a><b>RegNtPostSetValueKey</b>

<dd>
<p>Specifies that the system has attempted to set a value entry for a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostDeleteValueKey"></a><a id="regntpostdeletevaluekey"></a><a id="REGNTPOSTDELETEVALUEKEY"></a><b>RegNtPostDeleteValueKey</b>

<dd>
<p>Specifies that the system has attempted to delete a value entry for a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostSetInformationKey"></a><a id="regntpostsetinformationkey"></a><a id="REGNTPOSTSETINFORMATIONKEY"></a><b>RegNtPostSetInformationKey</b>

<dd>
<p>Specifies that the system has attempted to set the key's metadata. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostRenameKey"></a><a id="regntpostrenamekey"></a><a id="REGNTPOSTRENAMEKEY"></a><b>RegNtPostRenameKey</b>

<dd>
<p>Specifies that the system has attempted to rename the key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostEnumerateKey"></a><a id="regntpostenumeratekey"></a><a id="REGNTPOSTENUMERATEKEY"></a><b>RegNtPostEnumerateKey</b>

<dd>
<p>Specifies that the system has attempted to enumerate the subkey of a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostEnumerateValueKey"></a><a id="regntpostenumeratevaluekey"></a><a id="REGNTPOSTENUMERATEVALUEKEY"></a><b>RegNtPostEnumerateValueKey</b>

<dd>
<p>Specifies that the system has attempted to enumerate the value entry of a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostQueryKey"></a><a id="regntpostquerykey"></a><a id="REGNTPOSTQUERYKEY"></a><b>RegNtPostQueryKey</b>

<dd>
<p>Specifies that the system has attempted to query the metadata for a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostQueryValueKey"></a><a id="regntpostqueryvaluekey"></a><a id="REGNTPOSTQUERYVALUEKEY"></a><b>RegNtPostQueryValueKey</b>

<dd>
<p>Specifies that the system has attempted to query a value entry for the key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostQueryMultipleValueKey"></a><a id="regntpostquerymultiplevaluekey"></a><a id="REGNTPOSTQUERYMULTIPLEVALUEKEY"></a><b>RegNtPostQueryMultipleValueKey</b>

<dd>
<p>Specifies that the system has attempted to query multiple value entries for the key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostKeyHandleClose"></a><a id="regntpostkeyhandleclose"></a><a id="REGNTPOSTKEYHANDLECLOSE"></a><b>RegNtPostKeyHandleClose</b>

<dd>
<p>Specifies that the system has attempted to close a key handle. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPreCreateKeyEx"></a><a id="regntprecreatekeyex"></a><a id="REGNTPRECREATEKEYEX"></a><b>RegNtPreCreateKeyEx</b>

<dd>
<p>Specifies that a thread is attempting to create a key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostCreateKeyEx"></a><a id="regntpostcreatekeyex"></a><a id="REGNTPOSTCREATEKEYEX"></a><b>RegNtPostCreateKeyEx</b>

<dd>
<p>Specifies that the system has attempted to create a key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPreOpenKeyEx"></a><a id="regntpreopenkeyex"></a><a id="REGNTPREOPENKEYEX"></a><b>RegNtPreOpenKeyEx</b>

<dd>
<p>Specifies that a thread is attempting to open an existing key. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostOpenKeyEx"></a><a id="regntpostopenkeyex"></a><a id="REGNTPOSTOPENKEYEX"></a><b>RegNtPostOpenKeyEx</b>

<dd>
<p>Specifies that the system has attempted to open an existing key. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Server 2003 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPreFlushKey"></a><a id="regntpreflushkey"></a><a id="REGNTPREFLUSHKEY"></a><b>RegNtPreFlushKey</b>

<dd>
<p>Specifies that a thread is attempting to write a key to disk. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostFlushKey"></a><a id="regntpostflushkey"></a><a id="REGNTPOSTFLUSHKEY"></a><b>RegNtPostFlushKey</b>

<dd>
<p>Specifies that the system has attempted to write a key to disk. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPreLoadKey"></a><a id="regntpreloadkey"></a><a id="REGNTPRELOADKEY"></a><b>RegNtPreLoadKey</b>

<dd>
<p>Specifies that a thread is attempting to load a registry hive from a file. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostLoadKey"></a><a id="regntpostloadkey"></a><a id="REGNTPOSTLOADKEY"></a><b>RegNtPostLoadKey</b>

<dd>
<p>Specifies that the system has attempted to load a registry hive from a file. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPreUnLoadKey"></a><a id="regntpreunloadkey"></a><a id="REGNTPREUNLOADKEY"></a><b>RegNtPreUnLoadKey</b>

<dd>
<p>Specifies that a thread is attempting to unload a registry hive. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostUnLoadKey"></a><a id="regntpostunloadkey"></a><a id="REGNTPOSTUNLOADKEY"></a><b>RegNtPostUnLoadKey</b>

<dd>
<p>Specifies that the system has attempted to unload a registry hive. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPreQueryKeySecurity"></a><a id="regntprequerykeysecurity"></a><a id="REGNTPREQUERYKEYSECURITY"></a><b>RegNtPreQueryKeySecurity</b>

<dd>
<p>Specifies that a thread is attempting to obtain a registry key's security information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostQueryKeySecurity"></a><a id="regntpostquerykeysecurity"></a><a id="REGNTPOSTQUERYKEYSECURITY"></a><b>RegNtPostQueryKeySecurity</b>

<dd>
<p>Specifies that a thread has attempted to obtain a registry key's security information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPreSetKeySecurity"></a><a id="regntpresetkeysecurity"></a><a id="REGNTPRESETKEYSECURITY"></a><b>RegNtPreSetKeySecurity</b>

<dd>
<p>Specifies that a thread is attempting to set a registry key's security information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostSetKeySecurity"></a><a id="regntpostsetkeysecurity"></a><a id="REGNTPOSTSETKEYSECURITY"></a><b>RegNtPostSetKeySecurity</b>

<dd>
<p>Specifies that a thread has attempted to set a registry key's security information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtCallbackObjectContextCleanup"></a><a id="regntcallbackobjectcontextcleanup"></a><a id="REGNTCALLBACKOBJECTCONTEXTCLEANUP"></a><b>RegNtCallbackObjectContextCleanup</b>

<dd>
<p>
      Specifies that the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff541928">CmUnRegisterCallback</a> or the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a> routine has just finished processing a <b>RegNtPreKeyHandleClose</b> class value. Use this value on Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPreRestoreKey"></a><a id="regntprerestorekey"></a><a id="REGNTPRERESTOREKEY"></a><b>RegNtPreRestoreKey</b>

<dd>
<p>Specifies that a thread is attempting to restore a registry key's information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system. </p>
</dd>

### -field <a id="RegNtPostRestoreKey"></a><a id="regntpostrestorekey"></a><a id="REGNTPOSTRESTOREKEY"></a><b>RegNtPostRestoreKey</b>

<dd>
<p>Specifies that a thread has attempted to restore a registry key's information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPreSaveKey"></a><a id="regntpresavekey"></a><a id="REGNTPRESAVEKEY"></a><b>RegNtPreSaveKey</b>

<dd>
<p>Specifies that a thread is attempting to save a registry key's information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostSaveKey"></a><a id="regntpostsavekey"></a><a id="REGNTPOSTSAVEKEY"></a><b>RegNtPostSaveKey</b>

<dd>
<p>Specifies that a thread has attempted to save a registry key's information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPreReplaceKey"></a><a id="regntprereplacekey"></a><a id="REGNTPREREPLACEKEY"></a><b>RegNtPreReplaceKey</b>

<dd>
<p>Specifies that a thread is attempting to replace a registry key's information. This value indicates a pre-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostReplaceKey"></a><a id="regntpostreplacekey"></a><a id="REGNTPOSTREPLACEKEY"></a><b>RegNtPostReplaceKey</b>

<dd>
<p>Specifies that a thread has attempted to replace a registry key's information. This value indicates a post-notification call to <i>RegistryCallback</i>. Use this value on Windows Vista SP2 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPreQueryKeyName"></a><a id="regntprequerykeyname"></a><a id="REGNTPREQUERYKEYNAME"></a><b>RegNtPreQueryKeyName</b>

<dd>
<p>Specifies that a thread is attempting to obtain the full path of a registry key. Use this value on Windows 10 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="RegNtPostQueryKeyName"></a><a id="regntpostquerykeyname"></a><a id="REGNTPOSTQUERYKEYNAME"></a><b>RegNtPostQueryKeyName</b>

<dd>
<p>Specifies that a thread has attempted to obtain the full path of a registry key. Use this value on Windows 10 and later versions of the Windows operating system.</p>
</dd>

### -field <a id="MaxRegNtNotifyClass"></a><a id="maxregntnotifyclass"></a><a id="MAXREGNTNOTIFYCLASS"></a><b>MaxRegNtNotifyClass</b>

<dd>
<p>Specifies the maximum value in this enumeration type.</p>
</dd>
</dl>

## -remarks
<p>When the configuration manager calls a driver's <i>RegistryCallback</i> routine, it passes a <b>REG_NOTIFY_CLASS</b> enumeration value to the routine. The configuration manager also passes a notification-specific structure that contains information about the notification. For a list of these structures, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a>.</p>

<p>When the configuration manager calls a driver's <i>RegistryCallback</i> routine, it passes a <b>REG_NOTIFY_CLASS</b> enumeration value to the routine. The configuration manager also passes a notification-specific structure that contains information about the notification. For a list of these structures, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a>.</p>

<p>When the configuration manager calls a driver's <i>RegistryCallback</i> routine, it passes a <b>REG_NOTIFY_CLASS</b> enumeration value to the routine. The configuration manager also passes a notification-specific structure that contains information about the notification. For a list of these structures, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541928">CmUnRegisterCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20REG_NOTIFY_CLASS Enumeration enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
