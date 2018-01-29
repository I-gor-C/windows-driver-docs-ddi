---
UID : NI:usbscan.IOCTL_WAIT_ON_DEVICE_EVENT
title : IOCTL_WAIT_ON_DEVICE_EVENT
author : windows-driver-content
description : Returns information about an event occurring on a USB interrupt pipe.
old-location : image\ioctl_wait_on_device_event.htm
old-project : image
ms.assetid : 0895a19b-bb28-405a-98df-28522a18ec2b
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : image.ioctl_wait_on_device_event, IOCTL_WAIT_ON_DEVICE_EVENT control code [Imaging Devices], IOCTL_WAIT_ON_DEVICE_EVENT, usbscan/IOCTL_WAIT_ON_DEVICE_EVENT, stifnc_ef4b6e5f-ed60-4354-adae-443e1a27b215.xml
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

# IOCTL_WAIT_ON_DEVICE_EVENT IOCTL
Returns information about an event occurring on a USB interrupt pipe.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<b>NULL</b>

### Input Buffer Length
Zero.

### Output Buffer
Pointer to a buffer that is large enough to receive the largest packet the device is capable of sending on the interrupt pipe.

### Output Buffer Length
Size of the output buffer.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
<b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code.

## Remarks
<h3><a id="ddk_ioctl_wait_on_device_event_si"></a><a id="DDK_IOCTL_WAIT_ON_DEVICE_EVENT_SI"></a>DeviceIoControl Parameters</h3>

When the <b>DeviceloControl</b> function is called with the IOCTL_WAIT_ON_DEVICE_EVENT control code, the caller must specify a buffer pointer as the function's <i>lpOutBuffer</i> parameter. The buffer must be large enough to hold the largest packet the device can send on its interrupt pipe.

The type and size of information returned are device-specific. For example, a still image device might issue an interrupt when a user presses one of its buttons, and the return packet might indicate which button was pressed.

For more information, see <a href="https://msdn.microsoft.com/f9216d3c-4930-4c26-8eac-6ee500b038e0">Accessing Kernel-Mode Drivers for Still Image Devices</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | usbscan.h (include Usbscan.h) |
| **IRQL** |  |