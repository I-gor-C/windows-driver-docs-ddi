---
UID: NS.ntddk._KEY_NAME_INFORMATION
title: KEY_NAME_INFORMATION
author: windows-driver-content
description: The KEY_NAME_INFORMATION structure holds the name and name length of the key.
old-location: kernel\key_name_information.htm
old-project: kernel
ms.assetid: 5b46e7d9-fbb0-4e55-b1f5-d9d0f1dd1f2c
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KEY_NAME_INFORMATION, KEY_NAME_INFORMATION, *PKEY_NAME_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KEY_NAME_INFORMATION
req.alt-loc: Ntddk.h
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
---

# KEY_NAME_INFORMATION structure



## -description
<p>The <b>KEY_NAME_INFORMATION</b> structure holds the name and name length of the key.</p>


## -syntax

````
typedef struct _KEY_NAME_INFORMATION {
  ULONG NameLength;
  WCHAR Name[1];
} KEY_NAME_INFORMATION, *PKEY_NAME_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>NameLength</b>

<dd>
<p>The size, in bytes, of the key name string in the <b>Name</b> array.</p>
</dd>

### -field <b>Name</b>

<dd>
<p>An array of wide characters that contains the name of the key. This character string is <u>not</u> null-terminated. Only the first element in this array is included in the <b>KEY_NAME_INFORMATION</b> structure definition. The storage for the remaining elements in the array immediately follows this element.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff567060">ZwQueryKey</a> routine uses the <b>KEY_NAME_INFORMATION</b> structure to contain the registry key name. When the <i>KeyInformationClass</i> parameter of this routine is <b>KeyNameInformation</b>, the <i>KeyInformation</i> buffer is treated as a <b>KEY_NAME_INFORMATION</b> structure.  For more information about the <b>KeyNameInformation</b> enumeration value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff553373">KEY_INFORMATION_CLASS</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553392">KEY_NODE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554221">KEY_VIRTUALIZATION_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567060">ZwQueryKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KEY_NAME_INFORMATION structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
