---
UID: NI:usbioctl.IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS
title: IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS
author: windows-driver-content
description: The IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS I/O request returns information about the host controller the USB device is attached to, and the device's location in the USB device tree.
old-location: buses\ioctl_internal_usb_get_topology_address.htm
old-project: usbref
ms.assetid: 15a196de-7d6a-408a-97e1-58d6756433db
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS, IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS control code [Buses], buses.ioctl_internal_usb_get_topology_address, usbioctl/IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: usbioctl.h
req.include-header: Usbioctl.h
req.target-type: Windows
req.target-min-winverclnt: Windows Vista and later operating systems.
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
-	Usbioctl.h
api_name:
-	IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS
product:
- Windows
targetos: Windows
req.typenames: USB_HUB_TYPE
req.product: Windows 10 or later.
---

# IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS IOCTL
The <b>IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS</b> 
   I/O request returns information about the host controller the USB device is attached to, and the device's location in the USB device tree.

<b>IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS</b> is a kernel-mode I/O control request. This request targets the USB hub PDO. This request must be sent at an IRQL of DISPATCH_LEVEL or lower.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<b>Parameters.Others.Argument1</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540164">USB_TOPOLOGY_ADDRESS</a> structure to receive the device topology information.

### Input Buffer Length
The size of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540164">USB_TOPOLOGY_ADDRESS</a> structure.

### Output Buffer
<b>Parameters.Others.Argument1</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540164">USB_TOPOLOGY_ADDRESS</a> structure containing the device topology information.

### Output Buffer Length
The size of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540164">USB_TOPOLOGY_ADDRESS</a> structure.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The hub or port driver sets <b>Irp-&gt;IoStatus.Status</b> to STATUS_SUCCESS or the appropriate error status.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows Vista and later operating systems. Windows Vista and later operating systems. |
| **Header** | usbioctl.h (include Usbioctl.h) |

## See Also

<b>USB_TOPOLOGY_ADDRESS</b>