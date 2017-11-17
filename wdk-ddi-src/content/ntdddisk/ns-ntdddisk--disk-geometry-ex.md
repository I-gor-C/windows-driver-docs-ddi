---
UID: NS.ntdddisk._DISK_GEOMETRY_EX
title: DISK_GEOMETRY_EX
author: windows-driver-content
description: The DISK_GEOMETRY_EX structure is a variable-length structure composed of a DISK_GEOMETRY structure followed by a DISK_PARTITION_INFO structure followed, in turn, by a DISK_DETECTION_INFO structure.
old-location: storage\disk_geometry_ex.htm
ms.assetid: 6397c0dd-4dc7-49fa-85a7-841f6c2b30d8
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntdddisk.h
req.include-header: Ntdddisk.h, Ntddk.h, Ntdddisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DISK_GEOMETRY_EX
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
ms.keywords: DISK_GEOMETRY_EX, DISK_GEOMETRY_EX, *PDISK_GEOMETRY_EX
req.iface: 
---

# DISK_GEOMETRY_EX structure



## -description
<p>The <b>DISK_GEOMETRY_EX</b> structure is a variable-length structure composed of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552613">DISK_GEOMETRY</a> structure followed by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552629">DISK_PARTITION_INFO</a> structure followed, in turn, by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552601">DISK_DETECTION_INFO</a> structure. </p>


## -syntax

````
typedef struct _DISK_GEOMETRY_EX {
  DISK_GEOMETRY Geometry;
  LARGE_INTEGER DiskSize;
  UCHAR         Data[1];
} DISK_GEOMETRY_EX, *PDISK_GEOMETRY_EX;
````


## -struct-fields
<dl>

### -field <b>Geometry</b>

<dd>
<p>See <a href="https://msdn.microsoft.com/library/windows/hardware/ff552613">DISK_GEOMETRY</a> for a description of this member. </p>
</dd>

### -field <b>DiskSize</b>

<dd>
<p>Contains the size in bytes of the disk. </p>
</dd>

### -field <b>Data</b>

<dd>
<p>Pointer to a variable length area containing a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552629">DISK_PARTITION_INFO</a> structure followed by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552601">DISK_DETECTION_INFO</a> structure.</p>
</dd>
</dl>

## -remarks
<p>DISK_GEOMETRY_EX is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560359">IOCTL_DISK_GET_DRIVE_GEOMETRY_EX</a> and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560371">IOCTL_DISK_GET_MEDIA_TYPES</a> IOCTLs, in order to retrieve information about the geometry of a physical disk (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).</p>

<p>Because the partition and detect information are not at fixed locations within the <b>DISK_GEOMETRY_EX</b> structure, <i>ntdddisk.h</i> provides two macros for accessing this information. Both macros take a pointer to a structure of type <b>DISK_GEOMETRY_EX</b> as an argument:</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntdddisk.h (include Ntdddisk.h, Ntddk.h, or Ntdddisk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552613">DISK_GEOMETRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552629">DISK_PARTITION_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552601">DISK_DETECTION_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560357">IOCTL_DISK_GET_DRIVE_GEOMETRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560371">IOCTL_DISK_GET_MEDIA_TYPES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20DISK_GEOMETRY_EX structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
