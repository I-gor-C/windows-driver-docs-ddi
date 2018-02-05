---
UID : NI:usbscan.IOCTL_RESET_PIPE
title : IOCTL_RESET_PIPE
author : windows-driver-content
description : Resets the specified USB transfer pipe that is associated with the specified device handle.
old-location : image\ioctl_reset_pipe.htm
old-project : image
ms.assetid : aeca126a-449a-4a10-a4ce-1cd3939ac076
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : image.ioctl_reset_pipe, IOCTL_RESET_PIPE control code [Imaging Devices], IOCTL_RESET_PIPE, usbscan/IOCTL_RESET_PIPE, stifnc_907d0aea-158a-4219-9235-85a16d6da30f.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : usbscan.h
req.include-header : Usbscan.h
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
req.typenames : RAW_PIPE_TYPE
req.product : Windows 10 or later.
---

# IOCTL_RESET_PIPE IOCTL
Resets the specified USB transfer pipe that is associated with the specified device handle.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
Pointer to a location that contains a value of type <a href="..\usbscan\ne-usbscan-pipe_type.md">PIPE_TYPE</a>.

### Input Buffer Length
Size of the input buffer.

### Output Buffer
<b>NULL</b>.

### Output Buffer Length
Zero.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
<b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code.

## Remarks
<h3><a id="ddk_ioctl_reset_pipe_si"></a><a id="DDK_IOCTL_RESET_PIPE_SI"></a>DeviceIoControl Parameters</h3>

When the <b>DeviceloControl</b> function is called with the IOCTL_RESET_PIPE I/O control code, the caller must specify one of the <a href="..\usbscan\ne-usbscan-pipe_type.md">PIPE_TYPE</a>-typed values as the function's <i>lpInBuffer</i> parameter. This value indicates on which of the transfer pipes (interrupt, bulk IN, bulk OUT) the operation should be performed. For more information, see <a href="https://msdn.microsoft.com/f9216d3c-4930-4c26-8eac-6ee500b038e0">Accessing Kernel-Mode Drivers for Still Image Devices</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbscan.h (include Usbscan.h) |