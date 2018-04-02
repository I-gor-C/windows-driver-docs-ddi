---
UID: NI:ntdddisk.IOCTL_DISK_GET_DRIVE_GEOMETRY
title: IOCTL_DISK_GET_DRIVE_GEOMETRY
author: windows-driver-content
description: Returns information about the physical disk's geometry (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).
old-location: storage\ioctl_disk_get_drive_geometry.htm
old-project: storage
ms.assetid: 571308bc-1e8e-437a-8819-8b28251a3f03
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IOCTL_DISK_GET_DRIVE_GEOMETRY, IOCTL_DISK_GET_DRIVE_GEOMETRY control code [Storage Devices], k307_e6bc4a05-f2cf-40f7-9632-b78da2087662.xml, ntdddisk/IOCTL_DISK_GET_DRIVE_GEOMETRY, storage.ioctl_disk_get_drive_geometry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntdddisk.h
req.include-header: Ntdddisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntdddisk.h
api_name:
-	IOCTL_DISK_GET_DRIVE_GEOMETRY
product: Windows
targetos: Windows
req.typenames: DETECTION_TYPE
---

# IOCTL_DISK_GET_DRIVE_GEOMETRY IOCTL
Returns information about the physical disk's geometry (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
None

### Input Buffer Length
None

### Output Buffer
The driver returns the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552613">DISK_GEOMETRY</a> data in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>.

### Output Buffer Length
<b>Parameters.DeviceIoControl.OutputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the buffer, which must be &gt;= <b>sizeof</b>(DISK_GEOMETRY).

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The <b>Information</b> field is set to the size, in bytes, of the returned data. The <b>Status</b> field can be set to STATUS_SUCCESS, or possibly to STATUS_UNRECOGNIZED_MEDIA, STATUS_INVALID_PARAMETER, STATUS_INVALID_DEVICE_REQUEST, STATUS_INFO_LENGTH_MISMATCH, STATUS_INSUFFICIENT_RESOURCES, or STATUS_BUFFER_TOO_SMALL.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntdddisk.h (include Ntdddisk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552613">DISK_GEOMETRY</a>