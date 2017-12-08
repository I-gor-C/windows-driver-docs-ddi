---
UID: NI.mountmgr.IOCTL_MOUNTMGR_VOLUME_MOUNT_POINT_DELETED
title: IOCTL_MOUNTMGR_VOLUME_MOUNT_POINT_DELETED
author: windows-driver-content
description: The mount manager clients use this IOCTL to alert the mount manager that a volume mount point has been deleted so that the mount manager can replicate the database entry for the given mount point.
old-location: storage\ioctl_mountmgr_volume_mount_point_deleted.htm
old-project: storage
ms.assetid: 8a436053-87c2-4fa2-9280-7035a990d0b4
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MOUNTDEV_UNIQUE_ID, MOUNTDEV_UNIQUE_ID, *PMOUNTDEV_UNIQUE_ID
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: mountmgr.h
req.include-header: Mountmgr.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_MOUNTMGR_VOLUME_MOUNT_POINT_DELETED
req.alt-loc: Mountmgr.h
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

# IOCTL_MOUNTMGR_VOLUME_MOUNT_POINT_DELETED IOCTL



## -description
<p>The mount manager clients use this IOCTL to alert the mount manager that a volume mount point has been deleted so that the mount manager can replicate the database entry for the given mount point.</p>
<p>The Microsoft Win32 routine <b>DeleteVolumeMountPoint</b> sends this IOCTL to the mount manager, to inform the mount manager that a directory junction is no longer pointing to a volume name. The mount manager responds by deleting the volume name formerly contained in the directory junction along with its unique ID from the volume hosting the directory junction. </p>


## -ioctlparameters

### -input-buffer
<p>The mount manager client initializes the <a href="..\mountmgr\ns-mountmgr--mountmgr-volume-mount-point.md">MOUNTMGR_VOLUME_MOUNT_POINT</a> structure, defined in <i>Mountmgr.h</i>, at the beginning of the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>.</p>

### -input-buffer-length
<p><b>Parameters.DeviceIoControl.InputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the input buffer, which must be greater than or equal to <b>sizeof</b>(MOUNTMGR_VOLUME_MOUNT_POINT).</p>

<p><b>Parameters.DeviceIoControl.InputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the input buffer, which must be greater than or equal to <b>sizeof</b>(MOUNTMGR_VOLUME_MOUNT_POINT).</p>

### -output-buffer
<p>None</p>

<p>None</p>

<p>None</p>

### -output-buffer-length
<p>None</p>

<p>None</p>

<p>None</p>

<p>None</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>If the operation is successful, the <b>Status</b> field is set to STATUS_SUCCESS.</p>

<p>If <b>InputBufferLength</b> is less than <b>sizeof</b>(MOUNTMGR_VOLUME_MOUNT_POINT), the <b>Status</b> field is set to STATUS_INVALID_PARAMETER.</p>

<p>If the operation is successful, the <b>Status</b> field is set to STATUS_SUCCESS.</p>

<p>If <b>InputBufferLength</b> is less than <b>sizeof</b>(MOUNTMGR_VOLUME_MOUNT_POINT), the <b>Status</b> field is set to STATUS_INVALID_PARAMETER.</p>

<p>If the operation is successful, the <b>Status</b> field is set to STATUS_SUCCESS.</p>

<p>If <b>InputBufferLength</b> is less than <b>sizeof</b>(MOUNTMGR_VOLUME_MOUNT_POINT), the <b>Status</b> field is set to STATUS_INVALID_PARAMETER.</p>

<p>If the operation is successful, the <b>Status</b> field is set to STATUS_SUCCESS.</p>

<p>If <b>InputBufferLength</b> is less than <b>sizeof</b>(MOUNTMGR_VOLUME_MOUNT_POINT), the <b>Status</b> field is set to STATUS_INVALID_PARAMETER.</p>

<p>If the operation is successful, the <b>Status</b> field is set to STATUS_SUCCESS.</p>

<p>If <b>InputBufferLength</b> is less than <b>sizeof</b>(MOUNTMGR_VOLUME_MOUNT_POINT), the <b>Status</b> field is set to STATUS_INVALID_PARAMETER.</p>

## -remarks


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
<a href="..\mountmgr\ns-mountmgr--mountmgr-volume-mount-point.md">MOUNTMGR_VOLUME_MOUNT_POINT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_MOUNTMGR_VOLUME_MOUNT_POINT_DELETED control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
