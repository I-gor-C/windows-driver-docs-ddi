---
UID: NS.ntdddisk._FORMAT_PARAMETERS
title: FORMAT_PARAMETERS
author: windows-driver-content
description: The FORMAT_PARAMETERS structure is used in conjunction with the IOCTL_DISK_FORMAT_TRACKS request to format the specified set of contiguous tracks on the disk.
old-location: storage\format_parameters.htm
old-project: storage
ms.assetid: 9c92e010-35d7-40ff-8025-51e945861b9c
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: FORMAT_PARAMETERS, FORMAT_PARAMETERS, *PFORMAT_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntdddisk.h
req.include-header: Ntdddisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FORMAT_PARAMETERS
req.alt-loc: ntdddisk.h
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

# FORMAT_PARAMETERS structure



## -description
<p>The FORMAT_PARAMETERS structure is used in conjunction with the <a href="..\ntdddisk\ni-ntdddisk-ioctl-disk-format-tracks.md">IOCTL_DISK_FORMAT_TRACKS</a> request to format the specified set of contiguous tracks on the disk. </p>


## -syntax

````
typedef struct _FORMAT_PARAMETERS {
  MEDIA_TYPE MediaType;
  ULONG      StartCylinderNumber;
  ULONG      EndCylinderNumber;
  ULONG      StartHeadNumber;
  ULONG      EndHeadNumber;
} FORMAT_PARAMETERS, *PFORMAT_PARAMETERS;
````


## -struct-fields
<dl>

### -field MediaType

<dd>
<p>Indicates format information, such as the disk size and the number of bytes per sector. For a list of the values that can be assigned to this member, see <a href="storage.media_type">MEDIA_TYPE</a>. </p>
</dd>

### -field StartCylinderNumber

<dd>
<p>Indicates the number of the cylinder where the formatting should begin. </p>
</dd>

### -field EndCylinderNumber

<dd>
<p>Indicates the number of the cylinder where the formatting should end. </p>
</dd>

### -field StartHeadNumber

<dd>
<p>Indicates the number of the head where the formatting should begin. </p>
</dd>

### -field EndHeadNumber

<dd>
<p>Indicates the number of the head where the formatting should end. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntdddisk.h (include Ntdddisk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntdddisk\ni-ntdddisk-ioctl-disk-format-tracks.md">IOCTL_DISK_FORMAT_TRACKS</a>
</dt>
<dt>
<a href="storage.media_type">MEDIA_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20FORMAT_PARAMETERS structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
