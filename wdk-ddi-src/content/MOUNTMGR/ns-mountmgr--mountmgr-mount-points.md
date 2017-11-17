---
UID: NS.mountmgr._MOUNTMGR_MOUNT_POINTS
title: MOUNTMGR_MOUNT_POINTS
author: windows-driver-content
description: The MOUNTMGR_MOUNT_POINTS structure is used by mount manager to send a client the list of mount points associated with a device.
old-location: storage\mountmgr_mount_points.htm
ms.assetid: e85c0d92-d989-4afc-8516-c63535d2c728
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
req.alt-api: MOUNTMGR_MOUNT_POINTS
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
ms.keywords: MOUNTMGR_MOUNT_POINTS, MOUNTMGR_MOUNT_POINTS, *PMOUNTMGR_MOUNT_POINTS
req.iface: 
---

# MOUNTMGR_MOUNT_POINTS structure



## -description
<p>The MOUNTMGR_MOUNT_POINTS structure is used by mount manager to send a client the list of mount points associated with a device.</p>


## -syntax

````
typedef struct _MOUNTMGR_MOUNT_POINTS {
  ULONG                Size;
  ULONG                NumberOfMountPoints;
  MOUNTMGR_MOUNT_POINT MountPoints[1];
} MOUNTMGR_MOUNT_POINTS, *PMOUNTMGR_MOUNT_POINTS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Contains the size, in bytes, of the output buffer. </p>
</dd>

### -field <b>NumberOfMountPoints</b>

<dd>
<p>Contains the number of mount points that the mount manager is returning. </p>
</dd>

### -field <b>MountPoints</b>

<dd>
<p>Contains an array of elements of type MOUNTMGR_MOUNT_POINT that contain information about each mount point associated with the device.</p>
</dd>
</dl>

## -remarks
<p>For a discussion of the different between symbolic links, unique IDs, and nonpersistent device names, see <a href="NULL">Supporting Mount Manager Requests in a Storage Class Driver</a>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560474">IOCTL_MOUNTMGR_QUERY_POINTS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20MOUNTMGR_MOUNT_POINTS structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
