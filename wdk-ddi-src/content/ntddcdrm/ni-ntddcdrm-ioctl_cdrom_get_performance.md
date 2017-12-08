---
UID: NI.ntddcdrm.IOCTL_CDROM_GET_PERFORMANCE
title: IOCTL_CDROM_GET_PERFORMANCE
author: windows-driver-content
description: Retrieves the supported speeds from the device. The IOCTL_CDROM_GET_PERFORMANCE I/O control request is a wrapper over the MMC command, GET PERFORMANCE.
old-location: storage\ioctl_cdrom_get_performance.htm
old-project: storage
ms.assetid: 3BA2D85A-052B-4851-B31C-072F2872F3FE
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: _WRITE_ROTATION, *PWRITE_ROTATION, WRITE_ROTATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddcdrm.h
req.include-header: Winioctl.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_CDROM_GET_PERFORMANCE
req.alt-loc: ntddcdrm.h
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
---

# IOCTL_CDROM_GET_PERFORMANCE IOCTL



## -description
Retrieves the supported speeds from the device. The <b>IOCTL_CDROM_GET_PERFORMANCE</b> 
   I/O control request   is a wrapper over the MMC command, GET PERFORMANCE.
To perform this operation, call the 
   <a href="base.deviceiocontrol">DeviceIoControl</a> 
   function with   <b>IOCTL_CDROM_GET_PERFORMANCE</b> as the <i>dwIoControlCode</i> parameter.


## -ioctlparameters

### -input-buffer

<text></text>

### -input-buffer-length

<text></text>

### -output-buffer

<text></text>

### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block

Irp->IoStatus.Status is set to STATUS_SUCCESS if the request is successful.
Otherwise, Status to the appropriate error condition as a NTSTATUS code. 
For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntddcdrm.h (include Winioctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="base.deviceiocontrol">DeviceIoControl</a>
</dt>
<dt>
<a href="storage.cdrom_performance_request">CDROM_PERFORMANCE_REQUEST</a>
</dt>
<dt>
<a href="storage.cdrom_write_speed_request">CDROM_WRITE_SPEED_REQUEST</a>
</dt>
<dt>
<a href="storage.cdrom_performance_header">CDROM_PERFORMANCE_HEADER</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_CDROM_GET_PERFORMANCE control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
