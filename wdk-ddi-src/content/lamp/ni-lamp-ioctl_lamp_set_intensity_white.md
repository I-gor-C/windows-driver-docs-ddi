---
UID : NI:lamp.IOCTL_LAMP_SET_INTENSITY_WHITE
title : IOCTL_LAMP_SET_INTENSITY_WHITE
author : windows-driver-content
description : The IOCTL_LAMP_SET_INTENSITY_WHITE control code sets the lamp to the specified light intensity.
old-location : stream\ioctl_lamp_set_intensity_white.htm
old-project : stream
ms.assetid : 78541C4C-AA0E-4C1F-A7B5-E2A39DF5E2CE
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
req.alt-api : IOCTL_LAMP_SET_INTENSITY_WHITE
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

# IOCTL_LAMP_SET_INTENSITY_WHITE IOCTL
The <b>IOCTL_LAMP_SET_INTENSITY_WHITE</b> 
   control code sets the lamp to the specified light intensity.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<code>Irp-&gt;AssociatedIrp.SystemBuffer</code> points to a <a href="..\lamp\ns-lamp-lamp_intensity_white.md">LAMP_INTENSITY_WHITE</a> structure.

### Input Buffer Length
Length of a <a href="..\lamp\ns-lamp-lamp_intensity_white.md">LAMP_INTENSITY_WHITE</a> structure.

### Output Buffer
None.

### Output Buffer Length
None.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
The driver sets <code>Irp-&gt;IoStatus.Status</code> to <b>STATUS_SUCCESS</b> or the appropriate error status.

If the device has been acquired by a camera driver, the lamp driver should return a  <b>STATUS_RESOURCE_IN_USE</b> error via <code>Irp-&gt;IoStatus.Status</code>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | lamp.h |
| **IRQL** |  |