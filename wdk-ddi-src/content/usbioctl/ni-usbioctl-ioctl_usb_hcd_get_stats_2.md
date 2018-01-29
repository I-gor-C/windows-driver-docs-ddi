---
UID : NI:usbioctl.IOCTL_USB_HCD_GET_STATS_2
title : IOCTL_USB_HCD_GET_STATS_2
author : windows-driver-content
description : The IOCTL_USB_HCD_GET_STATS_2 IOCTL has been deprecated. Do not use.
old-location : buses\ioctl_usb_hcd_get_stats_2.htm
old-project : usbref
ms.assetid : 64d229b3-9f06-432d-8d4f-7469e0deb11a
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : buses.ioctl_usb_hcd_get_stats_2, IOCTL_USB_HCD_GET_STATS_2 control code [Buses], IOCTL_USB_HCD_GET_STATS_2, usbioctl/IOCTL_USB_HCD_GET_STATS_2, usbirp_62df7d2d-dc01-46bf-8ce8-aa1a0082387e.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : usbioctl.h
req.include-header : Usbioctl.h
req.target-type : Windows
req.target-min-winverclnt : Available on Microsoft Windows Server 2003, Windows XP, and Windows 2000, but it is not available on Windows Vista.
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

# IOCTL_USB_HCD_GET_STATS_2 IOCTL
The <b>IOCTL_USB_HCD_GET_STATS_2</b> IOCTL has been deprecated. Do not use.

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
| **Header** | usbioctl.h (include Usbioctl.h) |
| **IRQL** |  |