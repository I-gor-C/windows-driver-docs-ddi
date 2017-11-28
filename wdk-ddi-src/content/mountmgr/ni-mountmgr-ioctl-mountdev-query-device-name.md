---
UID: NI.mountmgr.IOCTL_MOUNTDEV_QUERY_DEVICE_NAME
title: IOCTL_MOUNTDEV_QUERY_DEVICE_NAME
author: windows-driver-content
description: Support for this IOCTL by the mount manager clients is mandatory.
old-location: storage\ioctl_mountdev_query_device_name.htm
old-project: storage
ms.assetid: 3df96552-d4f6-4d1c-bc07-3eff5f3eabfb
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
req.alt-api: IOCTL_MOUNTDEV_QUERY_DEVICE_NAME
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

# IOCTL_MOUNTDEV_QUERY_DEVICE_NAME IOCTL



## -description
<p>Support for this IOCTL by the mount manager clients is mandatory. Upon receiving this IOCTL a client driver must provide the (nonpersistent) device (or target) name for the volume. The mount manager uses the <i>device name</i> returned by the client as the target of a symbolic link. An example of a device name would be "\Device\HarddiskVolume1".</p>


## -ioctlparameters

### -input-buffer

<text></text>

### -input-buffer-length

<text></text>

### -output-buffer
<p>The mount manager client returns a variable-length structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff562256">MOUNTDEV_NAME</a>, defined in <i>Mountmgr.h</i>, at the beginning of the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>. The device name must be inserted at the address pointed to by the <i>Name</i> member of this structure.</p>

### -output-buffer-length
<p><b>Parameters.DeviceIoControl.OutputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the output buffer, which must be greater than or equal to <b>sizeof</b>(MOUNTDEV_NAME).</p>

<p><b>Parameters.DeviceIoControl.OutputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the output buffer, which must be greater than or equal to <b>sizeof</b>(MOUNTDEV_NAME).</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The <b>Information</b> field is set to FIELD_OFFSET(<a href="https://msdn.microsoft.com/library/windows/hardware/ff562256">MOUNTDEV_NAME</a>, Name) + output-&gt;NameLength, or alternatively, output-&gt;NameLength + sizeof(USHORT), where output points to the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b></p>

<p>If the operation is successful, the mount manager client must set the <b>Information</b> field to the length of the <b>NULL</b>-terminated string containing the device name and the <b>Status</b> field to STATUS_SUCCESS. </p>

<p>If the output buffer is too small to hold the device name, the mount manager client must set the <b>Information</b> field to <b>sizeof</b>(MOUNTDEV_NAME) and the <b>Status</b> field to STATUS_BUFFER_OVERFLOW. In addition, the mount manager client fills in the NameLength member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562256">MOUNTDEV_NAME</a> structure.</p>

<p>The <b>Information</b> field is set to FIELD_OFFSET(<a href="https://msdn.microsoft.com/library/windows/hardware/ff562256">MOUNTDEV_NAME</a>, Name) + output-&gt;NameLength, or alternatively, output-&gt;NameLength + sizeof(USHORT), where output points to the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b></p>

<p>If the operation is successful, the mount manager client must set the <b>Information</b> field to the length of the <b>NULL</b>-terminated string containing the device name and the <b>Status</b> field to STATUS_SUCCESS. </p>

<p>If the output buffer is too small to hold the device name, the mount manager client must set the <b>Information</b> field to <b>sizeof</b>(MOUNTDEV_NAME) and the <b>Status</b> field to STATUS_BUFFER_OVERFLOW. In addition, the mount manager client fills in the NameLength member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562256">MOUNTDEV_NAME</a> structure.</p>

<p>The <b>Information</b> field is set to FIELD_OFFSET(<a href="https://msdn.microsoft.com/library/windows/hardware/ff562256">MOUNTDEV_NAME</a>, Name) + output-&gt;NameLength, or alternatively, output-&gt;NameLength + sizeof(USHORT), where output points to the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b></p>

<p>If the operation is successful, the mount manager client must set the <b>Information</b> field to the length of the <b>NULL</b>-terminated string containing the device name and the <b>Status</b> field to STATUS_SUCCESS. </p>

<p>If the output buffer is too small to hold the device name, the mount manager client must set the <b>Information</b> field to <b>sizeof</b>(MOUNTDEV_NAME) and the <b>Status</b> field to STATUS_BUFFER_OVERFLOW. In addition, the mount manager client fills in the NameLength member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562256">MOUNTDEV_NAME</a> structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562256">MOUNTDEV_NAME</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_MOUNTDEV_QUERY_DEVICE_NAME control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
