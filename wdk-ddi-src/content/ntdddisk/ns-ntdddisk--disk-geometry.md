---
UID: NS.ntdddisk._DISK_GEOMETRY
title: DISK_GEOMETRY
author: windows-driver-content
description: The DISK_GEOMETRY structure is obsolete and provided only to support existing drivers.
old-location: storage\disk_geometry.htm
old-project: storage
ms.assetid: f92d1f63-4361-4775-88f8-be1c9bf781ef
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DISK_GEOMETRY, DISK_GEOMETRY, *PDISK_GEOMETRY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntdddisk.h
req.include-header: Ntdddisk.h, Ntddk.h, Ntdddisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DISK_GEOMETRY
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

# DISK_GEOMETRY structure



## -description
<p>The DISK_GEOMETRY structure is obsolete and provided only to support existing drivers. New drivers must use <a href="https://msdn.microsoft.com/library/windows/hardware/ff552618">DISK_GEOMETRY_EX</a>. DISK_GEOMETRY is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560357">IOCTL_DISK_GET_DRIVE_GEOMETRY</a> and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560371">IOCTL_DISK_GET_MEDIA_TYPES</a> requests, in order to retrieve information about the geometry of a physical disk. </p>


## -syntax

````
typedef struct _DISK_GEOMETRY {
  LARGE_INTEGER Cylinders;
  MEDIA_TYPE    MediaType;
  ULONG         TracksPerCylinder;
  ULONG         SectorsPerTrack;
  ULONG         BytesPerSector;
} DISK_GEOMETRY, *PDISK_GEOMETRY;
````


## -struct-fields
<dl>

### -field <b>Cylinders</b>

<dd>
<p>Indicates the number of cylinders on the disk device.</p>
</dd>

### -field <b>MediaType</b>

<dd>
<p>Indicates the type of disk. The enumeration <a href="https://msdn.microsoft.com/library/windows/hardware/ff562216">MEDIA_TYPE</a> lists the values that can be assigned to this member. </p>
</dd>

### -field <b>TracksPerCylinder</b>

<dd>
<p>Indicates the number of tracks in a cylinder.</p>
</dd>

### -field <b>SectorsPerTrack</b>

<dd>
<p>Indicates the number of sectors in each track.</p>
</dd>

### -field <b>BytesPerSector</b>

<dd>
<p>Indicates the number of bytes in a disk sector.</p>
</dd>
</dl>

## -remarks
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552618">DISK_GEOMETRY_EX</a> must be used with new drivers, in order to accommodate GUID Partition Table (GPT) partitions. The DISK_GEOMETRY structure is nested within the DISK_GEOMETRY_EX structure.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560371">IOCTL_DISK_GET_MEDIA_TYPES</a> causes an array of these structures to be returned. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552618">DISK_GEOMETRY_EX</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DISK_GEOMETRY structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
