---
UID: NI:usbioctl.IOCTL_INTERNAL_USB_GET_BUS_INFO
title: IOCTL_INTERNAL_USB_GET_BUS_INFO
author: windows-driver-content
description: The IOCTL_INTERNAL_USB_GET_BUS_INFO I/O request queries the bus driver for certain bus information.
old-location: buses\ioctl_internal_usb_get_bus_info.htm
old-project: usbref
ms.assetid: 31a5a829-1bb7-45cb-93b0-e899f7737df2
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: IOCTL_INTERNAL_USB_GET_BUS_INFO, IOCTL_INTERNAL_USB_GET_BUS_INFO control code [Buses], buses.ioctl_internal_usb_get_bus_info, usbioctl/IOCTL_INTERNAL_USB_GET_BUS_INFO, usbirp_6f2e2c9c-3bbc-40bd-a2e7-6fc79cfcc02b.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: usbioctl.h
req.include-header: Usbioctl.h
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
-	Usbioctl.h
api_name:
-	IOCTL_INTERNAL_USB_GET_BUS_INFO
product: Windows
targetos: Windows
req.typenames: USB_HUB_TYPE
req.product: Windows 10 or later.
---

# IOCTL_INTERNAL_USB_GET_BUS_INFO IOCTL
The <b>IOCTL_INTERNAL_USB_GET_BUS_INFO</b> I/O request queries the bus driver for certain bus information. 

<b>IOCTL_INTERNAL_USB_GET_BUS_INFO</b> is a kernel-mode I/O control request. This request targets the USB hub PDO. This request must be sent at an IRQL of PASSIVE_LEVEL.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<b>Parameters.Others.Argument1</b> should be a pointer to a <b>USB_BUS_NOTIFICATION</b> structure.

### Input Buffer Length
The size of a <b>USB_BUS_NOTIFICATION</b> structure.

### Output Buffer
<b>Parameters.Others.Argument1</b> points to a <b>USB_BUS_NOTIFICATION</b> structure that has the <b>TotalBandwidth</b>, <b>ConsumedBandwidth</b>, and <b>ControllerNameLength</b> fields filled in.

### Output Buffer Length
The size of a <b>USB_BUS_NOTIFICATION</b> structure.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The bus or port driver sets <b>Irp-&gt;IoStatus.Status</b> to STATUS_SUCCESS or the appropriate error status.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbioctl.h (include Usbioctl.h) |

## See Also

<b>USB_BUS_NOTIFICATION</b>