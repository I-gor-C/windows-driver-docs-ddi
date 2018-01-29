---
UID : NI:ntdddisk.IOCTL_DISK_IS_CLUSTERED
title : IOCTL_DISK_IS_CLUSTERED
author : windows-driver-content
description : Allows a driver or application to determine if a disk is clustered.
old-location : storage\ioctl_disk_is_clustered.htm
old-project : storage
ms.assetid : 46b72c16-2656-4ceb-a786-5fb24818b2a7
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : storage.ioctl_disk_is_clustered, IOCTL_DISK_IS_CLUSTERED control code [Storage Devices], IOCTL_DISK_IS_CLUSTERED, ntdddisk/IOCTL_DISK_IS_CLUSTERED, k307_a812ef4f-f10c-4d75-aaf8-a3ad4d41703e.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : ntdddisk.h
req.include-header : Ntdddisk.h
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
req.typenames : DETECTION_TYPE
---

# IOCTL_DISK_IS_CLUSTERED IOCTL
Allows a driver or application to determine if a disk is clustered.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
None.

### Input Buffer Length
None.

### Output Buffer
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains a Boolean value, with <b>TRUE</b> indicating that the disk is clustered.

### Output Buffer Length
Length of a Boolean.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
<b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | ntdddisk.h (include Ntdddisk.h) |
| **IRQL** |  |