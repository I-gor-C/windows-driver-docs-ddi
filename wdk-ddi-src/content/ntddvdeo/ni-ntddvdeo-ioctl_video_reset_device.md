---
UID : NI:ntddvdeo.IOCTL_VIDEO_RESET_DEVICE
title : IOCTL_VIDEO_RESET_DEVICE
author : windows-driver-content
description : Resets the video hardware to the default mode, to which it was initialized at system boot. Miniport drivers are required to support this nonmodal request.
old-location : display\ioctl_video_reset_device.htm
old-project : display
ms.assetid : 98746cae-aed1-4cf4-86d2-eb7cc91e45fc
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
req.alt-api : IOCTL_VIDEO_RESET_DEVICE
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

# IOCTL_VIDEO_RESET_DEVICE IOCTL
Resets the video hardware to the default mode, to which it was initialized at system boot. Miniport drivers are required to support this nonmodal request.



Resets the video hardware to the default mode, to which it was initialized at system boot. Miniport drivers are required to support this nonmodal request.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
None

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