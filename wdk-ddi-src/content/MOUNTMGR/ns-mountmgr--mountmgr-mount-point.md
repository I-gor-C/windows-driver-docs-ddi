---
UID: NS.mountmgr._MOUNTMGR_MOUNT_POINT
title: MOUNTMGR_MOUNT_POINT
author: windows-driver-content
description: The MOUNTMGR_MOUNT_POINT structure is used by mount manager clients in conjunction with an IOCTL_MOUNTMGR_QUERY_POINTS request to query the mount manager for all of the mount points (symbolic links) associated with a device.
old-location: storage\mountmgr_mount_point.htm
ms.assetid: a4142380-1596-49dc-a18d-ac5c3cef73fe
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
req.alt-api: MOUNTMGR_MOUNT_POINT
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
ms.keywords: MOUNTMGR_MOUNT_POINT, MOUNTMGR_MOUNT_POINT, *PMOUNTMGR_MOUNT_POINT
req.iface: 
---

# MOUNTMGR_MOUNT_POINT structure



## -description
<p>The MOUNTMGR_MOUNT_POINT structure is used by mount manager clients in conjunction with an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560474">IOCTL_MOUNTMGR_QUERY_POINTS</a> request to query the mount manager for all of the mount points (symbolic links) associated with a device. The mount manager responds by sending an array of MOUNTMGR_MOUNT_POINT structures containing the mount points. </p>


## -syntax

````
typedef struct _MOUNTMGR_MOUNT_POINT {
  ULONG  SymbolicLinkNameOffset;
  USHORT SymbolicLinkNameLength;
  ULONG  UniqueIdOffset;
  USHORT UniqueIdLength;
  ULONG  DeviceNameOffset;
  USHORT DeviceNameLength;
} MOUNTMGR_MOUNT_POINT, *PMOUNTMGR_MOUNT_POINT;
````


## -struct-fields
<dl>

### -field <b>SymbolicLinkNameOffset</b>

<dd>
<p>Contains an offset, in bytes, into the output buffer where the symbolic link is located.</p>
</dd>

### -field <b>SymbolicLinkNameLength</b>

<dd>
<p>Contains the length, in bytes, of the symbolic link. </p>
</dd>

### -field <b>UniqueIdOffset</b>

<dd>
<p>Contains an offset, in bytes, into the output buffer where the unique ID is located. </p>
</dd>

### -field <b>UniqueIdLength</b>

<dd>
<p>Contains the length, in bytes, of the unique ID. </p>
</dd>

### -field <b>DeviceNameOffset</b>

<dd>
<p>Contains an offset, in bytes, into the output buffer where the nonpersistent device name is located. </p>
</dd>

### -field <b>DeviceNameLength</b>

<dd>
<p>Contains the length, in bytes, of the nonpersistent device name. </p>
</dd>
</dl>

## -remarks
<p>None of the names returned are <b>NULL</b> terminated, nor do the buffers require terminating <b>NULL</b> characters. The caller of <a href="https://msdn.microsoft.com/library/windows/hardware/ff560474">IOCTL_MOUNTMGR_QUERY_POINTS</a> is not required to provide data in all of the members of the MOUNTMGR_MOUNT_POINT structure, but empty members must have an offset of zero.</p>

<p>On input, offsets are from the beginning of the MOUNTMGR_MOUNT_POINT structure. On output offsets are from the beginning of the buffer. This is usually the same as the beginning of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562288">MOUNTMGR_MOUNT_POINTS</a> container structure (as opposed to the embedded MOUNTMGR_MOUNT_POINT array instance).</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560474">IOCTL_MOUNTMGR_QUERY_POINTS</a> request is available in Windows 2000 and later operating systems.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20MOUNTMGR_MOUNT_POINT structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
