---
UID: NI:ntddcdrm.IOCTL_CDROM_GET_PERFORMANCE
title: IOCTL_CDROM_GET_PERFORMANCE
author: windows-driver-content
description: Retrieves the supported speeds from the device. The IOCTL_CDROM_GET_PERFORMANCE I/O control request is a wrapper over the MMC command, GET PERFORMANCE.
old-location: storage\ioctl_cdrom_get_performance.htm
old-project: storage
ms.assetid: 3BA2D85A-052B-4851-B31C-072F2872F3FE
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IOCTL_CDROM_GET_PERFORMANCE, IOCTL_CDROM_GET_PERFORMANCE control code [Storage Devices], ntddcdrm/IOCTL_CDROM_GET_PERFORMANCE, storage.ioctl_cdrom_get_performance
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
-	IOCTL_CDROM_GET_PERFORMANCE
product:
- Windows
targetos: Windows
req.typenames: WRITE_ROTATION, *PWRITE_ROTATION
---

# IOCTL_CDROM_GET_PERFORMANCE IOCTL
Retrieves the supported speeds from the device. The <b>IOCTL_CDROM_GET_PERFORMANCE</b> 
   I/O control request   is a wrapper over the MMC command, GET PERFORMANCE.

To perform this operation, call the 
   <a href="https://msdn.microsoft.com/1d35c087-6672-4fc6-baa1-a886dd9d3878">DeviceIoControl</a> 
   function with   <b>IOCTL_CDROM_GET_PERFORMANCE</b> as the <i>dwIoControlCode</i> parameter.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<a href="https://msdn.microsoft.com/library/windows/hardware/gg441233">CDROM_PERFORMANCE_REQUEST</a> requests performance data.
<a href="https://msdn.microsoft.com/library/windows/hardware/gg441240">CDROM_WRITE_SPEED_REQUEST</a> requests write speed descriptor.

### Input Buffer Length
Length of a <a href="https://msdn.microsoft.com/library/windows/hardware/gg441233">CDROM_PERFORMANCE_REQUEST</a>.

### Output Buffer
For request type CdromWriteSpeedRequest, this IOCTL returns the <a href="https://msdn.microsoft.com/library/windows/hardware/gg441232">CDROM_PERFORMANCE_HEADER</a> structure followed by a number of CDROM_WRITE_SPEED_DESCRIPTOR descriptors.

For request type CdromPerformanceRequest, this  IOCTL returns the <a href="https://msdn.microsoft.com/library/windows/hardware/gg441232">CDROM_PERFORMANCE_HEADER</a> structure followed by an optional descriptor. The descriptor following this header depends on the value in the <b>Except</b> field of the <b>CDROM_PERFORMANCE_HEADER</b> structure. If <b>Except</b> is false, CDROM_NOMINAL_PERFORMANCE_DESCRIPTOR is used; otherwise, CDROM_EXCEPTION_PERFORMANCE_DESCRIPTOR is used.

### Output Buffer Length
Length of a <a href="https://msdn.microsoft.com/library/windows/hardware/gg441232">CDROM_PERFORMANCE_HEADER</a>.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The <b>Information</b> field is set to the number of bytes returned. 

Because of  status code propagation from other APIs, the <b>Status</b> field can be set to (but is not limited to) the following:


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddcdrm.h (include Winioctl.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/gg441232">CDROM_PERFORMANCE_HEADER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/gg441233">CDROM_PERFORMANCE_REQUEST</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/gg441240">CDROM_WRITE_SPEED_REQUEST</a>



<a href="https://msdn.microsoft.com/1d35c087-6672-4fc6-baa1-a886dd9d3878">DeviceIoControl</a>