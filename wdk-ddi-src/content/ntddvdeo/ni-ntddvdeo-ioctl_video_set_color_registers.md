---
UID : NI:ntddvdeo.IOCTL_VIDEO_SET_COLOR_REGISTERS
title : IOCTL_VIDEO_SET_COLOR_REGISTERS
author : windows-driver-content
description : Sets the adapter's color registers to the specified RGB values. If the adapter has a color look up table (CLUT), sometimes called a palette, the miniport driver is required to support this modal request.
old-location : display\ioctl_video_set_color_registers.htm
old-project : display
ms.assetid : efaea94e-0cfd-49a7-b8dc-452aa006b024
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _TAPE_WRITE_MARKS, *PTAPE_WRITE_MARKS, TAPE_WRITE_MARKS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : ntddvdeo.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IOCTL_VIDEO_SET_COLOR_REGISTERS
req.alt-loc : Ntddvdeo.h
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
req.typenames : "*PTAPE_WRITE_MARKS, TAPE_WRITE_MARKS"
---

# IOCTL_VIDEO_SET_COLOR_REGISTERS IOCTL
Sets the adapter's color registers to the specified RGB values. If the adapter has a color look up table (CLUT), sometimes called a palette, the miniport driver is required to support this modal request.



Sets the adapter's color registers to the specified RGB values. If the adapter has a color look up table (CLUT), sometimes called a palette, the miniport driver is required to support this modal request.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The VRP <b>InputBuffer</b> contains a VIDEO_CLUT structure, specifying an array of RGB values to be set.

### Input Buffer Length
<text></text>

### Output Buffer
None

### Output Buffer Length
<text></text>

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
The miniport driver does not set the <b>Information</b> member of the <a href="..\video\ns-video-_status_block.md">STATUS_BLOCK</a> structure.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | ntddvdeo.h |
| **IRQL** |  |