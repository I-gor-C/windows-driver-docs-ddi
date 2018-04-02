---
UID: NF:ntddk.IoCreateDisk
title: IoCreateDisk function
author: windows-driver-content
description: The IoCreateDisk routine initializes a raw disk by creating a new partition table.
old-location: storage\iocreatedisk.htm
old-project: storage
ms.assetid: 0ad85551-a8d2-4f7f-958b-fe23111de340
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IoCreateDisk, IoCreateDisk routine [Storage Devices], ntddk/IoCreateDisk, rtns-disk_5f69686f-f812-4ccc-8bc8-4caa70230d20.xml, storage.iocreatedisk
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: This routine is only available on Windows XP and later.
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
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	IoCreateDisk
product: Windows
targetos: Windows
req.typenames: WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# IoCreateDisk function
The <b>IoCreateDisk</b> routine initializes a raw disk by creating a new partition table.

## Syntax

```
NTKERNELAPI NTSTATUS IoCreateDisk(
  PDEVICE_OBJECT DeviceObject,
  _CREATE_DISK   *Disk
);
```

## Parameters

`DeviceObject`

Specifies the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> for the raw disk.

`Disk`

Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552484">CREATE_DISK</a> structure that specifies the type and parameters for the partition table. If <i>Disk</i> is <b>NULL</b>, the routine deletes the partition table on the disk.


## Return Value

Returns STATUS_SUCCESS on success, or the appropriate error code on failure.

## Remarks

<b>IoCreateDisk</b> must only be used by disk drivers. Other drivers should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559436">IOCTL_DISK_CREATE_DISK</a> I/O request instead.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This routine is only available on Windows XP and later.  |
| **Target Platform** | Universal |
| **Header** | ntddk.h (include Ntddk.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552484">CREATE_DISK</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559436">IOCTL_DISK_CREATE_DISK</a>