---
UID: NI:ntddchgr.IOCTL_CHANGER_SET_ACCESS
title: IOCTL_CHANGER_SET_ACCESS
author: windows-driver-content
description: Sets the state of the device's import/export port (IEport), door, or keypad.
old-location: storage\ioctl_changer_set_access.htm
old-project: storage
ms.assetid: 8927e862-94e4-45ce-9245-5c6f5629fc01
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IOCTL_CHANGER_SET_ACCESS, IOCTL_CHANGER_SET_ACCESS control code [Storage Devices], k307_08d52a8e-d7a0-42c6-92f9-c5099670473c.xml, ntddchgr/IOCTL_CHANGER_SET_ACCESS, storage.ioctl_changer_set_access
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddchgr.h
req.include-header: Ntddchgr.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntddchgr.h
api_name:
-	IOCTL_CHANGER_SET_ACCESS
product: Windows
targetos: Windows
req.typenames: ELEMENT_TYPE, *PELEMENT_TYPE
---

# IOCTL_CHANGER_SET_ACCESS IOCTL
Sets the state of the device's import/export port (IEport), door, or keypad.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains a <a href="..\ntddchgr\ns-ntddchgr-_changer_set_access.md">CHANGER_SET_ACCESS</a> structure indicating the element and the operation to perform.

### Input Buffer Length
<b>Parameters.DeviceIoControl.InputBufferLength</b> in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= <b>sizeof</b>(CHANGER_SET_ACCESS).

### Output Buffer
None.

### Output Buffer Length
None.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
The <b>Information</b> field is set to the number of bytes set. The <b>Status</b> field is set to STATUS_SUCCESS, or possibly to STATUS_INFO_LENGTH_MISMATCH, STATUS_INSUFFICIENT_RESOURCES, STATUS_INVALID_DEVICE_REQUEST, or STATUS_INVALID_PARAMETER.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddchgr.h (include Ntddchgr.h) |

## See Also

<a href="..\ntddchgr\ns-ntddchgr-_changer_set_access.md">CHANGER_SET_ACCESS</a>



<a href="..\mcd\nf-mcd-changersetaccess.md">ChangerSetAccess</a>