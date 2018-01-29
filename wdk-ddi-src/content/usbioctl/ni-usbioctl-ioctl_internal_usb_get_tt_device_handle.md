---
UID : NI:usbioctl.IOCTL_INTERNAL_USB_GET_TT_DEVICE_HANDLE
title : IOCTL_INTERNAL_USB_GET_TT_DEVICE_HANDLE
author : windows-driver-content
description : The IOCTL_INTERNAL_USB_GET_TT_DEVICE_HANDLE is used by the USB hub driver. Do not use.
old-location : buses\ioctl_internal_usb_get_tt_device_handle.htm
old-project : usbref
ms.assetid : 1ea77cc4-bee4-4e0a-92a4-6413d3e5871a
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : buses.ioctl_internal_usb_get_tt_device_handle, IOCTL_INTERNAL_USB_GET_TT_DEVICE_HANDLE control code [Buses], IOCTL_INTERNAL_USB_GET_TT_DEVICE_HANDLE, usbioctl/IOCTL_INTERNAL_USB_GET_TT_DEVICE_HANDLE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : usbioctl.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : USB_HUB_TYPE
req.product : Windows 10 or later.
---

# IOCTL_INTERNAL_USB_GET_TT_DEVICE_HANDLE IOCTL
The <b>IOCTL_INTERNAL_USB_GET_TT_DEVICE_HANDLE</b> is used by the USB hub driver. Do not use.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<text></text>

### Input Buffer Length
<text></text>

### Output Buffer
<text></text>

### Output Buffer Length
<text></text>

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
Irp->IoStatus.Status is set to STATUS_SUCCESS if the request is successful.
Otherwise, Status to the appropriate error condition as a NTSTATUS code. 
For more information, see [XREF-LINK:NTSTATUS Values].


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | usbioctl.h |
| **IRQL** |  |