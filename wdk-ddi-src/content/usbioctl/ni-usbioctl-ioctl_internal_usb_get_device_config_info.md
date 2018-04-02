---
UID: NI:usbioctl.IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO
title: IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO
author: windows-driver-content
description: The IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO I/O request returns information about a USB device and the hub it is attached to.
old-location: buses\ioctl_internal_usb_get_device_config_info.htm
old-project: usbref
ms.assetid: 518de598-6281-4838-b453-9f699524cbf4
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO, IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO control code [Buses], buses.ioctl_internal_usb_get_device_config_info, usbioctl/IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO
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
-	IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO
product: Windows
targetos: Windows
req.typenames: USB_HUB_TYPE
req.product: Windows 10 or later.
---

# IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO IOCTL
The <b>IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO</b> 
   I/O request returns information about a USB device and the hub it is attached to.


<b>IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO</b> is a kernel-mode I/O control request. This request targets the USB hub PDO. This request must be sent at an IRQL of DISPATCH_LEVEL or lower.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<b>Parameters.Others.Argument1</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff537179">HUB_DEVICE_CONFIG_INFO</a> structure to receive the device configuration information.

### Input Buffer Length
The size of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff537179">HUB_DEVICE_CONFIG_INFO</a> structure.

### Output Buffer
<b>Parameters.Others.Argument1</b> points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff537179">HUB_DEVICE_CONFIG_INFO</a> structure containing the device configuration information.

### Output Buffer Length
The size of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff537179">HUB_DEVICE_CONFIG_INFO</a> structure.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The hub or port driver sets <b>Irp-&gt;IoStatus.Status</b> to STATUS_SUCCESS or the appropriate error status.

## Remarks
Upon successful completion, the HardwareIds, CompatibleIds, DeviceDescription <a href="https://msdn.microsoft.com/library/windows/hardware/ff540043">USB_ID_STRING</a> structures contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537179">HUB_DEVICE_CONFIG_INFO</a> structure  points to string buffers allocated by the hub driver.  The caller driver is responsible for releasing these buffers before the driver unloads.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows Vista and later operating systems. Windows Vista and later operating systems. |
| **Header** | usbioctl.h (include Usbioctl.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537179">HUB_DEVICE_CONFIG_INFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff540043">USB_ID_STRING</a>