---
UID: NI:parallel.IOCTL_INTERNAL_PARALLEL_SET_CHIP_MODE
title: IOCTL_INTERNAL_PARALLEL_SET_CHIP_MODE
author: windows-driver-content
description: The IOCTL_INTERNAL_PARALLEL_SET_CHIP_MODE request sets the operating mode of a parallel port.
old-location: parports\ioctl_internal_parallel_set_chip_mode.htm
old-project: parports
ms.assetid: c6bf2f5a-1682-4437-93b1-1a7e5794befd
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: IOCTL_INTERNAL_PARALLEL_SET_CHIP_MODE, IOCTL_INTERNAL_PARALLEL_SET_CHIP_MODE control code [Parallel Ports], cisspd_f9ea9799-8d87-44e2-89d6-ae1fc0a4f673.xml, parallel/IOCTL_INTERNAL_PARALLEL_SET_CHIP_MODE, parports.ioctl_internal_parallel_set_chip_mode
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: parallel.h
req.include-header: Parallel.h
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
-	parallel.h
api_name:
-	IOCTL_INTERNAL_PARALLEL_SET_CHIP_MODE
product: Windows
targetos: Windows
req.typenames: RILGBATOKEN, *LPRILGBATOKEN
---

# IOCTL_INTERNAL_PARALLEL_SET_CHIP_MODE IOCTL
The <b>IOCTL_INTERNAL_PARALLEL_SET_CHIP_MODE</b> request sets the operating mode of a parallel port.

For more information, see <a href="https://msdn.microsoft.com/a22cdeef-4ae7-49f8-b0b5-a4d68feb4235">Setting and Clearing the Communication Mode on a ParallelPort</a>.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The <b>AssociatedIrp.SystemBuffer</b> member points to a <a href="..\parallel\ns-parallel-_parallel_chip_mode.md">PARALLEL_CHIP_MODE</a> structure that the client allocates to input chip mode information. The client sets the <b>ChipMode</b> member to the requested operating mode.

### Input Buffer Length
The <b>Parameters.DeviceIoControl.InputBufferLength</b> member is set to the size, in bytes, of a PARALLEL_CHIP_MODE structure.

### Output Buffer
None.

### Output Buffer Length
None.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The <b>Information</b> member is set to zero. 

The <b>Status</b> member is set to one of the generic status values returned by internal device control requests for parallel ports or to one of the following values:


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | parallel.h (include Parallel.h) |

## See Also

<a href="..\parallel\ni-parallel-ioctl_internal_parallel_clear_chip_mode.md">IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE</a>



<a href="..\parallel\ns-parallel-_parallel_chip_mode.md">PARALLEL_CHIP_MODE</a>