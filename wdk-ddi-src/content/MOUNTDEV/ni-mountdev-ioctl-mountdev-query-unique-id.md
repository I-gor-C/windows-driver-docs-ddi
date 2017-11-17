---
UID: NI.mountdev.IOCTL_MOUNTDEV_QUERY_UNIQUE_ID
title: IOCTL_MOUNTDEV_QUERY_UNIQUE_ID
author: windows-driver-content
description: Support for this IOCTL by mount manager clients is mandatory.
old-location: storage\ioctl_mountdev_query_unique_id.htm
ms.assetid: 866b9383-d73d-4be1-a4de-b78c9558c3ce
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: ioctl
ms.prod: windows-hardware
ms.technology: Storage
req.header: mountdev.h
req.include-header: Mountdev.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_MOUNTDEV_QUERY_UNIQUE_ID
req.alt-loc: Mountdev.h
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
ms.keywords: PST_PARAMETER_DATA, ST_PARAMETER_DATA, *PST_PARAMETER_DATA
req.iface: 
---

# IOCTL_MOUNTDEV_QUERY_UNIQUE_ID IOCTL



## -description
<p>Support for this IOCTL by mount manager clients is mandatory. Upon receiving this IOCTL, the mount manager client must provide a counted byte string identifier that is unique to the client (that is, the device or the volume). The client cannot change this unique ID without alerting the mount manager (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560443">IOCTL_MOUNTDEV_UNIQUE_ID_CHANGE_NOTIFY</a>). </p>


## -ioctlparameters

### -input-buffer

<text></text>

### -input-buffer-length

<text></text>

### -output-buffer
<p>The device class or volume driver returns the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562264">MOUNTDEV_UNIQUE_ID</a> structure in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>.</p>

### -output-buffer-length
<p><b>Parameters.DeviceIoControl.OutputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the output buffer, which must be greater than or equal to <b>sizeof</b>(MOUNTDEV_UNIQUE_ID).</p>

<p><b>Parameters.DeviceIoControl.OutputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the output buffer, which must be greater than or equal to <b>sizeof</b>(MOUNTDEV_UNIQUE_ID).</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The <b>Information</b> field is set to FIELD_OFFSET(<a href="https://msdn.microsoft.com/library/windows/hardware/ff562264">MOUNTDEV_UNIQUE_ID</a>, UniqueId) + output-&gt;UniqueIdLength; or alternatively to sizeof(USHORT) + output-&gt;UniqueIdLength, where output points to the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>.</p>

<p>The <b>Information</b> field is set to FIELD_OFFSET(<a href="https://msdn.microsoft.com/library/windows/hardware/ff562264">MOUNTDEV_UNIQUE_ID</a>, UniqueId) + output-&gt;UniqueIdLength; or alternatively to sizeof(USHORT) + output-&gt;UniqueIdLength, where output points to the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>.</p>

<p>The <b>Information</b> field is set to FIELD_OFFSET(<a href="https://msdn.microsoft.com/library/windows/hardware/ff562264">MOUNTDEV_UNIQUE_ID</a>, UniqueId) + output-&gt;UniqueIdLength; or alternatively to sizeof(USHORT) + output-&gt;UniqueIdLength, where output points to the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mountdev.h (include Mountdev.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560443">IOCTL_MOUNTDEV_UNIQUE_ID_CHANGE_NOTIFY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562264">MOUNTDEV_UNIQUE_ID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20IOCTL_MOUNTDEV_QUERY_UNIQUE_ID control code%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
