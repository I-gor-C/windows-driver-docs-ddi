---
UID: NS.wdm._KEY_FULL_INFORMATION
title: KEY_FULL_INFORMATION
author: windows-driver-content
description: The KEY_FULL_INFORMATION structure defines the information available for a registry key, including information about its subkeys and the maximum length for their names and value entries.
old-location: kernel\key_full_information.htm
old-project: kernel
ms.assetid: dd099435-e3e3-4d78-a829-0f12f2db46d9
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KEY_FULL_INFORMATION, KEY_FULL_INFORMATION, *PKEY_FULL_INFORMATION
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
req.alt-api: KEY_FULL_INFORMATION
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

# KEY_FULL_INFORMATION structure



## -description
<p>The <b>KEY_FULL_INFORMATION</b> structure defines the information available for a registry key, including information about its subkeys and the maximum length for their names and value entries. This information can be used to size buffers to get the names of subkeys and their value entries.</p>


## -syntax

````
typedef struct _KEY_FULL_INFORMATION {
  LARGE_INTEGER LastWriteTime;
  ULONG         TitleIndex;
  ULONG         ClassOffset;
  ULONG         ClassLength;
  ULONG         SubKeys;
  ULONG         MaxNameLen;
  ULONG         MaxClassLen;
  ULONG         Values;
  ULONG         MaxValueNameLen;
  ULONG         MaxValueDataLen;
  WCHAR         Class[1];
} KEY_FULL_INFORMATION, *PKEY_FULL_INFORMATION;
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
<p>The byte offset from the start of this structure to the <b>Class</b> member.</p>
</dd>

### -field <b>ClassLength</b>

<dd>
<p>The size, in bytes, of the key class name string in the <b>Class</b> array.</p>
</dd>

### -field <b>SubKeys</b>

<dd>
<p>The number of subkeys for this key.</p>
</dd>

### -field <b>MaxNameLen</b>

<dd>
<p>The maximum size, in bytes, of any name for a subkey.</p>
</dd>

### -field <b>MaxClassLen</b>

<dd>
<p>The maximum size, in bytes, of a class name.</p>
</dd>

### -field <b>Values</b>

<dd>
<p>The number of value entries for this key.</p>
</dd>

### -field <b>MaxValueNameLen</b>

<dd>
<p>The maximum size, in bytes, of a value entry name.</p>
</dd>

### -field <b>MaxValueDataLen</b>

<dd>
<p>The maximum size, in bytes, of a value entry data field.</p>
</dd>

### -field <b>Class</b>

<dd>
<p>An array of wide characters that contains the name of the class of the key. This character string is <u>not</u> null-terminated. Only the first element in this array is included in the <b>KEY_FULL_INFORMATION</b> structure definition. The storage for the remaining elements in the array immediately follows this element.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff566447">ZwEnumerateKey</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567060">ZwQueryKey</a> routines use the <b>KEY_FULL_INFORMATION</b> structure to contain the full information for a registry key. When the <i>KeyInformationClass</i> parameter of either routine is <b>KeyFullInformation</b>, the <i>KeyInformation</i> buffer is treated as a <b>KEY_FULL_INFORMATION</b> structure.  For more information about the <b>KeyFullInformation</b> enumeration value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff553373">KEY_INFORMATION_CLASS</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553355">KEY_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553358">KEY_CACHED_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553373">KEY_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553381">KEY_NAME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553392">KEY_NODE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554221">KEY_VIRTUALIZATION_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566447">ZwEnumerateKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567060">ZwQueryKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KEY_FULL_INFORMATION structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
