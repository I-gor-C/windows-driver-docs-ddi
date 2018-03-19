---
UID: NI:ntddpar.IOCTL_PAR_SET_INFORMATION
title: IOCTL_PAR_SET_INFORMATION
author: windows-driver-content
description: The IOCTL_PAR_SET_INFORMATION request resets and initializes a parallel device.
old-location: parports\ioctl_par_set_information.htm
old-project: parports
ms.assetid: a54902d0-aa07-4cd0-8ef1-a3c17dff2ac9
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: IOCTL_PAR_SET_INFORMATION, IOCTL_PAR_SET_INFORMATION control code [Parallel Ports], cisspd_950d6397-7eff-4966-a734-0497f1a84257.xml, ntddpar/IOCTL_PAR_SET_INFORMATION, parports.ioctl_par_set_information
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddpar.h
req.include-header: Ntddpar.h
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
-	ntddpar.h
api_name:
-	IOCTL_PAR_SET_INFORMATION
product: Windows
targetos: Windows
req.typenames: OFFLOAD_SECURITY_ASSOCIATION, *POFFLOAD_SECURITY_ASSOCIATION
---

# IOCTL_PAR_SET_INFORMATION IOCTL
The IOCTL_PAR_SET_INFORMATION request resets and initializes a parallel device.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The <b>AssociatedIrp.SystemBuffer</b> member points to a <a href="..\ntddpar\ns-ntddpar-_par_set_information.md">PAR_SET_INFORMATION</a> structure that the client allocates to input set information. The client sets the <b>Init</b> member to PARALLEL_INIT.

### Input Buffer Length
The <b>Parameters.DeviceIoControl.InputBufferLength</b> member is set to the size, in bytes, of a PAR_SET_INFORMATION structure.

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

The <b>Status</b> member is set to one of the generic status values returned by device control requests for parallel devices or to one of the following values:


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddpar.h (include Ntddpar.h) |

## See Also

<a href="..\ntddpar\ns-ntddpar-_par_set_information.md">PAR_SET_INFORMATION</a>



<a href="..\ntddpar\ni-ntddpar-ioctl_par_query_information.md">IOCTL_PAR_QUERY_INFORMATION</a>