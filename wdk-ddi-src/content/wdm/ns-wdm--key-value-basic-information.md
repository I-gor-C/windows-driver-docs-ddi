---
UID: NS.wdm._KEY_VALUE_BASIC_INFORMATION
title: KEY_VALUE_BASIC_INFORMATION
author: windows-driver-content
description: The KEY_VALUE_BASIC_INFORMATION structure defines a subset of the full information available for a value entry of a registry key.
old-location: kernel\key_value_basic_information.htm
old-project: kernel
ms.assetid: b3b14c21-3613-4f84-9e7d-368c4cc3fa9d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KEY_VALUE_BASIC_INFORMATION, KEY_VALUE_BASIC_INFORMATION, *PKEY_VALUE_BASIC_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KEY_VALUE_BASIC_INFORMATION
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

# KEY_VALUE_BASIC_INFORMATION structure



## -description
<p>The <b>KEY_VALUE_BASIC_INFORMATION</b> structure defines a subset of the full information available for a value entry of a registry key. </p>


## -syntax

````
typedef struct _KEY_VALUE_BASIC_INFORMATION {
  ULONG TitleIndex;
  ULONG Type;
  ULONG NameLength;
  WCHAR Name[1];
} KEY_VALUE_BASIC_INFORMATION, *PKEY_VALUE_BASIC_INFORMATION;
````


## -struct-fields
<dl>

### -field TitleIndex

<dd>
<p>Device and intermediate drivers should ignore this member.</p>
</dd>

### -field Type

<dd>
<p>Specifies the system-defined type for the value entry in the registry key, which is one of the following:</p>
<table>
<tr>
<th>REG_<i>XXX</i> type</th>
<th>Value</th>
</tr>
<tr>
<td>
<p>REG_BINARY</p>
</td>
<td>
<p>Binary data in any form</p>
</td>
</tr>
<tr>
<td>
<p>REG_DWORD</p>
</td>
<td>
<p>A 4-byte numerical value</p>
</td>
</tr>
<tr>
<td>
<p>REG_DWORD_LITTLE_ENDIAN</p>
</td>
<td>
<p>A 4-byte numerical value whose least significant byte is at the lowest address</p>
</td>
</tr>
<tr>
<td>
<p>REG_DWORD_BIG_ENDIAN</p>
</td>
<td>
<p>A 4-byte numerical  value whose least significant byte is at the highest address</p>
</td>
</tr>
<tr>
<td>
<p>REG_EXPAND_SZ</p>
</td>
<td>
<p>A null-terminated Unicode string, containing unexpanded references to environment variables, such as "%PATH%"</p>
</td>
</tr>
<tr>
<td>
<p>REG_LINK</p>
</td>
<td>
<p>A Unicode string naming a symbolic link. This type is irrelevant to device and intermediate drivers</p>
</td>
</tr>
<tr>
<td>
<p>REG_MULTI_SZ</p>
</td>
<td>
<p>An array of null-terminated strings, terminated by another zero</p>
</td>
</tr>
<tr>
<td>
<p>REG_NONE</p>
</td>
<td>
<p>Data with no particular type</p>
</td>
</tr>
<tr>
<td>
<p>REG_SZ</p>
</td>
<td>
<p>A null-terminated Unicode string</p>
</td>
</tr>
<tr>
<td>
<p>REG_RESOURCE_LIST</p>
</td>
<td colspan="2">
<p>A device driver's list of hardware resources, used by the driver or one of the physical devices it controls, in the <b>\ResourceMap</b> tree</p>
</td>
</tr>
<tr>
<td>
<p>REG_RESOURCE_REQUIREMENTS_LIST</p>
</td>
<td colspan="2">
<p>A device driver's list of possible hardware resources it or one of the physical devices it controls can use, from which the system writes a subset into the <b>\ResourceMap</b> tree</p>
</td>
</tr>
<tr>
<td>
<p>REG_FULL_RESOURCE_DESCRIPTOR</p>
</td>
<td colspan="2">
<p>A list of hardware resources that a physical device is using, detected and written into the <b>\HardwareDescription</b> tree by the system</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field NameLength

<dd>
<p>Specifies the size in bytes of the following value entry name.</p>
</dd>

### -field Name

<dd>
<p>A string of Unicode characters naming a value entry of the key.</p>
</dd>
</dl>

## -remarks
<p>A kernel-mode driver can obtain a <b>KEY_VALUE_BASIC_INFORMATION</b> that describes a registry key by calling the <a href="..\wdm\nf-wdm-zwqueryvaluekey.md">ZwQueryValueKey</a> or <a href="..\wdm\nf-wdm-zwenumeratevaluekey.md">ZwEnumerateValueKey</a> routine.</p>

## -requirements
<table>
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
<a href="..\wdm\ns-wdm--key-value-full-information.md">KEY_VALUE_FULL_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--key-value-information-class.md">KEY_VALUE_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--key-value-partial-information.md">KEY_VALUE_PARTIAL_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwenumeratevaluekey.md">ZwEnumerateValueKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwqueryvaluekey.md">ZwQueryValueKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KEY_VALUE_BASIC_INFORMATION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
