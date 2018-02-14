---
UID: NI:parallel.IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE
title: IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE
author: windows-driver-content
description: The IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE request clears the operating mode of a parallel port.
old-location: parports\ioctl_internal_parallel_clear_chip_mode.htm
old-project: parports
ms.assetid: bca93bca-96f6-46bb-ba24-9f39b5ad1ab4
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: parports.ioctl_internal_parallel_clear_chip_mode, IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE control code [Parallel Ports], IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE, parallel/IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE, cisspd_912d58fe-f6f8-40c5-b4fe-e8237ea64c04.xml
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	parallel.h
apiname:
-	IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE
product: Windows
targetos: Windows
req.typenames: "*LPRILGBATOKEN, RILGBATOKEN"
---

# IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE IOCTL
The <b>IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE</b> request clears the operating mode of a parallel port.

For more information see, <a href="https://msdn.microsoft.com/a22cdeef-4ae7-49f8-b0b5-a4d68feb4235">Setting and Clearing the Communication Mode on a ParallelPort</a>.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The <b>AssociatedIrp.SystemBuffer</b> member points to a <a href="..\parallel\ns-parallel-_parallel_chip_mode.md">PARALLEL_CHIP_MODE</a> structure that the client allocates to input chip mode information. The client sets the <b>ModeFlags</b> member to the current operating mode.

### Input Buffer Length
The request sets the <b>Parameters.DeviceIoControl.InputBufferLength</b> member to the size, in bytes, of a PARALLEL_CHIP_MODE structure.

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

<a href="..\parallel\ni-parallel-ioctl_internal_parallel_set_chip_mode.md">IOCTL_INTERNAL_PARALLEL_SET_CHIP_MODE</a>



<a href="..\parallel\ns-parallel-_parallel_chip_mode.md">PARALLEL_CHIP_MODE</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE control code%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>