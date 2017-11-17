---
UID: NS.mountmgr._MOUNTMGR_VOLUME_MOUNT_POINT
title: MOUNTMGR_VOLUME_MOUNT_POINT
author: windows-driver-content
description: The MOUNTMGR_VOLUME_MOUNT_POINT structure is used in conjunction with the IOCTL_MOUNTMGR_VOLUME_MOUNT_POINT_CREATED request to inform the mount manager that a volume mount point has been created.
old-location: storage\mountmgr_volume_mount_point.htm
ms.assetid: 2a267992-b4d3-49e1-bb80-3849220f0d1f
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: mountmgr.h
req.include-header: Mountmgr.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MOUNTMGR_VOLUME_MOUNT_POINT
req.alt-loc: mountmgr.h
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
ms.keywords: MOUNTMGR_VOLUME_MOUNT_POINT, MOUNTMGR_VOLUME_MOUNT_POINT, *PMOUNTMGR_VOLUME_MOUNT_POINT
req.iface: 
---

# MOUNTMGR_VOLUME_MOUNT_POINT structure



## -description
<p>The MOUNTMGR_VOLUME_MOUNT_POINT structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560485">IOCTL_MOUNTMGR_VOLUME_MOUNT_POINT_CREATED</a> request to inform the mount manager that a volume mount point has been created. </p>


## -syntax

````
typedef struct _MOUNTMGR_VOLUME_MOUNT_POINT {
  USHORT SourceVolumeNameOffset;
  USHORT SourceVolumeNameLength;
  USHORT TargetVolumeNameOffset;
  USHORT TargetVolumeNameLength;
} MOUNTMGR_VOLUME_MOUNT_POINT, *PMOUNTMGR_VOLUME_MOUNT_POINT;
````


## -struct-fields
<dl>

### -field <b>SourceVolumeNameOffset</b>

<dd>
<p>Contains an offset, in bytes, into the output buffer where the name of the mount point is located. </p>
</dd>

### -field <b>SourceVolumeNameLength</b>

<dd>
<p>Contains the length, in bytes, of the mount point name. </p>
</dd>

### -field <b>TargetVolumeNameOffset</b>

<dd>
<p>Contains an offset, in bytes, into the output buffer where the unique (persistent) volume name of the target device is located. </p>
</dd>

### -field <b>TargetVolumeNameLength</b>

<dd>
<p>Contains the length, in bytes, of the target name. </p>
</dd>
</dl>

## -remarks
<p>Mount point names must contain the full path of a mount point object name in the system object tree. For example: "\DosDevices\E:\FilesysD\mnt". For an explanation of unique volume names and how the mount manager uses them, see <a href="NULL">Supporting Mount Manager Requests in a Storage Class Driver</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mountmgr.h (include Mountmgr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560485">IOCTL_MOUNTMGR_VOLUME_MOUNT_POINT_CREATED</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20MOUNTMGR_VOLUME_MOUNT_POINT structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
