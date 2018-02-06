---
UID: NI:usbfnioctl.IOCTL_INTERNAL_USBFN_TRANSFER_IN
title: IOCTL_INTERNAL_USBFN_TRANSFER_IN
author: windows-driver-content
description: The class driver sends this request to initiate a data transfer to the host on the specified pipe.
old-location: buses\_ioctl_internal_usbfn_transfer_in.htm
old-project: usbref
ms.assetid: 53F895F8-596D-464C-866E-67028CF644E4
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: buses._ioctl_internal_usbfn_transfer_in, IOCTL_INTERNAL_USBFN_TRANSFER_IN control code [Buses], IOCTL_INTERNAL_USBFN_TRANSFER_IN, usbfnioctl/IOCTL_INTERNAL_USBFN_TRANSFER_IN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: usbfnioctl.h
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	usbfnioctl.h
apiname:
-	IOCTL_INTERNAL_USBFN_TRANSFER_IN
product: Windows
targetos: Windows
req.typenames: USBFN_USB_STRING, *PUSBFN_USB_STRING
req.product: Windows 10 or later.
---

# IOCTL_INTERNAL_USBFN_TRANSFER_IN IOCTL
The class driver sends this request to initiate a data transfer to the host on the specified pipe.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
A pointer to a <b>USBFNPIPEID</b> type that specifies the pipe ID.

### Input Buffer Length
The size of a <b>USBFNPIPEID</b> type.

### Output Buffer
The  output buffer points to a buffer containing the data to be sent. The IN direction is from the host perspective representing an outbound transfer from the device to the host.

### Output Buffer Length
The length of the data to be sent.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
If the request is successful, the USB function class extension (UFX) returns STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it returns a status value for which NT_SUCCESS(status) equals FALSE.

## Remarks
This request must be sent after sending the <a href="..\usbfnioctl\ni-usbfnioctl-ioctl_internal_usbfn_activate_usb_bus.md">IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS</a> request.

UFX forwards this IOCTL request to the transfer queue created for the endpoint by <a href="..\ufxclient\nf-ufxclient-ufxendpointcreate.md">UfxEndpointCreate</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbfnioctl.h |