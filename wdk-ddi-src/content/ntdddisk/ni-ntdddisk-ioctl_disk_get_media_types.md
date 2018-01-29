---
UID : NI:ntdddisk.IOCTL_DISK_GET_MEDIA_TYPES
title : IOCTL_DISK_GET_MEDIA_TYPES
author : windows-driver-content
description : In Microsoft Windows 2000 and later operating systems, this IOCTL is replaced by IOCTL_STORAGE_GET_MEDIA_TYPES. The only difference between the two IOCTLs is the base value.
old-location : storage\ioctl_disk_get_media_types.htm
old-project : storage
ms.assetid : d6e6cd4c-680d-4885-b910-3de8de143e2b
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : storage.ioctl_disk_get_media_types, IOCTL_DISK_GET_MEDIA_TYPES control code [Storage Devices], IOCTL_DISK_GET_MEDIA_TYPES, ntdddisk/IOCTL_DISK_GET_MEDIA_TYPES, k307_692b21f7-7d14-4ba9-9d56-381606f5f5b1.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : ntdddisk.h
req.include-header : TBD
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

# IOCTL_DISK_GET_MEDIA_TYPES IOCTL
In Microsoft Windows 2000 and later operating systems, this IOCTL is replaced by <a href="..\ntddstor\ni-ntddstor-ioctl_storage_get_media_types.md">IOCTL_STORAGE_GET_MEDIA_TYPES</a>. The only difference between the two IOCTLs is the base value.

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
| **Header** | ntdddisk.h (include TBD) |
| **IRQL** |  |