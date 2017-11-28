---
UID: NS.wdm._FILE_FULL_EA_INFORMATION
title: FILE_FULL_EA_INFORMATION
author: windows-driver-content
description: The FILE_FULL_EA_INFORMATION structure provides extended attribute (EA) information. This structure is used primarily by network drivers.
old-location: kernel\file_full_ea_information.htm
old-project: kernel
ms.assetid: 1b9bbb6a-2dfb-4f3f-8083-62b51a62dec6
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: FILE_FULL_EA_INFORMATION, FILE_FULL_EA_INFORMATION, *PFILE_FULL_EA_INFORMATION
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
req.alt-api: FILE_FULL_EA_INFORMATION
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

# FILE_FULL_EA_INFORMATION structure



## -description
<p>The <b>FILE_FULL_EA_INFORMATION</b> structure provides extended attribute (EA) information. This structure is used primarily by network drivers.</p>


## -syntax

````
typedef struct _FILE_FULL_EA_INFORMATION {
  ULONG  NextEntryOffset;
  UCHAR  Flags;
  UCHAR  EaNameLength;
  USHORT EaValueLength;
  CHAR   EaName[1];
} FILE_FULL_EA_INFORMATION, *PFILE_FULL_EA_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>NextEntryOffset</b>

<dd>
<p>The offset of the next <b>FILE_FULL_EA_INFORMATION</b>-type entry. This member is zero if no other entries follow this one. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Can be zero or can be set with FILE_NEED_EA, indicating that the file to which the EA belongs cannot be interpreted without understanding the associated extended attributes.</p>
</dd>

### -field <b>EaNameLength</b>

<dd>
<p>The length in bytes of the <b>EaName</b> array. This value does not include a null-terminator to <b>EaName</b>. </p>
</dd>

### -field <b>EaValueLength</b>

<dd>
<p>The length in bytes of each EA value in the array.</p>
</dd>

### -field <b>EaName</b>

<dd>
<p>An array of characters naming the EA for this entry.</p>
</dd>
</dl>

## -remarks
<p>This structure is longword-aligned. If a set of <b>FILE_FULL_EA_INFORMATION</b> entries is buffered, <b>NextEntryOffset</b> value in each entry, except the last, falls on a longword boundary. </p>

<p>The value(s) associated with each entry follows the <b>EaName</b> array. That is, an EA's values are located at <b>EaName</b> + (<b>EaNameLength</b> + 1). </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20FILE_FULL_EA_INFORMATION structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
