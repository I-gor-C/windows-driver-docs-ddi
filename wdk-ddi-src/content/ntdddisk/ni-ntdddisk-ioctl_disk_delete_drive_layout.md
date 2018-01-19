---
UID : NI:ntdddisk.IOCTL_DISK_DELETE_DRIVE_LAYOUT
title : IOCTL_DISK_DELETE_DRIVE_LAYOUT
author : windows-driver-content
description : Removes partition information from the disk.
old-location : storage\ioctl_disk_delete_drive_layout.htm
old-project : storage
ms.assetid : 787fa1ce-5305-4159-8710-3c6971133c4c
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _DETECTION_TYPE, DETECTION_TYPE
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
req.alt-api : IOCTL_DISK_DELETE_DRIVE_LAYOUT
req.alt-loc : Ntdddisk.h
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
req.typenames : DETECTION_TYPE
---

# IOCTL_DISK_DELETE_DRIVE_LAYOUT IOCTL
Removes partition information from the disk. If the partition style of the disk is Master Boot Record (MBR), sector 0 of the disk is wiped clean except for the bootstrap code. All signatures, such as the AA55 boot signature and the NTFT disk signature, will be removed. If the partition style of the disk is GUID Partition Table (GPT), the primary partition table header in sector 1 and the backup partition table in the last sector of the disk are wiped clean. This operation can be used to generate so-called "superfloppies" that contain a file system starting at the first sector of the disk rather than in a partition on the disk.



Removes partition information from the disk. If the partition style of the disk is Master Boot Record (MBR), sector 0 of the disk is wiped clean except for the bootstrap code. All signatures, such as the AA55 boot signature and the NTFT disk signature, will be removed. If the partition style of the disk is GUID Partition Table (GPT), the primary partition table header in sector 1 and the backup partition table in the last sector of the disk are wiped clean. This operation can be used to generate so-called "superfloppies" that contain a file system starting at the first sector of the disk rather than in a partition on the disk.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
None.

### Input Buffer Length
None.

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
The <b>Status</b> field is set to STATUS_SUCCESS, or possibly to STATUS_INSUFFICIENT_RESOURCES.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | ntdddisk.h (include Ntdddisk.h) |
| **IRQL** |  |