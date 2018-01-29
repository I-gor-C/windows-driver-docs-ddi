---
UID : NI:ntddvdeo.IOCTL_VIDEO_PREPARE_FOR_EARECOVERY
title : IOCTL_VIDEO_PREPARE_FOR_EARECOVERY
author : windows-driver-content
description : This IOCTL is for internal use only.
old-location : display\ioctl_video_prepare_for_earecovery.htm
old-project : display
ms.assetid : 71cd4559-9cb3-468e-a53e-fb40b97a90b6
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.ioctl_video_prepare_for_earecovery, IOCTL_VIDEO_PREPARE_FOR_EARECOVERY control code [Display Devices], IOCTL_VIDEO_PREPARE_FOR_EARECOVERY, ntddvdeo/IOCTL_VIDEO_PREPARE_FOR_EARECOVERY, Video_IOCTLs_72bcebdd-6335-4953-9a23-00061760b4a4.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : ntddvdeo.h
req.include-header : Ntddvdeo.h
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

# IOCTL_VIDEO_PREPARE_FOR_EARECOVERY IOCTL
This IOCTL is for internal use only.

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
| **Header** | ntddvdeo.h (include Ntddvdeo.h) |
| **IRQL** |  |