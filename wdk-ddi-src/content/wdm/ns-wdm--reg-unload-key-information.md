---
UID: NS.wdm._REG_UNLOAD_KEY_INFORMATION
title: REG_UNLOAD_KEY_INFORMATION
author: windows-driver-content
description: The REG_UNLOAD_KEY_INFORMATION structure contains information that a driver's RegistryCallback routine can use when a registry hive is unloaded.
old-location: kernel\reg_unload_key_information.htm
old-project: kernel
ms.assetid: 171d712d-89e0-44f4-aa52-b9048c20abf2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: REG_UNLOAD_KEY_INFORMATION, REG_UNLOAD_KEY_INFORMATION, *PREG_UNLOAD_KEY_INFORMATION
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
req.alt-api: REG_UNLOAD_KEY_INFORMATION
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

# REG_UNLOAD_KEY_INFORMATION structure



## -description
<p>The <b>REG_UNLOAD_KEY_INFORMATION</b> structure contains information that a driver's <a href="kernel.registrycallback">RegistryCallback</a> routine can use when a registry hive is unloaded.</p>


## -syntax

````
typedef struct _REG_UNLOAD_KEY_INFORMATION {
  PVOID Object;
  PVOID UserEvent;
  PVOID CallContext;
  PVOID ObjectContext;
  PVOID Reserved;
} REG_UNLOAD_KEY_INFORMATION, *PREG_UNLOAD_KEY_INFORMATION;
````


## -struct-fields
<dl>

### -field Object

<dd>
<p>A pointer to a registry key object. This object represents the root key of the hive that is being unloaded.</p>
</dd>

### -field UserEvent

<dd>
<p>A pointer to an event object.</p>
</dd>

### -field CallContext

<dd>
<p>Optional driver-defined context information that the driver's <a href="kernel.registrycallback">RegistryCallback</a> routine can supply. This member is defined starting with Windows Vista.</p>
</dd>

### -field ObjectContext

<dd>
<p>A pointer to driver-defined context information that the driver has associated with a registry object by calling <a href="..\wdm\nf-wdm-cmsetcallbackobjectcontext.md">CmSetCallbackObjectContext</a>. This member is defined starting with Windows Vista.</p>
</dd>

### -field Reserved

<dd>
<p>This member is reserved for future use. This member is defined starting with Windows Vista.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="kernel.registrycallback">RegistryCallback</a> routine. When the <i>Argument1</i> parameter to the <i>RegistryCallback</i> routine is <b>RegNtPreUnloadKey</b>, the <i>Argument2</i> parameter is a pointer to a <b>REG_UNLOAD_KEY_INFORMATION</b> structure.</p>

<p>The operating system passes the <b>REG_UNLOAD_KEY_INFORMATION</b> structure to the <i>RegistryCallback</i> routine every time a thread attempts to unload a key—for example, when a user-mode thread calls the <a href="base.regunloadkey">RegUnloadKey</a> function. In response to a <b>RegNtPreUnloadKey</b> notification, the <i>RegistryCallback</i> routine should free any resources the driver previously allocated for use with the hive before the hive is unloaded.</p>

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
<a href="..\wdm\nf-wdm-cmsetcallbackobjectcontext.md">CmSetCallbackObjectContext</a>
</dt>
<dt>
<a href="kernel.registrycallback">RegistryCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20REG_UNLOAD_KEY_INFORMATION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
