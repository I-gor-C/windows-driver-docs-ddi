---
UID : NI:usbfnioctl.IOCTL_INTERNAL_USBFN_TRANSFER_OUT
title : IOCTL_INTERNAL_USBFN_TRANSFER_OUT
author : windows-driver-content
description : The class driver sends this request to initiate a data transfer from the host on the specified pipe.
old-location : buses\ioctl_internal_usbfn_transfer_out.htm
old-project : usbref
ms.assetid : DDC99C5F-B959-44E4-A4A8-1CBA4E9BDA5A
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : buses.ioctl_internal_usbfn_transfer_out, IOCTL_INTERNAL_USBFN_TRANSFER_OUT control code [Buses], IOCTL_INTERNAL_USBFN_TRANSFER_OUT, usbfnioctl/IOCTL_INTERNAL_USBFN_TRANSFER_OUT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : usbfnioctl.h
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
req.typenames : USBFN_USB_STRING, *PUSBFN_USB_STRING
req.product : Windows 10 or later.
---

# IOCTL_INTERNAL_USBFN_TRANSFER_OUT IOCTL
The class driver sends this request to initiate a data transfer from the host on the specified pipe.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
A pointer to a <b>USBFNPIPEID</b> type that specifies the pipe ID.

### Input Buffer Length
The size of a <b>USBFNPIPEID</b> type.

### Output Buffer
A data buffer to receive data from the host.

### Output Buffer Length
The length of the buffer.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
Irp->IoStatus.Status is set to STATUS_SUCCESS if the request is successful.
Otherwise, Status to the appropriate error condition as a NTSTATUS code. 
For more information, see [XREF-LINK:NTSTATUS Values].

## Remarks
This request must be sent after sending the <a href="..\usbfnioctl\ni-usbfnioctl-ioctl_internal_usbfn_activate_usb_bus.md">IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS</a> request.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | usbfnioctl.h |
| **IRQL** |  |