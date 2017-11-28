---
UID: NS.ntddvol._VOLUME_DISK_EXTENTS
title: VOLUME_DISK_EXTENTS
author: windows-driver-content
description: The VOLUME_DISK_EXTENTS structure is used in conjunction with the IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS request to retrieve information about all the extents on a given volume.
old-location: storage\volume_disk_extents.htm
old-project: storage
ms.assetid: 227846c2-8794-4859-89af-c139ead32143
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: VOLUME_DISK_EXTENTS, VOLUME_DISK_EXTENTS, *PVOLUME_DISK_EXTENTS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddvol.h
req.include-header: Ntddvol.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VOLUME_DISK_EXTENTS
req.alt-loc: ntddvol.h
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

# VOLUME_DISK_EXTENTS structure



## -description
<p>The VOLUME_DISK_EXTENTS structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560644">IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS</a> request to retrieve information about all the extents on a given volume.</p>


## -syntax

````
typedef struct _VOLUME_DISK_EXTENTS {
  ULONG       NumberOfDiskExtents;
  DISK_EXTENT Extents[ANYSIZE_ARRAY];
} VOLUME_DISK_EXTENTS, *PVOLUME_DISK_EXTENTS;
````


## -struct-fields
<dl>

### -field <b>NumberOfDiskExtents</b>

<dd>
<p>Indicates the number of extents that comprise the volume, which can span multiple disks. </p>
</dd>

### -field <b>Extents</b>

<dd>
<p>Indicates the number of extents that comprise the volume, which can span multiple disks. </p>
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
<dt>Ntddvol.h (include Ntddvol.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552606">DISK_EXTENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560644">IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS</a>
</dt>
<dt>disk extent</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20VOLUME_DISK_EXTENTS structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
