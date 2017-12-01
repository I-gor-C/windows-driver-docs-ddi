---
UID: NS.wdm._KEY_NODE_INFORMATION
title: KEY_NODE_INFORMATION
author: windows-driver-content
description: The KEY_NODE_INFORMATION structure defines the basic information available for a registry (sub)key.
old-location: kernel\key_node_information.htm
old-project: kernel
ms.assetid: 2eed1a3d-fc40-4416-ad61-d82bf4fb69a1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KEY_NODE_INFORMATION, KEY_NODE_INFORMATION, *PKEY_NODE_INFORMATION
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
req.alt-api: KEY_NODE_INFORMATION
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

# KEY_NODE_INFORMATION structure



## -description
<p>The <b>KEY_NODE_INFORMATION</b> structure defines the basic information available for a registry (sub)key.</p>


## -syntax

````
typedef struct _KEY_NODE_INFORMATION {
  LARGE_INTEGER LastWriteTime;
  ULONG         TitleIndex;
  ULONG         ClassOffset;
  ULONG         ClassLength;
  ULONG         NameLength;
  WCHAR         Name[1];
} KEY_NODE_INFORMATION, *PKEY_NODE_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>LastWriteTime</b>

<dd>
<p>The last time this key or any of its values changed. This time value is expressed in absolute system time format. Absolute system time is the number of 100-nanosecond intervals since the start of the year 1601 in the Gregorian calendar.</p>
</dd>

### -field <b>TitleIndex</b>

<dd>
<p>Device and intermediate drivers should ignore this member.</p>
</dd>

### -field <b>ClassOffset</b>

<dd>
<p>The byte offset from the start of this structure to the class name string, which is located in the <b>Name</b> array immediately following the key name string. Like the key name string, the class name string is not null-terminated.</p>
</dd>

### -field <b>ClassLength</b>

<dd>
<p>The size, in bytes, in the class name string.</p>
</dd>

### -field <b>NameLength</b>

<dd>
<p>The size, in bytes, of the key name string contained in the <b>Name</b> array.</p>
</dd>

### -field <b>Name</b>

<dd>
<p>An array of wide characters that contains the name of the registry key. This character string is <u>not</u> null-terminated. Only the first element in this array is included in the <b>KEY_NODE_INFORMATION</b> structure definition. The storage for the remaining elements in the array immediately follows this element.</p>
</dd>
</dl>

## -remarks
<p>The <a href="..\wdm\nf-wdm-zwenumeratekey.md">ZwEnumerateKey</a> and <a href="..\wdm\nf-wdm-zwquerykey.md">ZwQueryKey</a> routines use the <b>KEY_NODE_INFORMATION</b> structure to contain the registry key name and key class name. When the <i>KeyInformationClass</i> parameter of either routine is <b>KeyNodeInformation</b>, the <i>KeyInformation</i> buffer is treated as a <b>KEY_NODE_INFORMATION</b> structure. For more information about the <b>KeyNodeInformation</b> enumeration value, see <a href="..\wdm\ne-wdm--key-information-class.md">KEY_INFORMATION_CLASS</a>.</p>

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
<a href="..\wdm\ns-wdm--key-basic-information.md">KEY_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--key-cached-information.md">KEY_CACHED_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--key-full-information.md">KEY_FULL_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--key-information-class.md">KEY_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--key-name-information.md">KEY_NAME_INFORMATION</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--key-virtualization-information.md">KEY_VIRTUALIZATION_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwenumeratekey.md">ZwEnumerateKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwquerykey.md">ZwQueryKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KEY_NODE_INFORMATION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
