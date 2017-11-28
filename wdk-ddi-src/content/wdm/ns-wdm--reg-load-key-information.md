---
UID: NS.wdm._REG_LOAD_KEY_INFORMATION
title: REG_LOAD_KEY_INFORMATION
author: windows-driver-content
description: The REG_LOAD_KEY_INFORMATION structure contains information about a registry hive that is being loaded.
old-location: kernel\reg_load_key_information.htm
old-project: kernel
ms.assetid: 4012667b-d287-4846-8860-0cca977f9792
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: REG_LOAD_KEY_INFORMATION, REG_LOAD_KEY_INFORMATION, *PREG_LOAD_KEY_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: REG_LOAD_KEY_INFORMATION
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

# REG_LOAD_KEY_INFORMATION structure



## -description
<p>The <b>REG_LOAD_KEY_INFORMATION</b> structure contains information about a registry hive that is being loaded.</p>


## -syntax

````
typedef struct _REG_LOAD_KEY_INFORMATION {
  PVOID           Object;
  PUNICODE_STRING KeyName;
  PUNICODE_STRING SourceFile;
  ULONG           Flags;
  PVOID           TrustClassObject;
  PVOID           UserEvent;
  ACCESS_MASK     DesiredAccess;
  PHANDLE         RootHandle;
  PVOID           CallContext;
  PVOID           ObjectContext;
  PVOID           Reserved;
} REG_LOAD_KEY_INFORMATION, *PREG_LOAD_KEY_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>Object</b>

<dd>
<p>A pointer to the registry key object for the root key of the hive that is about to be loaded.</p>
</dd>

### -field <b>KeyName</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure that contains the name of the root key.</p>
</dd>

### -field <b>SourceFile</b>

<dd>
<p>A pointer to a <b>UNICODE_STRING</b> structure that contains the path name of a file that contains the registry hive information that is being loaded.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>TrustClassObject</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>UserEvent</b>

<dd>
<p>A pointer to an event object that is signaled when the hive is unloaded.</p>
</dd>

### -field <b>DesiredAccess</b>

<dd>
<p>The access mask that was specified by the thread that is trying to load the registry key. For more information about this access mask, see the description of the <i>DesiredAccess</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566425">ZwCreateKey</a> routine.</p>
</dd>

### -field <b>RootHandle</b>

<dd>
<p>An optional pointer to a location that receives the handle to the root of the hive that is being loaded. This member can be non-<b>NULL</b> if an application hive is  being loaded. In all other cases, this member should be <b>NULL</b>.</p>
</dd>

### -field <b>CallContext</b>

<dd>
<p>Optional driver-defined context information that the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a> routine can supply.</p>
</dd>

### -field <b>ObjectContext</b>

<dd>
<p>A pointer to driver-defined context information that the driver has associated with a registry object by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541924">CmSetCallbackObjectContext</a> routine.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>The operating system passes the <b>REG_LOAD_KEY_INFORMATION</b> structure to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a> routine every time a user-mode thread calls <a href="base.regloadkey">RegLoadKey</a> to load a registry hive.</p>

<p>For more information about registry filtering operations, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545879">Filtering Registry Calls</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
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
<dt>
<a href="base.regloadkey">RegLoadKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566425">ZwCreateKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20REG_LOAD_KEY_INFORMATION structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
