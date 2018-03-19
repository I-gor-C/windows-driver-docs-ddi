---
UID: NI:ntddser.IOCTL_SERIAL_INTERNAL_CANCEL_WAIT_WAKE
title: IOCTL_SERIAL_INTERNAL_CANCEL_WAIT_WAKE
author: windows-driver-content
description: The IOCTL_SERIAL_INTERNAL_CANCEL_WAIT_WAKE request disables the wait/wake operation of a serial device.
old-location: serports\ioctl_serial_internal_cancel_wait_wake.htm
old-project: serports
ms.assetid: 007701f4-4ee0-46e1-963c-e2af2a441a81
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: IOCTL_SERIAL_INTERNAL_CANCEL_WAIT_WAKE, IOCTL_SERIAL_INTERNAL_CANCEL_WAIT_WAKE control code [Serial Ports], ntddser/IOCTL_SERIAL_INTERNAL_CANCEL_WAIT_WAKE, serports.ioctl_serial_internal_cancel_wait_wake, serref_0976b701-5c14-4912-854f-4d5a356744d2.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddser.h
req.include-header: Ntddser.h
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
-	ntddser.h
api_name:
-	IOCTL_SERIAL_INTERNAL_CANCEL_WAIT_WAKE
product: Windows
targetos: Windows
req.typenames: SD_REQUEST_FUNCTION
---

# IOCTL_SERIAL_INTERNAL_CANCEL_WAIT_WAKE IOCTL
The IOCTL_SERIAL_INTERNAL_CANCEL_WAIT_WAKE request disables the wait/wake operation of a serial device.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
None.

### Input Buffer Length
None.

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

The <b>Status</b> member is set to one of the <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/serports/serial-device-control-requests2">Generic Status Values for Serial Device Control Requests</a>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddser.h (include Ntddser.h) |

## See Also

<a href="..\ntddser\ni-ntddser-ioctl_serial_internal_do_wait_wake.md">IOCTL_SERIAL_INTERNAL_DO_WAIT_WAKE</a>