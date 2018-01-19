---
UID : NI:ntdd8042.IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER
title : IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER
author : windows-driver-content
description : The IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER request is not supported.
old-location : hid\ioctl_internal_i8042_controller_write_buffer.htm
old-project : hid
ms.assetid : c4970f78-fa4f-4ce9-a538-332f00e0df28
ms.author : windowsdriverdev
ms.date : 12/21/2017
ms.keywords : _MOUSE_STATE, MOUSE_STATE, *PMOUSE_STATE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : ntdd8042.h
req.include-header : Ntdd8042.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER
req.alt-loc : ntdd8042.h
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
req.typenames : MOUSE_STATE, *PMOUSE_STATE
---

# IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER IOCTL
The IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER request is not supported.



The IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER request is not supported.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
None

### Input Buffer Length
None

### Output Buffer
None

### Output Buffer Length
None

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
The <b>Status</b> member is set to STATUS_NOT_SUPPORTED.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | ntdd8042.h (include Ntdd8042.h) |
| **IRQL** |  |