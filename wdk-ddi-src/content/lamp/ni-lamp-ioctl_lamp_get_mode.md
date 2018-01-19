---
UID : NI:lamp.IOCTL_LAMP_GET_MODE
title : IOCTL_LAMP_GET_MODE
author : windows-driver-content
description : The IOCTL_LAMP_GET_MODE control code queries the mode with which the lamp is currently configured.
old-location : stream\ioctl_lamp_get_mode.htm
old-project : stream
ms.assetid : 741FFB14-B6F1-452B-AD8A-E82C0E34CB6A
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : LAMP_MODE, LAMP_MODE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : lamp.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IOCTL_LAMP_GET_MODE
req.alt-loc : lamp.h
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
req.typenames : LAMP_MODE
---

# IOCTL_LAMP_GET_MODE IOCTL
The <b>IOCTL_LAMP_GET_MODE</b> 
   control code queries the mode with which the lamp is currently configured.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<code>Irp-&gt;AssociatedIrp.SystemBuffer</code> points to a buffer of type <a href="..\lamp\ne-lamp-lamp_mode.md">LAMP_MODE</a>.

### Input Buffer Length
Length of <a href="..\lamp\ne-lamp-lamp_mode.md">LAMP_MODE</a>.

### Output Buffer
<code>Irp-&gt;AssociatedIrp.SystemBuffer</code> is filled with a <b>LAMP_MODE</b> value.

### Output Buffer Length
<code>IO_STACK_LOCATION.Parameters.DeviceIoControl.OutputBufferLength</code> is the length of the buffer in bytes passed in the <code>Irp-&gt;AssociatedIrp.SystemBuffer</code> field.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
The driver sets <code>Irp-&gt;IoStatus.Status</code> to <b>STATUS_SUCCESS</b> or the appropriate error status. It will set <code>Irp-&gt;IoStatus.Information</code> to the number of bytes required to hold a <b>DWORD</b> value.

If the device has been acquired by a camera driver, the lamp driver should return a   <b>STATUS_RESOURCE_IN_USE</b> error via <code>Irp-&gt;IoStatus.Status</code>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | lamp.h |
| **IRQL** |  |