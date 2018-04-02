---
UID: NI:ntddcdrm.IOCTL_CDROM_READ_Q_CHANNEL
title: IOCTL_CDROM_READ_Q_CHANNEL
author: windows-driver-content
description: Returns the current position, media catalog, or ISRC track data. Obsolete, beginning with Windows Vista.
old-location: storage\ioctl_cdrom_read_q_channel.htm
old-project: storage
ms.assetid: bbcf1535-6454-45b5-bcbd-752b8bfd6517
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IOCTL_CDROM_READ_Q_CHANNEL, IOCTL_CDROM_READ_Q_CHANNEL control code [Storage Devices], k307_1b91e5f3-ecd0-429d-a4d1-8b77170d14e7.xml, ntddcdrm/IOCTL_CDROM_READ_Q_CHANNEL, storage.ioctl_cdrom_read_q_channel
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddcdrm.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: Obsolete, beginning with Windows Vista.
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
-	ntddcdrm.h
api_name:
-	IOCTL_CDROM_READ_Q_CHANNEL
product: Windows
targetos: Windows
req.typenames: WRITE_ROTATION, *PWRITE_ROTATION
---

# IOCTL_CDROM_READ_Q_CHANNEL IOCTL
Returns the current position, media catalog, or ISRC track data. Obsolete, beginning with Windows Vista.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551371">CDROM_SUB_Q_DATA_FORMAT</a> structure with the <b>Format</b> member set to one of the following:

IOCTL_CDROM_CURRENT_POSITION

IOCTL_CDROM_MEDIA_CATALOG

IOCTL_CDROM_TRACK_ISRC

If <b>Format</b> is set to IOCTL_CDROM_TRACK_ISRC, <b>Track</b> must be set to the track for which ISRC data is requested.

### Input Buffer Length
Length of a <b>
       Parameters.DeviceIoControl.OutputBufferLength</b> in the I/O stack location indicates the size, in bytes, of the buffer, which must be &gt;= <b>sizeof</b>(SUB_Q_CHANNEL_DATA).

.

### Output Buffer
The driver returns the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567595">SUB_Q_CHANNEL_DATA</a> information in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>.

### Output Buffer Length
Length of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567595">SUB_Q_CHANNEL_DATA</a>.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The <b>Information</b> field is set to the number of bytes returned. The <b>Status</b> field is set to STATUS_SUCCESS, or possibly to STATUS_BUFFER_TOO_SMALL, STATUS_IO_DEVICE_ERROR, STATUS_INSUFFICIENT_RESOURCES, STATUS_INVALID_DEVICE_REQUEST, STATUS_NO_MEDIA_IN_DEVICE, STATUS_DEVICE_NOT_READY, STATUS_IO_TIME_OUT, or STATUS_VERIFY_REQUIRED.

## Remarks
Beginning with Windows Vista, CDROM class drivers do not use this IOCTL. Prior to Windows Vista, this IOCTL was used for audio playback on older CD-ROM drives that supported direct audio output in hardware.

Client applications should use the <i>Media Control Interface (MCI) API</i> rather than issuing this IOCTL.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Obsolete, beginning with Windows Vista. Obsolete, beginning with Windows Vista. |
| **Header** | ntddcdrm.h (include Ntddcdrm.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff567595">SUB_Q_CHANNEL_DATA</a>