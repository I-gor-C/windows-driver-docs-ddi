---
UID: NS.wdm._REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION
title: REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION
author: windows-driver-content
description: The REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION structure describes the multiple value entries that are being retrieved for a key.
old-location: kernel\reg_query_multiple_value_key_information.htm
old-project: kernel
ms.assetid: 764045c0-9057-4abc-a1bd-8713797082c6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION, REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION, *PREG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available on Microsoft Windows XP and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION
req.alt-loc: wdm.h
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

# REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION structure



## -description
<p>The <b>REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION</b> structure describes the multiple value entries that are being retrieved for a key.</p>


## -syntax

````
typedef struct _REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION {
  PVOID            Object;
  PKEY_VALUE_ENTRY ValueEntries;
  ULONG            EntryCount;
  PVOID            ValueBuffer;
  PULONG           BufferLength;
  PULONG           RequiredBufferLength;
  PVOID            CallContext;
  PVOID            ObjectContext;
  PVOID            Reserved;
} REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION, *PREG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION;
````


## -struct-fields
<dl>

### -field Object

<dd>
<p>A pointer to the registry key object for the key whose value entries are being retrieved.</p>
</dd>

### -field ValueEntries

<dd>
<p>A pointer to an array of <a href="..\wdm\ns-wdm--key-value-entry.md">KEY_VALUE_ENTRY</a> structures, one for each value entry that is retrieved.</p>
</dd>

### -field EntryCount

<dd>
<p>The number of entries in the <b>ValueEntries</b> array.</p>
</dd>

### -field ValueBuffer

<dd>
<p>A pointer to a buffer that receives (from the system) the data for all the value entries specified by the <b>ValueEntries</b> array.</p>
</dd>

### -field BufferLength

<dd>
<p>A pointer to a variable that contains the length, in bytes, of the <b>ValueBuffer</b> buffer.</p>
</dd>

### -field RequiredBufferLength

<dd>
<p>A pointer to a variable that receives (from the system) the number of bytes required to hold the data for all the value entries that the <b>ValueEntries</b> array specifies. This member can be <b>NULL</b>.</p>
</dd>

### -field CallContext

<dd>
<p>Optional driver-defined context information that the driver's <a href="kernel.registrycallback">RegistryCallback</a> routine can supply. This member is defined for Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field ObjectContext

<dd>
<p>A pointer to driver-defined context information that the driver has associated with a registry object by calling <a href="..\wdm\nf-wdm-cmsetcallbackobjectcontext.md">CmSetCallbackObjectContext</a>. This member is defined for Windows Vista and later versions of the Windows operating system.</p>
</dd>

### -field Reserved

<dd>
<p>This member is reserved for future use. This member is defined for Windows Vista and later versions of the Windows operating system.</p>
</dd>
</dl>

## -remarks
<p>The system passes this structure to the <a href="kernel.registrycallback">RegistryCallback</a> routine every time a thread attempts to retrieve multiple value entries for a key at once—for example, when a user-mode thread calls <b>RegQueryMultipleValues</b>.</p>

<p>Each <a href="..\wdm\ns-wdm--key-value-entry.md">KEY_VALUE_ENTRY</a> structure in the <b>ValueEntries</b> array describes one value entry in the <b>ValueBuffer</b> buffer. Specifically, the <b>DataOffset</b> member of <b>KEY_VALUE_ENTRY</b> contains the offset within <b>ValueBuffer</b> where the data for that value entry begins, and the <b>DataLength</b> member contains the length, in bytes, of the data for that value entry.</p>

<p>For more information about registry filtering operations, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545879">Filtering Registry Calls</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available on Microsoft Windows XP and later versions of the Windows operating system.</p>
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
<a href="..\wdm\ns-wdm--key-value-entry.md">KEY_VALUE_ENTRY</a>
</dt>
<dt>
<a href="kernel.registrycallback">RegistryCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
