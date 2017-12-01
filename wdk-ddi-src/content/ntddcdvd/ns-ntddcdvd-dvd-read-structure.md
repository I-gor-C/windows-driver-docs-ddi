---
UID: NS.ntddcdvd.DVD_READ_STRUCTURE
title: DVD_READ_STRUCTURE
author: windows-driver-content
description: The DVD_READ_STRUCTURE structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD descriptor containing information about a DVD disc.
old-location: storage\dvd_read_structure.htm
old-project: storage
ms.assetid: fe8c55de-e542-4c0d-a96b-31ad39e11dff
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DVD_READ_STRUCTURE, DVD_READ_STRUCTURE, *PDVD_READ_STRUCTURE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddcdvd.h
req.include-header: Ntddcdvd.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DVD_READ_STRUCTURE
req.alt-loc: ntddcdvd.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# DVD_READ_STRUCTURE structure



## -description
<p>The DVD_READ_STRUCTURE structure is used in conjunction with the <a href="..\ntddcdvd\ni-ntddcdvd-ioctl-dvd-read-structure.md">IOCTL_DVD_READ_STRUCTURE</a> request to retrieve a DVD descriptor containing information about a DVD disc. </p>


## -syntax

````
typedef struct DVD_READ_STRUCTURE {
  LARGE_INTEGER        BlockByteOffset;
  DVD_STRUCTURE_FORMAT Format;
  DVD_SESSION_ID       SessionId;
  UCHAR                LayerNumber;
} DVD_READ_STRUCTURE, *PDVD_READ_STRUCTURE;
````


## -struct-fields
<dl>

### -field <b>BlockByteOffset</b>

<dd>
<p>Contains an offset to the logical block address of the descriptor to be retrieved. </p>
</dd>

### -field <b>Format</b>

<dd>
<p>Indicates the type of DVD descriptor to retrieve. See the <a href="..\ntddcdvd\ne-ntddcdvd-dvd-structure-format.md">DVD_STRUCTURE_FORMAT</a> enumeration type for further information about the values that can be assigned to this member. </p>
</dd>

### -field <b>SessionId</b>

<dd>
<p>Contains the DVD session ID. </p>
</dd>

### -field <b>LayerNumber</b>

<dd>
<p>Contains the number of the layer where the descriptor is to be retrieved.</p>
</dd>
</dl>

## -remarks
<p>The DVD_READ_STRUCTURE structure contains data such as copyright information, or manufacturer-specific information.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddcdvd.h (include Ntddcdvd.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddcdvd\ni-ntddcdvd-ioctl-dvd-read-structure.md">IOCTL_DVD_READ_STRUCTURE</a>
</dt>
<dt>
<a href="..\ntddcdvd\ne-ntddcdvd-dvd-structure-format.md">DVD_STRUCTURE_FORMAT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DVD_READ_STRUCTURE structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
