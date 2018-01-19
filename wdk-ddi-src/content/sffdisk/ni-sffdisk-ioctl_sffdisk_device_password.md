---
UID : NI:sffdisk.IOCTL_SFFDISK_DEVICE_PASSWORD
title : IOCTL_SFFDISK_DEVICE_PASSWORD
author : windows-driver-content
description : User-mode applications use this IOCTL to perform basic operations on a Secure Digital (SD) card, such as setting the password on the card, resetting the card, or locking and unlocking the card.
old-location : sd\ioctl_sffdisk_device_password.htm
old-project : SD
ms.assetid : 76b65ada-06b8-411e-83e9-62088f697f02
ms.author : windowsdriverdev
ms.date : 12/18/2017
ms.keywords : SFFDISK_DPCMD, SFFDISK_DPCMD
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : sffdisk.h
req.include-header : Sffdisk.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IOCTL_SFFDISK_DEVICE_PASSWORD
req.alt-loc : sffdisk.h
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
req.typenames : SFFDISK_DPCMD
req.product : Windows 10 or later.
---

# IOCTL_SFFDISK_DEVICE_PASSWORD IOCTL
User-mode applications use this IOCTL to perform basic operations on a Secure Digital (SD) card, such as setting the password on the card, resetting the card, or locking and unlocking the card. For a description of this command, see the <i>Secure Digital I/O (SDIO)</i> specification.

To perform this operation, call the <a href="https://msdn.microsoft.com/1d35c087-6672-4fc6-baa1-a886dd9d3878">DeviceIoControl</a> function (described in the Microsoft Windows SDK documentation) using the following parameters.

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
I/O Status block
If the operation succeeds, <a href="https://msdn.microsoft.com/1d35c087-6672-4fc6-baa1-a886dd9d3878">DeviceIoControl</a> returns a nonzero value.

If the operation fails, <a href="https://msdn.microsoft.com/1d35c087-6672-4fc6-baa1-a886dd9d3878">DeviceIoControl</a> returns zero. To get extended error information, call <b>GetLastError</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | sffdisk.h (include Sffdisk.h) |
| **IRQL** |  |