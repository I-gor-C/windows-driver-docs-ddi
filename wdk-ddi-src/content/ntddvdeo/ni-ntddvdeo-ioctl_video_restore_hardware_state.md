---
UID : NI:ntddvdeo.IOCTL_VIDEO_RESTORE_HARDWARE_STATE
title : IOCTL_VIDEO_RESTORE_HARDWARE_STATE
author : windows-driver-content
description : Restores all values used to set the hardware registers. Miniport drivers for VGA-compatible adapters are required to support this nonmodal request; optional for other miniport drivers.
old-location : display\ioctl_video_restore_hardware_state.htm
old-project : display
ms.assetid : 94ea36b6-3390-4e67-982d-ee6c2500c0de
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
req.alt-api : IOCTL_VIDEO_RESTORE_HARDWARE_STATE
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

# IOCTL_VIDEO_RESTORE_HARDWARE_STATE IOCTL
Restores all values used to set the hardware registers. Miniport drivers for VGA-compatible adapters are required to support this nonmodal request; optional for other miniport drivers.



Restores all values used to set the hardware registers. Miniport drivers for VGA-compatible adapters are required to support this nonmodal request; optional for other miniport drivers.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The VRP <b>InputBuffer</b> contains the previously-saved VIDEO_HARDWARE_STATE structure.

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