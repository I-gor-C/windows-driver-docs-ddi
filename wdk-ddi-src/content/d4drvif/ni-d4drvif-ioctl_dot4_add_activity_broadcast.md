---
UID: NI:d4drvif.IOCTL_DOT4_ADD_ACTIVITY_BROADCAST
title: IOCTL_DOT4_ADD_ACTIVITY_BROADCAST
author: windows-driver-content
description: This topic describes IOCTL_DOT4_ADD_ACTIVITY_BROADCAST.
old-location: print\ioctl_ioctl_dot4_add_activity_broadcast.htm
old-project: print
ms.assetid: 5B4E96FB-3214-4303-B8EB-9AB5CB42D8C7
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IOCTL_DOT4_ADD_ACTIVITY_BROADCAST, IOCTL_DOT4_ADD_ACTIVITY_BROADCAST control code [Print Devices], d4drvif/IOCTL_DOT4_ADD_ACTIVITY_BROADCAST, print.ioctl_ioctl_dot4_add_activity_broadcast
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: d4drvif.h
req.include-header: 
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
-	D4drvif.h
api_name:
-	IOCTL_DOT4_ADD_ACTIVITY_BROADCAST
product:
- Windows
targetos: Windows
req.typenames: D3DDDIARG_GETENCRYPTIONBLTKEY
---

# IOCTL_DOT4_ADD_ACTIVITY_BROADCAST IOCTL
This topic describes <b>IOCTL_DOT4_ADD_ACTIVITY_BROADCAST</b>.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer


### Input Buffer Length
None

### Output Buffer


### Output Buffer Length


### Input / Output Buffer


### Input / Output Buffer Length


### Status Block
<b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d4drvif.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542894">Creating IOCTL Requests in Drivers</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548651">WdfIoTargetSendInternalIoctlOthersSynchronously</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548656">WdfIoTargetSendInternalIoctlSynchronously</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548660">WdfIoTargetSendIoctlSynchronously</a>