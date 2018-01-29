---
UID : NI:ntddvdeo.IOCTL_VIDEO_SET_POINTER_POSITION
title : IOCTL_VIDEO_SET_POINTER_POSITION
author : windows-driver-content
description : Sets the pointer position. Support for this modal request is optional. A supporting miniport driver should have already processed an enable-pointer request before processing this request.
old-location : display\ioctl_video_set_pointer_position.htm
old-project : display
ms.assetid : de581a49-da6d-410b-82be-28cc1eccfde4
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.ioctl_video_set_pointer_position, IOCTL_VIDEO_SET_POINTER_POSITION control code [Display Devices], IOCTL_VIDEO_SET_POINTER_POSITION, ntddvdeo/IOCTL_VIDEO_SET_POINTER_POSITION, Video_IOCTLs_cc9ab1b6-f2be-4dab-b657-f686bc0af329.xml
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
req.typenames : TAPE_WRITE_MARKS, *PTAPE_WRITE_MARKS
---

# IOCTL_VIDEO_SET_POINTER_POSITION IOCTL
Sets the pointer position. Support for this modal request is optional. A supporting miniport driver should have already processed an enable-pointer request before processing this request.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The VRP <b>InputBuffer</b> contains the VIDEO_POINTER_POSITION structure to be set.

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
The miniport driver does not set the <b>Information</b> member of the <a href="..\video\ns-video-_status_block.md">STATUS_BLOCK</a> structure.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | ntddvdeo.h |
| **IRQL** |  |