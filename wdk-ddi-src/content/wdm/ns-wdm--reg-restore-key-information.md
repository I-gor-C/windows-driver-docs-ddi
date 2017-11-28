---
UID: NS.wdm._REG_RESTORE_KEY_INFORMATION
title: REG_RESTORE_KEY_INFORMATION
author: windows-driver-content
description: The REG_RESTORE_KEY_INFORMATION structure contains the information for a registry key that is about to be restored.
old-location: kernel\reg_restore_key_information.htm
old-project: kernel
ms.assetid: df9180d8-37aa-4b75-a8c6-a786901bd8a6
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: REG_RESTORE_KEY_INFORMATION, REG_RESTORE_KEY_INFORMATION, *PREG_RESTORE_KEY_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available on Windows Vista SP2 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: REG_RESTORE_KEY_INFORMATION
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
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# REG_RESTORE_KEY_INFORMATION structure



## -description
<p>The <b>REG_RESTORE_KEY_INFORMATION</b> structure contains the information for a registry key that is about to be restored.</p>


## -syntax

````
typedef struct _REG_RESTORE_KEY_INFORMATION {
  PVOID  Object;
  HANDLE FileHandle;
  ULONG  Flags;
  PVOID  CallContext;
  PVOID  ObjectContext;
  PVOID  Reserved;
} REG_RESTORE_KEY_INFORMATION, *PREG_RESTORE_KEY_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>Object</b>

<dd>
<p>A pointer to a registry key object for the key whose name is about to be changed.</p>
</dd>

### -field <b>FileHandle</b>

<dd>
<p>A handle to the file from which the hive will be restored.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p><b>REG_FORCE_RESTORE</b></p>
<p>0x00000008L</p>
<p>If specified, the restore operation is executed even if open handles exist at or beneath the location in the registry hierarchy to which the <i>hKey</i> parameter points.</p>
<p><b>REG_WHOLE_HIVE_VOLATILE</b></p>
<p>0x00000001L</p>
<p>If specified, a new, volatile (memory-only) set of registry information, or <i>hive</i>, is created. If REG_WHOLE_HIVE_VOLATILE is specified, the key identified by the <i>hKey</i> parameter must be either the HKEY_USERS or HKEY_LOCAL_MACHINE value.</p>
<p><b>REG_REFRESH_HIVE</b></p>
<p>0x00000002</p>
<p>If set, the location of the subtree that the <i>hKey</i> parameter points to is restored to its state immediately following the last flush. The subtree must not be lazy flushed (by calling <b>RegRestoreKey</b> with REG_NO_LAZY_FLUSH specified as the value of this parameter); the caller must have the trusted computing base (TCB) privilege; and the handle to which the <i>hKey</i> parameter refers must point to the root of the subtree.</p>
</dd>

### -field <b>CallContext</b>

<dd>
<p>Optional driver-defined context information that the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a> routine can supply. This member is defined for Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field <b>ObjectContext</b>

<dd>
<p>A pointer to driver-defined context information, which the driver has associated with a registry object by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff541924">CmSetCallbackObjectContext</a>. This member is defined for Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved for future use. This member is defined for Windows Vista and later versions of the Windows operating system.</p>
</dd>
</dl>

## -remarks
<p>Note that when a key is restored, only the last component of the path can be changed.</p>

<p>The REG_REFRESH_HIVE flag is opaque and a filter should not attempt to change it.</p>

<p>For more information about registry filtering operations, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545879">Filtering Registry Calls</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available on Windows Vista SP2 and later versions of the Windows operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541924">CmSetCallbackObjectContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20REG_RESTORE_KEY_INFORMATION structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
